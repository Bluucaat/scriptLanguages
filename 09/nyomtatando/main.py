def print_pages(pages: str) -> list:
    number = 0
    pagesToPrint = pages.split(",")
    result = []

    for item in pagesToPrint:
        if len(item) == 1:
            result.append(item)
        else:
            numbers = item.split("-")
            result.extend(list(range(int(numbers[0]), int(numbers[1])+1)))

    return result


def main() -> None:
    pages = "1-4,7,9,11-15"
    print(print_pages(pages))



if __name__ == '__main__':
    main()

