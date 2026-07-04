import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def generate_email(company_info):
    prompt = f"""
    You are a sales development rep writing a short cold outreach email opener.
    Here is some information about a company:

    {company_info}

    Write a 2-3 sentence personalized email opener that references something 
    specific about this company. Keep it friendly and professional. 
    Do not include a subject line or sign-off, just the opener.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    from scraper import scrape_website
    from enrich import clean_text

    raw = scrape_website("https://stripe.com")
    cleaned = clean_text(raw)
    email = generate_email(cleaned)

    print("----- GENERATED EMAIL OPENER -----")
    print(email)
