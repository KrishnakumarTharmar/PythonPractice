data = input("Enter data to write to the file: ")

file_name = "D:\Python\Py Func\sample.txt"

try:
    with open(file_name, 'w') as file:
        file.write(data)
    print(f"Data has been written to '{file_name}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
