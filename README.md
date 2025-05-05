
# 📊 Internship Application Data Cleaning Project

This project demonstrates a full **data cleaning and preprocessing pipeline** using Python and Pandas. The dataset simulates internship application data including applicant details, skills, and experience. The goal is to prepare the data for efficient analysis by handling missing values, duplicates, outliers, and standardizing formats.

---

## 🧱 Project Steps

### 1. 📁 Dataset Creation
A synthetic dataset is created using Python’s `pandas` and `numpy` libraries. It includes:
- Applicant demographics (Name, Age, Degree)
- Contact info (Email)
- Skills (e.g., Python, SQL, Excel)
- Experience (in years)

---

### 2. 🧼 Handling Missing Values
Missing entries are filled with appropriate defaults:
- Names → `"unknown"`
- Age → Replaced with column mean
- Skills → `"unknown"`

This ensures consistency and avoids null-related errors during analysis.

---

### 3. 🔁 Removing Duplicates
Duplicate rows are detected and dropped using `drop_duplicates()`.  
This ensures that each applicant entry is unique.

---

### 4. 📉 Outlier Detection and Removal
The Interquartile Range (IQR) method is used to detect and remove outliers from the `Age` column:
- Q1 and Q3 calculated
- Outliers beyond `1.5 * IQR` are filtered out

This helps keep the dataset within a realistic and reliable range.

---

### 5. 🧹 Standardization and Feature Engineering
- Degree names are standardized to uppercase.
- Skill strings are lowercased and stripped of extra spaces.
- Skills are split and converted into dummy (binary) columns using one-hot encoding for analysis.

---

## 📦 Technologies Used
- Python
- Pandas
- NumPy

---

## 📁 Project Files
- `data_cleaning.py` – Python script with all 5 data cleaning steps.
- `README.md` – Project documentation.

---

## ✅ Output
The cleaned dataset includes:
- Standardized skill columns (Python, SQL, Excel)
- No missing or duplicate data
- No outliers in age
- Ready-to-analyze format

---

## 🚀 How to Run

1. Clone this repository
2. Run the script using:
```bash
python data_cleaning.py
```
