import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('cars.csv')

# Encode categorical columns
le = LabelEncoder()
for column in ['brand','fuel','owner']:
    df[column] = le.fit_transform(df[column])

# Features and target
X = df.drop(columns=['selling_price'])
y = df['selling_price']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
clf = DecisionTreeClassifier(max_depth=5,random_state=42)
clf.fit(X_train,y_train)

# Accuracy
accuracy = clf.score(X_test,y_test)
print("Model Accuracy:",accuracy)

# Prediction report
y_pred = clf.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test,y_pred))

# Tree visualization
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=X.columns,filled=True)
plt.title("Decision Tree Visualization")
plt.show()
