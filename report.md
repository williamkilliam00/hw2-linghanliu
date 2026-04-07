# Evaluation Report: Meeting Action Item Extractor

## Business Use Case
This tool is designed for project managers to automate the extraction of tasks from unstructured meeting notes. It saves time and ensures no commitments are forgotten after a meeting.

## Model Choice
I initially attempted to use **Gemini 1.5 Flash** and **Gemini Pro**. Due to regional API availability issues and 404 errors, I implemented a robust "Failover" system. In a production environment, Gemini 1.5 Flash would be the preferred choice for its speed and cost-effectiveness in text extraction.

## Prompt Improvement
The main improvement was adding a **System Persona (Project Manager)** and a **Strict Output Format**. This prevented the LLM from adding "chatter" and made the output machine-readable for potential integration with tools like Jira or Trello.

## Limitations
The system currently relies on the names being explicitly mentioned near the task. If a person says "I will do that" without their name being captured in the text, the attribution might fail.

## Recommendation
I recommend deploying this as a **sidebar tool** in meeting platforms (like Zoom or Teams). It should provide a "Draft" list for the user to approve before officially assigning tasks.