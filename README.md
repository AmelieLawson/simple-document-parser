# Simple LLM Document Parser
## Project Overview

Following [Niharika Batra's 16-Week AI/ML Series](https://niharikabatra.substack.com/p/week-6-day-7-lets-build-our-first), I have built my first LLM application. It reads and parses a job description, producing a Python object with the following fields: job title (str), highest qualification level (str), valid degree fields (str), years of experience (int), whether remote work is permitted (bool), and salary range (str).

## Method

The method is largely adapted from Niharika's example of a document parser for a remote work policy:

1. Create the client object.
2. Define the job description.
3. Define the system prompt.
4. Define the user prompt.
5. Define the LLM output structure using Pydantic.
6. Make the API call to the LLM.
7. Print the LLM response as a Python object.

## How to Run

Install the required Python libraries: 

```bash
pip install openai pydantic
```

Load the google/gemma-4-e4b model in LM Studio and start the local server.

Run ```python parser.py```

## What I Learnt

Below is a summary of what I have learnt in understanding Niharika's original code and adapting it to my own example:

- What is meant by an API call (when a program makes a request to another piece of software via its API).
- What is meant by an API (short for application programming interface, the gateway which facilitates communication between different pieces of software).
- What is meant by a client (the object via which the program makes an API call).
- How to create a client object to communicate with an LLM.
- The difference between a system prompt (sets the model's role) and a user prompt (sets the model's task).
- How to use Pydantic to define a class which specifies the desired output structure from an LLM.
- How make an API call to an LLM.

## Opportunities for Advancement

This program could be improved by allowing it to parse job descriptions which aren't hard-coded, such as pdf documents, so it has more generalisable usage.
