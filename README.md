# VOMI - Voice Assistant

VOMI is an intelligent voice-controlled assistant that combines speech recognition, AI processing, and text-to-speech capabilities to provide a hands-free computing experience. It can perform various tasks including web searches, system operations, application management, and more.

## Features

- **Voice Recognition**: Real-time speech-to-text using Google Speech Recognition
- **AI Processing**: Powered by OpenAI GPT-4o-mini for intelligent responses
- **Text-to-Speech**: High-quality voice synthesis using ElevenLabs
- **System Integration**: Control applications, take screenshots, manage windows
- **Web Capabilities**: Search the internet, crawl websites, open URLs
- **System Monitoring**: Get system info, battery status, running applications
- **Conversation Memory**: Maintains context across interactions

## Prerequisites

- Python 3.10 or higher
- Microphone and speakers/headphones
- FFmpeg (for audio processing)
- Windows 10/11 (primary platform)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd VOMI
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:

   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Install FFmpeg** (if not already installed):
   - Windows: Install via Chocolatey: `choco install ffmpeg`
   - macOS: Install via Homebrew: `brew install ffmpeg`
   - Or download from [FFmpeg official website](https://ffmpeg.org/download.html)

## Configuration

1. **Create a `.env` file** in the project root with your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

2. **Get API Keys**:
   - **OpenAI**: Sign up at [OpenAI Platform](https://platform.openai.com/) and get your API key
   - **Tavily**: Sign up at [Tavily](https://tavily.com/) for web search capabilities
   - **ElevenLabs**: Sign up at [ElevenLabs](https://elevenlabs.io/) for high-quality TTS

## Usage

1. **Start VOMI**:

   ```bash
   python main.py
   ```

2. **Voice Commands**: Speak naturally to interact with VOMI. Examples:

   - "What's the weather like today?"
   - "Open Chrome browser"
   - "Take a screenshot"
   - "Search for Python tutorials"
   - "What time is it?"
   - "Lock my computer"

3. **Exit**: Say "exit", "quit", "stop", or "bye" to close VOMI

## Available Commands

### System Operations

- Open applications: "Open [application name]"
- Take screenshots: "Take a screenshot"
- Window management: "Minimize windows", "Close windows", "Restore windows"
- System control: "Lock computer"
- System info: "Get system information", "Show running apps", "Check battery"

### Web & Information

- Web search: "Search for [query]"
- Website crawling: "Crawl [website]"
- Open websites: "Open [website URL]"
- Current time: "What time is it?"

### General Conversation

- Ask questions: "What is [topic]?"
- Get help: "How do I [task]?"
- General chat: Any natural conversation

## Project Structure

```
VOMI/
├── main.py                 # Entry point
├── vomi.py                 # Main VOMI class
├── ai_handler.py           # OpenAI integration and tool execution
├── speech_handler.py       # Speech recognition and TTS
├── tools.py               # Available tools and functions
├── dextop_agent.py        # Desktop automation
├── conversation_handler.py # Conversation memory
├── config.py              # Configuration settings
├── prompts.py             # AI system prompts
├── requirements.txt       # Python dependencies
└── .env                   # API keys (create this)
```

## Configuration Options

Edit `config.py` to customize:

- **Speech Recognition**: Adjust energy threshold, pause threshold
- **OpenAI**: Change model, temperature settings
- **ElevenLabs**: Modify voice ID, model, output format
- **Conversation**: Set maximum history length

## Troubleshooting

### Common Issues

1. **Microphone not working**:

   - Check microphone permissions
   - Ensure microphone is set as default input device
   - Try recalibrating: VOMI will calibrate automatically on startup

2. **Speech recognition errors**:

   - Check internet connection (required for Google Speech Recognition)
   - Speak clearly and reduce background noise
   - Adjust energy threshold in `config.py`

3. **API errors**:

   - Verify API keys in `.env` file
   - Check API key validity and quotas
   - Ensure proper internet connection

4. **Audio playback issues**:
   - Install FFmpeg properly
   - Check audio output device settings
   - Verify ElevenLabs API key

### Performance Tips

- Use a good quality microphone for better speech recognition
- Reduce background noise for optimal performance
- Ensure stable internet connection for API calls
- Close unnecessary applications to free up system resources

## Dependencies

- **PyAudio**: Audio input/output
- **SpeechRecognition**: Speech-to-text
- **pyttsx3**: Basic text-to-speech
- **elevenlabs**: High-quality TTS
- **openai**: AI processing
- **tavily-python**: Web search
- **PyAutoGUI**: Desktop automation
- **psutil**: System information
- **python-dotenv**: Environment variables

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
