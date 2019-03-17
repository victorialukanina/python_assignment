
class Token(object):
    
    def __init__(self, pos, word):
        """Метод инит вызывается, когда мы создаем объект или экземпляр на основе этого класса
	селф дает способность классу ссылаться самому на себя
	два аттрибута pos,token, они описывают объект: позицию начального символа и сам токен"""
        self.pos = pos
        self.word = word

class Tokenizer:
    
    def tokenize(text):
        """Метод tokenize разбивает поданную на вход строку на символы, проходится по символам и определяет буква или нет"""
	#список, куда будут записываться токены
        tokens = []
        isToken = False
        for i,s in enumerate(text):
	    #если символ буквенный
            if s.isalpha():
                if isToken == False:
                    #начинаем счетчик
                    start = i
                    isToken = True
            else:
	        #токен закончился
                isToken = False
                #Добавляем его в конец списка
                tokens.append(Token(start, text[start:i]))
        if isToken == True:
            tokens.append(Token(start, text[start:i+1]))
        for token in tokens:
            print(token.word, token.pos)
        return tokens		
	
text = "kjhkj huiuhi yuyt"	
Tokenizer.tokenize(text)
