questions = {
    'In which Italian city can you find the Colosseum?' : ['1. Venice', '2. Rome','3. Naples' ,'4. Milan'],
    'In the TV show New Girl, which actress plays Jessica Day?' : ['1. Zooey Deschanel', '2. Kaley Cuoco','3. Jennifer Aniston' ,'4. Alyson Hannigan'],
    'What is the largest canyon in the world??' : ['1. Verdon Gorge, France', '2. King’s Canyon, Australia','3. Grand Canyon, USA' ,'4. Fjaðrárgljúfur Canyon, Iceland'],
    'How long is the border between the United States and Canada?' : ['1. 3,525 miles', '2. 4,525 miles','3. 5,525 miles' ,'4. 6,525 miles']
             }
correct_choices = [1, 2, 1, 4]


def game():
    print("\t"+".-"*10 + "    QUIZ    " + ".-."*10)
    user_answers = []
    for question, answer in questions.items():
        show_questions(question, answer)
        user_answer = int(input())
        user_answers.append(user_answer)
    print("\n" + "-"*50 + " \n")
    print(count_score(user_answers))


def count_score(user_answers):
    correct_answers = 0
    for user_answer, correct_answer in zip(user_answers, correct_choices):
        if user_answer == correct_answer:
            correct_answers += 1
    return f'You scored {(correct_answers / len(correct_choices)) * 100}' + '\n'


def show_questions(question, choices):
    maxlen = len(max(questions.keys(), key=len))
    header = '.' + '_' * (maxlen+10) + '.'
    footer = '_' * (maxlen+10) + '.'
    print(header)
    print('|\t' + question + ' '*(len(header) - len(question)-9) + '|')
    for choice in choices:
        print('|  '+choice+' '*(len(header) - len(choice) - 5) + ' |')
    print("|"+footer)

    
while True:
    game()
    print("Wanna Play Again? (YES / NO)")
    ans = input().upper() 
    while ans not in ["YES", "NO"]:
        print("enter YES or NO")
        ans = input().upper() 
    if ans == "NO":
        break

print("BYE then! \n")