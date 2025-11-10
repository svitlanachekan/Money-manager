# Проєкт: “Менеджер покупок”
# Створити невелику консольну програму, яка допомагає користувачу планувати покупки, рахувати суму, зберігати дані у файл і завантажувати їх при повторному запуску.

# Вітаю у менеджері покупок!
# Меню:
# 1. Додати покупку
# 2. Переглянути список
# 3. Порахувати загальну суму
# 4. Зберегти у файл
# 5. Завантажити з файлу
# 6. Вихід
# Ваш вибір: 1
# Введіть назву товару: Хліб
# Введіть кількість: 2
# Введіть ціну за одиницю: 25
# ✅ Хліб додано до списку!

def add_item(shopping_list):
    name = input("Enter a name: ")
    quantity = int(input("Enter a quantity: "))
    price = float(input("Enter a price: "))
    
    item = { #cписок словників, у яких різні ключі
        "name": name,
        "quantity": quantity,
        "price": price

    }

    shopping_list.append(item)

    print(f"✅ {name} is added to list!") # "✅" + "name" is added to list!

def show_list(shopping_list):
    # shopping_list = [{"name": "Bread", "quantity": 2, "price"; 2.0}]
    # for i in range(len(shopping_list)):
    #     print(f"{i+1}. {shopping_list[i]["name"]} - {shopping_list[i]["quantity"]} x {shopping_list[i]["price"]}€") # зверниться до словника і поверне Хліб

 if not shopping_list:
        print("List is empty")
        return
    
    print("\nYour list: ")

def count_total():
    pass

def save_to_file():
    pass

def load_from_file():
    pass
                


def main():
    print("Вітаю у менеджері покупок!")
    shopping_list = []

    while True:
        print('''
    Меню:
    1. Додати покупку
    2. Переглянути список
    3. Порахувати загальну суму
    4. Зберегти у файл
    5. Завантажити з файлу
    6. Вихід
            ''')
        try:
            choice = int(input("Enter a buying: "))
        except ValueError:
            print("Enter number 1-6!!")

        # if choice == 1: #иконується тільки одна із умов
        #     pass
        # elif choice == 2:
        #     pass

        match choice:
            case 1: # необхідно зупиняти
                add_item(shopping_list)
            case 2:
                show_list(shopping_list)
            case 3:
                count_total()
            case 4:
                save_to_file()
            case 5:
                load_from_file()
            case 6:
                print("See you!")
                break
            case _: # не знайшло попереднє, виконай це
                pass




main()



