import numpy as np

# Transition matrix
A = np.array([
    [0.0, 0.5, 0.5],
    [1/3, 0.0, 0.5],
    [2/3, 0.5, 0.0]
])

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print()

# Find eigenvalue closest to 1
index = np.argmin(np.abs(eigenvalues - 1))

pagerank = eigenvectors[:, index].real

# Normalize
pagerank = pagerank / np.sum(pagerank)

print("Stationary Distribution")
print(pagerank)
print()

# Ranking
ranking = np.argsort(-pagerank)

print("Page Ranking")
for i, page in enumerate(ranking):
    print(f"{i+1}. Page {page+1} : {pagerank[page]:.4f}")