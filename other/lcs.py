def lcs(a, b):
    h, j = len(a), len(b)
    if h < 1 or j < 1: return ''
    if a[h - 1] == b[j - 1]:
        return lcs(a[:h - 1], b[:j - 1]) + a[h - 1]
    else:
        return get_max(lcs(a[:h - 1], b), lcs(a, b[:j - 1]))


def get_max(a, b): return a if len(a) > len(b) else b


if __name__ == '__main__':
    print(lcs('sasadwkpeqswe', 'sdjasfjaswe'))
