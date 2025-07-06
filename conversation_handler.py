from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class Message:
    content: str
    role: str
    timestamp: datetime

class ConversationHandler:
    def __init__(self):
        self.conversation_history: List[Message] = []
        self.max_history: int = 100
    
    def add_message(self, content: str, role: str) -> Message:
        message = Message(
            content=content,
            role=role,
            timestamp=datetime.now()
        )
        self.conversation_history.append(message)
        
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        return message
    
    def get_conversation_history(self) -> List[Message]:
        return self.conversation_history
    
    def clear_history(self) -> None:
        self.conversation_history = []