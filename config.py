import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

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

ELEVENLABS_SETTINGS = {
    'voice_id': "21m00Tcm4TlvDq8ikWAM",
    'model_id': "eleven_flash_v2_5",
    'output_format': "mp3_44100_128",
    'optimize_streaming_latency': 0,
}

CONTEXT_SETTINGS = {
    'max_history': 20,
}

os.environ["PATH"] += os.pathsep + r"C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin"