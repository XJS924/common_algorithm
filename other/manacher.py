def manacher(s):
    s = "$#" + "#".join(s) + "#*"
    p = [0] * len(s)
    R = C = 0
    for i in range(1, len(s) - 1):
        p[i] = min(R - i, p[2 * C - i])
        while s[1 + i + p[i]] == s[i - 1 - p[i]]: p[i] += 1
        if p[i] + i - 1 > R:
            R = p[i] + i - 1
            C = i
    m = max(p)
    idx = p.index(m)
    return s[idx - m:idx + m].replace('#', '')


if __name__ == '__main__':
    print(manacher('tattarrattat'))
