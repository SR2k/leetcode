import { restoreIpAddresses } from '../93.复原-ip-地址'

describe('93.复原-ip-地址', () => {
  it('should work', () => {
    expect(restoreIpAddresses('25525511135').sort())
      .toStrictEqual(['255.255.11.135', '255.255.111.35'].sort())
    expect(restoreIpAddresses('0000').sort())
      .toStrictEqual(['0.0.0.0'].sort())
    expect(restoreIpAddresses('101023').sort())
      .toStrictEqual(['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'].sort())
    expect(restoreIpAddresses('99999999'))
      .toStrictEqual(['99.99.99.99'])
    expect(restoreIpAddresses('999999999'))
      .toStrictEqual([])
  })
})
