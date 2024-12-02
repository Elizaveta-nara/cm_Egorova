import os
from filesystem import FileSystem
from commands import CommandHandler

class Shell:
    def __init__(self, hostname, tar_path, start_script):
        self.hostname = hostname
        self.fs = FileSystem(tar_path)
        self.command_handler = CommandHandler(self.fs)
        self.start_script = start_script
        self.current_dir = "/"

    def run(self):
        self.run_start_script()
        while True:
            command = input(f"{self.hostname}:{self.current_dir}$ ")
            if command.strip() == "":
                continue
            self.execute_command(command)

    def run_start_script(self):
        if not os.path.exists(self.start_script):
            print(f"Start script '{self.start_script}' not found.")
            return

        with open(self.start_script, 'r') as file:
            for line in file:
                self.execute_command(line.strip())

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "exit":
            self.command_handler.exit()
        elif cmd == "ls":
            result = self.command_handler.ls(args)
            print(result)
        elif cmd == "cd":
            result = self.command_handler.cd(args)
            if result == '':
                self.current_dir = self.command_handler._cur_path
            else:
                print(result)
        elif cmd == "chown":
            result = self.command_handler.chown(args)
            print(result)
        elif cmd == "uptime":
            result = self.command_handler.uptime()
            print(result)
        elif cmd == "tac":
            result = self.command_handler.tac(args)
            print(result)
        elif cmd == "owner":
            result = self.command_handler.get_owner(args)
            print(result)
        else:
            print(f"Command not found: {cmd}")