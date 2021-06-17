/*
 * @lc app=leetcode.cn id=207 lang=javascript
 *
 * [207] 课程表
 *
 * https://leetcode-cn.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (54.63%)
 * Likes:    808
 * Dislikes: 0
 * Total Accepted:    111K
 * Total Submissions: 203.2K
 * Testcase Example:  '2\n[[1,0]]'
 *
 * 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
 * 
 * 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
 * ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
 * 
 * 
 * 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
 * 
 * 
 * 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：numCourses = 2, prerequisites = [[1,0]]
 * 输出：true
 * 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
 * 
 * 示例 2：
 * 
 * 
 * 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
 * 输出：false
 * 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 0 
 * prerequisites[i].length == 2
 * 0 i, bi < numCourses
 * prerequisites[i] 中的所有课程对 互不相同
 * 
 * 
 */

// @lc code=start
class ScheduleGraph {
  dependencyCountMap = {}
  postCoursesMap = {}

  passedCourses = new Set()
  queue = []

  constructor(numCourses, prerequisites) {
    this.courcesCount = numCourses

    for (const prerequisite of prerequisites) {
      const [postCourse, preCourse] = prerequisite

      if (!this.dependencyCountMap[postCourse]) {
        this.dependencyCountMap[postCourse] = 1
      } else {
        this.dependencyCountMap[postCourse]++
      }

      if (!this.postCoursesMap[preCourse]) {
        this.postCoursesMap[preCourse] = [postCourse]
      } else {
        this.postCoursesMap[preCourse].push(postCourse)
      }
    }

    console.log(`We have ${numCourses} course(s)`)
    console.log('Dependency count (the value) of each course (the key):', this.dependencyCountMap)
    console.log('Post course(s) (the value) of each course (the key):', this.dependencyCountMap)
  }

  getEntrance() {
    const ret = []
    for (let i = 0; i < this.courcesCount; i++) if (!this.dependencyCountMap[i]) ret.push(i)
    return ret
  }

  learnNext() {
    const nextCourse = this.queue.shift()
    console.log(`Now learning #${nextCourse}`)

    const postCourses = this.postCoursesMap[nextCourse] || []
    console.log(`    ==> After #${nextCourse} learnt, these courses may be learnt: ${postCourses.join(', ') || '<No courses>'}`)

    for (const postCourse of postCourses) {
      console.log(`    ==> Checking #${postCourse} can be learnt`)

      this.dependencyCountMap[postCourse]--
      if (this.dependencyCountMap[postCourse] !== 0) {
        console.log(`    ======> #${postCourse} still got ${this.dependencyCountMap[postCourse]} dependent courses, will skip`)
        continue
      }

      console.log(`    ======> #${postCourse} can be learnt, will added to queue`)
      this.passedCourses.add(postCourse)
      this.queue.push(postCourse)
      console.log(`    ======> The queue now contains:`, this.queue)
      console.log(`    ======> Courses learnt:`, this.passedCourses)

      // console.log(this.passedCourses, this.queue)
    }
  }

  learnAll() {
    const entrance = this.getEntrance()
    console.log('From the beginning, there are these courses with no dependent courses:', entrance)
    this.queue = entrance
    this.passedCourses = new Set(entrance)

    while (this.queue.length) this.learnNext()
  }

  hasLearntAll() {
    console.log(`Finally, we learnt ${this.passedCourses.size} courses`)
    return this.passedCourses.size === this.courcesCount
  }
}

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
  if (!prerequisites.length) return true

  const scheduleGraph = new ScheduleGraph(numCourses, prerequisites)
  scheduleGraph.learnAll()
  return scheduleGraph.hasLearntAll()
};
// @lc code=end

