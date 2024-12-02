import tarfile

class FileSystem:
    def __init__(self, tar_path):
        self.tar_path = tar_path
        self.tar = tarfile.open(tar_path, 'r')

    def list_directory(self, path):
        return [name for name in self.tar.getnames() if name.startswith(path)]

    def read_file(self, path):
        if path not in self.tar.getnames():
            raise FileNotFoundError(f"File not found: {path}")
        return self.tar.extractfile(path).read().decode('utf-8')

    def change_owner(self, path, owner):
        # Эмуляция chown, просто выводим сообщение
        print(f"Changed owner of {path} to {owner}")

    def get_uptime(self):
        # Эмуляция uptime, просто возвращаем фиктивное значение
        return "10:00 up 2 days, 4:30, 2 users, load average: 0.01, 0.05, 0.10"