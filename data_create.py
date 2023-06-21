def name_data():
    name = input('Введите Ваше имя: ')
    print('Очень красивое имя!')
    return name

def surname_data():
    surname = input('Введите Вашу фамилию: ')
    return surname

def phone_data():
    import re
    phone = input('Введите Ваш телефон: ')
    result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    while not result:
        print('Проверьте правильность Вашего номера телефона и повторите попытку')
        return phone_data()
    else:
        return phone

def address_data():
    address = input('Введите Ваш адрес: ')
    return address