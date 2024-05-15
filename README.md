#Study Smart, Live Well: The Canadian Student's Cost-of-Living Tool

A Streamlit-powered cost-of-living calculator designed to help students in Canada make informed decisions about where to live and study based on their budget and lifestyle preferences.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)


## Project Description

Study Smart, Live Well: The Canadian Student's Cost-of-Living Tool leverages the power of the Gemini Pro AI model to estimate the monthly expenses students can expect in various Canadian cities. By considering factors like housing, transportation, food, and user-specified preferences, this tool provides personalized insights into affordability and budgeting.

## Features

- **Personalized cost estimation:** Tailored to the user's income and preferences.
- **City-specific data:** Utilizes up-to-date information on living costs in Canadian cities.
- **Budget analysis:** Evaluates whether estimated expenses fit within the user's income.
- **Easy-to-use interface:** Simple Streamlit web app for seamless interaction.
- **Potential for expansion:** Can be enhanced with additional features like:
    - Detailed breakdowns of expense categories
    - Comparison of multiple cities
    - Savings goal tracking
    - Recommendation engine for affordable housing options

## Installation

1. **Clone the repository:** `git clone https://github.com/lakshaya17/StudentHousingCanada.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set up environment variables:**
    - Create a `.env` file in the project directory.
- Add your Google API key: `GOOGLE_API_KEY=your_api_key`

## Usage

1. **Run the app:** `streamlit run app.py`
2. **Enter city, income, and preferences:** Fill in the input fields in the web app.
3. **Click "Calculate":** Get an instant cost-of-living estimation and budget analysis.

## Technologies Used

- **Google Gemini Pro:** Language model for AI-powered estimations.
- **LangChain:** Framework for connecting the language model to the app.
- **Streamlit:** Web app framework for easy UI development.
  You can check on: https://studenthousingcanada.streamlit.app/ 
- **Python:** Programming language for the backend logic.
