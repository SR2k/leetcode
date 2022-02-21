export const deepSorted = (arr: number[][]) => arr.map((x) => [...x].sort((a, b) => a - b))
  .sort((a, b) => a[0] - b[0])

export const mergeSorted = (arr: number[][]) => arr.map((x) => [...x].sort((a, b) => a - b))
  .sort((a, b) => (a.join(',') > b.join(',') ? 1 : -1))
