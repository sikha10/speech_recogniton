import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Say something: ")
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"recognized: {text}")

    except speech_recognition.UnknownValueError():
        print("could not recognize")
        recognizer = speech_recognition.Recognizer()
        continue
