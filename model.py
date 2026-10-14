import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Read dataset
data = pd.read_csv("student_data.csv")

# Inputs
X = data[["StudyHours", "Attendance", "PreviousMarks"]]

# Output
y = data["Result"]

# Train model
model = DecisionTreeClassifier()

model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")