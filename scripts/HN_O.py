import math

def hn_O_series(n_terms=10000):
    terms = []
    partial_sum = 2.0
    partial_sums = [partial_sum]  # Include the starting offset
    display_terms = []

    for k in range(1, n_terms + 1):
        # Compute harmonic modular reflection term
        term = ((2 * k) / (2 * k - 1)) * ((2 * k + 1) / (2 * k + 2))
        signed_term = (-1)**k * term
        partial_sum += signed_term
        avg_sum = (partial_sum + partial_sums[-1]) / 2
        partial_sums.append(partial_sum)

        terms.append((k, term, signed_term, partial_sum, avg_sum))

    print("HN_O Series (First 12 Terms):")
    for i in range(12):
        k, term, signed, psum, avg = terms[i]
        print(f"k={k:<5} term={term:<13.10f}  partial_sum={psum:<13.10f}  avg={avg:<13.10f}")

    print("\nHN_O Series (Last 12 Terms):")
    for i in range(-12, 0):
        k, term, signed, psum, avg = terms[i]
        print(f"k={k:<5} term={term:<13.10f}  partial_sum={psum:<13.10f}  avg={avg:<13.10f}")

if __name__ == "__main__":
    hn_O_series()
