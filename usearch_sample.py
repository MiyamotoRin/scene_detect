import numpy as np
from usearch.index import Index

index = Index(ndim=3)

vector = np.array([0.2, 0.6, 0.4])
index.add(42, vector)

matches = index.search(vector, 10)

assert matches[0].key == 42
assert matches[0].distance <= 0.001
assert np.allclose(index[42], vector)
