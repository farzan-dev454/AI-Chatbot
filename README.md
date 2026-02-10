# AI Chatbot

A conversational AI chatbot powered by Groq API (Llama 3.1) with conversation history tracking and logging.

## Features

- 💬 Interactive chat interface
- 📝 Automatic conversation logging with timestamps
- 📊 Message counter
- 🗂️ Saves chat history to file
- ⚙️ Customizable AI temperature settings
- 🚪 Multiple exit commands (quit, exit, bye, goodbye)

## Technologies Used

- Python 3
- Groq API (Llama 3.1-8b-instant)
- python-dotenv (environment variables)
- datetime (timestamp tracking)

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one free here](https://console.groq.com))

### Installation

1. Clone this repository or download the files

2. Install required packages:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_api_key_here
```

4. Run the chatbot:
```bash
python step6.py
```

## Usage
```
Chatbot started! Type 'quit' to exit.

You: Hello
Message count: 1
Bot: Hi! How can I help you today?

You: What is AI?
Message count: 2
Bot: AI (Artificial Intelligence) refers to...
```

## Features Explained

### Conversation Logging
All conversations are automatically saved to `chat_log.txt` with timestamps:
```
[14:35:22] User: Hello
[14:35:22] Bot: Hi! How can I help you today?
```

### Message Counter
Tracks the number of messages in the current session.

### Temperature Control
Set to 0.9 for creative responses. Can be adjusted in the code (0.0-1.0).

## Project Structure
```
ai-chatbot/
├── .env                # API key (DO NOT share)
├── .gitignore         # Files to ignore in git
├── step6.py           # Main chatbot (command line)
├── groq_chatbot.py    # Streamlit version (web interface)
├── chat_log.txt       # Conversation history  "Note: chat_log.txt is generated locally and is ignored by Git to keep the repository clean."
└── README.md          # This file
```

## Future Improvements

- [ ] Add conversation memory (AI remembers context)
- [ ] Export chat history to different formats
- [ ] Add voice input/output
- [ ] Multiple AI model selection

## License

Free to use for learning and portfolio purposes.

## Author

Built as part of NLP/LLM learning journey - February 2026

## Contact

Github: [@farzan-dev454](https://github.com/farzan-dev454)
Email: farzan7856@gmail.com


**Built with ❤️ using Groq API**
