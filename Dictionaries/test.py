import numpy as np

def kmeans(X, k, max_iterations=100):
    # Initialize the centroids randomly
    centroids = X[np.random.choice(X.shape[0], k, replace=False), :]
    for i in range(max_iterations):
        # Compute distances between each data point and the centroids
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        # Assign each data point to the nearest centroid
        labels = np.argmin(distances, axis=0)
        # Update the centroids to be the mean of the data points assigned to each cluster
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        if np.all(centroids == new_centroids):
            # The centroids have stopped moving, so we have converged
            break
        centroids = new_centroids
    return centroids, labels
  
# Generate sample data
np.random.seed(0)
X = np.random.rand(20, 2)
X=X*10
print("Input X\n",X)

# Run k-means on the sample data
requiredcentroids=int(input("no of centroids\n"))
centroids, labels = kmeans(X, k=requiredcentroids)
print("Centroids\n",centroids,"\nLabels\n",labels)
import matplotlib.pyplot as plt

# Plot the data points
for label in np.unique(labels):
    print("X=\n",X[labels == label, 0])
    print("Y=\n", X[labels == label, 1])
    plt.scatter(X[labels == label, 0], X[labels == label, 1])
    plt.plot(X[labels == label, 0], X[labels == label, 1], label=f"Cluster {label}")

# Plot the final centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=200, linewidths=3, color="pink", label="Centroids")

plt.legend()
plt.show()
