def personInit(name='', secondName='', birthdayYear='', city='', email='', tel=''):
    print(f'Person: name={name}, secondName={secondName}, '
          f'birthdayYear={birthdayYear}, city={city}, '
          f'email={email}, tel={tel}')


myPerson = {'name': input('Введите имя: '),
            'secondName': input('Введите фамилию: '),
            'birthdayYear': input('Введите год рождения: '),
            'city': input('Введите город проживания: '),
            'email': input('Введите Email: '),
            'tel': input('Введите телефон: ')
            }

personInit(**myPerson)
