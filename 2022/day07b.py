class Directory:
    def __init__(self, name, parent = None, directories = None, files = None):
        self.name = name
        self.parent = parent
        if directories:
            self.directories = {directory.name: directory for directory in directories}
        else:
            self.directories = {}
        if files:
            self.files = {file.name: file for file in files}
        else:
            self.files = {}

    def sum(self):
        dir_sum = sum(directory.sum() for directory in self.directories.values()) if self.directories else 0
        file_sum = sum(file.size for file in self.files.values()) if self.files else 0
        return dir_sum + file_sum

    def get_file(self, name):
        return self.files[name]

    def get_directory(self, name):
        return self.directories[name]

    def add_directory(self, directory):
        self.directories[directory.name] = directory

    def add_file(self, file):
        self.files[file.name] = file

    def get_all_dir_names(self):
        sub_dirs = []
        for dir in self.directories.values():
            dirs_to_add = dir.get_all_dir_names()
            if dirs_to_add:
                sub_dirs.append(dirs_to_add)
        return_dirs = list(self.directories.values())
        return_dirs.extend(sub_dirs)
        return return_dirs

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


if __name__ == "__main__":
    previous_dir = None
    current_dir = Directory('/')
    root_dir = current_dir
    with open('day07.txt', 'r') as inputfile:
        # Know that first line will go to root so can ignore
        inputfile.readline()
        command = inputfile.readline().split()[1:]
        while True:
            try:
                if command[0] == 'cd':
                    dir_name = command[1]
                    if dir_name == '..':
                        previous_dir = current_dir
                        current_dir = current_dir.parent
                    else:
                        previous_dir = current_dir
                        current_dir = current_dir.get_directory(dir_name)

                    command = inputfile.readline().split()[1:]
                else:
                    # Read ls output
                    while True:
                        line = inputfile.readline().split()
                        if line[0] == '$':
                            command = line[1:]
                            break
                        elif line[0] == 'dir':
                            directory = Directory(line[1], parent = current_dir)
                            current_dir.add_directory(directory)
                        else:
                            size, name = line
                            current_dir.add_file(File(name, size))
            except IndexError:
                break

    directories_to_check = [root_dir]
    total_space = 70000000
    total_needed_space = 30000000
    total_used_space = root_dir.sum()
    space_to_delete = total_needed_space - (total_space - total_used_space)
    smallest_dir = root_dir
    smallest_dir_size = total_used_space
    while directories_to_check:
        current_dir = directories_to_check.pop(0)
        sum_amt = current_dir.sum()
        if sum_amt >= space_to_delete:
            if sum_amt < smallest_dir_size:
                smallest_dir = current_dir
                smallest_dir_size = sum_amt
            directories_to_check.extend(list(current_dir.directories.values()))
    print(smallest_dir_size)