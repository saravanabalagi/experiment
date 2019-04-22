import os
import re

class Experiment():
    def __init__(self, parent='experiments'):
        os.makedirs(parent, exist_ok=True)
        self.path = os.path.join(parent)
        self.parent = parent

    def new(self, name=''):
        old_number = get_last_folder_number(self.path)
        new_number = old_number + 1

        if len(name) > 0:
            exp_folder = '{:02d}_{}'.format(new_number, name)
        else: exp_folder = '{:02d}'.format(new_number)
        os.makedirs(os.path.join(self.parent, exp_folder))
        return exp_folder

# All directories are files, but not all files are directories
def get_last_file_number(path=None, prefix='', extension='', folder=False):

    if path is None:
        path = os.getcwd()

    index = 1 if folder else 2
    fs_objects = next(os.walk(path))[index]

    r = re.compile(prefix + '([0-9]+)' + '.*' + extension + '$')
    matches = list(map(r.match, fs_objects))
    matches = list(filter(lambda x: x is not None, matches))

    # # For debugging
    # print(matches)
    # print([match.group(1) for match in matches])
    # print(list(filter(r.match, fs_objects)))

    numbers_list = [ int(match.group(1)) for match in matches ]
    return max(numbers_list) if len(numbers_list) > 0 else -1

# For those files that are directories
def get_last_folder_number(path=None, prefix=''):
    return get_last_file_number(path=path, prefix=prefix, extension='', folder=True)

def main():
    my_exp = Experiment(parent='experiments')
    print(my_exp.new('nasnet'))
    print(my_exp.new('vgg'))
    print(my_exp.new('inceptionv3'))

if __name__ == '__main__':
    main()
