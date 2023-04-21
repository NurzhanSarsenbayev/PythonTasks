# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

text=str(input('Type in your string: '))
count_dict={}
for letter in text:
    count_dict[letter] = count_dict.get(letter,0)+1
    print(f'{letter}' if count_dict.get(letter)<2 else f'{letter}_{count_dict.get(letter)-1}', end=' ' )
    # print(f'{letter} if {count_dict.get==0} : else _{count_dict.get(letter) - 1} ')

