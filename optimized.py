# Optimized: Remove redundancy
import time


start_time = time.time()
C_optimized = A @ B
C_optimized += C_optimized  # Reuse result
optimized_time = time.time() - start_time
print(f"Optimized time without redundancy: {optimized_time:.4f} seconds")
