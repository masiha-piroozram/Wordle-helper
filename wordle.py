import os
rl = open('5letterwords.txt').readlines()
try:
    cache = open('cache.txt','w' , encoding='utf-8')
    cache.truncate(0)
except:
    cache = open('cache.txt' , 'w+' ,encoding='utf-8')


def correct_letter_place(letter , place):
    cache_rl = open('cache.txt').readlines()
    if os.path.getsize('cache.txt') == 0:
        cache = open('cache.txt','w')
        for i in rl:
            if i[int(place)-1] == letter:
                cache.write(i)
                #print(i)
    else:
        #cache_rl = open('cache.txt').readlines()
        cache = open('cache.txt' , 'w')
        
        for i in cache_rl :
            if i[int(place)-1] == letter:
                cache.write(i)
                #print(i)

########################

def wrong_letter(wrong_letter):
    cache_rl = open('cache.txt').readlines()
    cache = open('cache.txt' , 'a')
    if os.path.getsize('cache.txt') == 0:
        cache = open('cache.txt' , 'w')
        for i in rl:
            if wrong_letter not in i:
                cache.write(i)
                #print(i)
    else:
        cache = open('cache.txt' , 'w')
        for i in cache_rl:
            if wrong_letter not in i:
                cache.write(i)

########################


def correct_letter(correct_letter , wrong_place):
    cache_rl = open('cache.txt').readlines()
    cache = open('cache.txt' , 'a')
    if os.path.getsize('cache.txt') == 0:
        cache = open('cache.txt' , 'w')
        for i in rl:
            if correct_letter  in i and correct_letter != i[int(wrong_place)-1] :
                cache.write(i)
                #print(i)
    else:
        cache = open('cache.txt' , 'w')
        for i in cache_rl:
            if correct_letter in i and correct_letter != i[int(wrong_place)-1]:
                cache.write(i)
