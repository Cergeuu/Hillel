#Створити файл та записати в нього рядок.
f = open('new_file.txt', mode='w')
f.write('Hello, world!')
f.close()

#Прочитати створений файл та вивести на консоль вміст файлу
f = open('new_file.txt', 'r')
print(f.read())
f.close()

#Додати ще один рядок до створеного файлу.
f = open('new_file.txt', mode='a')
f.write('Hello, Bob!')
f.close()

#Прочитати всі рядки з файлу та вивести на консоль.
f = open('new_file.txt', 'r')
print(f.readlines())
f.close()

#Завдання 1-4 прошу зробити міксовано щось через Context manager, а щось класично.

# Записати рядок у файл
with open("file.txt", "w") as file:
    file.write("Hello, world!")

# Прочитати вміст файлу та вивести на консоль
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Додати ще один рядок до файлу
with open("file.txt", "a") as file:
    file.write("\nThis is another line.")

# Прочитати всі рядки з файлу та вивести на консоль
with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Записати у файл все, що користувач вводить з консолі
with open("user_input.txt", "w") as file:
    while True:
        user_input = input("Enter a line (or 'exit' to quit): ")
        if user_input == "exit":
            break
        file.write(user_input + "\n")