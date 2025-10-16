import random

#1
password = input('Enter any password(at least 8 symbols): ')  #Пользователь вводит пароль. 

#Проверка пароля на длину: 
if len(password)<8:
    print('Password was too short.')
if len(password) >= 8:
    print('Your password was saved succesfully!')


#2
#задаем рандомное значение для состояния сервера. Выбор происходит --
#из двух состояний: онлайн и оффлайн

server_conditions = ['online', 'offline']
server = random.choice(server_conditions)  #функция choice в рандом, выбирает рандомное значение


if server == 'online':
    print('Connection was successful!')
elif server == 'offline':
    print('There is NO connection.')
else:
    print('Emm...what`s that bro?')


#3
num = random.randrange(1, 101)

if num in range(1, 31):
    print(f'{num} -- Low level')
elif num in range(31, 71):
    print(f'{num} -- Middle level')
elif num in range(71, 101):
    print(f'{num} -- Hight level')
else:
    print('You entered wrong num.')


#4
checksum_original = []
checksum_current = []

status = 'File wasn`t changed' if checksum_current == checksum_original else 'File was changed.'
print(status)

#5
conditions = ['ERR', 'WRN', 'INF']
event_code = random.choice(conditions)

match event_code:
    case 'ERR':
        print('System fault')
    case 'WRN':
        print('Warning.')
    case 'INF':
        print('Message with information!')
    case _:
        print('Unknown code')

