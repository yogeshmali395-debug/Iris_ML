import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("C:/Users/admin/Desktop/iris.csv")

print(df.head())

print(df.shape)

print(df.describe)

print(df.info())

print(df.columns)

print(df.isnull().sum())

print(df['species'].value_counts())

X = df.drop("species", axis=1) # X = features (input)
y = df["species"] # y = target (output)

# species string me hai (setosa, etc.), to encode karna padega.
# from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split (X,y, test_size=0.2, random_state=42)

# from sklearn.preprocessing import StandardScaler
# common mistake ==> ❌ scaling test pe fit karna

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=X.columns ) # SAME column names
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
print("Flower:", le.inverse_transform(prediction))

print(model.predict_proba(new_data_scaled))

print("Coefficients:\n", model.coef_)

# Class-wise meaning
# 👉 Class 0 (setosa)
# [-1.00, +1.14, -1.81, -1.70]
# petal length & width → strong negative
# 👉 petal chhota → setosa ✔️
# 👉 Class 1 (versicolor)
# [+0.53, -0.28, -0.34, -0.71]
# sab moderate values
# 👉 middle type flower
# 👉 Class 2 (virginica)
# [+0.47, -0.85, +2.15, +2.41]
# petal length & width → strong positive 🔥
# 👉 petal bada → virginica ✔️

print("Intercept:\n", model.intercept_)

# from sklearn.metrics import confusion_matrix
# Confusion Matrix hamesha target (labels) par hi lagti hai, features par nahi.

cm = confusion_matrix(y_test, y_pred)
print(cm)

# from sklearn.metrics import classification_report

# Precision = correct predictions / total predicted

# 👉 Example:
# model ne bola 10 baar “setosa”
# usme se 10 sahi → precision = 1.0
# Meaning: "jab model ne bola ye class hai, kitni baar sahi tha?"

# Recall = correct predictions / total actual

# 👉 Example:
# actual me 10 setosa the
# model ne sab pakad liye → recall = 1.0
# Meaning: "jo real me tha, usme se kitna pakda?"

# F1 = balance of precision & recall
# Jab dono perfect → F1 = 1.0
# 💡 Meaning: "overall performance"

# support = kitne samples the us class ke 
# Example: setosa = 10 samples

print(classification_report(y_test, y_pred))