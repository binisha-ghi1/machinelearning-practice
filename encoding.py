from sklearn.preprocessing import LabelEncoder
data = ["red", "blue", "blue", "red"]
le = LabelEncoder()
encoded = le.fit_transform(data)
print(encoded)