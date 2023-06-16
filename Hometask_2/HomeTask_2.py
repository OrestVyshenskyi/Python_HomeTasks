# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
from typing import Callable
def notebook() -> Callable[[str], None] [[None], list[str]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all

add_tod, all_todos = notebook()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def sum(number: int) -> str:
    num = str(number)
    length = len(num)
    nums = []

    for i, j in enumerate(num):
        if j == '0':
            pass
        else:
            nums.append(j + '0' * (length - 1 - i))

    return ' + '.join(nums)


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(count)

    return inner

@counter
def sum(a, b):
    return a + b


sum(1, 3)
sum(1, 3)
sum(1, 3)
sum(1, 3)