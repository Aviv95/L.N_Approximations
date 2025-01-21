

def lagrange(table,x):
    """
    Lagrange Interpolation

    Parameters:
    table: list of tuples
    x: Interpolated value

    Returns:result The interpolated value at x
    """
    n = len(table)
    result = 0.0
    print(f"{'Iteration':<10} | {'x':<15} | {'y':<10} | {'Result':<10}")

    for i in range(n):
        term = table[i][1]
        for j in range(n):
            if i != j:
                term *= (x - table[j][0]) / (table[i][0] - table[j][0])

        result += term
        print(f"{i:<10} | {table[i][0]:<15} | {table[i][1]:<10} | {result:<10.8f}")

    return result
