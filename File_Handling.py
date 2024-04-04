def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Python File Handling")

        print("File created successfully.")

    except FileNotFoundError:
        print("File not found or cannot be created.")
    except PermissionError:
        print("Permission denied to create the file.")
    finally:
        print("File creation process completed.\n")


def read_file():
    try:
        # Open "my_file.txt" in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            print(file.read())

    except FileNotFoundError:
        print("File not found or cannot be opened for reading.")
    except PermissionError:
        print("Permission denied to read the file.")
    finally:
        print("File reading process completed.\n")


def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("\nAppending line 1\n")
            file.write("98765\n")
            file.write("Appending more text")

        print("File appended successfully.")

    except FileNotFoundError:
        print("File not found or cannot be opened for appending.")
    except PermissionError:
        print("Permission denied to append to the file.")
    finally:
        print("File appending process completed.\n")


if __name__ == "__main__":
    # Create a new file
    create_file()

    # Read and display the file contents
    read_file()

    # Append additional content to the file
    append_file()
