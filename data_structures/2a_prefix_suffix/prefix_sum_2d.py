import numpy as np


class PrefixSum:
    def __init__(self, initial: list):
        self.initial = np.array(initial)
        self.num_rows = self.initial.shape[0] + 1
        self.num_cols = self.initial.shape[1] + 1
        self._pref = np.zeros((self.num_rows, self.num_cols))

        self._init_prefix_sum()

    def _init_prefix_sum(self):
        for i in range(1, self.num_rows):
            for j in range(1, self.num_cols):
                self._pref[i][j] = (
                    self.initial[i - 1][j - 1]
                    + self._pref[i - 1][j]
                    + self._pref[i][j - 1]
                    - self._pref[i - 1][j - 1]
                )

    def get_prefix_sum_list(self) -> np.array:
        return self._pref

    def get_range_sum_inclusively(self, x1, y1, x2, y2):
        return (
            self._pref[x2][y2]
            - self._pref[x1 - 1][y2]
            - self._pref[x2][y1 - 1]
            + self._pref[x1 - 1][y1 - 1]
        )


def main():
    p = PrefixSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(p.get_prefix_sum_list())
    assert p.get_range_sum_inclusively(2, 2, 3, 3) == 28
    assert p.get_range_sum_inclusively(1, 1, 2, 3) == 21


if __name__ == "__main__":
    main()
