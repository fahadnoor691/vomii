import time
from config import CONTEXT_SETTINGS


class ConversationHandler:
    def __init__(self):
        self.conversation_history = []
        self.max_history = CONTEXT_SETTINGS['max_history']
    
    def add_message(self, content: str, role: str) -> None:
        message = {
            "content": content,
            "role": role,
            "timestamp": time.time()
        }
        self.conversation_history.append(message)
        
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        return message
    
    def get_conversation_history(self):
        return self.conversation_history
    
    def clear_history(self) -> None:
        self.conversation_history = []