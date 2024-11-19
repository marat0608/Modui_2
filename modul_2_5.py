def get_matrix(n, m, value):
    matrix = []
    for r1 in range(0, n):
        mat = []
        for r2 in range(0, m):
            mat.append(value)
        matrix.append(mat)
    return matrix
t = get_matrix(2, 2, 44)
t2 = get_matrix(5, 1, 44)
t3 = get_matrix(3, 4, 44)

print(t)
print(t2)
print(t3)


def test(a=2, b=True):
    print(a,b)
test('dde',[12])
