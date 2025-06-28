
from sympy import primerange

num_terms = 10000
primes = list(primerange(1, 200000))[:num_terms]

partial_sum = 1.6
for k, pk in enumerate(primes, start=1):
    term = 1 / ((pk / 4 + 1 / pk) / 2)
    signed_term = (-1) ** k * term
    partial_sum += signed_term
    if k <= 12 or k > num_terms - 12:
        print(f"k={k:<5} prime={pk:<7} term={signed_term:.10f} partial_sum={partial_sum:.10f}")
