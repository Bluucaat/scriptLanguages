
def hamming_distance(str1, str2):
    # Check if the input strings have the same length
    if len(str1) != len(str2):
        raise ValueError("A ket szo hosszanak meg kell egyeznie!")

    # Calculate Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))

    return distance


def main():
    # Example usage
    string1 = "bone"
    string2 = "gone"

    result = hamming_distance(string1, string2)
    print(f"A hamming tavolsag'{string1}' es '{string2}' kozott: {result}")


if __name__ == "__main__":
    main()