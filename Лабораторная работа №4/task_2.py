# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file, json_file) -> None:

    ...  # TODO считать содержимое csv файла
    with open(csv_file, 'r') as csv_file:
        readcsv = csv.DictReader(csv_file)
        data = []
        for i in readcsv:
            data.append(i)

    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)



    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
