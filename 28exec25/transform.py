def TransformTransform(a, n):

    def Transform(a, n):
        b = []
        for i in range(n):
            for j in range(n-i):
                k = i + j
                b.append(max(a[j:k+1]))
        return b

    b = Transform(a, n)
    if not sum(Transform(b, len(b))) % 2:
        return True
    else:
        return False
