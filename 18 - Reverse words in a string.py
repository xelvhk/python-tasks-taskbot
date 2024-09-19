words = input("String to reverse:")
def reverse_Words(s: str) -> str:
    s = s.split()
    s.reverse()
    return " ".join(s)

print(reverse_Words(words))