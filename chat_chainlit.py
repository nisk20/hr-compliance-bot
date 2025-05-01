import chainlit as cl
import os
from openai import AzureOpenAI

# Load Azure OpenAI credentials from .env or Azure
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="👋 Welcome to the HR Compliance Bot (Azure-powered)! Ask me anything about labor laws, safety, or human rights.").send()

@cl.on_message
async def on_message(message: cl.Message):
    completion = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are an HR compliance expert in labor law, safety and human rights."},
            {"role": "user", "content": message.content}
        ]
    )
    await cl.Message(content=completion.choices[0].message.content).send()
