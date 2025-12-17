from functions.run_python_file import run_python_file


def main():
    Test1 = run_python_file("calculator", "main.py")
    print(Test1)

    Test2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(Test2)

    Test3 = run_python_file("calculator", "tests.py")
    print(Test3)

    Test4 = run_python_file("calculator", "../main.py")
    print(Test4)

    Test5 = run_python_file("calculator", "nonexistent.py")
    print(Test5)

    Test6 = run_python_file("calculator", "lorem.txt")
    print(Test6)


if __name__ == "__main__":
    main()
