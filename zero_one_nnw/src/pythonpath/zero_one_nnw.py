"""数字の1か0かを判定するNNW。"""

import numpy as np
from typing import List


class ZeroOneNNW:
    """数字の1か0かを判定するNNW。"""

    # 入力層のユニット数
    unit_num_layer_1 = 12
    # 中間層のユニット数
    unit_num_layer_2 = 3
    # 出力層のユニット数
    unit_num_layer_3 = 2

    def __init__(self):
        """コンストラクタ。"""
        # 入力層の入力ユニット
        self.layer_1_in = np.zeros(self.unit_num_layer_1)
        # 入力層の出力ユニット
        self.layer_1_out = np.zeros(self.unit_num_layer_1)
        # 中間層の入力ユニット
        self.layer_2_in = np.zeros(self.unit_num_layer_2)
        # 中間層の出力ユニット
        self.layer_2_out = np.zeros(self.unit_num_layer_2)
        # 出力層の入力ユニット
        self.layer_3_in = np.zeros(self.unit_num_layer_3)
        # 出力層の出力ユニット
        self.layer_3_out = np.zeros(self.unit_num_layer_3)

        # 中間層への重み行列
        self.w_1 = np.random.randn(3, 12)
        # 出力層への重み行列2
        self.w_2 = np.random.randn(2, 3)
        # 中間層へのバイアス
        self.b_1 = np.zeros(3)
        # 出力層へのバイアス
        self.b_2 = np.zeros(2)

    def fit(self,
            train_data: List[List[int]],
            train_label: List[List[int]],
            epoc: int = 50,
            eta: float = 0.01) -> None:
        """モデルの学習を行う。

        重みとバイアスを更新する。

        Args:
            train_data (List[List[int]]): 学習用データ
            train_label (List[List[int]]): 学習用ラベル
            epoc (int): 学習の繰り返し数
            eta (float): 学習係数
        """
        data_num = len(train_data)
        # 中間層への重み行列の勾配
        w_1_gradient = np.zeros(3, 12)
        # 出力層への重み行列2の勾配
        w_2_gradient = np.zeros(2, 3)
        # 中間層へのバイアスの勾配
        b_1_gradient = np.zeros(3)
        # 出力層へのバイアスの勾配
        b_2_gradient = np.zeros(2)
        # 各データのコスト
        cost = np.zeros(data_num)

        for e in range(epoc):
            for t_data, t_label in zip(train_data, train_label):
                self.__forward(t_data, t_label, cost)
                self.__backpropagation(
                    w_1_gradient, w_2_gradient, b_1_gradient, b_2_gradient)
            self.__update_parameter(
                eta, w_1_gradient, w_2_gradient, b_1_gradient, b_2_gradient)
            print(f'epoc: {e} cost: {self.__get_cost(cost)}')

    def __forward(self, t_data: List[int], t_label: List[int],
                  cost: np.ndarray) -> None:
        """Forwardの計算を行う。

        データ毎のコストを算出する。
        各レイヤーの値を設定する。

        Args:
            t_data (List[int]): 学習データ1件
            t_label (List[int]): 学習ラベル1件
            cost (np.ndarray):
        """
        # 各レイヤーの値を計算
        # 入力データのコスト計算
        pass

    def __backpropagation(self, w_1_gradient: np.ndarry, w_2_gradient: np.ndarry,
                          b_1_gradient: np.ndarry, b_2_gradient: np.ndarry) -> None:
        """重みとバイアスの微分を求める。

        Args:
            w_1_gradient (np.ndarry): 中間層への重みの勾配
            w_2_gradient (np.ndarry): 中間層へのバイアスの勾配
            b_1_gradient (np.ndarry): 出力層への重みの勾配
            b_2_gradient (np.ndarry): 出力層へのバイアスの勾配
        """
        # 出力層の出力ユニットの誤差
        error_3_out = np.zeros(2)
        # 出力層の入力ユニットの誤差
        error_3_in = np.zeros(2)
        # 中間層の出力ユニットの誤差
        error_2_out = np.zeros(3)
        # 中間層の入力ユニットの誤差
        error_2_in = np.zeros(3)

        # 重み行列1の微分
        error_w_1 = np.zeros((3, 12))
        # 中間層のバイアスの微分
        error_b_1 = np.zeros((2))
        # 重み行列2の微分
        error_w_2 = np.zeros((2, 3))
        # 出力層のバイアスの微分
        error_b_2 = np.zeros((2))

        # 誤差と微分を計算
        # w_1_gradient, w_2_gradient, b を算出。アイテムごとの重みとバイアスの微分を足し合わせる
        pass

    def __update_parameter(self, eta: float, w_1_gradient: np.ndarry,
                           w_2_gradient: np.ndarry,
                           b_1_gradient: np.ndarry, b_2_gradient: np.ndarry) -> None:
        """重みとバイアスを更新する。

        Args:
            eta (float): 学習係数
            w_1_gradient (np.ndarry): 中間層への重みの勾配
            w_2_gradient (np.ndarry): 中間層へのバイアスの勾配
            b_1_gradient (np.ndarry): 出力層への重みの勾配
            b_2_gradient (np.ndarry): 出力層へのバイアスの勾配
        """
        # self.w, self.bに、w_1_gradientとイータをかけ合わせた値をかけたものを足し合わせる。
        pass

    def __get_total_cost(self, cost: np.ndarray) -> float:
        """トータルコストを取得する。

        Args:
            cost (np.ndarray): データごとのコストを格納する配列

        Returns:
            float: トータルコスト
        """
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
