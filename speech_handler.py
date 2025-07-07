import speech_recognition as sr
import pyttsx3

from config import RECOGNITION_SETTINGS


class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        
        self.recognizer.energy_threshold = RECOGNITION_SETTINGS['energy_threshold']
        self.recognizer.dynamic_energy_threshold = RECOGNITION_SETTINGS['dynamic_energy_threshold']
        self.recognizer.pause_threshold = RECOGNITION_SETTINGS['pause_threshold']
        self.recognizer.operation_timeout = RECOGNITION_SETTINGS['operation_timeout']
    
    def calibrate_microphone(self, duration=0.5):
        print("Calibrating microphone...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=duration)
        print("Calibration complete!")
        
    def listen(self):
        with self.microphone as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, phrase_time_limit=6, timeout=20)
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected, continuing to listen...")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def stop(self):
        self.engine.stop()
