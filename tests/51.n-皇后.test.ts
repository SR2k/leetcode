import { solveNQueens } from '../51.n-皇后'

describe('51.n-皇后', () => {
  it('should work', () => {
    expect(solveNQueens(1))
      .toStrictEqual([['Q']])

    expect(solveNQueens(4).sort((a, b) => (a[0] > b[0] ? 1 : -1)))
      .toStrictEqual([
        ['.Q..', '...Q', 'Q...', '..Q.'],
        ['..Q.', 'Q...', '...Q', '.Q..'],
      ].sort((a, b) => (a[0] > b[0] ? 1 : -1)))
  })
})
