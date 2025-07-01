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

# ElevenLabs Configuration
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
ELEVENLABS_MODEL_ID = "eleven_multilingual_v2"
ELEVENLABS_OUTPUT_FORMAT = "mp3_44100_128"

# FFmpeg Configuration
FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "ffmpeg", "bin")
os.environ["PATH"] += os.pathsep + FFMPEG_PATH