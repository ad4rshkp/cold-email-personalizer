# Cold Email Personalizer

An AI-powered tool that researches companies and writes personalized cold outreach emails — built as a GTM (Go-To-Market) engineering portfolio project.

**Live demo:** https://cold-email-personalizer-tkkkgusbuujtdwtga75vve.streamlit.app
**GitHub:** https://github.com/ad4rshkp/cold-email-personalizer

---

## What it does

Sales teams often send generic, templated cold emails that get ignored. This tool automates the research and personalization process:

1. Upload a CSV of leads (name, company, title, website)
2. The tool scrapes each company's website for real information
3. Google's Gemini AI generates a short, specific email opener referencing that company
4. Gemini also scores each lead (1–10) on how good a fit they are, with a reason
5. Results are shown in a table, saved to a database, and available to download as CSV

## Demo

Upload a CSV like this:

| name | company | title | website |
|------|---------|-------|---------|
| Sarah Lee | ProductCo | VP Sales | https://stripe.com |

And get back:

> "I was really impressed by Stripe's commitment to providing financial infrastructure that helps businesses grow their revenue, especially how you're enabling custom revenue models from the first transaction to the billionth."
>
> **Lead Score:** 8/10 — Stripe's focus on financial infrastructure and revenue growth strongly suggests a need for tools that manage customer relationships and sales processes efficiently.

## Features

- **Web scraping** — pulls real, live text from each lead's company website
- **AI email personalization** — Google Gemini generates a unique, specific opener per lead (not a generic template)
- **AI lead scoring** — Gemini rates and explains how good a fit each lead is
- **Interactive dashboard** — built with Streamlit: upload, preview, generate, and download, all in the browser
- **Persistent history** — every processed lead is saved to a SQLite database, so results aren't lost between runs
- **Reliability** — automatic retry logic handles temporary API failures gracefully instead of crashing

## Tech stack

- **Python** — core language
- **Streamlit** — web dashboard/UI
- **Google Gemini API** — AI personalization and lead scoring
- **requests + BeautifulSoup** — web scraping
- **pandas** — data handling
- **SQLite** — persistent storage
- **python-dotenv** — secure local API key management

## Architecture

The project follows a simple pipeline structure, with each file responsible for one step:

```
leads.csv → scraper.py → enrich.py → personalize.py → output.py / database.py
                                                              ↓
                                                          app.py (Streamlit UI)
```

- `scraper.py` — visits a company website and extracts raw text
- `enrich.py` — cleans and trims the scraped text
- `personalize.py` — sends cleaned text to Gemini to generate an email opener and a lead score
- `output.py` — saves results to CSV
- `database.py` — saves results to a SQLite database and retrieves lead history
- `main.py` — runs the full pipeline from the command line
- `app.py` — Streamlit web interface wrapping the same pipeline

## Running it locally

```bash
git clone https://github.com/ad4rshkp/cold-email-personalizer.git
cd cold-email-personalizer
python -m venv .venv
.venv\Scripts\activate      # on Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root with your own Gemini API key:

```
GEMINI_API_KEY=your_key_here
```

Get a free key at [Google AI Studio](https://aistudio.google.com).

Then run either:

```bash
python main.py          # command-line pipeline, uses data/leads.csv
streamlit run app.py    # interactive web dashboard
```

## Planned future improvements

- Multi-source enrichment (LinkedIn, recent news, funding data)
- Multiple email tone variants (formal / casual / direct) per lead
- Direct email sending and open-rate tracking via an email API

## About this project

Built as a hands-on portfolio project to demonstrate GTM engineering skills — chaining data pipelines, web scraping, and AI APIs into a usable, deployed tool. Every part of this pipeline (scraping, cleaning, prompting, scoring, storage, and UI) was built and understood step by step rather than templated.