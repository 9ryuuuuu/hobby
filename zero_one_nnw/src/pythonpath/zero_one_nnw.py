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

        # 各層のユニット(共有する必要はないが、共通のサイズの配列)
        self.layer_1_in = np.zeros(12)  # 入力層の入力ユニット
        self.layer_1_out = np.zeros(12)  # 入力層の出力ユニット
        self.layer_2_in = np.zeros(3)  # 中間層の入力ユニット
        self.layer_2_out = np.zeros(3)  # 中間層の出力ユニット
        self.layer_3_in = np.zeros(2)  # 出力層の入力ユニット
        self.layer_3_out = np.zeros(2)  # 出力層の出力ユニット

        # 重みとバイアス
        self.w_1 = np.random.randn(3, 12)  # 重み行列1
        self.w_2 = np.random.randn(2, 3)  # 重み行列2
        self.b_1 = np.zeros(3)  # 中間層のバイアス
        self.b_2 = np.zeros(2)  # 出力層のバイアス

    def fit(self, train_data: List[List[int]], train_label: List[List[int]],
            epoc: int = 50) -> None:
        """モデルの学習を行う。

        Args:
            train_data (List[List[int]]): 学習用データ
            train_label (List[List[int]]): 学習用ラベル
            epoc (int): 学習の繰り返し数
        """
        data_num = len(train_data)
        error_w_1 = np.zeros((data_num, 3, 12))  # 重み行列1の微分
        error_b_1 = np.zeros((data_num, 2))  # 中間層のバイアスの微分
        error_w_2 = np.zeros((data_num, 2, 3))  # 重み行列2の微分
        error_b_2 = np.zeros((data_num, 2))  # 出力層のバイアスの微分
        cost = np.zeros(data_num)  # 各データのコスト

        for e in range(epoc):
            for t_data, t_label in zip(train_data, train_label):
                self.__forward(t_data, t_label, cost)
                self.__backpropagation()

            self.__update_parameter()
            print(f'epoc: {e} cost: {self.__get_cost()}')

    def __forward(t_data: List[int], t_label: [int], cost: np.ndarray)->None:
        # 各層のユニットの値を計算
        # 入力データのコスト計算
        pass

    # TODO: ここまで
    def __backpropagation(error_w_1, error_b_1, error_w_2, error_b_2)->None:
        # 誤差と微分を計算
        error_3_out = np.zeros(2)  # 出力層の出力ユニットの誤差
        error_3_in = np.zeros(2)  # 出力層の入力ユニットの誤差
        error_2_out = np.zeros(3)  # 中間層の出力ユニットの誤差
        error_2_in = np.zeros(3)  # 中間層の入力ユニットの誤差

    def __update_parameter()->None:
        # 重みとバイアス更新(各データごとの値を足し合わせる)
        pass

    def __get_cost()->None:
        # コスト取得(各データごとのコストを足し合わせる)
        pass

    def predict(self, test_data: List[List[int]]) -> List[str]:
        """学習したモデルを用いて予測を行う。

        Args:
            test_data (List[List[int]]): テストデータの配列

        Returns:
            List[str]: 予測結果の配列
        """
        pass
