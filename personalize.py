import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
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


def score_lead(company_info):
    prompt = f"""
    You are a sales analyst. Based on the following company information, 
    rate how good a fit this company is for a sales automation and CRM tool, 
    on a scale of 1 to 10 (10 = excellent fit, 1 = poor fit).

    Company information:
    {company_info}

    Respond in EXACTLY this format, nothing else:
    Score: <number>
    Reason: <one short sentence explaining why>
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
    score = score_lead(cleaned)

    print("\n----- LEAD SCORE -----")
    print(score)
