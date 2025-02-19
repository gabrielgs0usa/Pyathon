#Ainda em desenvolvimento

import pytube
import ffmpeg
import openai
import sys

#chave da API
openai.api_key = "key"

#Baixar audio do video do youtube 
import sys 
url = sys.argv[1]
filename = 'audio.wav'
yt = pytube.YouTube(url)
audio_path = str.download(filename="downloaded_audio.mp4")
ffmpeg.input(audio_path).output(filename, format='wav', loglevel='quiet').run()

#traqnscrever audio
audio_file = open(filename, 'rb')
transcript = openai.Audio.transcribe(
    model='whisper-1',
    file=audio_file
)["text"]

#pede do texto
completions = openai.ChatCompletion.create(
    model = "gpt-3.0-turbo", 
    messages = [
    {"role": "system",
     "content": """
     Você é uma assistente virtual que ajuda a analisar vídeos do YouTube detalhadamente.
     Responda no formato Markdown.
     """},
    {"role": "user",
     "content": f"Descreva o vídeo: {transcript}"} 
    ]
)

print(completions["choices"][0]["message"]["content"])