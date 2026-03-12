from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from mcp_client import get_linkedin, get_instagram, get_resume

client = Groq(api_key=GROQ_API_KEY)


def hobby_agent(name: str):

    linkedin = get_linkedin(name)
    instagram = get_instagram(name)
    resume = get_resume(name)

    # 🔽 Combine MCP data
    combined_text = linkedin + instagram + resume

    # 🔽 If MCP returned nothing, allow model to assume hobbies
    if combined_text.strip() == "":
        combined_text = f"No social data found for {name}. Assume general hobbies."

    # 🔽 Structured information for model
    combined_data = f"""
LinkedIn: {linkedin}

Instagram: {instagram}

Resume: {resume}

Additional Info: {combined_text}
"""

    prompt = f"""
    You are an AI agent that extracts hobbies of a person.

    STRICT RULES:
    1. Return ONLY hobbies.
    2. Do NOT include explanations.
    3. Do NOT include assumptions text.
    4. Do NOT include introductory sentences.
    5. Output must contain only a bullet list.
    6. If no hobbies found, still provide common hobbies without explanation.

    Information:
    {combined_data}

    Output format (follow exactly):
    Hobbies:
    - Hobby 1
    - Hobby 2
    - Hobby 3
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
