print("===== TASK 4: File Reader =====")

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:

        print("\nFirst 3 lines of the file:\n")

        for i in range(3):
            line = file.readline()

            if not line:
                break

            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("File operation attempted")

print("\n" + "=" * 50)