import speech_recognition as sr

def voice_to_text():
    r = sr.Recognizer()
    audio_file = sr.AudioFile('output.wav')
    with audio_file as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text