def remove_comments(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    lines_without_comments = []

    for line in lines:
            line = line.split('#')[0].strip()
            lines_without_comments.append(line)
            lines_without_comments.append("\n")

    with open(input_file, 'w') as f:
        f.writelines(lines_without_comments)


def main():
    input_file = "fajl.txt"
    remove_comments(input_file)


if __name__ == "__main__":
    main()
