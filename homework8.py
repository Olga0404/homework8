first= input ('Введите число:')
second= input ('Введите второе число:')
third= input ('Введите третье число:')
if first== second and first== third:
    print ("Совпадений", 3)
elif first== second or first== third or second== third:
    print ("Совпадений",2)
elif first!= second or first!= third or second!= third:
    print ("Совпадений",0)