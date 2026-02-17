import pandas as pd  
data = {'Ad_Spend': [100, 200, 300, 400], 'Sales': [400, 600, 800, 1000]} 
df = pd.DataFrame(data) 
correlation = df.corr()     
print(correlation) 