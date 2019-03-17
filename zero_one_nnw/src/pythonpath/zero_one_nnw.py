"""数字の1か0かを判定するNNW。"""

import numpy as np
from typing import List, Tuple


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
        self.w_1 = np.random.randn(self.unit_num_layer_2,
                                   self.unit_num_layer_1)
        # 中間層へのバイアス
        self.b_1 = np.zeros(self.unit_num_layer_2)
        # 出力層への重み行列
        self.w_2 = np.random.randn(self.unit_num_layer_3,
                                   self.unit_num_layer_2)
        # 出力層へのバイアス
        self.b_2 = np.zeros(self.unit_num_layer_3)

    def fit(self,
            train_data: List[List[int]],
            train_label: List[List[int]],
            epoc: int = 50,
            eta: float = 0.1) -> None:
        """モデルの学習を行う。

        重みとバイアスを更新する。

        Args:
            train_data (List[List[int]]): 学習用データ
            train_label (List[List[int]]): 学習用ラベル
            epoc (int): 学習の繰り返し数
            eta (float): 学習係数
        """

        # 中間層への重み行列の勾配
        w_1_gradient = np.zeros((self.unit_num_layer_2, self.unit_num_layer_1))
        # 中間層へのバイアスの勾配
        b_1_gradient = np.zeros(self.unit_num_layer_2)
        # 出力層への重み行列の勾配
        w_2_gradient = np.zeros((self.unit_num_layer_3, self.unit_num_layer_2))
        # 出力層へのバイアスの勾配
        b_2_gradient = np.zeros(self.unit_num_layer_3)
        # 各データのコスト
        cost = np.zeros(len(train_data))

        for e in range(epoc):
            for i, (t_data, t_label) in enumerate(zip(train_data, train_label)):
                self.__forward(t_data, i)
                cost[i] = ((self.layer_3_out - t_label)**2).sum()
                self.__backpropagation(t_label, w_1_gradient, w_2_gradient,
                                       b_1_gradient, b_2_gradient)
            self.__update_parameter(eta, w_1_gradient, w_2_gradient,
                                    b_1_gradient, b_2_gradient)
            print(f'epoc: {e} cost: {cost.sum()}')

    def __forward(self, t_data: List[int], data_num: int) -> None:
        """Forwardの計算を行う。

        データ毎のコストを算出する。
        各レイヤーの値を設定する。

        Args:
            t_data (List[int]): 学習データ1件
            data_num (int): データ番号
        """
        self.__initialize_layer()

        # 各レイヤーの値を計算
        self.layer_1_in = np.array(t_data)
        self.layer_1_out = self.layer_1_in
        self.layer_2_in = np.dot(self.w_1, self.layer_1_out) + self.b_1
        self.layer_2_out = self.__sigmoid(self.layer_2_in)
        self.layer_3_in = np.dot(self.w_2, self.layer_2_out) + self.b_2
        self.layer_3_out = self.__sigmoid(self.layer_3_in)

    def __backpropagation(self, t_label: List[int], w_1_gradient: np.ndarray,
                          w_2_gradient: np.ndarray, b_1_gradient: np.ndarray,
                          b_2_gradient: np.ndarray) -> None:
        """重みとバイアスの微分を求める。

        Args:
            t_label (List[int]): 学習ラベル1件
            w_1_gradient (np.ndarray): 中間層への重みの勾配
            w_2_gradient (np.ndarray): 中間層へのバイアスの勾配
            b_1_gradient (np.ndarray): 出力層への重みの勾配
            b_2_gradient (np.ndarray): 出力層へのバイアスの勾配
        """
        # 各レイヤーの微分を計算

        # 出力層の出力ユニットの微分
        l_3_out_error = self.layer_3_out - t_label
        # 出力層の入力ユニットの微分
        l_3_in_error = l_3_out_error * \
            self.__derivative_sigmoid(self.layer_3_in)
        # 出力層への重み行列の微分
        w_2_error = np.array([self.layer_2_out * l_3_in_error[i]
                              for i in range(2)])
        # 出力層へのバイアスの微分
        b_2_error = l_3_in_error
        # 中間層の出力ユニットの微分
        l_2_out_error = np.dot(self.w_2.T, l_3_in_error)
        # 中間層の入力ユニットの微分
        l_2_in_error = l_2_out_error * \
            self.__derivative_sigmoid(self.layer_2_in)
        # 中間層への重み行列の微分
        w_1_error = np.array([self.layer_1_out * l_2_in_error[i]
                              for i in range(3)])
        # 中間層へのバイアスの微分
        b_1_error = l_2_in_error

        # 勾配の計算(アイテムごとの微分を足し合わせる)
        # print(w_1_gradient)
        # print(w_1_error)
        w_1_gradient += w_1_error
        b_1_gradient += b_1_error
        w_2_gradient += w_2_error
        b_2_gradient += b_2_error

    def __update_parameter(self, eta: float, w_1_gradient: np.ndarray,
                           w_2_gradient: np.ndarray, b_1_gradient: np.ndarray,
                           b_2_gradient: np.ndarray) -> None:
        """重みとバイアスを更新する。

        Args:
            eta (float): 学習係数
            w_1_gradient (np.ndarray): 中間層への重みの勾配
            w_2_gradient (np.ndarray): 中間層へのバイアスの勾配
            b_1_gradient (np.ndarray): 出力層への重みの勾配
            b_2_gradient (np.ndarray): 出力層へのバイアスの勾配
        """
        self.w_1 -= eta * w_1_gradient
        self.w_2 -= eta * w_2_gradient
        self.b_1 -= eta * b_1_gradient
        self.b_2 -= eta * b_2_gradient

    def predict(self,
                test_data: List[List[int]]) -> List[Tuple[int, float, float]]:
        """学習したモデルを用いて予測を行う。

        Args:
            test_data (List[List[int]]): テストデータの配列

        Returns:
            List[(int, float, float)]: テストデータの予測結果(ラベル、1の確信度、2の確信度)
        """
        ret_list = []
        for i, t_data in enumerate(test_data):
            self.__forward(t_data, i)
            label = 0 if self.layer_3_out[0] > self.layer_3_out[1] else 1
            ret_list.append([label, self.layer_3_out[0], self.layer_3_out[1]])
        return ret_list

    def __initialize_layer(self):
        """各レイヤーのユニットの値を初期化(ゼロクリア)する。"""
        self.layer_1_in *= 0
        self.layer_1_out *= 0
        self.layer_2_in *= 0
        self.layer_2_out *= 0
        self.layer_3_in *= 0
        self.layer_3_out *= 0

    def __sigmoid(self, x: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-x))

    def __derivative_sigmoid(self, x: np.ndarray) -> np.ndarray:
        return self.__sigmoid(x) * (1 - self.__sigmoid(x))
