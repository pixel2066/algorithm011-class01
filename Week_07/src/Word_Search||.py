class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {} # 构造字典树
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True       
        
        # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
        def search(i, j, node, pre, visited):
            if '#' in node:  # 已有字典树结束
                res.add(pre) # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i+di, j+dj
                # 可继续搜索
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:
                    # dfs搜索
                    search(_i, _j, node[board[_i][_j]], pre+board[_i][_j], visited | {(_i, _j)})
        
        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                # 可继续搜索
                if board[i][j] in trie:
                    # dfs搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        
        return list(res)