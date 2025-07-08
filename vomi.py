from speech_handler import SpeechHandler
from ai_handler import AIHandler
import getpass


class Vomi:
    def __init__(self):
        self.is_running = False
        self.speech_handler = SpeechHandler()
        self.ai_handler = AIHandler()

    def start(self):
        username = getpass.getuser()
        print(f"Username: {username}")
        
        self.is_running = True
        self.speech_handler.speak(f"Hi {username}, how can I help you today?")
        self.speech_handler.calibrate_microphone()
        
        while self.is_running:
            self._main_loop()
    
    def _main_loop(self):
        while self.is_running:
            text = self.speech_handler.listen()
            
            if text is None:
                continue
            
            query = text.lower()
        
            if query.lower() in ["exit", "quit", "stop", "bye"]:
                self.is_running = False
                self.speech_handler.stop()
                print("Exiting...")
                self.speech_handler.speak("Thank you for using Vomi. Goodbye!")
                break
                
            if query:
                response = self.ai_handler.process_query(text)
                print("AI Response: ", response)
                self.speech_handler.speak(response)