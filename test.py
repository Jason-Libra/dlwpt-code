var: str = "Hello, World!"

print(f"{var}")
print(f"{var:5}")
print(f"{var:20}")
print(f"{var:>20}")
print(f"{var:<20}")
print(f"{var:^20}")
print(f"{var:_^20}")
print(f"{var:*<20}")
print(f"{var:#>20}")


def sum(a, b):
    for i in range(32):
        if i == 12:
            print(f"{a} + {b} = {a + b}")
    return a + b
