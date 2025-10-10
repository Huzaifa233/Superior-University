from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import numpy as np
import os

app = Flask(__name__)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
   
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = cv2.imread(filepath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS
            )

    output_path = os.path.join(UPLOAD_FOLDER, 'output_' + file.filename)
    cv2.imwrite(output_path, image)

    personality = "You seem confident and positive-minded! 😄"

    return render_template("result.html",
                           input_image=filepath,
                           output_image=output_path,
                           personality=personality)

if __name__ == "__main__":
    app.run(debug=True)
