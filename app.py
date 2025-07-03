import streamlit as st
import requests
import os

st.title("Maternal Health Assistant (Kiswahili)")

user_input = st.text_area("Enter your maternal health question in Kiswahili:", "")

def query(payload):
    # Retrieve API token from Streamlit secrets
    api_token = st.secrets["HF_API_TOKEN"]
    # Alternatively, if using environment variables: api_token = os.getenv("HF_API_TOKEN")


    API_URL = "https://api-inference.huggingface.co/models/wibonela/maternal-assistant-llm"
    headers = {"Authorization": f"Bearer {maternal-assistant-llm}"}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if st.button("Get Response"):
    if user_input:
        with st.spinner("Getting response..."):
            # Wrap the input in the required format for the API
            payload = {"inputs": user_input}
            output = query(payload)

            # Check if the response is valid and display it
            if output and isinstance(output, list) and "generated_text" in output[0]:
                st.write("### Response:")
                st.write(output[0]["generated_text"])
            else:
                st.error("Could not get a valid response. Please try again later.")
                if output:
                    st.write("API response:")
                    st.write(output) # Display raw output for debugging
    else:
        st.warning("Please enter a question.")
