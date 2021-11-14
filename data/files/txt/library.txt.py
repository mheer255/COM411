def display_chars():
    with open(file_path) as file:
        data = file.read()
        print("The Law Section")


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print("The Art Section")


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run():
    display_chars("library.txt")
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
