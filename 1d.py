import statsmodels.api as sm 
import numpy as np 
X = np.array([1, 2, 3, 4, 5])   
y = np.array([1.2, 1.9, 3.2, 3.8, 5.1])  
X = sm.add_constant(X)   
model = sm.OLS(y, X)    
results = model.fit() 
print(results.summary())   
predicted = results.predict(X)   
print("\nPredicted values:", predicted) 