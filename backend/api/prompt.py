from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()  
client = OpenAI()

EXTRACTION_PROMPT = """
You are a data-extraction assistant. When given a free-form fitness journal entry, you must output **only** a JSON object (no extra text) matching this schema:

{
  "injuries": [
    {
      "location": string,
      "severity": string  // one of: "none","low","moderate","high"
      // OPTIONAL: additional_notes: string
    },
    …
  ],
  "workout": [
    {
      "exercise": string,
      "sets": number,     // integer or float
      "reps": number,     // integer or float
      "type": string      // one of: "strength","cardio","mobility","warmup"
      // OPTIONAL: weight: string or number
    },
    …
  ],
  // OPTIONAL: "notes": string
}

Rules:
1. Output **only** valid JSON—no markdown or prose.
2. If nothing to extract for a field, use an empty array (or omit optional fields).
3. Map “tweak”/“niggle” → “low”, “pinch”/“sharp” → “moderate”, “severe”/“shooting” → “high”.
4. Normalize exercise synonyms (“DL” → “deadlift”).
5. Infer “strength” vs “cardio” vs “mobility” if type isn’t explicit.
"""

def get_prompt_response(prompt: str):
    # prompt for user journal

    # call the Chat API
    resp = client.chat.completions.create(
        model="gpt-4o-mini",            # or another model of your choice
        messages=[
            {"role": "system", "content": EXTRACTION_PROMPT},
            {"role": "user",   "content": prompt}
        ]
    )

    return json.loads(resp.choices[0].message.content)


if __name__ == "__main__":
    pass
