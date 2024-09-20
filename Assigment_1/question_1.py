import pandas as pd

auto_mpg_data = pd.read_csv('Assigment_1\AutoMPG.csv')
print(auto_mpg_data.head())

#(a):

auto_mpg_data['horsepower'] = pd.to_numeric(auto_mpg_data['horsepower'], errors='coerce')
mean_horsepower = auto_mpg_data['horsepower'].mean()
auto_mpg_data['horsepower'].fillna(mean_horsepower, inplace=True)

auto_mpg_data = pd.get_dummies(auto_mpg_data, columns=['cylinders', 'origin'], prefix=['cyl', 'origin'])

numeric_data = auto_mpg_data.select_dtypes(include=['float64', 'int64'])

Q1 = numeric_data.quantile(0.25)
Q3 = numeric_data.quantile(0.75)
IQR = Q3 - Q1

auto_mpg_data_cleaned = auto_mpg_data[~((auto_mpg_data < (Q1 - 1.5 * IQR)) | (auto_mpg_data > (Q3 + 1.5 * IQR))).any(axis=1)]

output_file_path = 'Assigment_1\AutoMPG_cleaned.csv'
auto_mpg_data.to_csv(output_file_path, index=False)