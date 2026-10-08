x = int(input('введите ваше x: '))

match x:
    case _ if x < -5:
        print('-infinity, -5')
    case _ if -5 <= x <=5:
        print('-5,5')
    case _ if x>5:
        print('5,+infinity')