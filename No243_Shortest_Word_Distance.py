#No.243_Shortest_Word_Distance
#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#Given word1 = "coding", word2 = "practice", return 3.
#Given word1 = "makes", word2 = "coding", return 1.

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1

        return dist


if __name__ == '__main__':
	words = words = ["practice", "makes", "perfect", "coding", "makes"]
	word1 = "coding"
	word2 = "practice"
    print Solution().shortestDistance(words,word1,word2)