import time


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        while True:
            user_answer = input("Your answer (enter the option number): ")
            if self.is_valid_answer(user_answer, question_data["options"]):
                break
            else:
                print("Invalid input. Please enter a valid option number.")

        if question_data["options"][int(user_answer) - 1] == question_data["correct_option"]:
            print("Correct!\n")
            return True
        else:
            print(f"Wrong! The correct answer is {
                  question_data['correct_option']}.")
            self.show_explanation(question_data)
            return False

    def is_valid_answer(self, answer, options):
        return answer.isdigit() and 1 <= int(answer) <= len(options)

    def run_quiz(self):
        for question_data in self.questions:
            if self.ask_question(question_data):
                self.score += 1

        print(f"\nYour final score: {self.score}/{len(self.questions)}")

        if self.score == len(self.questions):
            self.show_reward()

    def show_reward(self):
        print("Congratulations! You scored 3 out of 3. Here's your reward:")
        time.sleep(1)
        print("🎉🎊🥳 Amazing job! 🥳🎊🎉")

    def show_explanation(self, question_data):
        print("\nExplanation:")
        print(question_data["explanation"])
        print()


def main():
    questions = [
        {"question": "The metal whose salts are sensitive to light is?", "options": [
            "Zinc", "Aluminum", "Silver"], "correct_option": "Silver", "explanation": "Silver is the metal whose salts are sensitive to light."},
        {"question": "Which programming language is known for its readability?",
            "options": ["Java", "Python", "C++"], "correct_option": "Python", "correct_option": "Python", "explanation": "Python is known for its clean and readable syntax."},
        {"question": "What is the largest ocean on Earth?", "options": [
            "Atlantic", "Indian", "Pacific"], "correct_option": "Pacific", "correct_option": "Pacific", "explanation": "The Pacific Ocean is the largest and deepest of Earth's oceanic divisions."}
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
