#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Hard (46.41%)
# Likes:    780
# Dislikes: 0
# Total Accepted:    111.2K
# Total Submissions: 239.5K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：
# 
# 
# 序列中第一个单词是 beginWord 。
# 序列中最后一个单词是 endWord 。
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典 wordList 中的单词。
# 
# 
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0。
# 
# 
# 示例 1：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 
# 
# 示例 2：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
# 
# 
# 
# 提示：
# 
# 
# 1 
# endWord.length == beginWord.length
# 1 
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, value: str, neighbors: set['Node'] = None) -> None:
        self.value = value
        self.neighbors = neighbors or set()
    
    # def __str__(self) -> str:
    #     return 'Node # ' + self.value

    # def __repr__(self) -> str:
    #     return self.__str__()

class Graph:
    @staticmethod
    def check_connection(a: str, b: str) -> bool:
        changed = False
        for i in range(len(a)):
            if a[i] != b[i] and changed:
                return False
            elif a[i] != b[i]:
                changed = True
        return True

    def get_node(self, value: str, auto_create = True) -> Node:
        if not value in self.node_map:
            if not auto_create: return None
            self.node_map[value] = Node(value)
        return self.node_map[value]

    def __init__(self, words: list[str]) -> None:
        self.node_map: dict[str, Node] = {}

        for i in range(len(words)):
            w1 = words[i]
            for j in range(i + 1, len(words)):
                w2 = words[j]
                if not Graph.check_connection(w1, w2): continue
                self.get_node(w1).neighbors.add(self.get_node(w2))
                self.get_node(w2).neighbors.add(self.get_node(w1))

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        graph = Graph([beginWord] + wordList)
        begin_node, end_node = graph.get_node(beginWord, False), graph.get_node(endWord, False)
        if not begin_node or not end_node: return 0

        queue = [begin_node]
        visited = set(queue)
        step_count = 0

        while queue:
            step_count += 1
            level_node_count = len(queue)
            # print(queue)

            for _ in range(level_node_count):
                curr_node = queue.pop(0)
                if curr_node == end_node: return step_count

                for n in curr_node.neighbors:
                    if not n in visited:
                        queue.append(n)
                        visited.add(n)

        return 0
# @lc code=end

