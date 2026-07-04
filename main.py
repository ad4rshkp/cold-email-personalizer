import csv
from scraper import scrape_website
from enrich import clean_text
from personalize import generate_email
from output import save_results


def load_leads(filename="data/leads.csv"):
    leads = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            leads.append(row)
    return leads


def run_pipeline():
    leads = load_leads()
    results = []

    for lead in leads:
        print(f"Processing {lead['name']} at {lead['company']}...")

        raw_text = scrape_website(lead["website"])
        cleaned_text = clean_text(raw_text)
        email_opener = generate_email(cleaned_text)

        lead["email_opener"] = email_opener
        results.append(lead)

    save_results(results)
    print("\nAll done! Check data/output.csv for your personalized emails.")


if __name__ == "__main__":
    run_pipeline()
