#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#
# https://leetcode-cn.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (83.99%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 17.3K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl
# 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
# 
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode
# 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
# 
#

# @lc code=start
ORD_A, ORD_Z, ORD_0, ORD_9, ORD_a, ORD_z = ord('A'), ord('Z'), ord('0'), ord('9'), ord('a'), ord('z')

class StorageService:
    def __init__(self) -> None:
        self.next_index = 0
        self.storage: list[str] = []

    @staticmethod
    def n_to_char(n: int) -> str:
        if n <= 9:
            return str(n)
        if n >= 10 and n <= 35:
            return chr(n - 10 + ORD_a)
        if n >= 36 and n <= 61:
            return chr(n - 36 + ORD_A)

    @staticmethod
    def int_to_62_bit(n: int) -> str:
        ret = ''
        while n:
            ret += StorageService.n_to_char(n % 62)
            n //= 62
        return ret or '0'

    @staticmethod
    def n_from_char(c: str) -> int:
        curr_ord = ord(c)
        if curr_ord >= ORD_0 and curr_ord <= ORD_9:
            return curr_ord - ORD_0
        if curr_ord >= ORD_a and curr_ord <= ORD_z:
            return curr_ord - ORD_a + 10
        if curr_ord >= ORD_A and curr_ord <= ORD_Z:
            return curr_ord - ORD_A + 36

    @staticmethod
    def int_from_62_bit(encoded: str) -> int:
        ret = 0
        for i in range(len(encoded) - 1, -1, -1):
            ret *= 62
            ret += StorageService.n_from_char(encoded[i])
        return ret

    def insert(self, value: str) -> str:
        idx = StorageService.int_to_62_bit(self.next_index)
        self.storage.append(value)
        self.next_index += 1
        return idx

    def select(self, idx: str) -> str:
        index = StorageService.int_from_62_bit(idx)
        return self.storage[index]

class Codec:
    def __init__(self) -> None:
        self.service = StorageService()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        path = self.service.insert(longUrl)
        return 'https://a.com/' + path

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        path = shortUrl.split('/')[-1]
        return self.service.select(path)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

