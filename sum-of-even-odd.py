def sum_of_odd_and_even(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Input from the user
try:
    n = int(input("Enter the number of elements: "))
    print("Enter the numbers:")
    numbers = [int(input()) for _ in range(n)]

    # Calculate the sums
    even_sum, odd_sum = sum_of_odd_and_even(numbers)

    # Output the results
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

except ValueError:
    print("Please enter valid integers.")
