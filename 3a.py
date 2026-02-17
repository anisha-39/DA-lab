import pandas as pd 
data = { 
"Name": ["Alice", "Bob", "Charlie", "David", "Eve"], 
"Age": [25, 30, 35, 40, 28], 
"Salary": [50000, 54000, 58000, 62000, 52000], 
"Department": ["HR", "IT", "Finance", "IT", "HR"] 
} 
df = pd.DataFrame(data) 
print("DataFrame:\n", df)  
print("\nBasic Statistics:\n", df.describe()) 
print("\nCount of Unique Values in Each Column:\n", df.nunique())  
print("\nData Type Information:\n") 
df.info() 
grouped = df.groupby("Department")["Salary"].mean() 
print("\nAverage Salary by Department:\n", grouped)