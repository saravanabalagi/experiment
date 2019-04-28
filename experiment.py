import os
from find_utils import get_last_folder_number

class Experiment():
    def __init__(self, name='experiments', parent=None):

        if parent is not None and parent.path is not None:
            old_number = get_last_folder_number(parent.path)
            new_number = old_number + 1

            if len(name) > 0:
                exp_folder = '{:02d}_{}'.format(new_number, name)
            else:
                exp_folder = '{:02d}'.format(new_number)
            self.path = os.path.join(parent.path, exp_folder)
        else:
            self.path = os.path.join(name)

        os.makedirs(self.path, exist_ok=True)

        self.name = name
        self.parent = parent

    def new(self, name=''):
        return Experiment(name, self)

    def __str__(self):
        return self.path

    def __repr__(self):
        return 'Experiment({}, {})'.format(self.name, self.parent)
