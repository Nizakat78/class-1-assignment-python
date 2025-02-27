# Represents a sequence of numbers.
rang_number = range(1, 15, 10)  # (start stop step)

print(type(rang_number), "Range Example:", list(rang_number))  # Convert to list to see the values

print(type(rang_number), "Range Start:", rang_number.start)

print(type(rang_number), "Range Stop:", rang_number.stop)

print(type(rang_number), "Range Step:", rang_number.step)


# Loop that prints numbers from 1 to 89, with a step of 3
for i in range(1, 90, 3):
    print(i)  # This will print values from 1 to 89, in steps of 3
