import time
import csv
from scraper import scrape_website
from enrich import clean_text
from personalize import generate_email, score_lead
from output import save_results
from database import init_db, save_lead


def load_leads(filename="data/leads.csv"):
    leads = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            leads.append(row)
    return leads


def run_pipeline():
    init_db()
    leads = load_leads()
    results = []

    for lead in leads:
        print(f"Processing {lead['name']} at {lead['company']}...")

        raw_text = scrape_website(lead["website"])
        cleaned_text = clean_text(raw_text)
        email_opener = generate_email(cleaned_text)
        lead_score = score_lead(cleaned_text)

        lead["email_opener"] = email_opener
        lead["lead_score"] = lead_score
        results.append(lead)
        save_lead(lead)
        time.sleep(5)

    save_results(results)
    print("\nAll done! Check data/output.csv for your personalized emails.")


if __name__ == "__main__":
    run_pipeline()
