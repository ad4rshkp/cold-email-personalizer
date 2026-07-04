import csv


def save_results(results, filename="data/output.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "company", "title", "website", "email_opener"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)
