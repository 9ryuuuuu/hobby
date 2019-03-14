"""メイン処理。"""
from typing import List

from zero_one_nnw import ZeroOneNNW


def main():
    """メイン処理。"""
    print('hello')
    train_data_path = './input_data/train_data.tsv'
    train_label_path = './input_data/train_label.tsv'
    test_data_path = './input_data/test_data.tsv'
    result_path = './result.tsv'
    train_data, train_label = read_train_data(train_data_path,
                                              train_label_path)
    print('hello')


def __main():
    """メイン処理。"""
    train_data_path = './input_data/train_data.tsv'
    train_label_path = './input_data/train_label.tsv'
    test_data_path = './input_data/test_data.tsv'
    result_path = './result.tsv'
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
        List[int]: 学習データのラベルを格納するリスト
    """
    with open(train_data_path, mode='r', encoding='utf8') as f:
        for line in f:
            print(line)


def read_test_data(test_data_path: str) -> List[List[int]]:
    """テストデータを読み込む。

    Returns:
        List[List[int]]: テストデータを格納するリスト
    """
    pass


def file_output(result: List[str], result_path: str) -> None:
    """リストの要素をファイル出力する。

    Args:
        result (List[str]): ファイル出力する内容
        result_path (str): 出力先パス
    """
    pass


if __name__ == '__main__':
    main()
