import pandas as pd
import os                  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

if not os.path.exists('./results'):
  os.makedirs('results', exist_ok=True)

columns = ["Class", "Alcohol", "Malic Acid", "Ash", "Alcalinity of Ash", "Magnesium", 
                "Total Phenols", "Flavanoids", "Nonflavanoid Phenols", "Proanthocyanins", 
                "Color Intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
df=pd.read_csv("./data/wine/wine.data", names=columns, sep=',')


summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

classification_rep = classification_report(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("\nClassification Report:")
print(classification_rep)
print(f"\nAccuracy: {accuracy:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(X_test['Alcohol'], X_test['Color Intensity'], c=y_test, cmap='viridis', edgecolors='k')
plt.title('Wine Classification based on Alcohol and Color Intensity')
plt.xlabel('Alcohol')
plt.ylabel('Color Intensity')
plt.show()

summary_stats.to_csv('results/summary_statistics.csv')
with open('results/classification_report.txt', 'w') as f:
    f.write(classification_rep)
plt.savefig('results/wine_classification_plot.pdf')
