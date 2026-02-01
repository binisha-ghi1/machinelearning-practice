# scaling: it ensures that all features contribute equally to the model
# by bringing them to a common scale. improving model performance,
#  for distance-based algorithms. z= (x- mean)/s.d


from sklearn.preprocessing import StandardScaler
import numpy as np

Z = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
Z_scaled = scaler.fit_transform(Z)
print(Z_scaled)