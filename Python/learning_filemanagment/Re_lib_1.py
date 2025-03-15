import re


def get_email_zone(emails):
    pattern = r"(?<=@)\w+.\w+"
    email_domens = [re.search(pattern, email).group() for email in emails]
    domens = ["gmail.com", "test.in", "ya.ru", "mail.ru"]
    print(email_domens)
    for domen in domens:
        print(f"{domen}: {email_domens.count(domen)}")
        
        
get_email_zone(['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com'])
