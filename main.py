import streamlit as st
import logging
import requests
from dotenv import load_dotenv
import os
import time
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Load environment variables from a .env file
load_dotenv()

# Retrieve API key and other necessary variables from environment variables
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_SERVICE_URL')
project_id = os.getenv('IBM_PROJECT_ID')

# Set up the authenticator
authenticator = IAMAuthenticator(api_key)

# Function to call the IBM Watson API
def generate_content(input_text, access_token):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    body = {
        "input": input_text,
        "parameters": {
            "decoding_method": "sample",
            "max_new_tokens": 500,
            "temperature": 0.3,
            "top_k": 40,
            "top_p": 0.9,
            "repetition_penalty": 1.1
        },
        "model_id": "ibm/granite-13b-chat-v2",
        "project_id": project_id
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} , {response.text}")

    return response.json()

# Typing effect for gradual text display
def typing_effect(text, delay=0.005):  # Adjusted speed
    displayed_text = ""  
    text_display = st.empty()  

    for char in text:
        displayed_text += char  
        text_display.markdown(f"{displayed_text}")  
        time.sleep(delay)  

# Retrieve the access token from the IAMAuthenticator
access_token = os.getenv('IBM_Access_Token')

# Set up the Streamlit app layout
st.set_page_config(page_title="AI-Driven Content Creation", layout="centered")

st.markdown(
    """
    <style>
    h1, h2, h3 {
        color: #2E8B57;
    }
    .stButton > button {
        background-color: #2E8B57;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Company Details", "Content Generation"])

if selection == "Company Details":
    with st.container():
        st.title("Company Details")
        st.write("Provide your company details to help the AI generate personalized content.")

        company_name = st.text_input("Company Name", st.session_state.get('company_name', ''))
        industry_type = st.selectbox("Industry Type", ["Technology", "Healthcare", "Finance", "Education", "Retail", "Other"], index=st.session_state.get('industry_type_idx', 0))
        target_audience = st.selectbox("Target Audience", ["B2B", "B2C", "Millennials", "Gen Z", "Parents", "Professionals", "Students", "Retirees"], index=st.session_state.get('target_audience_idx', 0))
        brand_voice = st.selectbox("Brand's Voice and Tone", ["Professional", "Casual", "Playful", "Formal", "Friendly"], index=st.session_state.get('brand_voice_idx', 0))
        key_products = st.text_area("Key Products/Services", st.session_state.get('key_products', ''))

        if st.button("Save Company Details"):
            st.session_state['company_name'] = company_name
            st.session_state['industry_type'] = industry_type
            st.session_state['industry_type_idx'] = ["Technology", "Healthcare", "Finance", "Education", "Retail", "Other"].index(industry_type)
            st.session_state['target_audience'] = target_audience
            st.session_state['target_audience_idx'] = ["B2B", "B2C", "Millennials", "Gen Z", "Parents", "Professionals", "Students", "Retirees"].index(target_audience)
            st.session_state['brand_voice'] = brand_voice
            st.session_state['brand_voice_idx'] = ["Professional", "Casual", "Playful", "Formal", "Friendly"].index(brand_voice)
            st.session_state['key_products'] = key_products
            st.success("Company details saved successfully!")

elif selection == "Content Generation":
    with st.container():
        st.title("AI-Driven Content Generation")

        # Retrieve values from session state
        company_name = st.session_state.get('company_name', '')
        industry_type = st.session_state.get('industry_type', '')
        target_audience = st.session_state.get('target_audience', '')
        brand_voice = st.session_state.get('brand_voice', '')

        service_type = st.selectbox("Choose the type of content to generate:", 
                                    ["Social Media Post", "Email", "Ad Copy"])

        if service_type in ["Social Media Post", "Ad Copy"]:
            product_name = st.text_input("Product Name", st.session_state.get('product_name', ''))
            product_description = st.text_area("Product Description", st.session_state.get('product_description', ''))
            product_audience = st.selectbox("Product Audience", ["B2B", "B2C", "Millennials", "Gen Z", "Parents", "Professionals", "Students", "Retirees"], index=st.session_state.get('product_audience_idx', 0))
            product_features = st.text_area("Key Features/Benefits of the Product", st.session_state.get('product_features', ''))

        elif service_type == "Email":
            customer_name = st.text_input("Customer Name", st.session_state.get('customer_name', ''))
            customer_age = st.number_input("Customer Age", min_value=18, max_value=100, step=1, value=st.session_state.get('customer_age', 18))
            customer_interests = st.text_area("Customer Interests (comma-separated)", st.session_state.get('customer_interests', ''))
            product_name = st.text_input("Product Name", st.session_state.get('product_name', ''))
            product_features = st.text_area("Key Features/Benefits of the Product", st.session_state.get('product_features', ''))

        if st.button("Generate Content"):
            try:
                if service_type in ["Social Media Post", "Ad Copy"]:
                    input_text = f"""
                    Generate a high-quality {service_type.lower()} focusing on revenue-generating strategies for {company_name}. 
                    The {service_type.lower()} should align with the {brand_voice.lower()} voice and target {product_audience} audience. 
                    For the {service_type.lower()}:
                    - Use the following product details: {product_name}, {product_description}.
                    - Highlight key features: {product_features}.
                    - Ensure that the content is engaging, persuasive, and optimized for conversions.
                    - Include a call-to-action relevant to {company_name}.
                    """
                elif service_type == "Email":
                    input_text = f"""
                    Write a personalized email for a customer named {customer_name}, aged {customer_age}, interested in {customer_interests}. 
                    The email is from {company_name}, and it should promote {product_name}. 
                    The email should:
                    - Address the customer directly by name.
                    - Mention their specific interests to create a personal connection.
                    - Highlight the key features and benefits of {product_name}.
                    - Encourage the customer to take action (e.g., make a purchase, learn more).
                    - Maintain a {brand_voice.lower()} tone.
                    """

                with st.spinner('Generating content...'):
                    response = generate_content(input_text, access_token)

                if 'results' in response and len(response['results']) > 0:
                    generated_text = response['results'][0].get('generated_text', '')

                    if generated_text:
                        st.subheader(f"Generated {service_type}")

                        formatted_text = generated_text.replace('\n', '\n\n')
                        typing_effect(formatted_text)
                    else:
                        st.error("No generated text found in the response.")
                else:
                    st.error("The response does not contain the expected 'results' structure. Please check the response data.")

                # Real-time actionable recommendations
                recommendation_input_text = f"""
                Provide three real-time actionable recommendations based on the latest trends in the {industry_type} industry to enhance the marketing strategy for {company_name}.
                """

                with st.spinner('Generating recommendations...'):
                    recommendation_response = generate_content(recommendation_input_text, access_token)

                if 'results' in recommendation_response and len(recommendation_response['results']) > 0:
                    recommendations_text = recommendation_response['results'][0].get('generated_text', '')

                    if recommendations_text:
                        st.subheader("Content Strategy Recommendations")

                        formatted_recommendations = recommendations_text.replace('\n', '\n\n')
                        typing_effect(formatted_recommendations)
                    else:
                        st.error("No generated recommendations found in the response.")
                else:
                    st.error("The response does not contain the expected 'results' structure. Please check the response data.")

            except Exception as e:
                logging.error(f"Error generating content: {str(e)}")
                st.error(f"Error: {str(e)}. Please try again or contact support.")
