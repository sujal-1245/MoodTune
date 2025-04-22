from flask import Flask, render_template, request
import os
import random
from deepface import DeepFace
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Base directory (where app.py is located)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Folders
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
SONGS_FOLDER = os.path.join(BASE_DIR, 'static', 'songs')

# Configure upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create folders if missing
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Valid emotions
VALID_EMOTIONS = ['happy', 'sad', 'angry', 'mysterious', 'fear', 'disgust', 'surprise']

def detect_emotion(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
    if isinstance(analysis, list):
        analysis = analysis[0]
    emotion = analysis.get('dominant_emotion', 'mysterious').lower()
    if emotion not in VALID_EMOTIONS:
        emotion = 'mysterious'
    return emotion

def get_random_song(emotion):
    folder_path = os.path.join(SONGS_FOLDER, emotion)
    if not os.path.exists(folder_path):
        folder_path = os.path.join(SONGS_FOLDER, 'mysterious')

    song_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

    if not song_files:
        return None

    selected_song = random.choice(song_files)
    
    # Return path relative to static folder for rendering
    relative_path = os.path.relpath(os.path.join(folder_path, selected_song), BASE_DIR)
    return relative_path.replace("\\", "/")  # fix for Windows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return "No file uploaded."

        file = request.files['photo']

        if file.filename == '':
            return "No file selected."

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        emotion = detect_emotion(filepath)
        song_path = get_random_song(emotion)

        relative_photo_path = os.path.relpath(filepath, BASE_DIR).replace("\\", "/")

        return render_template('result.html', emotion=emotion, song_path=song_path, image_path=relative_photo_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
