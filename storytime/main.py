import sys
import os

# Update Python path so we can import modules easily
# (Alternatively, you can structure your project as proper packages and install them)
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from packages.listening_ears.speech_to_text import SpeechToText
from packages.good_parts.scene_extraction import scene_from_text
from packages.show_me_the_picture.illustrate import illustrate_from_prompt

speech_duration=30

test_text="a photo of an astronaut riding a horse on mars"

def main():
    print("Starting main application...")
    stt = SpeechToText(model_name="small")
    print(f"Speak now for the next {speech_duration} seconds...")
    transcribed_text = stt.transcribe_live(duration=speech_duration)
    print("You said:", transcribed_text)

    print("Passing transcription to scene extraction")
    scene_text = scene_from_text(transcribed_text)
    print(f"Obtained the following scene: {scene_text}")

    print("Passing scene description to illustration")
    illustration = illustrate_from_prompt("A photo of a black and white cat by a fireplace")
    illustration.save("illustration.png")

if __name__ == "__main__":
    main()