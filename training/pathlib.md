# pathlib - библиотека для работы с путями в питоне

Её отличие от классического os(работы со строками) в том, что оно воспринимает пути как объекты и имеет в своей логике объектно-ориентированный подход.
Path имеет множество методов, например
```python
from pathlib import Path

def main():
    print(Path.cwd())
    path = Path("usr/bin/python3")
    print(path)

if __name__ == '__main__':
    main()
```

Где внутри функции main мы принтуем текущую рабочую директорию и создаем объект типа Path, к которому так же можем применять методы

```python
from pathlib import Path
path = Path.cwd() / "bin" / "python3"
```

Благодаря такому доступу к файлу мы можем с ним взаимодействовать как нам нужно, например

```python
from pathlib import Path
path = Path.cwd() / "projectstructure.md"
with path.open() as f:
    print(f.read())
# альтерантивный вариант - написать
# print(path.read_text()) - тоже выведет содержимое файла
```
применяется path.open(), потому что open() - встроенный метод для объектов Path, то же самое, что и with open (filename) as f: по сути

### resolve

ВАЖНОЕ ЗАМЕЧАНИЕ. cwd - не имеет ничего общего с расположением файлов запускаемых или искомых. Это просто место в терминале, из которого мы запускаем скрипт. Можем запустить хоть из корневой папки, тогда она и будет cwd

Теперь поговорим о path.resolve()
Это такой метод, который возвращает новый объект типа path, если путь относительный (неполный) — resolve() соединяет его с cwd, если абсолютный — просто нормализует его (убирает лишние артефакты). resovle не проверяет существование файла!

```python
from pathlib import Path
path = Path("projectstructure.md")
print(path)
print(path.resolve()) 
# можно, например path.resolve.parent - выведет путь до родительской папки 
# конкретного файла, можно делать .parent.parent.parent...
print(path.resolve().name) # выводит полное имя файла
print(path.resolve().stem) # выводит только название файла без расширения и без точки
print(path.resolve().suffix) # выводит расширение файла с точкой 
# это само собой применимо и без resolve
```
### Проверка типа

```python
from pathlib import Path

path = Path("plibOverview.py")
print(path.is_dir())
print(path.is_file())
# можем проверять, чем является конечный элемент конкретного пути
``` 
### Создание файлов и директорий
```python
from pathlib import Path
from os import chdir
new_file = Path.cwd() / "new_file.txt" 
new_file.touch()
# то есть мы определяем путь, а потом при помощи .touch() создаем файл
new_file.write_text("Hello")
# можем записывать строки  в файл
new_file.unlink()
# удаляем файл

new_dir = Path.cwd() / "new_dir" # задаем путь будущей  директории
new_dir.mkdir() # создаем директорию
chdir(new_dir) # модуль os (переходим в новую директорию)
print(Path.cwd())
new_dir.rmdir() # удаляем

# всё логически просто, напоминает zsh из терминала
``` 
