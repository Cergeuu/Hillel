# Lambda
print_symbol = lambda symbol, count=100: print(str(symbol) * count)
print_symbol('#', 5)

get_max = lambda num1, num2: num1 if num1 > num2 else num2
print(get_max(3, 5))

always_return_10 = lambda: 10

print(always_return_10())


# Decorators
def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def hello_world():
    return "hello world"


formatted_text = hello_world()
print(formatted_text)


# List comprehension
list1 = [44, 54, 64, 74, 104]
list2 = [x + 6 for x in list1]
print(list2)

list3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [x ** 2 for x in list3]
print(list4)

car_dict = {
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}

list5 = [key.upper() for key in car_dict if car_dict[key] <= 5000]
print(list5)

