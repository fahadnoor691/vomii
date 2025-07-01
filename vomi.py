from speech_handler import SpeechHandler
from ai_handler import AIHandler
class Vomi:
    def __init__(self):
        self.is_running = False
        self.speech_handler = SpeechHandler()
        self.ai_handler = AIHandler()

    def start(self):
        self.is_running = True
        self.speech_handler.calibrate_microphone()
        while self.is_running:
            self._main_loop()
    
    def _main_loop(self):
        while self.is_running:
            text = self.speech_handler.listen_google()
            
            if text is None:
                continue
            
            query = text.lower().replace("jarvis", "").strip()
            if query:
                
                response = self.ai_handler.process_query(text)
            
                print("AI Response: ", response)
                self.speech_handler.speak(response)
