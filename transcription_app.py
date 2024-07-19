from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI( 
    api_key=os.environ.get("API_KEY") 
)

file_path = "memo1.m4a"
audio_file= open(file_path, "rb")

transcription = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file  
)

print(transcription.text)
