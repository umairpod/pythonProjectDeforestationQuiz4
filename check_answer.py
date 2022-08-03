def check_answer(answer, guess):
    if answer == guess:
        print("⭐️CORRECT⭐️")
        return 1
    else:
        print("❌WRONG❌")
        return 0