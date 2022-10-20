while True:
    a = float(input('Перше число = '))
    s = input ("Дія (+, - , *, /): ")
    if s == '0':
        break
    if s not in ('+', '-', '*', '/'):
        continue
    b = float(input('Друге число = '))
    if s == '+':
        print(a + b)
    if s == '-':
        print(a - b)
    if s == '*':
        print(a * b)
    if s == '/':
        if b!= 0:
            print(a / b)
        else:
            print("Ошибка")
        
        
