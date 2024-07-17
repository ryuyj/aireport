from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("API_KEY")
)

speech_file_path = Path(__file__).parent / "data/test1.mp3"

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello, my name is SON, and I'm currently studying programming with APIs."
)

#response.stream_to_file(speech_file_path)
response.with_streaming_response.method(speech_file_path)
