import speech_recognition as sr
import pyttsx3
import asyncio
import edge_tts
import tempfile
import os
import pygame
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from config import (
    ELEVENLABS_API_KEY, 
    RECOGNITION_SETTINGS,
    EDGE_TTS_VOICE, EDGE_TTS_RATE, EDGE_TTS_VOLUME
)

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        
        # Initialize TTS providers based on configuration
        self.voice = EDGE_TTS_VOICE
        self.rate = EDGE_TTS_RATE
        self.volume = EDGE_TTS_VOLUME
        pygame.mixer.init()
        
        self.recognizer.energy_threshold = RECOGNITION_SETTINGS['energy_threshold']
        self.recognizer.dynamic_energy_threshold = RECOGNITION_SETTINGS['dynamic_energy_threshold']
        self.recognizer.pause_threshold = RECOGNITION_SETTINGS['pause_threshold']
        self.recognizer.operation_timeout = RECOGNITION_SETTINGS['operation_timeout']
    
    def calibrate_microphone(self, duration=0.5):
        print("Calibrating microphone...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=duration)
        print("Calibration complete!")
        
    def listen_google(self):
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
    
    async def edge_text_to_speech(self, text):
        """Convert text to speech using Edge TTS"""
        try:
            # Create a temporary file for the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                temp_filename = temp_file.name
            
            # Generate speech using Edge TTS
            communicate = edge_tts.Communicate(text, self.voice, rate=self.rate, volume=self.volume)
            await communicate.save(temp_filename)
            
            # Play the audio using pygame
            pygame.mixer.music.load(temp_filename)
            pygame.mixer.music.play()
            
            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            
            # Clean up the temporary file
            os.unlink(temp_filename)
            
        except Exception as e:
            print(f"Error in Edge TTS: {e}")
    
    def speak(self, text):
        asyncio.run(self.edge_text_to_speech(text))