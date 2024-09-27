import random

class Question:
    def __init__(self, question_text, option, answer):
        self.question_text = question_text
        self.option = option
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

class Test:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        print("Question added")

    def take_test(self):
        score = 0

        for question in self.questions:
            print(question.question_text)

            for i, option in enumerate(question.option):
                print(f"{i + 1}. {option}")
            try:
                user_answer_index = int(input("Enter the number of your answer: ")) - 1

                if question.check_answer(question.option[user_answer_index]):
                    score += 1
            except ValueError as err:
                print(err)
        self.show_score(score)

    def show_score(self, score):
            print(f"You scored {score} out of {len(self.questions)}")

test = Test()

while True:

    print("1. Add question")
    print("2. Take test")
    print("3. Show score")

    choice = input("Enter your choice: ").lower()

    if choice == '1':
        question_text = input("Enter the question: ")
        options = input("Enter the options separated by commas: ").split(',')
        answer = input("Enter the correct answer: ")

        question = Question(question_text, [option.strip() for option in options], answer.strip())
        test.add_question(question)

    elif choice == '2':
        test.take_test()

    elif choice == '3':
        print("This option is not implemented yet. Please take the test to see your score.")

    else:
        print("Wrong choice")
