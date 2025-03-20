from typing import List, Dict, Tuple


class Solution:
    def search(self, board, target, i, j, memo: Dict[Tuple[int, int, str], bool]) -> bool:
        if not target:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != target[0]:
            return False

        key = (i, j, target)
        if key in memo:
            return memo[key]

        temp = board[i][j]
        board[i][j] = "*"

        found = (
                self.search(board, target[1:], i - 1, j, memo) or
                self.search(board, target[1:], i + 1, j, memo) or
                self.search(board, target[1:], i, j - 1, memo) or
                self.search(board, target[1:], i, j + 1, memo)
        )

        board[i][j] = temp
        memo[key] = found
        return found

    def exist(self, board: List[List[str]], word: str) -> List[str]:
        result = []
        memo = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j, memo):
                    return True

        return False


board = [["a", "b"], ["a", "a"]]
words = 'aba'
print(Solution().exist(board, words))
