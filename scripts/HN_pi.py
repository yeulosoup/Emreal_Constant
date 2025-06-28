import math

def hn_pi_series(n_terms=10000):
    terms = []
    partial_sum = 0
    last_sum = 0

    for k in range(1, n_terms + 1):
        numerator = 2 * k
        denominator = 2 * k - 1
        term = ((-1) ** (k + 1)) * (numerator / denominator)
        partial_sum += term
        average = (partial_sum + last_sum) / 2
        terms.append((k, term, partial_sum, average))
        last_sum = partial_sum

    # Print first 12
    print("HN_π Series (First 12 Terms):")
    for k, term, psum, avg in terms[:12]:
        print(f"k={k:<5} term={term:<18.10f} partial_sum={psum:<18.10f} average={avg:.10f}")
    print()

    # Print last 12
    print(f"HN_π Series (Last 12 Terms):")
    for k, term, psum, avg in terms[-12:]:
        print(f"k={k:<5} term={term:<18.10f} partial_sum={psum:<18.10f} average={avg:.10f}")

if __name__ == "__main__":
    hn_pi_series()
