import pytest
from main import read_train_data, read_test_data, file_output


class TestReadTrainData(object):

    def test_normal(self):
        train, label = read_train_data(
            './test/test_train.tsv', './test/test_label.tsv')
        assert train == [[1, 1, 0], [0, 1, 1]]
        assert label == [[0, 1], [1, 0]]


class TestReadTestData(object):

    def test_normal(self):
        test_data = read_test_data('./test/test_test.tsv')
        assert test_data == [[1, 1, 0], [0, 0, 1]]


class TestFileOutPut(object):

    def test_normal(self):
        data = [[1, 0.3, 0.5], [0, 0.8, 0.5]]
        file_output(data, './test/test_result.tsv')
