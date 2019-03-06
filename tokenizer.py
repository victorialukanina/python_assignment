﻿
class Token(object):
    """Метод инит вызывается, когда мы создаем объект или экземпляр на основе этого класса
	селф дает способность классу ссылаться самому на себя
	два аттрибута pos,token, они описывают объект: позицию начального символа и сам токен"""
    def __init__(self, pos, word):
        self.pos = pos
        self.word = word

class Tokenizer:
    """Метод tokenize разбивает поданную на вход строку на символы, проходится по символам и определяет буква или нет"""
    def tokenize(text):	
	
	#список, куда будут записываться токены
	tokens=[]
	isToken = False
	for i,s in enumerate(text):
	    #если символ буквенный
	    if s.isalpha():
		    #начинаем счетчик
			start = i
			isToken = True
		else:	
		    #если не буквенный
		    if not s.isalpha():
			    #токен закончился
			    isToken = False
				#Добавляем его в конец списка
		        tokens.append(Token(text[start:i], start))	    		           
	for token in tokens:
	    print(token.word, token.pos)
	return tokens	
#добавляем последний токен	
tokens.append(Token(text[start:i+i], start))	
	
text = ""	
Tokenizer.tokenize(text)