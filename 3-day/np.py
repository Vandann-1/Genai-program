
import numpy as np

# Create a one-dimensional array
scores = np.array([70, 85, 90, 65, 80])

print("Scores:", scores)
print("Shape:", scores.shape)
print("Average:", scores.mean())
print("Maximum:", scores.max())
print("Above 75:", scores[scores > 75])

# Create a two-dimensional array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix shape:", matrix.shape)
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
