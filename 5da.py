import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp
from scipy.optimize import minimize
import statsmodels.api as sm
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Std Dev:", np.std(arr))
matrix = np.random.rand(3, 3)
print("\nMatrix:\n", matrix)
print("Transpose:\n", matrix.T)
print("Dot Product:\n", np.dot(matrix, matrix.T))
t_stat, p_value = ttest_1samp(arr, 3)
print("\nT-test:", t_stat, p_value)
result = minimize(lambda x: x**2 + 5, 0)
print("Optimization:", result.x)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("Summary:\n", df.describe())
with open("sample.txt", "w") as f:
    f.write("Name,Age,Salary\nAlice,25,50000\nBob,30,60000\nCharlie,35,70000")
print("\nText File:\n", pd.read_csv("sample.txt"))
df.to_excel("sample.xlsx", index=False)
print("\nExcel File:\n", pd.read_excel("sample.xlsx"))
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
print("\nWeb Data:\n", pd.read_csv(url).head())
X = sm.add_constant([4, 5, 6])
Y = [1, 2, 3]
model = sm.OLS(Y, X).fit()
print("\nOLS Summary:\n", model.summary())
