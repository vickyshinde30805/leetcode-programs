class Node:
    __slots__ = ("length", "pref", "suff", "best", "lc", "rc")

    def __init__(self, ch=None):
        if ch is None:
            self.length = 0
            self.pref = self.suff = self.best = 0
            self.lc = self.rc = ""
        else:
            self.length = 1
            self.pref = self.suff = self.best = 1
            self.lc = self.rc = ch


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        seg = [Node() for _ in range(4 * n)]

        def merge(L: Node, R: Node) -> Node:
            res = Node()
            res.length = L.length + R.length
            res.lc = L.lc
            res.rc = R.rc

            # Prefix
            res.pref = L.pref
            if L.pref == L.length and L.rc == R.lc:
                res.pref = L.length + R.pref

            # Suffix
            res.suff = R.suff
            if R.suff == R.length and L.rc == R.lc:
                res.suff = R.length + L.suff

            # Best
            res.best = max(L.best, R.best)
            if L.rc == R.lc:
                res.best = max(res.best, L.suff + R.pref)

            return res

        def build(idx, l, r):
            if l == r:
                seg[idx] = Node(s[l])
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])

        def update(idx, l, r, pos, ch):
            if l == r:
                seg[idx] = Node(ch)
                return

            mid = (l + r) // 2
            if pos <= mid:
                update(idx * 2, l, mid, pos, ch)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, ch)

            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])

        build(1, 0, n - 1)

        s = list(s)
        ans = []

        for ch, pos in zip(queryCharacters, queryIndices):
            s[pos] = ch
            update(1, 0, n - 1, pos, ch)
            ans.append(seg[1].best)

        return ans