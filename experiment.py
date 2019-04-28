import os
from find_utils import get_last_folder_number

class Experiment():
    def __init__(self, name='experiments', parent=None):

        if parent is not None and parent.path is not None:
            self.path = os.path.join(parent.path, name)
        else: self.path = os.path.join(name)

        self.name = name
        self.parent = parent
        os.makedirs(self.path, exist_ok=True)

    def new(self, name=''):
        old_number = get_last_folder_number(self.path)
        new_number = old_number + 1

        if len(name) > 0:
            exp_folder = '{:02d}_{}'.format(new_number, name)
        else: exp_folder = '{:02d}'.format(new_number)
        os.makedirs(os.path.join(self.path, exp_folder), exist_ok=True)
        return exp_folder

    def subExperiment(self, name):
        return Experiment(name, self)

def main():
    my_exp = Experiment('experiments')
    print(my_exp.new('nasnet'))
    print(my_exp.new('vgg'))
    print(my_exp.new('inceptionv3'))
    adam = my_exp.subExperiment('adam')
    print(adam.new('001'))
    print(adam.new('0001'))

if __name__ == '__main__':
    main()
