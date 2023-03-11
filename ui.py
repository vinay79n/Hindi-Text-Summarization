import streamlit as st
import requests
import json


def generate_extractive_summary(input_text):
    # Code to generate extractive summary
    # Through Extractive Summary generation code's API call
    # Define the API endpoint URL
    API_URL = "http://127.0.0.1:8000/extractiveSummarization"


    # Call the API when button is clicked
    # if st.button("Call API"):
        # Make the API request
    response = requests.post(API_URL, data = json.dumps({"text": input_text}))

    # Check if the request was successful
    if response.ok:
        global summary_text
        # Extract the response data
        response_data = response.json()
        summary_text = response_data['summary']

        # Display the response data
        # output_text.text(response_data["output"])
    else:
        # Display an error message
        st.error(f"API request failed with status code {response.status_code}")
    
    return summary_text


def generate_abstractive_summary(input_text):
    # Code to generate extractive summary
    # Through Extractive Summary generation code's API call
    return input_text


# Define UI Elements
st.title("Hindi Text Summarization(NLP)")
input_text = st.text_area("Enter text to summarize : ")
output_text = st.empty()
summary_type = st.selectbox("Choose Summary Type : ", ["Extractive Summary", "Abstractive Summary"])
# copy_button = st.button("Copy Summary to Clipboard")
summary = ""

# Generate summary when button is clicked
if st.button("Generate Summary"):
    if summary_type == "Extractive Summary":
        summary = generate_extractive_summary(input_text)
    elif summary_type == "Abstractive Summary":
        summary = generate_abstractive_summary(input_text)
    else:
        summary = "Invalid summary type selected"

# Display output text box
if summary:
    st.subheader("Summary:")
    st.write(summary)