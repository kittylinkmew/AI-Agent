from functions.write_file import write_file


def main():
    Test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(Test1)

    Test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(Test2)

    Test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(Test3)


if __name__ == "__main__":
    main()
