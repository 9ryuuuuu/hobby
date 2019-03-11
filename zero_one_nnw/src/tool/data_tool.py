import numpy as np
import matplotlib.pyplot as plt
from typing import List


class DataTool:

    @classmethod
    def hist(cls, x: List[int], bins: int = 50) -> None:
        """ヒストグラムを作成する。

        Args:
            x ([List<int>]): 対象データ
            bins ([List<int>]): x軸の刻み数
        """
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.hist(x, bins=bins)
        fig.show()

    @classmethod
    def normalData(cls, num: int) -> List[float]:
        """平均0、標準偏差1の正規分布に従う乱数を返す。

        Args:
            num ([int]): データ数

        Returns:
            List[float]: 乱数
        """
        return np.random.randn(num)
