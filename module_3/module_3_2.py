def send_email(message: str, recipient: str, *, sender = 'university.help@gmail.com'):

    def verification_email(email: str):
        if not '@' in email:
            return False

        if not email.endswith('.com') and not email.endswith('.ru') and not email.endswith('.net'):
            return False

        return True


    if not verification_email(recipient) or not verification_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')