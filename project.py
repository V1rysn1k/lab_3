def logger(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            print(f"Вызов функции {func.__name__} с аргументами {args} {kwargs}")
        else:
            print(f"Вызов функции {func.__name__} с аргументами {args}")
        try:
            result = func(*args, **kwargs)
            print(f"Функция {func.__name__} вернула {result}")
            return result
        except Exception as e:
            print(f"Функция {func.__name__} вызвала ошибку: {e}")
            return None
    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


@logger
def greet(name):
    message = f"Привет, {name}!"
    print(message)
    return message

add(54, 12)
divide(21, 6)
divide(36, 0)
greet("Dazzle")