import sys
import os

# Update Python path so we can import modules easily
# (Alternatively, you can structure your project as proper packages and install them)
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from packages.listening_ears.speech_to_text import SpeechToText
from packages.good_parts.scene_extraction import scene_from_text

speech_duration=10

test_text="IN A HOLE IN THE GROUND there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort."

def main():
    # print("Starting main application...")
    # stt = SpeechToText(model_name="small")
    # print(f"Speak now for the next {speech_duration} seconds...")
    # text = stt.transcribe_live(duration=speech_duration)
    # print("You said:", text)

    print("{assing transcription to scene extraction")
    scene_text = scene_from_text(test_text)
    print(f"Obtained the following scene: {scene_text}")

if __name__ == "__main__":
    main()