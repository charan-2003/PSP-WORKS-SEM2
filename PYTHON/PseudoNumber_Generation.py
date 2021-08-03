import numpy as np

samples = np.random.normal(size=(4, 4))

print(samples)
print(np.random.seed(1234))
rng = np.random.RandomState(1234)
print(rng.randn(10))
