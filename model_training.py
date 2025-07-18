import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv('heart.csv')

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Split data (with stratify to balance classes)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Predictions on sample data:", model.predict(X_test[:20]))
print("Actual values:", y_test[:20].values)
