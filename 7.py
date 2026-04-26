import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
df = sns.load_dataset('iris') 
sns.boxplot(data=df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]) 
plt.title("Box Plot of Iris Features") 
plt.show() 
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', palette='deep') 
plt.title("Scatter Plot of Sepal Length vs Width by Species") 
plt.show() 
sns.histplot(data=df, x='sepal_length', hue='species', multiple='stack', bins=20, palette='muted') 
plt.title("Histogram of Sepal Length by Species") 
plt.xlabel("Sepal Length") 
plt.ylabel("Frequency") 
plt.show()    