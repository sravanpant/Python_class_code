def repeatedSubstringPattern(s):
    if len(s) % 2 == 0:
        sub = []
        for i in range(len(s) // 2):
            sub.append(s[i])
            if sub[0] * len(s) == s:
                return True
            elif i != 0:
                if "".join(sub) * (len(s) // i) == s:
                    return True
    else:
        if s[0] * len(s) == s:
            return True
