from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager, ConversableAgent
from decouple import config
import chainlit as cl


def chat_new_message(self, message, sender):
    cl.run_sync(
        cl.Message(
            content="",
            author=sender.name,
        ).send()
    )
    content = message.get("content")
    cl.run_sync(
        cl.Message(
            content=content,
            author=sender.name,
        ).send()
    )


def config_personas():
    config_list = [{
        "model": "gpt-3.5-turbo-1106",  # model name
        "api_key": config("OPENAI_API_KEY")  # api key
    }]

    llm_config = {
        "seed": 14,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0.7,  # temperature for sampling
    }

    user_proxy = UserProxyAgent(
        name="User_Proxy",
        system_message="A human admin.",
        max_consecutive_auto_reply=10,
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    content_creator = AssistantAgent(
        name="Content_Creator",
        system_message="I am a content creator that talks about exciting technologies about AI. "
                       "I want to create exciting content for my audience that is about the latest AI technology. "
                       "I want to provide in-depth details of the latest AI white papers.",
        llm_config=llm_config,
    )

    script_writer = AssistantAgent(
        name="Script_Writer",
        system_message="I am a script writer for the Content Creator. "
                       "This should be an eloquently written script so the Content Creator can "
                       "talk to the audience about AI.",
        llm_config=llm_config
    )

    researcher = AssistantAgent(
        name="Researcher",
        system_message="I am the researcher for the Content Creator and look up the latest white papers in AI."
                       " Make sure to include the white paper Title and Year it was introduced to the Script_Writer.",
        llm_config=llm_config
    )

    reviewer = AssistantAgent(
        name="Reviewer",
        system_message="I am the reviewer for the Content Creator, Script Writer, and Researcher once they are done "
                       "and have come up with a script.  I will double check the script and provide feedback.",
        llm_config=llm_config
    )

    group_chat = GroupChat(
        agents=[user_proxy, content_creator, script_writer, researcher, reviewer], messages=[]
    )
    manager = GroupChatManager(groupchat=group_chat, llm_config=llm_config)

    return user_proxy, manager


def start_chat_script(message, is_test=False):
    if not is_test:
        ConversableAgent._print_received_message = chat_new_message
    user_proxy, manager = config_personas()
    user_proxy.initiate_chat(manager, message=message)


if __name__ == "__main__":
    test_message = ("I need to create a YouTube Script that talks about the latest paper about gpt-4 on arxiv and its "
                    "potential applications in software.")
    start_chat_script(test_message, is_test=True)
