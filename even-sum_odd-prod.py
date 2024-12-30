def calculate_sum_and_product():
    try:
        # Input: Number of elements
        n = int(input("Enter the number of elements: "))
        numbers = []

        # Input: List of numbers
        print("Enter the numbers:")
        for _ in range(n):
            num = int(input())
            numbers.append(num)

        # Initialize sum and product
        even_sum = 0
        odd_product = 1
        odd_found = False  # To handle cases where there are no odd numbers

        for num in numbers:
            if num % 2 == 0:
                even_sum += num
            else:
                odd_product *= num
                odd_found = True

        # Handle the case where there are no odd numbers
        if not odd_found:
            odd_product = 0  # Conventionally, product is 0 if no odd numbers are present

        # Output the results
        print(f"Sum of even numbers: {even_sum}")
        print(f"Product of odd numbers: {odd_product}")

    except ValueError:
        print("Please enter valid integers.")

# Run the function
calculate_sum_and_product()
