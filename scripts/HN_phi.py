import math

# Define constants
phi = (1 + math.sqrt(5)) / 2
root5 = math.sqrt(5)
scale = 100 * root5 * phi

# Initialize variables
total_sum = 0
terms = []

# Compute and print first 12 terms
print("HN_phi Series (First 12 Terms):")
for k in range(1, 24):
    sign = (-1)**(k + 1)
    term_phi = sign / (phi**k)
    term_scaled = sign / (scale**k)
    term = term_phi + term_scaled
    total_sum += term
    terms.append((k, term, total_sum))
    print(f"k={k:<2} term={term: .12f}  partial_sum={total_sum: .12f}")
