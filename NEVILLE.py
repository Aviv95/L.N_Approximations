
def neville(table, x):
    """
    Neville Interpolation

    Parameters:
    table: list of tuples
    x: Interpolated value

    Returns:tableau The interpolated value at x
    """
    n = len(table)
    flag=1
    tableau = [[0.0]*n for _ in range(n)]
    print(f"{'Iteration':<10} | {'x':<15} | {'y':<10} | {'Result':<10}")

    for i in range(n):
        tableau[i][0] = table[i][1]

    for j in range(1, n):
        for i in range(n-j):
            tableau[i][j] = ((x - table[i+j][0]) * tableau[i][j-1] - (x - table[i][0]) * tableau[i+1][j-1]) / (table[i][0] - table[i+j][0])
            print(f"{j:<10} | {table[i][0]:<15} | {table[i][1]:<10} | {tableau[i][j]:<10.8f}")

    return tableau[0][n-1]