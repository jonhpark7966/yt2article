# yt2article/transcribers/whisper_transcriber.py
import os
from openai import OpenAI
from pydub import AudioSegment

from .transcriber import Transcriber

class WhisperTranscriber(Transcriber):
    def __init__(self):
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            # api_key="My API Key",
        )

    def transcribe(self, input_path: str, output_path: str):
        # Load the audio file
        audio = AudioSegment.from_file(input_path)

        # Define the maximum chunk file size (25 MB for the API limit)
        max_file_size = 25 * 1024 * 1024  # 25 MB in bytes

        # Open the output file in write mode
        with open(output_path, 'w') as output_file:

            # Start processing the audio file in chunks
            start = 0
            chunk_counter = 0

            while start < len(audio):
                # Dynamically calculate chunk duration to stay within the file size limit
                chunk_duration = 60 * 1000  # Start with 1 minute (in milliseconds)
                chunk_audio = audio[start:start + chunk_duration]

                # Export the chunk to check its size
                chunk_file = f"audio_chunk_{chunk_counter}.mp3"
                chunk_audio.export(chunk_file, format="mp3")

                # Open the chunk file and send it to the Whisper API
                with open(chunk_file, 'rb') as audio_file:
                    transcription = self.client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        response_format="text"
                    )

                    # Write the transcription to the output file
                    output_file.write(transcription + '\n')

                # Clean up the chunk file
                os.remove(chunk_file)

                # Move to the next chunk
                start += chunk_duration
                chunk_counter += 1

        return
