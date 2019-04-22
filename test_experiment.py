from experiment import get_last_folder_number
import os

def test_get_last_folder_number():
    folders = ['01_train_23', '12_train', '23_34', 'train_45', 'train_56_67']
    [ os.mkdir(folder) for folder in folders ]

    assert get_last_folder_number() is 23
    assert get_last_folder_number(prefix='train_') is 56

    [ os.rmdir(folder) for folder in folders ]
