import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

RECOGNITION_SETTINGS = {
    'energy_threshold': 100,
    'dynamic_energy_threshold': False,
    'pause_threshold': 0.5,
    'operation_timeout': None
}

OPENAI_SETTINGS = {
    'model': 'gpt-4o-mini',
    'temperature': 0.5,
}

CONTEXT_SETTINGS = {
    'max_history': 20,
}
