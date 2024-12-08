import numpy as np
import time

# Generate large matrices
size = 1000
A = np.random.rand(size, size)
B = np.random.rand(size, size)

# Baseline: Redundant multiplication
start_time = time.time()
C_baseline = A @ B  # NumPy's matrix multiplication
C_baseline += A @ B  # Redundant operation
baseline_time = time.time() - start_time
print(f"Baseline time with redundancy: {baseline_time:.4f} seconds")
