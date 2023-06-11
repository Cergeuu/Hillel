def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(n) for n in range(10)])


def sum_range(start, end):
    if start > end:
        start, end = end, start
    print(sum(range(start, end)))


sum_range(10, 1)


def season(month):
    if month in [12, 1, 2]:
        return "зима"
    elif month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "літо"
    elif month in [9, 10, 11]:
        return "осінь"
    else:
        return "неправильний номер місяця"


month_number = int(input("Введіть номер місяця (від 1 до 12): "))
result = season(month_number)
print("Пора року:", result)


def get_filtered(a):
    for element in a:
        if element < 5:
            print(element)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
get_filtered(a)
