
try:
    user_input = input("Enter text to write to the file:")
    # Write file
    file1 = open('output.txt', 'w')
    file1.write(user_input)
    file1.write("\n")
    print("Data successfully witten to output.txt")
    # Append file
    user_input = input("Enter additional text to append:")
    file1 = open('output.txt', 'a')
    file1.write(user_input)
    print("Data successfully append")

except:
    print("Data writing error to the file output.txt")


finally:
    file1 = open('output.txt', 'r')
    print("Final content of output.txt:","\n",file1.read())