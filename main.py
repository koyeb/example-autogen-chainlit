import chainlit as cl
from autogen import AssistantAgent, UserProxyAgent

from saas import start_chat_saas
from script import start_chat_script


@cl.set_chat_profiles
async def set_chat_profile():
    return [
        cl.ChatProfile(
            name="YouTube Scriptwriting",
            markdown_description="Your next YouTube video script is just a few messages away!",
        ),
        cl.ChatProfile(
            name="SaaS Product Ideation",
            markdown_description="Get your next SaaS product idea in a few messages!",
        ),
    ]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"Welcome to {chat_profile} chat. Please type your first message to get started."
    ).send()


@cl.on_message
async def on_message(message):
    chat_profile = cl.user_session.get("chat_profile")
    message_content = message.content
    if chat_profile == "YouTube Scriptwriting":
        start_chat_script(message_content)
    elif chat_profile == "SaaS Product Ideation":
        start_chat_saas(message_content)
