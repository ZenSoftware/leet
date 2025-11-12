class Solution(object):
    def findRelativeRanks(self, score):
        score_indexes = [(score[i], i) for i in range(len(score))]
        score_indexes.sort(reverse=True)

        ranks = [None] * len(score)
        for i in range(len(score_indexes)):
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i + 1)

            ranks[score_indexes[i][1]] = rank

        return ranks
