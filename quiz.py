name = input("Enter Name: ")
print("welcome to the quiz " + name)
questions = {
    "what city is the eifel tower in? ": "Paris",
    "Who is the current prime minister of UK: ": "Boris Johnson",
    "who is the Greatest Footballer of all time": "Lionel Messi", "Messi",
    "who was the 45th president of the United States": "Donald Trump",
}
score = 0
for question, value in questions.items():
    userinput = input(question)
    if userinput.strip().lower() == value.lower():
        print("correct")
        score += 1
    else:
        print("wrong")

print(f"{name} got {score} questions correctly")
