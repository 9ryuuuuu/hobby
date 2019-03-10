"""数字の1か0かを判定するNNW。"""

import numpy as np
from typing import List


class ZeroOneNNW:
    """数字の1か0かを判定するNNW。"""

    def __init__(self):
        pass

    def fit(self, train_data: List[List[int]], train_label: List[int]):
        """モデルの学習を行う。

        Args:
            train_data (List[List[int]]): 学習用データ
            train_label (List[int]): 学習用ラベル
        """
        pass

    def predict(self, test_data: List[List[int]]) -> List[str]:
        """学習したモデルを用いて予測を行う。

        Args:
            test_data (List[List[int]]): テストデータの配列

        Returns:
            List[str]: 予測結果の配列
        """
        pass
