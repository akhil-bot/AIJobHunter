from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()

LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

job_save_prompt = f'''
Your task is to navigate LinkedIn, login, and perform specific actions related to job postings. Follow these steps strictly:

1. Go to LinkedIn and login using the following credentials:
   - Username: {LINKEDIN_EMAIL}
   - Password: {LINKEDIN_PASSWORD}
2. Navigate to the job listings page.
3. Search for AI engineer roles in India.
4. For the first 5 job postings in the search results:
   - Click on each job posting.
   - Once the job posting loads, check if it is already saved.
   - If the job posting is not saved, click on "Save."
   - Confirm that the job posting has been saved before proceeding.
   - If the job posting was already saved, skip to the next one.
   - Only after confirming that the job posting has been saved, proceed to the next job posting.
5. Scroll the results page for the new job postings whenever needed.

REPEAT THE ACTION CAREFULLY FOR EACH STEP. It is crucial that each job posting is saved correctly. Do not assume that all job postings are saved after saving one; verify the save action for each job posting individually.
'''


async def main():
    agent = Agent(
        task=job_save_prompt,
        llm=llm,
    )
    result = await agent.run()
    print(result)


asyncio.run(main())

##TODO:1. Link it with the JOB Applier supervisor and use it
##TODO:2. See if we can use the same browser for each result
##TODO:3. Output the link source and store it as a PDF
