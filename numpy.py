import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)

n_samples = 100
a = np.random.randint(0, 1000, n_samples)
b = np.random.randint(0, 1000, n_samples)
c = np.random.randint(0, 1000, n_samples)

X = np.column_stack([a, b, c])
y = a + 2*b + 3*c
