def print_pages(pages: str) -> list:
    pagesToPrint = pages.split(",")
    result = []

    for item in pagesToPrint:
        if len(pages) == 0:
            return result

        if len(item) == 1:
            result.append(int(item))
        else:
            numbers = item.split("-")

            # Check if there is a second element in the numbers list
            if len(numbers) == 2:
                result.extend(list(range(int(numbers[0]), int(numbers[1]) + 1)))
            else:
                result.append(int(numbers[0]))

    return result
