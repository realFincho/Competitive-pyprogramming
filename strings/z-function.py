

def substr_count(s, sub):
    n, m = len(s), len(sub)
    occur = 0
    for i in range(n - m + 1):
        mismatch = False
        for j in range(m):
            if s[i+j] != sub[j]:
                mismatch = True
                break
        if not mismatch:
            occur += 1
    return occur


def max_palindrome_prefix1(s):
    n = len(s)
    mx = 0
    for i in range(n + 1):
        if s[:i] == s[i - 1::-1]:
            mx = i
    return mx


def max_palindrome_prefix2(s):
    n = len(s)
    mx = 0
    for i in range(n):
        mismatch = False
        for k in range(i // 2 + i % 2):
            if s[k] != s[i - k]:
                mismatch = True
                break
        if not mismatch:
            mx = i + 1
    return mx


def z_function_naive1(s):
    n = len(s)
    z = [0 for _ in range(n)]
    # substring position
    for i in range(1, n):
        # substring length
        mx = n - i
        for j in range(n - i):
            if s[j] != s[i + j]:
                mx = j
                break
        z[i] = mx
    return z


def z_function_naive2(s):
    n = len(s)
    z = [0 for _ in range(n)]
    # substring position
    for i in range(1, n):
        while z[i] + i < n and s[z[i] + i] == s[z[i]]:
            z[i] += 1
    return z


def common_prefix_suffix1(s):
    m = len(s)
    occur = 0
    # substring length 1 -- m-1
    for i in range(1, m):
        # substring position 0 -- m-1-i
        for j in range(m - i + 1):
            mismatch1 = False
            mismatch2 = False
            for k in range(i):
                # prefix
                if s[k] != s[j + k]:
                    mismatch1 = True
                # suffix
                if s[m - i + k] != s[j + k]:
                    mismatch2 = True
            if mismatch1 != mismatch2:
                occur += 1
    return occur


def common_prefix_suffix2(s):
    m = len(s)
    occur = 0
    # substring length 1 -- m-1
    for i in range(1, m):
        # substring position 0 -- m-1-i
        for j in range(m - i + 1):
            if (s[:i] == s[j:j + i]) != (s[m - i:] == s[j:j + i]):
                occur += 1
    return occur


def pattern_count1(s, sub):
    n, m = len(s), len(sub)
    if m > n:
        return 0
    occur = 0
    # substring position
    for i in range(n - m + 1):
        mismatch = False
        for j in range(m):
            if sub[j] != '?' and sub[j] != s[i + j]:
                mismatch = True
                break
        if not mismatch:
            occur += 1
    return occur


def good_substrings_count(s, t):
    n, m = len(s), len(t)
    if m > n:
        return (1 + n) * n // 2
    occur = (m - 1) * (2 * n - m + 2) // 2
    rate = 1
    # substring position
    for i in range(n - m + 1):
        if t == s[i:i + m]:
            rate = 1
        else:
            occur += rate
            rate += 1
    return occur


def z_function_gray_string(j):
    '''
    :param j: position of element in gray string
    :return: z-function value in j-pos
    '''
    if j & 1 or j == 0:
        return 0
    c = 0
    while j % 2 == 0:
        c += 1
        j //= 2
    return 2 ** c - 1

def z_function_fast1(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    # prefix pozition
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)

        while z[i] + i < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def z_function_fast2(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    # prefix pozition
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        mx = n - i
        for j in range(z[i], n - i):
            if s[j] != s[i + j]:
                mx = j
                break
        z[i] = mx
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z
print(z_function_fast2('abcabcabca$abcabcabcaabcabcabca'))
print(z_function_fast2('ABACABADABACABA$ABACABADABACABAABACABADABACABA'),'\n')
print(z_function_fast2('xoxxoxx$xoxxoxxxoxxoxx'))
print(z_function_fast2('xox$xoxxoxxxoxxoxx'),'\n')
print(z_function_fast2('abcdea$abcdeaabcdea'))

