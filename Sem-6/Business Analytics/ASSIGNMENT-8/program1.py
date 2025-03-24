from sklearn.base import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load data
df = pd.read_csv('business_data.csv')

# Encode
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

# Split
X = df.drop('Promotion', axis=1)
y = df['Promotion']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = DecisionTreeClassifier(max_depth=5, min_samples_split=4, criterion='entropy')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Show tree
print(export_text(model, feature_names=X.columns.tolist()))