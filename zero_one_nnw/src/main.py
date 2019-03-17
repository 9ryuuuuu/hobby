"""メイン処理。"""
from typing import List

from zero_one_nnw import ZeroOneNNW


def main():
    """メイン処理。"""
    train_data_path = './input_data/train_data.tsv'
    train_label_path = './input_data/train_label.tsv'
    test_data_path = './input_data/test_data.tsv'
    result_path = './result/result.tsv'
    train_data, train_label = read_train_data(train_data_path,
                                              train_label_path)

    model = ZeroOneNNW()

    model.fit(train_data, train_label)

    test_data = read_test_data(test_data_path)

    result = model.predict(test_data)

    file_output(result, result_path)


def read_train_data(train_data_path: str,
                    train_label_path: str) -> (List[List[int]], List[int]):
    """学習データを読み込む。

    Returns:
        List[List[int]]: 学習データを格納するリスト
        List[List[int]]: 学習データのラベルを格納するリスト
    """
    train_data = []
    with open(train_data_path, mode='r', encoding='utf8') as f:
        for line in f:
            train_data.append([int(i) for i in line.split()])

    train_label = []
    with open(train_label_path, mode='r', encoding='utf8') as f:
        for line in f:
            line = int(line)
            if line == 1:
                train_label.append([0, 1])
            elif line == 0:
                train_label.append([1, 0])

    return train_data, train_label


def read_test_data(test_data_path: str) -> List[List[int]]:
    """テストデータを読み込む。

    Returns:
        List[List[int]]: テストデータを格納するリスト
    """
    test_data = []
    with open(test_data_path, mode='r', encoding='utf8') as f:
        for line in f:
            test_data.append([int(i) for i in line.split()])

    return test_data


def file_output(result: List[str], result_path: str) -> None:
    """リストの要素をファイル出力する。

    Args:
        result (List[str]): ファイル出力する内容
        result_path (str): 出力先パス
    """
    with open(result_path, mode='w', encoding='utf8') as f:
        for line in result:
            f.write('\t'.join(map(str, line)) + '\n')


if __name__ == '__main__':
    main()
