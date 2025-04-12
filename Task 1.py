
def open_file(filename):
    try:
        with open(filename, 'r') as file1:
            lines = file1.readlines()
            num = 1
            print("Reading file content:")
            for i in lines:
                print(f"Line {num}: {i}")
                num+=1
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

open_file('sample.txt')