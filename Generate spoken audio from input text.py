from pathlib import Path
from openai import OpenAI
# # 加载 .env 到环境变量
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)