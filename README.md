# MoodTune - AI Mood Detection & Song Recommendation 🎵

## Overview
MoodTune is an AI-powered web application that detects the mood from a user-uploaded image and recommends a song based on the detected emotion. The application uses machine learning to analyze the image, determine the mood, and then provides a music playlist tailored to the user's emotional state. 

## Features
* **Mood Detection**: Uses AI to analyze facial expressions and detect the user's mood from an uploaded photo.
* **Song Recommendation**: Based on the detected emotion, a song is recommended to match the mood.
* **Simple UI**: Clean and minimal interface with a smooth user experience.

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/f244b134-5d21-45b7-8a2b-e5e370341032)
![image](https://github.com/user-attachments/assets/9e0a44cb-214e-421f-a050-b92d41aed38a)


## Contributors
* [Sujal-1245](https://github.com/sujal-1245)
* [Priyanshu-654](https://github.com/priyanshu-654)

## Folder Structure

```
moodtune/
│
├── app.py
│
├── static/
│   ├── uploads/           # Uploaded images go here
│   ├── songs/             # Songs stored in folders by mood
│   │    ├── happy/
│   │    ├── sad/
│   │    ├── angry/
│   │    ├── neutral/
│   │    ├── fear/
│   │    ├── disgust/
│   │    └── surprise/
│   ├── css/
│   │    └── style.css     
│   └── js/
│        └── script.js     
│
├── templates/
│   ├── index.html          # Upload page
│   └── result.html         # Results page after emotion detection
│
└── README.md               

```

## Requirements

Make sure to install the following Python packages to run the project. You can use the `requirements.txt` file to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
Flask==2.2.2
tensorflow==2.9.1
numpy==1.23.3
pillow==9.2.0
opencv-python==4.5.5.64
scikit-learn==1.1.1
matplotlib==3.5.3
requests==2.28.1
```

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/MoodTune.git
   cd MoodTune
   ```

2. **Install dependencies**:

   Make sure you have Python 3.7+ installed. Then install the dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   To run the Flask app locally, execute the following command:

   ```bash
   python app.py
   ```

4. **Access the app**:

   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using the app!

## How It Works

1. **Upload Photo**: The user uploads a photo from their device.
2. **Mood Detection**: The AI model processes the image and detects the user's mood based on facial expressions.
3. **Song Recommendation**: Once the mood is detected, a song matching the detected emotion is recommended.
4. **Listen**: The song is embedded in the web page for the user to listen to.


---
