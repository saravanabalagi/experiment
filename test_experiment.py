from experiment import get_last_folder_number, get_last_file_number
import os

def test_get_last_folder_number():
    folders = ['01_train_23', '12_train', '23_34', 'train_45', 'train_56_67']
    [ os.makedirs(folder, exist_ok=True) for folder in folders ]

    assert get_last_folder_number() is 23
    assert get_last_folder_number(prefix='train_') is 56

    [ os.rmdir(folder) for folder in folders ]

def test_get_last_file_number():
    folders = ['01_train_23', '12_train', '23_34', 'train_45', 'train_56_67']
    [ os.makedirs(folder, exist_ok=True) for folder in folders ]

    extension = '.somefile'
    files = [ f + extension for f in folders ]
    [ open(file, 'a') for file in files ]

    assert get_last_file_number(extension=extension) is 23
    assert get_last_file_number(prefix='train_', extension=extension) is 56

    assert get_last_file_number(extension='.someotherfile') is -1
    assert get_last_file_number(extension='.some') is -1

    [ os.remove(file) for file in files ]
    [ os.rmdir(folder) for folder in folders ]
