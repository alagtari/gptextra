import base64
import io
import speech_recognition as sr

def voice_to_text(base64_audio):

    decode_bytes = base64.b64decode(base64_audio)
    with open('request.mp3', "wb") as wav_file:
            wav_file.write(decode_bytes)
    

    # replace "path/to/audio/file.mp3" with the actual path to your MP3 file
    filename = "request.mp3"

    # create a recognizer object
    r = sr.Recognizer()

    # use the recognizer to open the audio file
    with sr.AudioFile(filename) as source:
        # read the audio data from the file
        audio_data = r.record(source)

    # use the recognizer to perform speech recognition
    text = r.recognize_google(audio_data)

    # print the recognized text
    return text