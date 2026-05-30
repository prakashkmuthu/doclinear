from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

# Read data from CSV
df = pd.read_csv("data.csv")

# Separate inputs and output
X = df.drop(columns=["target"])
y = df["target"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")