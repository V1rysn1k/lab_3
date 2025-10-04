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

def fibonaccі(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
list_number = []
for number in fibonaccі(5):
    list_number.append(number)
print('Список чисел последовательности Фибоначи длиной 5:', list_number)

def financial_calculator():
    from decimal import Decimal, getcontext, ROUND_HALF_UP

    getcontext().prec = 28
    getcontext().rounding = ROUND_HALF_UP

    initial_amount = Decimal(input("Введите начальную сумму вклада: ").strip())
    annual_rate = Decimal(input("Введите годовую процентную ставку: ").strip())
    years = Decimal(input("Введите срок вклада в годах: ").strip())

    monthly_rate = annual_rate / Decimal('12') / Decimal('100')
    months = years * Decimal('12')

    final_amount = initial_amount * ( (Decimal('1') + monthly_rate) ** months )
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount

    print(f"Итоговая сумма вклада: {final_amount} руб.")
    print(f"Общая прибыль: {profit.quantize(Decimal('0.01'))} руб.")

financial_calculator()

def fract():
    from fractions import Fraction


    frac1 = Fraction(3, 4)
    frac2 = Fraction(5, 6)

    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2

    print(f"3/4 + 5/6 = {addition}")
    print(f"3/4 - 5/6 = {subtraction}")
    print(f"3/4 * 5/6 = {multiplication}")
    print(f"3/4 / 5/6 = {division}")
    pass
fract()

def data_time():
    from datetime import datetime, date

    data_time = datetime.now()
    print("Текущая дата и время:", data_time.strftime("%Y-%m-%d %H:%M:%S"))
    data = date.today()
    print("Текущая дата:", data.strftime("%Y-%m-%d"))
    time = data_time.time()
    print("Текущее время:", time.strftime("%H:%M:%S"))
data_time()

def birthday():
    from datetime import date, timedelta


    birthday = date(2005, 9, 2)
    today = date.today()
    days_since_birthday = (today - birthday).days
    this_year_birthday = birthday.replace(year=today.year)

    if this_year_birthday < today:
        next_birthday = this_year_birthday.replace(year=today.year + 1)
    else:
        next_birthday = this_year_birthday

    days_until_next_birthday = (next_birthday - today).days

    print(f"Дней с момента рождения: {days_since_birthday}")
    print(f"Дней до следующего дня рождения: {days_until_next_birthday}")
birthday()