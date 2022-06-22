import os

dir_name = os.getcwd()
file_extension = r".txt"
files = [file for file in os.listdir(dir_name) if file.endswith(file_extension)]

processed_file = 'processed_file.txt'


def write_line(line, processed_file):
    try:
        with open(processed_file, 'a') as f:
            f.write(line)
    except FileNotFoundError:
        return 'Файл не найден'


def read_line_file(files):
    dict_numbers_file = {}
    for file in files:
        try:
            with open(file, 'r') as f:
                dict_numbers_file[file] = sum(1 for _ in f)
        except FileNotFoundError:
            return 'Файл не найден'
    return dict_numbers_file


def read_text_file(path):
    try:
        with open(str(path), 'r', encoding='utf_8') as f:
            list_text_file = []
            for line in f:
                line = line.rstrip('\n')
                list_text_file.append(line)
            return list_text_file
    except FileNotFoundError:
        return 'Файл не найден'


def write_processed_file(dict_files, dir_name):
    sorted_keys = sorted(files, key=dict_files.get)
    for file in sorted_keys:
        print(file)
        write_line(f'{file}\n', processed_file)
        num_line = dict_files[file]
        write_line(f'{num_line}\n', processed_file)
        path = os.path.join(dir_name, file)
        text_list = read_text_file(path)
        num = 0
        for line in text_list:
            num += 1
            new_line = f"Строка номер {num} файла номер {file.rstrip('.txt')}\n"
            write_line(new_line, processed_file)


print(read_line_file(files))

write_processed_file(read_line_file(files), dir_name)
