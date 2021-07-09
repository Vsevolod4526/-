import sys



def decimal_to_another(chislo,sistema_schislenia): #int первый аргумент

    int_basa_sistemi=len(sistema_schislenia)

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

    return itog_vivod





# перевод в 10ую
def another_to_decimal(number_in_first_base,first_base):

    spisok=[]

    for i in number_in_first_base:
        spisok.append(first_base.find(i))


    #print(spisok)
    spisok.reverse()

    base=len(first_base)
    summa=0
    x=0
    for i in spisok:
        summa=i*(base**x)+summa
        x+=1

    return summa
    
    
help_info='''

Справка о том,как пользоваться программой :

1) Вводить аргументы без кавычек и через пробел после названия файла с программой
2) Допустимое количество аргументов 2 или 3 .
3) В зависимости от количества аргументов запускается различная функциональность: 

Пример ввода с 2-мя аргументами: task1.py 50 01234567

1ый аргумент это число в 10ой системе
2ой аргумент это система исчисления
Вывод - число в системе исчисления, которая указана во втором аргументе



Пример с 3-мя аргументами: task1.py BDEA ABCDE 01

1ый аргумент это число в системе исчисления второго аргумента
2ой аргумент это система исчисления первого аргумента
3ий аргумент это система исчисления в которой предполагается вывод
Вывод - число в системе исчисления, указанной в третьем аргументе

'''    


if __name__ == "__main__":
    #print(sys.argv)

    if len(sys.argv)!=3 and len(sys.argv)!=4 :
        print('Ошибка , ввод предусмотрен только для двух или трех аргументов')
        print(help_info)
        sys.exit()
        

    if len(sys.argv)==3:
        if sys.argv[1].isdigit()!=True:
            print('Ошибка ,при вводе двух аргументов первый аргумент должен быть числовым.')
            sys.exit()
        print(decimal_to_another(int(sys.argv[1]),sys.argv[2]))
    elif len(sys.argv)==4:
        print(decimal_to_another(another_to_decimal(sys.argv[1],sys.argv[2]),sys.argv[3]))


    
        
        

    
    
