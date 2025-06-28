def HN_B(n_terms=10000):
    total = 1  # Start with 1
    series = [(1, 1.0, round(total, 10))]  # First term
    for k in range(2, n_terms + 1):
        term_value = 1 / (k + (1 / k))
        term = ((-1) ** (k + 1)) * term_value
        total += term
        series.append((k, round(term, 10), round(total, 10)))
    return series

if __name__ == "__main__":
    results = HN_B()

    print("\\nHN_B Series (First 12 Terms):")
    for row in results[:12]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")

    print("\\nHN_B Series (Last 12 Terms):")
    for row in results[-12:]:
        print(f"k={row[0]:<5} term={row[1]:<15} partial_sum={row[2]}")
