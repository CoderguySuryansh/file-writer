def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get input from the user
filename = input("Enter the name of the file to create or overwrite: ")
content = input("Enter the content to write to the file: ")

# Write content to the file
write_to_file(filename, content)
