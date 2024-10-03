# COVID-19 Data Analysis Project

## Introduction

This project involves the exploratory data analysis of COVID-19 datasets. The analysis aims to investigate various relationships and trends related to COVID-19 hospitalizations, deaths, and the socioeconomic impact on different demographics and job fields.

## Project Structure

Statistical-Inference-Project/
├── Datasets/
│ ├── DS-1/
│ │ ├── data_dictionary_covid_cases_public_use.xlsx
│ │ ├── dataset_1_link.txt
│ ├── DS-2/
├── Src/
│ ├── dataset1.ipynb
│ ├── full_Rep.ipynb
│ ├── Q1.ipynb
│ ├── Q2.ipynb
│ ├── Q3.ipynb
│ ├── Question 4 Regression Analysis.ipynb
│ ├── Question1.ipynb
├── .gitignore

## Technical Steps

### 1. Setup

#### Install Dependencies

Make sure you have Python and pip installed. Install the required libraries using the following command:

```bash
pip install pandas geopandas matplotlib plotly
```
## 2. Data Import
The data was imported from CSV files using the pandas library. Specific columns relevant to the analysis were selected to maintain focus and clarity. The columns were imported as “category” data types in pandas to ensure efficient and quick analysis.

## 3. Data Cleaning
Data cleaning involved several steps to ensure accuracy and reliability:

Filtering rows with missing, unknown, or irrelevant data.
Managing categories by removing unused categories from categorical variables.
Converting the case_month column to datetime format to facilitate time-series analysis.
Labeling categorical variables appropriately to enhance readability and interpretation.
## 4. Data Visualization
Visualization was a key component of the analysis, enabling the identification of trends and patterns. The seaborn, matplotlib, and plotly libraries were used to create various plots:

Bar (Histogram) Plots: To compare percentages of hospitalizations, deaths, and employment loss across different categories.
Line Plots: To visualize trends over time for hospitalizations and deaths.
KDE Plots: To show the density distribution of hospitalizations and deaths over time.
Choropleth Maps: To visualize the percentage of Economic Impact Payment (EIP) recipients by state.
# 5. Statistical Analysis
Statistical methods, such as the chi-square test, were used to test hypotheses and assess the significance of observed relationships.

Example Analysis and Visualization
Below is an example of how to create a choropleth map using Plotly to visualize the percentage of EIP recipients by state:

## Conclusion
The exploratory data analysis reveals significant insights into the impact of COVID-19 across different demographics and socioeconomic groups. The findings show higher risks for older individuals with underlying conditions, varying hospitalization and death rates across states, and significant challenges faced by lower-income households and certain racial groups.

For detailed analysis and results, please refer to the Jupyter notebooks in the Src directory.




