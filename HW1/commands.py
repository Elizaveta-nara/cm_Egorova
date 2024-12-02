import os
import time
import tarfile

class CommandHandler:
    def __init__(self, fs):
        self.fs = fs
        self._cur_path = "/"
        self._file_owners = {}
        self.start_time = time.time()

    def ls(self, args):
        if args:
            # абсолютный путь
            if args[0][0] == '/':
                path = args[0]
            else:
                # соединение пути с текущей директорией
                path = os.path.join(self._cur_path, args[0])
        else:
            # текущая директория
            path = self._cur_path

        file_set = set()
        for name in self.fs.tar.getnames():
            name = '/' + name
            if name.startswith(path):
                name = name[len(path):].strip('/').split('/')[0]
                if name:
                    file_set.add(name)
        result = sorted(file_set)
        if result:
            return '\n'.join(result) + '\n'
        return 'Директория не содержит файлы или не существует\n'

    def cd(self, args):
        if not args:
            return ''

        target_path = args[0]
        # Корневая директория
        if target_path == "/":
            self._cur_path = target_path
            return ''
        # Переход на родительскую директорию
        elif target_path == '..':
            if self._cur_path != '/':
                self._cur_path = os.path.dirname(self._cur_path)
            return ''`
        # Формирование полного пути
        if target_path[0] == '/':
            path = target_path
        else:
            if not self._cur_path.endswith('/'):
                self._cur_path += "/"
            path = os.path.join(self._cur_path, target_path)

        for name in self.fs.tar.getnames():
            name = '/' + name
            if (name.startswith(path + '/') and len(name) > len(path)):
                self._cur_path = path
                return ''

        return "Некорректный путь\n"

    def exit(self):
        try:
            self.fs.tar.close()
        except Exception as e:
            print(f"Ошибка при закрытии архива: {str(e)}")
        print("Выход из эмулятора...")
        sys.exit(0)

    def chown(self, args):
        if len(args) < 2:
            return "Использование: chown <новый_владелец> <файл>"

        new_owner = args[0]
        file_name = args[1]

        # Проверка существования файла в архиве
        if file_name in self.fs.tar.getnames():
            # Изменение владельца файла
            self._file_owners[file_name] = new_owner
            return f"Владелец файла '{file_name}' изменен на '{new_owner}'"
        else:
            return f"Файл '{file_name}' не найден"

    def uptime(self):
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)
        uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        return f"Время работы системы: {uptime_string}"

    def tac(self, args):
        if not args:
            return "Не указан файл"

        file_name = args[0]
        tar_path = self.fs.tar_path
        try:
            with tarfile.open(tar_path, 'r') as tar:
                # Проверяем, существует ли файл в архиве
                if file_name in tar.getnames():
                    # Извлекаем файл
                    with tar.extractfile(file_name) as f:
                        if f is not None:
                            content = f.read().decode('utf-8')  # Декодируем байты в строку
                            return content[::-1]  # Возвращаем строку задом наперед
                else:
                    return f"Файл '{file_name}' не найден в архиве."
        except Exception as e:
            return f"Ошибка при извлечении файла: {str(e)}"

    def get_owner(self, args):
        if len(args) < 1:
            return "Использование: owner <файл>"
        file_name = args[0]

        # Проверка существования файла в архиве
        if file_name in self.fs.tar.getnames():
            owner = self._file_owners.get(file_name, "Владелец не установлен")
            return f"Владелец файла '{file_name}': {owner}"
        else:
            return f"Файл '{file_name}' не найден"