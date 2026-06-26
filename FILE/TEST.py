import sys
import webbrowser

# --- STEP 1: PASSWORD BYPASS ---
print("PASSWORD BYPASS = FALSE")
password_attempt = input("INPUT PASSWORD: ")

if password_attempt.strip().upper() != "EDUCATION":
    print("Incorrect password. Access denied.")
    sys.exit()

print("\nAccess Granted!\n")

# --- STEP 2: DEFINE QUESTIONS AND ACCEPTABLE ANSWERS ---
# Each question is a dictionary containing the prompt and a list of valid lower-case answers.
questions = [
    {
        "prompt": "Question 1: When were you born?\n> ",
        "valid_answers": [
            "1995/2/2",
            "february second 1995",
            "february 2cd 1995",
            "february 2nd 1995",  # Added common variation just in case
        ],
    },
    {"prompt": "Question 2: A or B?\n> ", "valid_answers": ["b"]},
    {
        "prompt": "Question 3: What's you're skin color? Black, white or pale?\n> ",
        "valid_answers": ["pale"],
    },
    {
        "prompt": "Question 4: Where do you live: BALTIMORE or TEXAS?\n> ",
        "valid_answers": ["texas"],
    },
    {
        "prompt": "Question 5: ARE YOU HAVING FUN? YES OR NO?\n> ",
        "valid_answers": ["yes"],
    },
    {"prompt": "Question 6: 6, 7 OR 67?\n> ", "valid_answers": ["67"]},
    {
        "prompt": "Question 7: Do you like Mcdonalds? Bababababa i'm loving it! or Bababababa i'm hating it!\n> ",
        "valid_answers": ["bababababa i'm hating it!", "bababababa im hating it!"],
    },
    {
        "prompt": "Question 8: Have you beaten FNAF yet? Yes or No?\n> ",
        "valid_answers": ["no"],
    },
    {"prompt": "Question 9: Type 999\n> ", "valid_answers": ["999"]},
    {
        "prompt": "Question 10: ARE YOU Monte Jiaqi? yes or no?\n> ",
        "valid_answers": ["yes"],
    },
]

# --- STEP 3: GAME LOOP ---
game_won = True

for q_num, q in enumerate(questions, 1):
    attempts = 3
    correct = False

    while attempts > 0:
        user_input = input(q["prompt"]).strip().lower()

        # Check if the answer matches any of the valid answers
        if user_input in q["valid_answers"]:
            print("Correct!\n")
            correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer! You have {attempts} tries left.\n")
            else:
                print("Wrong answer! Out of tries.")

    # If the user failed to answer a question after 3 tries, stop the game
    if not correct:
        print("Game Over! Try again from the start.")
        game_won = False
        break

# --- STEP 4: REDIRECT TO WEBSITE ---
if game_won:
    print("Congratulations! You passed all 10 questions.")
    print("Waiting...")
    url = "https://jermon111.itch.io/welcome-monte-jiaqi"
    webbrowser.open(url)