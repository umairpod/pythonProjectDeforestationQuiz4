# This is a print statement at the start of the code to welcome the player and asks their name
print("Welcome to my deforestation Quiz")
user_name = input("What is your name? ")
print("You will be playing a game about deforestation " + user_name + " you will have to choose from A,B,C and D and "
                                                                      "the percentage of questions you get right will "
                                                                      "be calculated at the end. ")

print("The game will start know: ")


# This def is to start a new game
# guesses is an empty list, correct guesses is 0 since we haven't guessed anything yet
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# This def is used to make sure the guess they put in is correct or wrong
# It is also linked to correct_guesses by the +=
def check_answer(answer, guess):
    if answer == guess:
        print("⭐️CORRECT⭐️")
        return 1
    else:
        print("❌WRONG❌")
        return 0


# This def is used to display the score, print all the answers and the end="" is used to make it end on a new line
def display_score(correct_guesses, guesses):
    print(" ")
    print("RESULTS")
    print(" ")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
# This is used to print the amount of questions you got right as a percentage
    score = ((correct_guesses / len(questions)) * 100)
    print(user_name + " Your score is: " + str(score) + "%")


# This is used to ask the user if they want to play again
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper

    if response == "YES":
        return True
    else:
        return False


# I used a dictionary for my questions, so I don't have to repeat coding every time
questions = {
    "What is Deforestation?: ": "B",
    "Earth has lost how much of its original forest due to humans?: ": "A",
    "How many million acres of forests are left in the world? Hint: About the size of Panama": "A",
    "What is the number one reason for deforestation>": "A",
    "Which is not affected by deforestation?": "D",
    "A forestry practice in which most or all trees are cut down?": "B",
    "A forestry practice where a selected amount of trees are cut down so that growth isn't affected?": "A",
    "What gas do trees produce? Hint: It helps humans": "C"}

options = [["A. The loss of fish habitats", "B. The loss of forest habitats", "C. The loss of ground habitats",
            "D. the loss of all habitats"],
           ["A. 50%", "B. 75%", "C. 110%", "D. 68.5%"],
           ["A. 18 million", "B. 12.6 million", "C. 17 million", "D. 100 million"],
           ["A. Agricultural expansion", "B. The need for paper", "C. The need for shelter"],
           ["A. Amount of habits", "B. Amount of unique animals in an area", "C. Global Warming becomes worse",
            "D. Fish will not be able to grow"],
           ["A. Selective Cutting", "B. Clear Cutting "],
           ["A. Selective Cutting", "B. Clear Cutting "],
           ["A. Water", "B. Carbon Dioxide", "C. Sunlight", "D. Oxygen"]]


new_game()

while play_again():
    new_game()

print("Thank you for playing this game.")
