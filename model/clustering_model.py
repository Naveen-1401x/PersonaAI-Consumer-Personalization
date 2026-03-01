import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("../dataset/sample_dataset.csv")

# Select features
X = data[['time_spent', 'clicks', 'avg_spend']]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['persona'] = kmeans.fit_predict(X_scaled)

print("Clustered Data:")
print(data)
