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

def class_countdown():
    class Countdown:
        def __init__(self, n):
            self.n = n
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.n <= 0:
                raise StopIteration
            c = self.n
            self.n -= 1
            return c
    list_number = []
    for number in Countdown(5):
        list_number.append(number)
    return list_number
print('Список числел от 5 до 1:',class_countdown())