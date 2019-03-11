from unitokenizer import Token, UniTokenizer
import shelve
#метод сохраняет токены типа 'alpha' и 'digit' в базу данных
def indexator(text):
    #создается файл и присваивается переменной db
    db = shelve.open("test.db")
    #получаем токены при помощи универсального токенизатора
    tokens = UniTokenizer.tokenize(text)
    #счетчик токенов в тексте на вход
    i = 0
    for token in tokens:
        if token.type is 'Alpha' or token.type is 'Digit':
	    #в базу данных записывается позиция токена, значение сам токен
            db[str(i)] = token
            i += 1
    return db	
