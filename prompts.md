# Prompt Iteration History

## Version 1: Initial Baseline
**Prompt:** Extract tasks from these notes: [Notes]
**Result:** The output was too conversational and included unnecessary sentences like "Here are the tasks I found."

## Version 2: Adding Formatting
**Prompt:** Extract action items as a list. Format: [Name]: [Task]. Notes: [Notes]
**Result:** Better, but it sometimes missed deadlines or combined multiple tasks into one line.

## Version 3: Final Design (Professional Persona)
**Prompt:** You are a professional project manager. Extract action items from the following meeting notes. Use a strict bulleted list format: [Name]: [Task]. If no tasks are found, say 'No tasks identified.' Be concise and professional.
**Result:** Very clean and consistent output, suitable for a professional dashboard.