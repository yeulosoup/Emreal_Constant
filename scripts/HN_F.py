from sympy import primerange

def get_n_primes(n):
    primes = list(primerange(1, 200000))
    return primes[:n]

def HN_F(n_terms=10000):
    primes = get_n_primes(n_terms + 2)
    total = 1  # Start with 1
    series = [(1, 1.0, round(total, 10))]  # First term is 1

    for k in range(2, n_terms + 1):
        prime_k = primes[k - 1]
        inner1 = 1 / (k + 1 / k)
        inner2 = 1 / prime_k
        inner3 = (inner2 + inner1) / 2
        term_value = (2 * inner1 + inner2 + inner3) / 4
        term = ((-1) ** (k + 1)) * term_value
        total += term
        series.append((k, round(term, 10), round(total, 10)))
    return series

if __name__ == "__main__":
    results = HN_F()

    print("\nHN_F Series (First 12 Terms):")
    for row in results[:12]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")

    print("\nHN_F Series (Last 12 Terms):")
    for row in results[-12:]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")
