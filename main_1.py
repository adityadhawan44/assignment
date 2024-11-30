def nth_term_of_ap(a, d, n):
    return a + (n - 1) * d

a = int(input("Enter the first term (a) of the AP: "))
d = int(input("Enter the common difference (d) of the AP: "))
n = int(input("Enter the term number (n) you want to find: "))

nth_term = nth_term_of_ap(a, d, n)
print(f"The {n}th term of the AP is: {nth_term}")