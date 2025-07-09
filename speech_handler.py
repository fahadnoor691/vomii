import speech_recognition as sr
import pyttsx3
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from config import RECOGNITION_SETTINGS, ELEVENLABS_SETTINGS, ELEVENLABS_API_KEY


class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.elevenlabs = ElevenLabs(api_key=ELEVENLABS_API_KEY)

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
        audio = self.elevenlabs.text_to_speech.convert(
            text=text,
            voice_id=ELEVENLABS_SETTINGS['voice_id'],
            model_id=ELEVENLABS_SETTINGS['model_id'],
            output_format=ELEVENLABS_SETTINGS['output_format'],
            optimize_streaming_latency=ELEVENLABS_SETTINGS['optimize_streaming_latency'],
        )
        play(audio)
    