import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')  # Your Gemini API key here
genai.configure(api_key=API_KEY)

# Function to get user input
def get_user_input():
    city = st.text_input("Enter the city in Canada:")
    income = st.number_input("Enter your expected monthly income (CAD):", min_value=0)
    preferences = st.text_area("Enter your preferences (e.g., Housing, Transportation, Groceries):")
    return city, income, preferences

# Function to generate the Gemini prompt and get cost of living estimation
def get_cost_of_living_estimation(city, income, preferences_text):
    prompt = f"""
    You are an expert student advisor for cost-of-living in Canadian cities.

    A student is planning to live in **{city}**, Canada, and has an estimated **monthly income** of **${income:.2f} CAD**.

    The student has expressed the following **cost-of-living categories** to be considered:
    **{preferences_text.strip()}**

    **Instructions:**
    - Please provide a monthly cost estimate for each of the specified categories.
    - Use typical student budgets for {city}, but only for the listed preferences.
    - **Do NOT** include unrelated expenses (like healthcare, entertainment, insurance, etc.).
    - Clearly show:
        1. Breakdown of each category with estimated cost.
        2. Total estimated monthly cost.
        3. Final verdict on whether this budget is affordable within ${income:.2f} CAD.
        4. Suggestions if the cost exceeds income.

    Use bullet points or a table format for readability.
    """

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Function to display results
def display_results(estimated_expenses):
    st.subheader("Estimated Monthly Expenses:")
    st.write(estimated_expenses)

# Main app function
def main():
    st.header("Study Smart, Live Well: The Canadian Student's Cost-of-Living Tool")

    city, income, preferences = get_user_input()

    if st.button("Calculate"):
        if city and income and preferences:
            with st.spinner("Calculating..."):
                estimated_expenses = get_cost_of_living_estimation(city, income, preferences)
                display_results(estimated_expenses)
        else:
            st.warning("Please fill in all fields.")

    # Footer
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: lightgray;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>Created By Lakshay Arora. Powered by Google Gemini.</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()



