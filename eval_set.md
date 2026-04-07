# Evaluation Set: Meeting Summarizer
**Workflow:** Extracting Action Items from meeting notes.

## Test Cases

1. **Normal:** "Sarah will draft social media posts by Tuesday. Mike will contact influencers."
2. **Edge Case (No Tasks):** "The team had pizza and talked about the weather. No work was discussed."
3. **Fail Case (Ambiguity):** "Alice will do the report. No, wait, Bob will. Actually, Alice should do it but not send it."
4. **Multiple Tasks:** "John needs to fix the server bugs, update the security patch, and then email the client about the downtime."
5. **Long & Messy:** "We started late. Discussion moved from the marketing budget to the new logo. Eventually, Kevin agreed to finalize the logo design by Friday, although he's busy with the hiring process."