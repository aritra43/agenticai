from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,writing_task
from tools import yt_tool


#Forming the crew that will generate the report
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    tools=[yt_tool],
)

##Start the report generation tasks
result = crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
print(result)