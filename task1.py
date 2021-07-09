import sys



if __name__ == "__main__":
    #print(sys.argv)

    if len(sys.argv)!=3:
        print('Ошибка , два аргумента не введены(ввести строго два аргумента через пробел). Пример правильного ввода: task1.py 44 kotiki')
        sys.exit()
    if sys.argv[1].isdigit()!=True:
        print('Ошибка , первый аргумент должен быть числовым.Ввод аргументов через пробел (ввести строго два аргумента). Пример правильного ввода: task1.py 44 kotiki')
        sys.exit()
    if type(sys.argv[2])!=int and type(sys.argv[2])!=str:
        print('Ошибка , второй аргумент должен быть типа int или str (воод без скобок и кавычек).Ввод аргументов через пробел (строго два аргумента). Пример правильного ввода: task1.py 44 kotiki')
        sys.exit()
    chislo=int(sys.argv[1])
    sistema_schislenia=sys.argv[2]

    int_basa_sistemi=len(sys.argv[2])

    #print(chislo)
    #print(int_basa_sistemi)



    if chislo<int_basa_sistemi:
        perevod_celoe=chislo

    else:
        ostatok=chislo%int_basa_sistemi
        chislo=chislo-ostatok
        perevod_celoe=str(ostatok)
        while chislo>int_basa_sistemi:
            chislo=chislo//int_basa_sistemi
            
            if chislo<int_basa_sistemi:
                perevod_celoe=str(chislo)+perevod_celoe
            else:
                perevod_celoe=str(chislo%int_basa_sistemi)+perevod_celoe

    #перевод строки цифр в систему счисления
    itog_vivod=''

    for i in perevod_celoe:
        itog_vivod=itog_vivod+sistema_schislenia[int(i)]
    

    
    #print(perevod_celoe)

    print(itog_vivod)
    
