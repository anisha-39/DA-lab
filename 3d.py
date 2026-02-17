from scipy.optimize import linprog  
c = [20, 30]  
A = [[1, 1]] 
b = [100] 
result = linprog(c, A_eq=A, b_eq=b, method='highs') 
print("Optimal Solution:", result.x) 