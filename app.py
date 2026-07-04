import streamlit as st
import pandas as pd
from scraper import scrape_website
from enrich import clean_text
from personalize import generate_email

st.title("Cold Email Personalizer")
st.write("Upload a CSV of leads and get AI-personalized email openers for each one.")


uploaded_file = st.file_uploader("Upload your leads CSV", type=["csv"])

if uploaded_file is not None:
    leads_df = pd.read_csv(uploaded_file)
    st.write("Preview of your uploaded leads:")
    st.dataframe(leads_df)

    if st.button("Generate Personalized Emails"):
        st.write("Processing leads... this may take a moment.")

        email_openers = []

        for index, row in leads_df.iterrows():
            st.write(f"Processing {row['name']} at {row['company']}...")

            raw_text = scrape_website(row["website"])
            cleaned_text = clean_text(raw_text)
            email_opener = generate_email(cleaned_text)

            email_openers.append(email_opener)

        leads_df["email_opener"] = email_openers

        st.success("All done! Here are your personalized emails:")
        st.dataframe(leads_df)

        csv_data = leads_df.to_csv(index=False)
        st.download_button(
            label="Download results as CSV",
            data=csv_data,
            file_name="personalized_leads.csv",
            mime="text/csv"
        )
