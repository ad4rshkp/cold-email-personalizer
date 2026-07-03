def clean_text(raw_text):
    lines = raw_text.split()
    cleaned = " ".join(lines)
    short_version = cleaned[:1000]
    return short_version


if __name__ == "__main__":
    from scraper import scrape_website

    raw = scrape_website("https://stripe.com")
    cleaned = clean_text(raw)

    print("----- RAW (first 300 characters) -----")
    print(raw[:300])

    print("\n----- CLEANED (first 300 characters) -----")
    print(cleaned[:300])
