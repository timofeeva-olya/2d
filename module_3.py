def send_email(recipient,*, sender = "university.help@gmail.com"):

    if (('@' not in recipient or '@' not in sender) or not
    (recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')))):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса" , sender , "на адрес", recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email("olay")
send_email("university.help@gmail.com")
send_email("olya.sinyakova20.02@mail.ru")
send_email("olya@.ru", sender = "ient@example.com")