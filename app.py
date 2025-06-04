import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.schema import HumanMessage

# Load API key from .env file 
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY') # Enter you Google API here
genai.configure(api_key=API_KEY)

model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

# Function to get user input
def get_user_input():
    city = st.text_input("Enter the city in Canada:")
    income = st.number_input("Enter your expected monthly income (CAD):", min_value=0)
    preferences = st.text_area("Enter your preferences (housing, transportation, etc.). You can input multiple preferences as well:")
    return city, income, preferences

# Function to get cost of living estimation from Gemini Pro 
#def get_cost_of_living_estimation(city, income, preferences):
#    prompt = f"Estimate the monthly cost of living for a student in {city}, Canada. Assuming a monthly income of ${income}, estimate the cost of preferences ${preferences}. Consider only the specified preferences and exclude other expenses such as utilities or entertainment. Conclude by analyzing whether the estimated expenses are within the user's budget based on their income."

def get_cost_of_living_estimation(city, income, preferences):
    """
    Generates a detailed prompt for estimating the monthly cost of living for a student.

    Args:
        city (str): The specific city in Canada where the student will live (e.g., "Toronto, Ontario").
        income (float): The student's estimated monthly income in Canadian dollars.
        preferences (dict): A dictionary of specific living preferences and their estimated costs.
                           Keys should be categories (e.g., "Rent (1-bedroom apartment)", "Groceries", "Public Transit Pass")
                           and values should be estimated monthly costs in CAD.
                           Example: {"Rent (shared accommodation)": 800, "Groceries": 350, "Public Transit Pass": 150}
    """

    prompt = f"""
    Please provide a comprehensive and detailed estimation of the *monthly* cost of living for a student residing in {city}, Canada.

    The student has an estimated *monthly income* of ${income:.2f} CAD.

    Crucially, I need you to *focus exclusively* on the following specified preferences and their estimated costs. Please break down the expenses for each preference explicitly:

    """

    for preference, cost in preferences.items():
        prompt += f"- {preference}: ${cost:.2f} CAD (User's estimated cost)\n"

    prompt += f"""

    **IMPORTANT:** Please *exclude* all other expenses not explicitly listed above, such as:
    - Utilities (electricity, heating, internet, water)
    - Entertainment and leisure activities
    - Personal care products
    - Clothing
    - Health insurance or medical expenses
    - Textbooks and academic supplies
    - Travel outside of specified public transit
    - Miscellaneous unforeseen expenses

    Your response should clearly present:

    1.  A detailed breakdown of the *total estimated monthly expenses* based *only* on the provided preferences.
    2.  A clear and concise conclusion analyzing whether the total estimated expenses are within the student's stated monthly income of ${income:.2f} CAD.
    3.  If the expenses exceed the income, suggest which preference categories might be adjusted to fit the budget, given the provided estimates. If they are within budget, state how much surplus remains.

    Please present the information in an easy-to-read format, perhaps using bullet points or a table for the breakdown.
    """
    return prompt
    

    # Use the correct method for text generation
    message = HumanMessage(content=prompt)
    response = model([message])
    estimated_expenses = response.content
    return estimated_expenses

# Function to display the results
def display_results(estimated_expenses):
    st.subheader("Estimated Monthly Expenses:")
    st.write(estimated_expenses)
    

def main():

    
    
    st.header("Study Smart, Live Well: The Canadian Student's Cost-of-Living Tool")

    

     # Get user input
    city, income, preferences = get_user_input()
    # Calculate and display results when the button is clicked
    if st.button("Calculate"):
        if city and income and preferences:
                with st.spinner("Calculating..."):
                     estimated_expenses = get_cost_of_living_estimation(city, income, preferences)
                     display_results(estimated_expenses)
        else:
             st.warning("Please fill in all fields.")
    
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: lightgray;  /* Adjust color if desired */
        color: black;   /* Adjust color if desired  */
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>Created By Lakshay Arora. Powered by Google Gemini.</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
