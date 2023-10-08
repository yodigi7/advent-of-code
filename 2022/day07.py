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

    matched_directories = []
    directories_to_check = [root_dir]
    while directories_to_check:
        current_dir = directories_to_check.pop(0)
        sum_amt = current_dir.sum()
        if sum_amt < 100000:
            matched_directories.append(current_dir)
            matched_directories.extend(current_dir.get_all_dir_names())
        else:
            directories_to_check.extend(list(current_dir.directories.values()))
    print(sum(directory.sum() for directory in matched_directories))
