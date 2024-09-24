import random, time
def wordle():
    wordList =[line for line in open("WORDS.txt","r")]
    num = random.randint(0,len(wordList)-1)
    word = wordList[num].strip()
    round = len(word)+1
    times = 1
    print(f"\n\033[0mWelcome to Wordle! You have {round} chances to guess a {len(word)}-letter word.")
    with open("en.txt", "r") as f:
        dictionary = f.read().split("\n")
    while times <= round:
        guess = input(f"\nAttempt {times}/{round}: ")
        while len(guess) != len(word) or not guess.isalpha() or guess not in dictionary:
            if not guess.isalpha():
                print("Letters only. Please try again.")
                guess = input(f"Attempt {times}/{round}: ")
            elif len(guess) < len(word):
                print("Not enough letters. Please try again.")
                guess = input(f"Attempt {times}/{round}: ")
            elif len(guess) > len(word):
                print(f"Only {len(word)}-letter words. Please try again.")
                guess = input(f"Attempt {times}/{round}: ")
            elif guess not in dictionary:
                print("The word does not exist. Please try again.")
                guess = input(f"Attempt {times}/{round}: ")
        guess = guess.lower()
        correct = []
        n = 0
        for i in guess:
            if i == word[n]:
                correct.append("🟩")
            elif i in word:
                correct.append("🟨")
            else:
                correct.append("⬛️")
            n += 1
        print("".join(correct))
        if guess == word:
            print(f"\033[0;33mCongratulations! You guessed \"{word}\" correctly.")
            return (round+1-times)
        times += 1
    if times > round and guess != word:
        print(f"\033[0;31mSorry, you ran out of chances. The word was \"{word}\".")
        return 0
def main():
    print("===Wordle===\nMenu:\n1. Classic mode\n2. Customised mode\n3. Endless mode\n4. Point system mode\n5. Exit")
    n = input("What would you like to play?\n>> ")
    while n not in ["1","2","3","4","5"]:
        n = input("Invalid input. Please try again.\n>> ")
    if n == "1":
        wordle()
    elif n == "2":
        print("This mode needs you to win multiple Wordle games in a row to win the game.")
        round = input("How many games you want to win in order to win the whole game?\n>> ")
        while not round.isdigit() or int(round) <= 0:
            round = input("Invalid input. Please try again.\n>> ")
        count = 0
        print(f"You have to win {int(round)} wordles to win the whole game, and the new game will begin automatically.\nGood luck!")
        while count < int(round):
            point = wordle()
            if point > 0:
                count += 1
            else:
                exit("Game over :(")
        print("\033[1;33mWell done! You won the game.")
    elif n == "3":
        count = 0
        print("The game will keep running until you win 3 wordles!")
        while count < 3:
            point = wordle()
            if point > 0:
                count += 1
        if count == 3:
            exit("\033[1;33mWell done! You won the game.")
    elif n == "4":
        name = input("What is your name?\n>> ")
        while name == "":
            name = input("Invalid input. Please try again.\n>> ")
        print(f"Hello, {name}! Welcome to point system mode! Here is how it works:")
        time.sleep(1.75)
        print("\n✔︎ Points for Guesses\nYou earn points based on how many guesses it takes to solve the Wordle.\n - Guess on the first try: 6 points\n - Guess on the second try: 5 points, and so on, with fewer points the more guesses you use.")
        time.sleep(4.5)
        print("\n✔︎ Customise the Goal\nThe default goal is 20 points to win, but you can choose your own target if you want a bigger or smaller challenge!")
        time.sleep(3.5)
        print("\n✔︎ Endless Wordles\nAfter each game, your points are added up, and a new game begins automatically.\nKeep playing until you reach your target score!")
        time.sleep(3.5)
        print("\n✔︎ Leaderboard\nThe leaderboard will show the top 3 players with their scores at the end.\n\033[4;1mTRY TO GET IN THE TOP 3!")
        time.sleep(3)
        score = input("\n\033[0mHow many points would you like to set to win the game?\n>> ")
        while not score.isdigit() or int(score) <= 0:
            score = input("Invalid input. Please try again.\n>> ")
        score = int(score)
        points = 0
        count = 0
        while points < score:
            point = wordle()
            if point > 0:
                count += 1
            points += point
            if points < score:
                print(f"\033[0mYou have {score-points} {"point" if score-points == 1 else "points"} left to end the loop. Keep going!")
        print(f"\n\033[0;33mWell done! You won the game in {count} turns with a total of {points} points.")
        with open("scores.txt", "a") as f:
            f.write(f"\n{name}: {points}")
        f.close()
        with open("scores.txt", "r") as f:
            scores = [line for line in f.read().splitlines() if line and ":" in line]
        f.close()
        if len(scores) >= 3:
            top3 = sorted(scores, key=lambda x: int(x.split(":")[1]), reverse=True)[:3]
            print("\n\033[0mHere are the top 3 players:")
            grade = 1
            for player in top3:
                print(f"\n{grade}. {player.split(':')[0]} with{player.split(':')[1]} points.")
                grade += 1
            check = 0
            for i in top3:
                if f"{name}: {points}" == i:
                    print(f"\n\033[1;33mExcellent, {name}! You are in the leaderboard!")
                else:
                    check += 1
            if check == 3:
                print("\nKeep playing and you will be there!")
        else:
            print("The leaderboard will unlock until there are at least 3 players :)")
    else:
        exit("Thanks for playing!")
        
main()