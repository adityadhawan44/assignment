# To find the grades of the student by adding their name and grade respectively.

def a():
    print("\n1. Add")
    print("2. View")
    print("3. Avg")
    print("4. Pass/Fail")
    print("5. Exit")

def b(c):
    d = input("Enter name: ")
    e = float(input(f"Enter grade for {d}: "))
    c[d] = e
    print(f"{d} added.")

def f(c):
    if not c:
        print("No data.")
    else:
        print("\nList of grades:")
        for g, h in c.items():
            print(f"{g}: {h}")

def i(c):
    if not c:
        print("No grades.")
    else:
        j = sum(c.values()) / len(c)
        print(f"Avg: {j:.2f}")

def k(c, l=50):
    if not c:
        print("No grades.")
    else:
        print("\nResults:")
        for m, n in c.items():
            o = "Pass" if n >= l else "Fail"
            print(f"{m}: {o} (Grade: {n})")

def p():
    q = {}
    while True:
        a()
        r = input("Choice (1-5): ")
        
        if r == '1':
            b(q)
        elif r == '2':
            f(q)
        elif r == '3':
            i(q)
        elif r == '4':
            k(q)
        elif r == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    p()
