from termcolor import colored

#prompt = "> "
#answer = input(f"What does CTAC stand for?\n{prompt}")
#if answer == "Cyber Threat Action Center": 
#    print("Que Bueno!")
#else:
#        print(colored("The answer is 'Cyber Threat Action Center', not {!r}", 'red').format(answer))

#answer = input(f"What is the translation of 'Adios'?\n{prompt}")
#if answer == "Bye": 
#   print("Que Bueno!")
#else:
#    print(colored("The answer is 'Bye, not {!r}", 'red').format(answer))

QUESTIONS = [
    ("What does CTAC stand for?", "Cyber Threat Action Center"),
    ("What year was Abbott founded?", "1888"),
    ("Where was the first office outside of US opened?", "London")
]

QUESTIONS = {
    "Translate 'Hey'": [
        "Hola", "Adios", "Buenos Dias", "Buenas Noches"
    ],
    "Translate 'Bye'": [
        "Adios", "Hola", "Arroz", "Carro"
    ],
    "Translate 'Hacer'": [
        "To do", "To be", "To see", "To eat"
    ],
    "Translate 'Ver'": [
        "To see", "To drink", "To sleep", "To be"
    ]
}


for question, alternatives in sorted(QUESTIONS.items()):
    prompt = "> "
    print(f"{question}")
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"     {label}. {alternative}")
    
    answer_label = int(input(prompt))
    answer = sorted_alternatives[answer_label]
    if answer.lower() == correct_answer.lower():
        print(colored("Yay!\n", 'green'))
    else:
        print(colored("The answer is {!r}, not {!r}\n", 'red').format(correct_answer, answer))