'''
Секция 1. Практическое задание Python/Ruby

1.1 Экранирование
'''

class EmailEditor:
    '''
    Класс для экранирования почты
    '''

    def __init__(self, sym: str):
        self.sym = sym

    def edit(self, email: str):
        # Проверка на корректность почты
        if '@' not in email:
            return f'{len(email)*self.sym}'

        # Получение индекса @ (отображает кол-во символов до @)
        email_name_length = email.index('@')

        # Замена символов в почте
        formatted_email = self.sym * email_name_length + email[email_name_length:]
        return formatted_email


class PhoneNumberEditor:
    '''
    Класс для экранирования номера телефона
    '''

    def __init__(self, sym: str, length: int = 3):
        self.sym = sym
        self.length = length

    def edit(self, number: str):
        # Проверка на корректность номера
        if number[:2] != '+7':
            return None

        # Удаление пробелов
        number = number.replace(' ', '')

        # Скрытие номера
        number = f'{number[:-self.length]}{self.sym*self.length}'

        # Добавление пробелов
        formatted_phone = number[:2] + ' ' + number[2:5] + ' ' + number[5:8] + ' ' + number[8:]
        return formatted_phone


class SkypeEditor:
    '''
    Класс для экранирования скайпа
    '''

    def __init__(self, sym: str):
        self.sym = sym

    def edit(self, skype: str):
        # Проверка на корректность
        if 'skype' not in skype:
            return None

        # Проверка на отсутствие ссылки
        if skype.startswith('skype:'):
            return 'skype:xxx'

        # Проверка на наличие ссылки
        elif skype.startswith('<a'):
            start_index = skype.find('href="skype:') + len('href="skype:')
            end_index = skype.find('?call')

            # Скрытие скайпа
            formated_skype = skype[:start_index] + self.sym * 3 + skype[end_index:]
            return formated_skype



email_editor = EmailEditor('x')
print(email_editor.edit('test_test@mail.ru'))

number_editor = PhoneNumberEditor('x')
print(number_editor.edit('+7 666 777       888'))

skype_editor = SkypeEditor('x')
print(skype_editor.edit('<a href=\"skype:test?call\">skype</a>'))
print(skype_editor.edit('skype:test'))