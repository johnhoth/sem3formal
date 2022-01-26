import library


def main():
    raw_data = input().split()
    language, x = raw_data[0], raw_data[1]
    result = library.solve(language, x)

    print(result)


if __name__ == "__main__":
    main()
