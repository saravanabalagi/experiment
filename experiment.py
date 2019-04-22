import os
import re

class Experiment():
    def __init__(self, name):
        self.name = name
        if not os.path.exists(directory):
            os.makedirs(exp_folder)
        self.path = os.path.join(exp_folder)

    def new():
        pass

def get_last_folder_number(path=None, prefix=''):

    if path is None:
        path = os.getcwd()

    folders = next(os.walk(path))[1]
    r = re.compile(prefix + '[0-9]+')
    matches = list(map(r.match, folders))
    matches = list(filter(lambda x: x is not None, matches))

    # print(matches)
    # print(list(filter(r.match, folders)))

    numbers_list = [ int(e[0][len(prefix):]) for e in matches ]
    return max(numbers_list)

def main():
    print(get_last_folder())

if __name__ == '__main__':
    main()
