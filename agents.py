from crewai import Agent
from tools import yt_tool
# from dotenv import load_dotenv
from crewai import LLM
import litellm
import openai
import os
# load_dotenv()

llmnew = LLM(
    model="ollama/llama3.2", 
    base_url="http://localhost:11434"
)


##Create a senior blog content researcher

blog_researcher = Agent(
    role='Blog researcher fromm youtube videos',
    goal='get the relevant video for collecting the information of the given topic ',
    name='Senior blog content researcher',
    description='a senior blog researcher that will find the relevant information from the videos present in the youtube',
    verbose=True,
    memory=True,
    backstory=(
     "This is expert in understanding videos about ai and data science and machine learning"
    ),
    tools=[yt_tool],
    llm=llmnew,
    allow_delegation=True,
)

##Create a senior blog writer agent
blog_writer = Agent(
    role='Blog writer',
    goal='Write in brief on the topic {topic} from youtube channel',
    description='A senior blog writer who writes a blog on the researched content in a structured manner to produce a finaal reeport on a given topic',
    verbose=True,
    memory=True,
    backstory=(
     "This is a blog writer who is an expert in writing the searched data in a structured manner to produce a final report on a given topic"
    ),
    tools=[yt_tool],
    llm=llmnew,
    allow_delegation=True,
)