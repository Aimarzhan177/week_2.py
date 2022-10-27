year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"Год {year} - високосный")
elif year % 400 == 0 and 100 == 0:
    print(f"Год {year} - високосный")
elif year % 100 == 0:
    print(f"Год {year} - невисокосный")
else:
    print(f"Год {year} - невисокосный")