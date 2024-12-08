import os
import wave

import pyaudio
import tempfile
import whisper

class SpeechToText:
    def __init__(self, model_name="small"):
        """
        Initialize the Whisper model.
        Available models: tiny, base, small, medium, large.
        Choose one based on your hardware.
        """
        self.model = whisper.load_model(model_name)

    def record_audio(self, duration=5, output_file="temp_audio.wav"):
        """
        Record audio from the microphone for a fixed duration.
        """
        chunk = 1024    # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16
        channels = 1
        fs = 16000       # Whisper recommends 16kHz
        seconds = duration

        p = pyaudio.PyAudio()

        print("Recording...")
        stream = p.open(format=sample_format, channels=channels, rate=fs,
                        input=True, frames_per_buffer=chunk)
        frames = []

        for _ in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Recording finished.")

        # Save the recorded data as a WAV file
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        return output_file

    def transcribe(self, audio_file_path):
        """
        Transcribe the audio using Whisper.
        """
        print("Transcribing audio...")
        result = self.model.transcribe(audio_file_path, fp16=False)
        text = result['text']
        print("Transcription complete.")
        return text

    def transcribe_live(self, duration=5):
        """
        A convenience method to record then transcribe.
        """
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_filename = tmp.name
        self.record_audio(duration, tmp_filename)
        text = self.transcribe(tmp_filename)
        os.remove(tmp_filename)
        return text

if __name__ == "__main__":
    # For quick local testing, run this file directly.
    stt = SpeechToText(model_name="small")
    transcribed_text = stt.transcribe_live(duration=5)
    print("Transcribed Text:", transcribed_text)