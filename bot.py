import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot nyala sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!tanya"):
        user_input = message.content.replace("!tanya", "").strip()

        await message.channel.send("🤖 Tunggu bentar ya Bang, mikir dulu...")

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            # Optional headers buat OpenRouter ranking
            # "HTTP-Referer": "https://yourwebsite.com",
            # "X-Title": "My Discord Bot",
        }

        payload = {
            "model": "google/gemini-2.5-pro",  # Model gratis dari OpenRouter
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                     headers=headers, data=json.dumps(payload))
            result = response.json()
            reply = result['choices'][0]['message']['content']
            await message.channel.send(reply)

        except Exception as e:
            print("Error:", e)
            await message.channel.send("⚠️ Gagal manggil AI, ada error.")

client.run(DISCORD_TOKEN)
