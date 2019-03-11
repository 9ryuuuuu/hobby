"""数字の1か0かを判定するNNW。"""

import numpy as np
from typing import List


class ZeroOneNNW:
    """数字の1か0かを判定するNNW。"""

    def __init__(self, data_num: int):
        """コンストラクタ。

        Args:
            data_num (int): データ数
        """
        self.layer_1_in = np.zeros(12)  # 入力層のインプット
        self.layer_1_out = np.zeros(12)  # 入力層の出力ユニット
        self.layer_2_in = np.zeros(3)  # 中間層の入力ユニット
        self.layer_2_out = np.zeros(3)  # 中間層の出力ユニット
        self.layer_3_in = np.zeros(2)  # 出力層の入力ユニット
        self.layer_3_out = np.zeros(2)  # 出力層の出力ユニット
        self.w_1 = np.random.randn(3, 12)  # 重み行列1
        self.w_2 = np.random.randn(2, 3)  # 重み行列2
        self.b_1 = np.zeros(3)  # 中間層のバイアス
        self.b_2 = np.zeros(2)  # 出力層のバイアス
        self.error_3_out = np.zeros(2)  # 出力層の出力ユニットの誤差
        self.error_3_in = np.zeros(2)  # 出力層の入力ユニットの誤差
        self.error_w_2 = np.zeros((data_num, 2, 3))  # 重み行列2の微分
        self.error_b_2 = np.zeros((data_num, 2))  # 出力層のバイアスの微分
        self.error_2_out = np.zeros(3)  # 中間層の出力ユニットの誤差
        self.error_2_in = np.zeros(3)  # 中間層の入力ユニットの誤差
        self.error_2_i = np.zeros((data_num, 3, 12))  # 重み行列1の微分
        self.error_b_1 = np.zeros((data_num, 2))  # 中間層のバイアスの微分

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
