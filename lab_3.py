def list_sqr():
    sqr = [x**2 for x in range(1, 10)]
    return sqr
print('Список квадратов чисел от 1 до 10:',list_sqr())

def list_chet():
    chet = [x for x in range(1, 20) if x % 2 == 0]
    return chet
print('Список чётных чисел от 1 до 20:',list_chet())

def create_list_word():
    words = ["python", "Java", "c++", "Rust", "go"]
    up_words = [w.upper() for w in words if len(w) > 3]
    return up_words
print('Список слов в верхнем регистре и длиннее 3 символов:',create_list_word())