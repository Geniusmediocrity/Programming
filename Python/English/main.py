import random

from termcolor import colored

from tenses import tnss


def certificate(cor: int, inc: int, all_q: int) -> str:
    print()
    print(f'+{"-" * 39}+')
    print(colored("|             Certificate               |", "blue"))
    print(f'+{"-" * 39}+')
    print(f"| There were only a few questions: {colored(all_q, 'yellow')}    |")
    print(f"|          Correct answers: {colored(cor, 'green')}           |")
    print(f"|          Incorrect answers: {colored(inc, 'red')}         |")
    perc = round((cor / all_q) * 100, 1)
    print(f"| Percentage of correct answers: {colored(f"{perc}", "blue")}%{abs(len(str(perc)) - 6) * ' '}|")
    print(f'+{"-" * 39}+')

def check_ans(answer: str, task: str) -> bool:
    if answer == task:
        return True
    
def main():
    global correct, incorrect, all_questions
    
    rus_f = random.choice(list(tnss.keys()))
    task = " ".join(tnss[rus_f])
    print("Your word:", colored(f"{rus_f}", "yellow"))
    
    answer = input(colored("Enter three irregular verb forms: to ", "light_blue"))
    if check_ans(answer, task):
        print(colored("Success", "light_green"))
        del tnss[rus_f]
        correct += 1
    else:
        print(colored("Wrong answer: ", "red"))
        print(colored(f"Your answer:  {answer}\nRight answer: {task}"))
        incorrect += 1
    all_questions += 1
    print("-" * 100)   
    

try:
    if __name__ == "__main__":
        print(colored("Hint write ALL the words separated by a space", "light_magenta"))
        print(colored("If you can use two words in the same form, use: '/'", "light_magenta"))
        correct, incorrect, all_questions = 0, 0, 0
        while tnss:
            
            main()
        certificate(correct, incorrect, all_questions)
except:
    certificate(correct, incorrect, all_questions)
