import json


def main():
    print("1 - Посмотреть список задач; 2 - Добавить задачу; 3 - Изменить задачу; 4 - Удалить задачу; 5 - Найти задачу; 0 - Завершить работу программы;" + "\n" + "Введите номер команды (0-5):")
    number = int(input())
    if number == 0:
        exit()
    
    mask = ["Номер задачи в базе:", "Заголовок:", "Описание:", "Категория:", "Дедлайн:", "Приоритет:", "Статус:"]
    if number == 1:
        with open("data.json") as file:
            data = json.load(file)
        print("1 - Посмотреть список всех задач; 2 - Посмотреть список задач по категориям;" + "\n" + "Введите номер команды (1-2):")
        number = int(input())
        if number == 1:
            for dict in data:
                for counter in range(len(mask)):
                    print(mask[counter], list(dict.values())[counter])
                print("")
        
        if number == 2:
            categories = []
            for dict in data:
                if not dict['category'] in categories:
                    categories.append(dict['category'])

            for counter in range(len(categories)):
                print(counter + 1, "-", categories[counter] + ";", end = " ")
            print("\n" + "Введите номер команды " + "(1-" + str(len(categories)) + "):")
            number = int(input())
            category = categories[number-1]

            for dict in data:
                for counter in range(len(mask)):
                    if dict['category'] == category:
                        print(mask[counter], list(dict.values())[counter])
                print("")

    if number == 2:
        with open("data.json") as file:
            data = json.load(file)
        print("Введите название задачи: ")    
        title = input()
        print("Введите описание задачи: ")
        description = input()
        print("Введите категорию задачи: ") 
        category = input()
        print("Введите дедлайн задачи в формате YYYY-MM-DD: ")    
        deadline = input()
        print("Введите приоритет задачи (Высокий/Средний/Низкий): ")
        priority = input()
        print("Введите статус задачи (Выполнена/Невыполнена): ") 
        status = input()
        dict =  {"id": len(data)+1, "title": title, "description": description, "category": category, "due_date": deadline, "priority": priority, "status": status}
        data.append(dict)
        print(data)

    if number == 3:
        with open("data.json") as file:
            data = json.load(file)
        for dict in data:
            print("Номер задачи в базе:", dict["id"])
            print("Заголовок:", dict["title"])
            print("")
        print("Выберите номер задачи для изменения:")
        number = int(input())
        dict = data[number - 1]
        for counter in range(len(mask)):
            print(mask[counter], list(dict.values())[counter])
        print("Что вы хотите изменить? 1 - Заголовок; 2 - Описание; 3 - Категория; 4 - Дедлайн; 5 - Приоритет;" + "\n" + "Введите номер команды (1-5):")
        choice = int(input())
        print("Введите новое значение:")
        new_value = input()
        dict[list(dict.keys())[choice]] = new_value
        
    if number == 4:
        with open("data.json") as file:
            data = json.load(file)
        print("1 - Ввести номер задачи для удаления; 2 - Ввести категорию задач для удаления;" + "\n" + "Введите номер команды (1-2):")
        choice = int(input())
        if choice == 1:
            for dict in data:
                print("Номер задачи в базе:", dict["id"])
                print(dict["title"])
                print("")
            print("Введите номер задачи для удаления:")
            choice = int(input())
            data.pop(choice - 1)
            print(data)
        
        if choice == 2:
            for dict in data:
                print("Категория:", dict["category"])
                print(dict["title"])
                print("")
            print("Введите категорию задач для удаления:")
            category = input()
            for dict in data:
                if dict["category"] == category:
                    data.remove(dict)
            print(data)

    if number == 5:
        with open("data.json") as file:
            data = json.load(file)
        print("1 - Искать по ключевым словам; 2 - Искать по категории поиска; 3 - Искать по статусу выполнения задачи;" + "\n" + "Введите номер команды (1-3):")
        choice = int(input())
        if choice == 1:
            print("Введите слово(сочетание слов), содержащееся в названии или описании задачи: ")
            key_words = input()
            for dict in data:
                if (key_words in dict["title"]) or (key_words in dict["description"]):
                    for counter in range(len(mask)):
                        print(mask[counter], list(dict.values())[counter])
                    print("")

        if choice == 2:
            print("Введите категорию поиска: ")
            search_category = input()
            for dict in data:
                if dict["category"] == search_category:
                    for counter in range(len(mask)):
                        print(mask[counter], list(dict.values())[counter])
                    print("")

        if choice == 3:
            print("1 - Выполнена; 2 - Не выполнена;" + "\n" + "Введите номер команды (1-2):")
            search_status = int(input())
            for dict in data:
                if ((dict["status"] == "Выполнена") and (search_status == 1)) or ((dict["status"] == "Не выполнена") and (search_status == 2)):
                    for counter in range(len(mask)):
                        print(mask[counter], list(dict.values())[counter])
                    print("")

main()
