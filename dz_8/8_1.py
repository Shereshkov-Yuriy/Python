import re

email_address = ['monty@ya.ru', 'mon&ty@ya.ru', 'monty@dya&.ru', 'monty@yaru']


def email_parse(email_address):
    RE_EMAIL = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_EMAIL.match(email_address):
        raise ValueError(f'Неверный e-mail: {email_address}')
    print(RE_EMAIL.match(email_address).groupdict())


for email in email_address:
    try:
        email_parse(email)
    except ValueError as verr:
        print(verr)
