# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)
# import string
# def DeleteText(text):
#     textList = text.split()
#     countList = []
#     for i in range(0, len(textList)):
#         if 'абв' in textList[i]:
#             countList.append(i)
#     for i in range(len(countList)-1, -1, -1):
#         textList.pop(countList[i])
#     text = ' '.join(textList)
#     return text

# s = '1абв 2222 3бв33 абв 5абв абв6 777 888 999 '
# print ('Исходная строка: ' + s)
# print ('Итоговая строка: ' + DeleteText(s))




#---------------------------------------------------------------------------------------------------------
#Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
# def PrintField (pole): # вывести на экран текущее игровое поле
#     for i in pole:
#         s = ''
#         for j in i:
#             s += '|' + str(j)
#         s += '|'
#         print (s)

# def CheckSymbol (moveNum): # проверка кто сейчас ходит
#     if moveNum%2 == 0:
#         return 'O'
#     else:
#         return 'X'

# def CheckWin(pole): # проверка на победу
#     if (pole[0][0]) == 'X' and (pole[0][1]) == 'X' and (pole[0][2]) == 'X':
#         return 'X'
#     elif (pole[1][0]) == 'X' and (pole[1][1]) == 'X' and (pole[1][2]) == 'X':
#         return 'X'
#     elif (pole[2][0]) == 'X' and (pole[2][1]) == 'X' and (pole[2][2]) == 'X':
#         return 'X'
#     elif (pole[0][0]) == 'X' and (pole[1][0]) == 'X' and (pole[2][0]) == 'X':
#         return 'X'
#     elif (pole[0][1]) == 'X' and (pole[1][1]) == 'X' and (pole[2][1]) == 'X':
#         return 'X'
#     elif (pole[0][2]) == 'X' and (pole[1][2]) == 'X' and (pole[2][2]) == 'X':
#         return 'X'
#     elif (pole[0][2]) == 'X' and (pole[1][2]) == 'X' and (pole[2][2]) == 'X':
#         return 'X'
#     elif (pole[0][0]) == 'X' and (pole[1][1]) == 'X' and (pole[2][2]) == 'X':
#         return 'X'
#     elif (pole[0][2]) == 'X' and (pole[1][1]) == 'X' and (pole[2][0]) == 'X':
#         return 'X'
#     elif (pole[0][0]) == 'O' and (pole[0][1]) == 'O' and (pole[0][2]) == 'O':
#         return 'O'
#     elif (pole[1][0]) == 'O' and (pole[1][1]) == 'O' and (pole[1][2]) == 'O':
#         return 'O'
#     elif (pole[2][0]) == 'O' and (pole[2][1]) == 'O' and (pole[2][2]) == 'O':
#         return 'O'
#     elif (pole[0][0]) == 'O' and (pole[1][0]) == 'O' and (pole[2][0]) == 'O':
#         return 'O'
#     elif (pole[0][1]) == 'O' and (pole[1][1]) == 'O' and (pole[2][1]) == 'O':
#         return 'O'
#     elif (pole[0][2]) == 'O' and (pole[1][2]) == 'O' and (pole[2][2]) == 'O':
#         return 'O'
#     elif (pole[0][2]) == 'O' and (pole[1][2]) == 'O' and (pole[2][2]) == 'O':
#         return 'O'
#     elif (pole[0][0]) == 'O' and (pole[1][1]) == 'O' and (pole[2][2]) == 'O':
#         return 'O'
#     elif (pole[0][2]) == 'O' and (pole[1][1]) == 'O' and (pole[2][0]) == 'O':
#         return 'O'
#     else:
#         return '-'
    

# def Move(moveNumber, m, pole): # выполнить ход
#     if m == 1 or m ==2 or  m ==3:
#         y = 1
#     elif m == 4 or m ==5 or  m ==6:
#         y = 2
#     elif m == 7 or m ==8 or  m ==9:
#         y = 3
#     if m == 1 or m ==4 or  m ==7:
#         x = 1
#     elif m == 2 or m ==5 or  m ==8:
#         x = 2
#     elif m == 3 or m ==6 or  m ==9:
#         x = 3
#     if (pole[y-1][x-1]) == 'X' or (pole[y-1][x-1]) == 'O':
#         print ('Поле уже занято')
#         m = int(input ('Введите номер клетки куда поставить ' + CheckSymbol(moveNumber) + ': '))
#         Move (moveNumber, m, pole)
#     else:
#         pole[y-1][x-1] = CheckSymbol(moveNumber)
#     PrintField(pole)
#     if CheckWin(pole) == 'X':
#         print ('Победа X!')
#         return
#     elif CheckWin(pole) == 'O':
#         print ('Победа O!')
#         return
#     if moveNumber == 9:
#         print ('Ничья!')
#         return  
#     moveNumber += 1
#     m = int(input ('Введите номер клетки куда поставить ' + CheckSymbol(moveNumber) + ': '))
#     Move (moveNumber, m, pole)

# pole = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# PrintField(pole)
# m = int(input ('Введите номер клетки куда поставить X: '))
# Move (1, m, pole)


#---------------------------------------------------------------------------------------------------------
#40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def Encode(text):
    result = ''
    prev = text[0]
    count = 0
    for s in text:
            if s != prev:
                result += f'{count}{prev}'
                prev = s
                count = 1
            else:
                count += 1
    result += f'{count}{prev}'
    return result

def Decode(text):
    result = ''
    digit = True
    count = ''
    for s in text:
        if digit:
            count = int(s)
            digit = False
        else:
            result += int(count)*s
            digit = True
    return result

text = '111112222334445'
print ('Исходные текст: ' + text)
encodeText = Encode(text)
print ('Сжатый текст: ' + encodeText)
decodeText = Decode (encodeText)
print ('Восстановленный текст: ' + decodeText)

