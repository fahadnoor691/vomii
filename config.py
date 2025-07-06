import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

RECOGNITION_SETTINGS = {
    'energy_threshold': 100,
    'dynamic_energy_threshold': False,
    'pause_threshold': 0.5,
    'operation_timeout': None
}

OPENAI_SETTINGS = {
    'model': 'deepseek/deepseek-chat-v3-0324:free',
    'temperature': 0.5,
}

# Edge TTS Configuration
EDGE_TTS_VOICE = "en-US-AriaNeural"  # Default voice
EDGE_TTS_RATE = "+0%"  # Speech rate (can be +10%, -10%, etc.)
EDGE_TTS_VOLUME = "+0%"  # Volume (can be +10%, -10%, etc.)
