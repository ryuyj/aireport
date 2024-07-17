from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI( 
    api_key=os.environ.get("API_KEY") 
)

file_path = "d:/openai_project/src/speech/data/test4.mp3"
audio_file= open(file_path, "rb")

transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(transcription)
