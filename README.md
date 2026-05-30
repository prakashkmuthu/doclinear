# Linear Regression Prediction App

## Project Overview

This project demonstrates an end-to-end Machine Learning application using:

* Scikit-Learn
* FastAPI
* Streamlit
* Git & GitHub

The application trains a Linear Regression model using data from a CSV file, exposes predictions through a FastAPI backend, and provides a user-friendly Streamlit frontend.

## Project Structure

* data.csv
* train.py
* main.py
* app.py
* model.pkl
* requirements.txt
* .gitignore

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* FastAPI
* Streamlit
* Git
* GitHub

## How to Run

1. Create virtual environment

   `python -m venv venv`

2. Activate virtual environment

   `venv\Scripts\activate`

3. Install dependencies

   `pip install -r requirements.txt`

4. Train model

   `python train.py`

5. Start FastAPI

   `uvicorn main:app --reload`

6. Start Streamlit

   `streamlit run app.py`

## Sample Input

Feature 1 = 2

Feature 2 = 20

## Sample Output

Prediction = 30

## Future Enhancements

* Docker Containerization
* AWS Deployment
* GitHub Actions
* MLflow
* DVC
