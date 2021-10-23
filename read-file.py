try:
    with open(input("Enter path of a file: ")) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")