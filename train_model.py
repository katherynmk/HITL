# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

# Simulated training data: volume (orders), rate (orders/hour), output: staff needed
data = {
    'volume': [500, 800, 1000, 1500, 2000, 2500],
    'rate': [50, 55, 60, 65, 70, 75],
    'staff_needed': [10, 12, 14, 18, 22, 26]  # Example staffing levels
}

df = pd.DataFrame(data)

# Features and target
X = df[['volume', 'rate']]
y = df['staff_needed']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save model to .pkl file
joblib.dump(model, 'model.pkl')

print("Model saved to model.pkl")
