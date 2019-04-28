from experiment import Experiment
import shutil
import os

def experiment_new_helper(name, number, parent):
    test_sub_experiment = parent.new(name)
    expected_path = os.path.join(parent.path, '{}_{}'.format(number, name))
    assert (test_sub_experiment.path == expected_path) is True
    assert os.path.isdir(expected_path) is True

    assert (test_sub_experiment.name == name) is True
    assert (test_sub_experiment.path == expected_path) is True
    assert (test_sub_experiment.parent == parent) is True

def test_experiment_new():

    EXPERIMENT_ROOT = 'experiments';
    shutil.rmtree(EXPERIMENT_ROOT, ignore_errors=True)

    test_experiment = Experiment(EXPERIMENT_ROOT)

    experiment_new_helper('nasnet', '00', test_experiment)
    experiment_new_helper('vgg_16', '01', test_experiment)
    experiment_new_helper('inception_v3', '02', test_experiment)

    test_sub_experiment = test_experiment.new('adam')

    experiment_new_helper('001', '00', test_sub_experiment)
    experiment_new_helper('0001', '01', test_sub_experiment)

    shutil.rmtree(EXPERIMENT_ROOT, ignore_errors=True)
