def count_the_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the file content and convert to lowercase
            content = file.read().lower()
            # Split the content into words
            words = content.split()
            # Count occurrences of 'the'
            the_count = words.count('the')
            return the_count
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = 'example.txt'  # Replace with your file path
occurrences = count_the_occurrences(file_path)
if occurrences is not None:
    print(f"The word 'the' occurs {occurrences} times in the file.")
