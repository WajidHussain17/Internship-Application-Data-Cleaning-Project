import pandas as pd
import numpy as np

# Sample dataset creation
data = {
    'Applicant_ID': [101, 102, 103, 104, 105, 106, 107, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', np.nan, 'Frank'],
    'Age': [22, 24, np.nan, 23, 21, 25, 24, 25],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 
              'eva@example.com', 'frank@example.com', 'frank@example.com', 'frank@example.com'],
    'Degree': ['BSc', 'MSc', 'BSc', 'BSc', 'MSc', 'BSc', 'MSc', 'MSc'],
    'Skills': ['Python,SQL', 'Excel,SQL', np.nan, 'Python', 'Excel', 'Python,Excel', 'SQL', 'SQL'],
    'Experience(Years)': [0, 1, 2, 1, 0, 3, 1, 1]
}

df = pd.DataFrame(data)
print(df)


# Check missing values
print(df.isnull().sum())


# Handle missing values
df['Name'] = df['Name'].fillna("unknown")
df['Age'] = df['Age'].fillna(df["Age"].mean())
df['Skills'] = df['Skills'].fillna("unknown")

print(df)



# Check for duplicates
print(df.duplicated())

# Drop duplicates
drop_duplicates = df.drop_duplicates()

print(drop_duplicates)

# Describe Data
print(df['Age'].describe())


# Define outliers threshold through IQR method

Q1= df['Age'].quantile(0.25)
Q3= df['Age'].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR

# Filterout the outliers
df = df[(df['Age']<lower) & (df["Age"]>upper)]


# Standardize column values
df['Degree'] = df['Degree'].str.upper()

df['Skills'] = df['Skills'].str.lower().str.strip()

# Convert Skills into dummy variables
skills_dummies = df['Skills'].str.get_dummies(sep=',')

# Merge with original dataset
df = pd.concat([df, skills_dummies], axis=1)

# Preview cleaned data
print(df.head())










