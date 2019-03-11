"""メイン処理。"""
from typing import List

from zero_one_nnw import ZeroOneNNW


def main():
    """メイン処理。"""
    train_data, train_label = read_train_data()

    model = ZeroOneNNW()

    model.fit(train_data, train_label)

    test_data = read_test_data()

    result = model.predict(test_data)

    file_output(result)


def read_train_data() -> (List[List[int]], List[int]):
    """学習データを読み込む。

    Returns:
        List[List[int]]: 学習データを格納するリスト
        List[int]: 学習データのラベルを格納するリスト
    """
    pass


def read_test_data() -> List[List[int]]:
    """テストデータを読み込む。

    Returns:
        List[List[int]]: テストデータを格納するリスト
    """
    pass


def file_output(result: List[str]) -> None:
    """リストの要素をファイル出力する。

    Args:
        result (List[str]): ファイル出力する内容
    """
    pass


if __name__ == '__main__':
    main()
