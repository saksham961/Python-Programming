def quize_game():
    print("Welcome to the quiz game!")

    playing = input("Do you want to play the game? (yes/no): ")

    if playing.lower() != "yes":
        quit()

    print("Okay, let's play the game")

    # First question
    answer1 = input("What is the capital of France: ")
    if answer1.lower() == "paris":
        print("Correct!")
    else:
        print("Incorrect!")

    # Second question
    answer2 = input("What is the largest planet in our solar system: ")
    if answer2.lower() == "jupiter":
        print("Correct!")
    else:
        print("Incorrect!")

    # Third question
    answer3 = input("What is the hardest natural substance on Earth: ")
    if answer3.lower() == "diamond":
        print("Correct!")
    else:
        print("Incorrect!")

    # Fourth question
    answer4 = input("What planet is known as the Red Planet: ")
    if answer4.lower() == "mars":
        print("Correct!")
    else:
        print("Incorrect!")

    # Fifth question
    answer5 = input("Which country is known as the Land of the Rising Sun: ")
    if answer5.lower() == "japan":
        print("Correct!")
    else:
        print("Incorrect!")

    # Sixth question
    answer6 = input("What is the sum of the angles in a triangle: ")
    if answer6 == "180" or answer6.lower() == "180 degrees":
        print("Correct!")
    else:
        print("Incorrect!")

quize_game()
