from functions.get_file_content import get_file_content


def main():
    Test1 = get_file_content("calculator", "lorem.txt")
    print(Test1)

    Test2 = get_file_content("calculator", "main.py")
    print(Test2)

    Test3 = get_file_content("calculator", "pkg/calculator.py")
    print(Test3)

    Test4 = get_file_content("calculator", "/bin/cat")
    print(Test4)

    Test5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(Test5)


if __name__ == "__main__":
    main()
