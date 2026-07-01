class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        isSquare=True
        n=len(words)
        for i in range(n):
            for j in range(len(words[i])):
                if j>=n:
                    return False
                if i>=len(words[j]):
                    return False
                if words[i][j]!=words[j][i]:
                    return False
        return True