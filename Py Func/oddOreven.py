numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

count = 0

while count < len(numbers):
    num = numbers[count]
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    count += 1

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
