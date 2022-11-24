
# year = "Start"

# while year:

year = int(input("Year: "))

if not year % 400:
    print(f"The year {year} is a Leap Year")
elif not year % 100:
    print(f"The year {year} is not a Leap Year")
elif not year % 4:
    print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is not a Leap Year")