if __name__ == '__main__':
    s = input("Enter a string: ")

while True:
    try:
        if 0 < len(s) < 1000:
            break
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid string length. Enter a string: ")

print(any(s.isalnum() for s in s))
print(any(s.isalpha() for s in s))
print(any(s.isdigit() for s in s))
print(any(s.islower() for s in s))
print(any(s.isupper() for s in s))