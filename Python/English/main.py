import random
import time

from termcolor import colored

from tenses import tnss


def certificate(cor: int, inc: int, all_q: int) -> None:
    print()
    print(f'+{"-" * 39}+')
    print(colored("|             Certificate               |", "blue"))
    print(f'+{"-" * 39}+')
    print(f"| There were only a few questions: {colored(all_q, 'yellow')}  {" " * (3 - len(str(all_q)))}|")
    print(f"|          Correct answers: {colored(cor, 'green')}         {" " * (3 - len(str(cor)))}|")
    print(f"|          Incorrect answers: {colored(inc, 'red')}       {" " * (3 - len(str(inc)))}|")
    perc = round((cor / all_q) * 100, 1)
    print(f"| Percentage of correct answers: {colored(f"{perc}", "light_blue")}%{abs(len(str(perc)) - 6) * ' '}|")
    exec_time = f"{((time.time() - start) / 60):.3f}"
    print(f"|       Execution time: {colored(exec_time, "yellow")} min    {' ' * (4 - len(exec_time[: -4]))}|")
    print(f'+{"-" * 39}+')

def check_ans(answer: str, task: str) -> bool:
    if answer == task:
        return True
    
def answers_reaction(answer: str, task: str, rus_form: str) -> None:
    global correct, incorrect, all_questions
    if check_ans(answer, task):
            print(colored("Success", "light_green"))
            del tnss[rus_form]
            correct += 1
    else:
        print(colored("Wrong answer: ", "red"))
        print(colored(f"Your answer:  {answer}\nRight answer: {task}"))
        incorrect += 1
    all_questions += 1
    print(f"Remaind: {len(tnss)}/74")
    print("-" * 100)
    
def make_task() -> tuple:
    rus_form = random.choice(list(tnss.keys()))
    return (rus_form, " ".join(tnss[rus_form]))
    
def main() -> None:
    rus_form, task = make_task()
    print("Your word:", colored(f"{rus_form}", "yellow"))
    answer = input(colored("Enter three irregular verb forms: to ", "light_blue"))
    answers_reaction(answer, task, rus_form)

try:
    if __name__ == "__main__":
        start = time.time()
        print(colored("Hint write ALL the words separated by a space", "light_magenta"))
        print(colored("If you can use two words in the same form, use: '/'", "light_magenta"))
        correct, incorrect, all_questions = 0, 0, 0
        while tnss:
            main()
except:
    pass
finally:
    certificate(correct, incorrect, all_questions)
