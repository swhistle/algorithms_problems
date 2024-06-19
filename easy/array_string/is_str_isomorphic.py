def is_string_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_letters_dict = {}
    t_letters_dict = {}

    for i in range(len(s)):
        if s[i] in s_letters_dict:
            if t[i] != s_letters_dict[s[i]]:
                return False
        else:
            s_letters_dict[s[i]] = t[i]

        if t[i] in t_letters_dict:
            if s[i] != t_letters_dict[t[i]]:
                return False
        else:
            t_letters_dict[t[i]] = s[i]

    return True


s1 = "egg"
t1 = "add"

s2 = "foo"
t2 = "bar"

s3 = "paper"
t3 = "title"

s4 = "badc"
t4 = "baba"

print(is_string_isomorphic(s1, t1))
print(is_string_isomorphic(s2, t2))
print(is_string_isomorphic(s3, t3))
print(is_string_isomorphic(s4, t4))