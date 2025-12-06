from functions.get_files_info import get_files_info


def main():
    Test1 = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(Test1)

    Test2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(Test2)

    Test3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(Test3)

    Test4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(Test4)


if __name__ == "__main__":
    main()
