from sympy import primerange

def HN_P(n_terms=10000):
    primes = list(primerange(1, 105000))[:n_terms]
    total = 1  # Start with 1
    series = [(1, primes[0], 1.0, round(total, 10))]  # first term: 1 (prime=2)
    for k in range(2, n_terms + 1):
        p = primes[k - 1]
        term = ((-1)**(k+1)) * (1 / p)
        total += term
        series.append((k, p, round(term, 10), round(total, 10)))
    return series

if __name__ == "__main__":
    results = HN_P()

    print("\\nHN_P Series (First 12 Terms):")
    for row in results[:12]:
        print(f"k={row[0]:<5} prime={row[1]:<5} term={row[2]:<15} partial_sum={row[3]}")

    print("\\nHN_P Series (Last 12 Terms):")
    for row in results[-12:]:
        print(f"k={row[0]:<5} prime={row[1]:<5} term={row[2]:<15} partial_sum={row[3]}")
