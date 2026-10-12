from openai import OpenAI # How code interacts with LLM API
from pydantic import BaseModel # Defines and validates the LLM output structure
import os # Reads environment variables for API key

# Create a client object which will be used to make API calls to the LLM
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key=os.environ.get("OPENAI_API_KEY", "none"),
)

# Define the job description as a Python string
document = """Job Description: 

We are a private hospital looking for a data scientist to join our analytics division.
The ideal candidate will hold a master's degree in data science, computer science or mathematics and have at least 5 years of experience in similar roles.
This position is hybrid and employees are allowed to work from home up to 3 days per week.
The expected salary range is £80,000 to £120,000 per annum, subject to the experience of the candidate."""

# Define the system prompt to set the model's role
system_prompt = (
    "You are a careful assistant. You extract facts from documents "
    "and always answer with valid JSON." 
)

# Define the user prompt to set the model's task
user_prompt = f"""Here is a document:

{document}

Extract these details and return them as a single JSON object with exactly these fields:
- "role": the job title (text)
- "highest_qualification_level": the highest qualification level required (text)
- "valid_degree_fields": the valid fields of study (text)
- "years_experience": the number of years of experience required (number)
- "remote_work_allowed": whether remote work is permitted (true or false)
- "salary_range": the expected salary range (text)

Return only the JSON object. Do not include any other text."""

# Use Pydantic to define a class called Description which specifies the output structure we require from the LLM
# If the LLM output matches this structure, it is converted into a Description object, otherwise an error is raised
class Description(BaseModel):
    role: str
    highest_qualification_level: str
    valid_degree_fields: str
    years_experience: int
    remote_work_allowed: bool
    salary_range: str

# Make the API call to the LLM
response = client.beta.chat.completions.parse(
    model="google/gemma-4-e4b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=0, # Low temperature ensures more reliable output
    response_format=Description # Use Pydantic to specify the output structure
)

# Print the response from the LLM as a Python object
description = response.choices[0].message.parsed
print(f"Description: {description}")