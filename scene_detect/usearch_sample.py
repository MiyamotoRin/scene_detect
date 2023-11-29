import numpy as np
from usearch.index import Index, Matches

index = Index(
    ndim=3, # Define the number of dimensions in input vectors
    metric='cos', # Choose 'l2sq', 'haversine' or other metric, default = 'ip'
    dtype='f32', # Quantize to 'f16' or 'i8' if needed, default = 'f32'
    connectivity=16, # How frequent should the connections in the graph be, optional
    expansion_add=128, # Control the recall of indexing, optional
    expansion_search=64, # Control the quality of search, optional
)

vector = np.array([0.2, 0.6, 0.4])
print(vector)
print(vector.shape)
index.add(42, vector, log=True)
matches: Matches = index.search(vector, 10)

assert len(index) == 1
assert len(matches) == 1
assert matches[0].key == 42
assert matches[0].distance <= 0.001
assert np.allclose(index[42], vector)
