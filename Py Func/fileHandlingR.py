file_name = "D:\Python\Py Func\sample.txt"

try:
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print("Word count in '",file_name,"': ",word_count)
except FileNotFoundError:
    print("File '",file_name,"' not found.")
