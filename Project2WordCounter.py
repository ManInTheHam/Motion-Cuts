def word_count_and_length(input_text):
    if not input_text.strip():
        raise ValueError(
            "Error: Input text is empty. Please provide some text.")

    words = input_text.split()
    word_count = len(words)

    total_length = sum(len(word) for word in words)

    return word_count, total_length


if __name__ == "__main__":
    print("Welcome to the Word Counter Program!")
    print("Enter a sentence or paragraph.")

    while True:
        input_text = input(
            "Type or paste your text here (press Enter to exit): ")

        if not input_text:
            print("Exiting the program. Goodbye!")
            break

        try:
            count, total_length = word_count_and_length(input_text)
            print("\nWord Counter:")
            print(f"Number of words: {count}")
            print(f"Total length of words: {total_length}")
        except ValueError as e:
            print(f"Error: {e}\n")
