def get_name():
    with open('D:/lesson_Python/homework_python/homework_009/homework_task_002/homework_task_002_002/file.txt', 'r', encoding="utf-8") as f:
        listName = []
        for line in f.readlines()[::3]:
            listName.append(line.rstrip('\n'))
        return listName


def get_number():
    with open('D:/lesson_Python/homework_python/homework_009/homework_task_002/homework_task_002_002/file.txt', 'r', encoding="utf-8") as f:
        listNumber = []
        for line in f.readlines()[1::3]:
            listNumber.append(line.rstrip('\n'))
        return listNumber


def what_to_do():
    with open('D:/lesson_Python/homework_python/homework_009/homework_task_002/homework_task_002_002/file.txt', 'r', encoding="utf-8") as f:
        listWtd = []
        for line in f.readlines()[2::3]:
            listWtd.append(line.rstrip('\n'))
        return listWtd


def export_book(book: dict):
    with open('D:/lesson_Python/homework_python/homework_009/homework_task_002/homework_task_002_002/newfile.txt', 'w', encoding="utf-8") as newfile:
        for key, value in book.items():
            newfile.write(f'{key}:{value}\n')        