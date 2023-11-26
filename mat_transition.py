def m_transition(r):
    P = [[0 for _ in range(r)] for _ in range(r)]

    for i in range(r):
        for j in range(r):
            if j == i + 1 and i < r:
                P[i][j] = ((r - i) ** 2) / (r ** 2)
            elif j == i - 1 and i > 0:
                P[i][j] = (i ** 2) / (r ** 2)
            elif j == i:
                P[i][j] = (2 * i * (r - i)) / (r ** 2)

    return P


