from sympy import primerange

def HN_M(n_terms=10000):
    primes = list(primerange(2, 2000000))  # Get more than needed
    total = 1
    series = [(1, 1.0, round(total, 10))]
    for k in range(2, n_terms + 1):
        pk = primes[k - 1]
        term_value = (1 / pk + 1 / (k + 1 / k)) / 2
        term = ((-1) ** (k + 1)) * term_value
        total += term
        series.append((k, round(term, 10), round(total, 10)))
    return series

if __name__ == "__main__":
    results = HN_M()

    print("\nHN_M Series (First 12 Terms):")
    for row in results[:12]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")

    print("\nHN_M Series (Last 12 Terms):")
    for row in results[-12:]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")
