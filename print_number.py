def extract_number(user_input):
    digits = [char for char in user_input if char.isdigit()]
    return int("".join(digits)) if digits else None

def print_number(n):
    for i in range(1, n+1):
        print(i, end="")
    
while True:
    user_input = input("Nhap 1 day so nguyen: ").stript()
    n = extract_number(user_input)
    
    if n is not None and n > 0:
        print_number(n)
        break
    else:
        print("Vui long nhap lai so.")
        