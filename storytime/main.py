import sys
import os

# Update Python path so we can import modules easily
# (Alternatively, you can structure your project as proper packages and install them)
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from packages.listening_ears.speech_to_text import SpeechToText

def main():
    print("Starting main application...")
    stt = SpeechToText(model_name="small")
    print("Speak now for the next 5 seconds...")
    text = stt.transcribe_live(duration=5)
    print("You said:", text)

if __name__ == "__main__":
    main()