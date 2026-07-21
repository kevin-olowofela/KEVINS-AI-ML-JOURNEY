import numpy as np

# Dataset
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

mean = np.mean(X, axis=0)

X_centered = X - mean

covariance_matrix = np.cov(X_centered, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

sorted_indices = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

k = 1

principal_components = eigenvectors[:, :k]

X_reduced = X_centered @ principal_components

print("Eigenvalues")
print(eigenvalues)
print()

print("Principal Components")
print(principal_components)
print()

print("Reduced Dataset")
print(X_reduced)