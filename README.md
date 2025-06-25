# CodeClauseInternship-Heart-Disease-Risk-Assessment

A golden-level data science project for assessing heart disease risk using machine learning and an interactive user interface. Built with Streamlit and scikit-learn as part of the **CodeClause Data Science Internship**.

## What This Project Does

- Creates a user-friendly interface for inputting health data using **Streamlit**.
- Accepts 13 health-related metrics from the user (like age, cholesterol, heart rate, etc.).
- Uses a trained **Random Forest Classifier** to predict the risk of heart disease.
- Displays clear feedback on whether the user is at high or low risk.
- Built to support a real-world health assessment experience.

## Technologies Used

- **Programming Language**: Python  
- **Libraries & Tools**:
  - [Streamlit](https://streamlit.io/) – for building the interactive UI
  - [Scikit-learn](https://scikit-learn.org/) – for training the classification model
  - [Pandas](https://pandas.pydata.org/) – for data handling
  - [NumPy](https://numpy.org/) – for numerical input and transformations

## Project Structure

### 1. Dataset
- Based on the publicly available [UCI Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- Contains 13 features and 1 target column indicating disease presence (1) or absence (0)

### 2. Model Training
- `model_training.py` script loads the dataset, splits it, trains a **Random Forest** classifier, and saves the model as `model.pkl`

### 3. User Interface
- `app.py` builds a form using sliders and dropdowns for each health parameter
- On clicking **Predict**, the model analyzes the inputs and returns either:
  - ⚠️ High risk of heart disease
  - ✅ Low risk of heart disease

### 4. Output
- The prediction is displayed directly in the browser
- No need for technical knowledge to use the app

## How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CodeClauseInternship-Heart-Disease-Risk-Assessment-4-.git
cd CodeClauseInternship-Heart-Disease-Risk-Assessment
