/*
 * @lc app=leetcode.cn id=362 lang=typescript
 *
 * [362] 敲击计数器
 *
 * https://leetcode.cn/problems/design-hit-counter/description/
 *
 * algorithms
 * Medium (68.87%)
 * Likes:    87
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 8.3K
 * Testcase Example:  '["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n' +
  '[[],[1],[2],[3],[4],[300],[300],[301]]'
 *
 * 设计一个敲击计数器，使它可以统计在过去 5 分钟内被敲击次数。（即过去 300 秒）
 *
 * 您的系统应该接受一个时间戳参数 timestamp (单位为 秒 )，并且您可以假定对系统的调用是按时间顺序进行的(即 timestamp
 * 是单调递增的)。几次撞击可能同时发生。
 *
 * 实现 HitCounter 类:
 *
 *
 * HitCounter() 初始化命中计数器系统。
 * void hit(int timestamp) 记录在 timestamp ( 单位为秒 )发生的一次命中。在同一个 timestamp
 * 中可能会出现几个点击。
 * int getHits(int timestamp) 返回 timestamp 在过去 5 分钟内(即过去 300 秒)的命中次数。
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入：
 * ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
 * [[], [1], [2], [3], [4], [300], [300], [301]]
 * 输出：
 * [null, null, null, null, 3, null, 4, 3]
 *
 * 解释：
 * HitCounter counter = new HitCounter();
 * counter.hit(1);// 在时刻 1 敲击一次。
 * counter.hit(2);// 在时刻 2 敲击一次。
 * counter.hit(3);// 在时刻 3 敲击一次。
 * counter.getHits(4);// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
 * counter.hit(300);// 在时刻 300 敲击一次。
 * counter.getHits(300); // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
 * counter.getHits(301); // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= timestamp <= 2 * 10^9
 * 所有对系统的调用都是按时间顺序进行的（即 timestamp 是单调递增的）
 * hit and getHits 最多被调用 300 次
 *
 *
 *
 *
 * 进阶: 如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？
 *
 */

export
// @lc code=start
class HitCounter {
  private readonly hits: number[] = []

  constructor(
    private readonly duration = 5 * 60,
  ) {
  }

  hit(timestamp: number): void {
    this.hits.push(timestamp)
  }

  getHits(timestamp: number): number {
    const left = this.binarySearch(
      timestamp - this.duration + 1,
      BinarySearchMode.FirstGreaterOrEqual,
    )
    const right = this.binarySearch(
      timestamp,
      BinarySearchMode.LastLessOrEqual,
    )
    return Math.max(right - left + 1, 0)
  }

  binarySearch(target: number, mode: BinarySearchMode) {
    let left = 0, right = this.hits.length - 1
    while (left + 1 < right) {
      const middle = (left + right) >> 1
      const mid = this.hits[middle]

      if (mid > target) {
        right = middle
      } else if (mid < target) {
        left = middle
      } else if (mode === BinarySearchMode.FirstGreaterOrEqual) {
        right = middle
      } else {
        left = middle
      }
    }

    if (mode === BinarySearchMode.FirstGreaterOrEqual) {
      if (this.hits[left] >= target) {
        return left
      }
      if (this.hits[right] >= target) {
        return right
      }
      return this.hits.length
    } else {
      if (this.hits[right] <= target) {
        return right
      }
      if (this.hits[left] <= target) {
        return right
      }
      return -1
    }
  }
}

const enum BinarySearchMode {
  FirstGreaterOrEqual,
  LastLessOrEqual,
}
// @lc code=end

// ['HitCounter', 'hit', 'hit', 'hit', 'getHits', 'getHits', 'getHits', 'getHits', 'getHits', 'hit', 'getHits']
// [[],           [2],   [3],   [4],    [300],     [301],     [302],     [303],     [304],    [501],  [600]]
