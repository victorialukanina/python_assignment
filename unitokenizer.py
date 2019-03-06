import unicodedata
class Token(object):
    """Метод инит вызывается, когда мы создаем объект или экземпляр на основе этого класса
	селф дает способность классу ссылаться самому на себя
	два аттрибута pos,token, они описывают объект: позицию начального символа и сам токен + type  для определения типа символа"""
    def __init__(self, pos, word, symbol_type):
        self.pos = pos
        self.word = word
		self.type = type

class UniTokenizer:
    #метод определяет тип символа
    def symbol_identificator(text):
	    if input.isalpha():
		    symbol_type = 'Alpha'
		if input.isdigit():
		    symbol_type = 'Digit'
        if input.isspace():
		    symbol_type = 'Space'
        if unicodedata.category(input) == 'P':
		    symbol_type = 'Punctuation'
        else:
            symbol_type = 'Undefined'		

    """Метод tokenize разбивает поданную на вход строку на символы, возвращает список токенов, похицию первого символа и тип"""
    def tokenize(text):	
	
	#список, куда будут записываться токены
	tokens=[]
	#в переменную записывается позиция первого символа
	first_pos = 0
	#в переменную записывается тип первого символа
	first_type = symbol_type(text[0])
	#если сменяется тип, записываем токен в список
	for i,s in enumerate(text):
	     #в тип записываем полученное значение тип_идентификатор для символа
	    type = symbol_type(s) 	
		#тип не соответствует предыдущему, значит токен закончился
		if type != first_type:
			#Добавляем его в конец списка
		    tokens.append(Token(first_pos,text[first_pos:i], first_type))
            first_pos = i
            first_type = type	
	#добавление последнего токена в строке		
    tokens.append(Token(first_pos,text[first_pos:i+1], first_type))
			
	for token in tokens:
	    print(token.word, token.pos, token.type)
	return tokens	
	
text = "ghjfy jhgj nbvfh"	
Tokenizer.tokenize(text)