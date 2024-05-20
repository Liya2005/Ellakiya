def is_oneful_pair(a, b):
    return "Yes" if a + b + (a * b) == 111 else "No"

a, b = map(int, input().split())


print(is_oneful_pair(a, b))
