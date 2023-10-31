def merge_files(input_files, output_file):

    with open(output_file, "w") as out_file:
        for input_file in input_files:
            with open(input_file, "r") as in_file:
                out_file.write(in_file.read() + "\n")

input_files = ["D:\Python\Py Func\demo.txt", "D:\Python\Py Func\dummy.txt", "D:\Python\Py Func\sample.txt"]
output_file = "merged_output.txt"
merge_files(input_files, output_file)

print("Files merged into",output_file)
