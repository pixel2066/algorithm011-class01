class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.left = set()
        self.right = set()
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row - col in self.left or row + col in self.right:
                continue
            self.cols.add(col)
            self.left.add(row - col)
            self.right.add(row + col)
            self.DFS(n, row + 1, cur_state + [col])
            self.cols.remove(col)
            self.left.remove(row - col)
            self.right.remove(row + col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i : i + n] for i in range(0, len(board), n)]