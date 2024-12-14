# Function to display a question and validate the user's answer
def ask_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if 1 <= user_answer <= len(options):
                break
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if user_answer == correct_option:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is {correct_option}. {options[correct_option - 1]}")
        return 0

# Function to run the quiz
def run_quiz(quiz):
    score = 0
    print("\nWelcome to the Quiz!\n")
    
    for question in quiz:
        score += ask_question(question["question"], question["options"], question["correct_option"])
    
    print("\nQuiz Completed!")
    print(f"Your final score: {score} / {len(quiz)}")

# Function to customize the quiz
def create_quiz():
    # Example questions, options, and correct answers
    return [
        {
            "question": "I am an odd number. take away one letter , and I become even. what number am I?",
            "options": [" 7 "," 9 "," 11 "," 13 "],
            "correct_option": 1
        },
        {
            "question": "I am a three digit number. My tens digit is five more than my ones digit. My hundreds digit is eigit less than my tens digit. What number am I?",
            "options": [" 285 "," 491 "," 914 "," 194"],
            "correct_option": 4
        },
        {
            "question": "I am a number. when you multiply me with any other number the result is always remains same. What number am I?",
            "options": [" 1 "," 0 "," 11 "," 10"],
            "correct_option": 2
        },
        {
            "question": "I am a number that is twice the sum of my digit. What number am I?",
            "options": [" 12 "," 24 "," 18 "," 81 "],
            "correct_option": 3
        },
        {
            "question": "I am a two-digit number. The sum of my digits is 10 and the difference of my digits is 2. What number am I?",
            "options": [" 64 "," 57 "," 55 "," 82"],
            "correct_option": 1
        }
    ]

# Main function
if __name__ == "__main__":
    quiz = create_quiz()
    run_quiz(quiz)
