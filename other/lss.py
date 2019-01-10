def lss(a, b):
    h, j = len(a), len(b)
    maxlen = maxid = 0
    import numpy as np
    p = np.zeros([h, j], 'int64')
    for m in range(1,h):
        for n in range(1,j):
            if a[m - 1] == b[n - 1]:
                p[m, n] = p[m - 1, n - 1] + 1
            if p[m, n] > maxlen:
                maxlen = p[m, n]
                maxid = m
    print(maxid,maxlen)
    return a[maxid-maxlen:maxid]

if __name__=='__main__':
    print(lss('sasdwkpeqswe', 'sdjasfjaswe'))
