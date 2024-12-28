from crewai import Task
from agents import blog_researcher,blog_writer
from tools import yt_tool

##Research Task

research_task = Task(
    description=(
        "Identify the video on the basis of {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraph report on {topic}',
    tools=[yt_tool],
    agent=blog_researcher,
)

writing_task = Task(
    description=(
        "Get the information from the youtube videos on {topic}"
        "And write  a detailed report of 3 paragraphs on {topic}"
    ),
    expected_output='Summarize the information from the obtained by the researcher from the youtube videos on {topic}',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new1-blog-post.md',
)