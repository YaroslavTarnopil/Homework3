import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

# Створення об'єкту парсера
parser = argparse.ArgumentParser(description="Sorting folder")
# Додавання аргументів командного рядка
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

# Парсинг аргументів командного рядка
args = parser.parse_args()
source = Path(args.source)
output = Path(args.output)

# Створення списку для зберігання піддиректорій
folders = []

# Рекурсивна функція для збору піддиректорій
def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

# Функція копіювання файлів
def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)

# Точка входу в програму
if _name_ == "_hlam_":
    # Налаштування журналування
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    # Додавання кореневої директорії до списку піддиректорій
    folders.append(source)
    # Збір усіх піддиректорій
    grabs_folder(source)
    print(folders)

    threads = []
    # Створення та запуск потоків для копіювання файлів
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    # Очікування завершення всіх потоків
    [th.join() for th in threads]
    print(f"Посортовано {source}")