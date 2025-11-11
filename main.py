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

def add_item(shopping_list): # додаємо до списку покупок това
    name = input("Enter a name: ") # найменування
    quantity = int(input("Enter a quantity: ")) # кількість
    price = float(input("Enter a price: ")) # ціна
    
    item = { # словник, у яких різні ключі та значення
        "name": name, # ключ "name" має значення, яке зберігається у змінній "name" (z.B: bread, milk)
        "quantity": quantity, # кількість товару 
        "price": price # ціна
    }

    shopping_list.append(item) # додаємо до списку список покупок

    print(f"✅ {name} is added to list!") # "✅" + "name" is added to list! виводимо на екран

    
def show_list(shopping_list): # продивилися перелік покупок
    # shopping_list = [{"name": "Bread", "quantity": 2, "price"; 2.0}]
    # for i in range(len(shopping_list)):
    #     print(f"{i+1}. {shopping_list[i]["name"]} - {shopping_list[i]["quantity"]} x {shopping_list[i]["price"]}€") # зверниться до словника і поверне Хліб

    if not shopping_list: # якщо вони відсутні, придбання відсутнє
        print("\nList is empty")
        return
    
    print("\nYour list: ")
    for i, item in enumerate(shopping_list, start=1): # у списку покупок, починаючи з первої позиції перебирає елементи послідовності (покупки) одночасно отримує їх індекси, тобто додає автоматичну нумерацію (1., 2., ...) 
        # print(i, item)
        print(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€") # видає список у вигляді номер товара, крапочка, найменування товару через тіре кількіть помножена на ціну у евро


def count_total(shopping_list): # розраховує загальну суму покупок
    total = 0 # спочатку загальна сума покупок дорівнює 0, і потім все до неї додається 
    for item in shopping_list: # 
        total += item["quantity"] * item["price"]
    print(f"Total price: {total:.2f}€") # виводить суму з округленням у два символа після коми

def save_to_file(shopping_list): # зберігаємо список до текстового файлу 
    # "w" - перезаписує файл, якщо той є або створює новий, якщо немає
    # "a" - дописує (за замовчуванням у кінці файлу) у існуючий файл, якщо файлу немає - помилка, редагує-?
    # file = open("text.txt", "w", encoding="utf-8")
    # file.write("Ok")
    # file.write("2 line")
    # file.write("new_line")
    # file.close()
    # with open("text.txt", "w", encoding="utf-8") as f:
    #     f.write("Ok")
    #     f.write("2 line")
    #     f.write("new_line")
    with open("text.txt", "w", encoding="utf-8") as f: # щоб зберігти файл, спочатку потрібно відкрити, при умові написання українскькою зазначаємо шифрування utf-8, файл не потрібно закривати - робить автоматично
        for i, item in enumerate(shopping_list, start=1): # зберігаючи файл, знов проходить по списку з першого та до і-того
            # print(i, item)
            f.write(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€\n") # кожний новий товар виводиться з нового рядку за допомогою \n
    print("✅Shopping_list saved to text.txt") # виводить список покупок у текстовому файлі (окрема вкладка .txt)

def load_from_file():
    shopping_list = []
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip()[:-1].split()
            # for i in range(1, len(line_list), 2):
            name, quantity, price = line_list[1], line_list[3], line_list[5]
            item = {
                "name": name,
                "quantity": int(quantity),
                "price": float(price)
            }
            shopping_list.append(item)
    return shopping_list

                


def main():
    print("Вітаю у менеджері покупок!")
    shopping_list = []

    while True:
        print("----------#-----------")
        print('''
    Меню:
    1. Додати покупку
    2. Переглянути список
    3. Порахувати загальну суму
    4. Зберегти у файл
    5. Завантажити з файлу
    6. Вихід
            ''')

        try: # перевірка на наявність помилок
            choice = int(input("Ваш вибір: "))

            # if choice == 1:
            #     pass
            # elif choice == 2:
            #     pass
            match choice:
                case 1:
                    try:
                        add_item(shopping_list)
                    except:
                        print("Error!")
                case 2:
                    show_list(shopping_list)
                case 3:
                    count_total(shopping_list)
                case 4:
                    save_to_file(shopping_list)
                case 5:
                    load_from_file()
                case 6:
                    print("See you!!")
                    break
                case _: # накшталт else
                    print("Error! Enter number 1-6!")
                    
        except ValueError:
            print("Enter number 1-6!!")


if __name__ == "__main__": #якщо імʼя співпадає, то виконай main
    main() 

# try:  # перша основна перевірка
#     "program"
#     result = "OK"
# except ValueError:
#     print("ValueError")
#     result = "ValueError"
# except ZeroDivisionError:
#     print()
#     result = "ZeroDivisionError"
# except:
#     print("any errors")
#     result = "any errors"
# else:
#     result = "else"
#     pass
# finally:  # виконується завжди!
#     print(result)
#     pass

# try -> finally
# try -> except -> ... -> except -> finally
# try -> except -> ... -> except --> else -> finally

# try -> finally
# except -> finally
# else -> finally
