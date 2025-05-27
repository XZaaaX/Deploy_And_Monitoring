import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

data = {
    'IPK': [3.5, 2.7, 3.0, 2.5, 3.8],
    'Kehadiran': [90, 70, 85, 60, 95],
    'Organisasi': [1, 0, 1, 0, 1],
    'Lulus': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['IPK', 'Kehadiran', 'Organisasi']]
y = df['Lulus']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Akurasi: {accuracy_score(y_test, y_pred):.2f}")

joblib.dump(model, 'model_kelulusan.pkl')
