def count_words(input_text):
    
    words = input_text.split()
    return len(words)

def main():
    
    print("Welcome to the Word Count Program!")
    print("Please enter a sentence or paragraph below:")

    user_input = input("Your input: ").strip()

    if not user_input:
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return

    word_count = count_words(user_input)

    print(f"The number of words in your input is: {word_count}")

if __name__ == "__main__":
    main()
