import { magicalString, sample } from './magical-string';

describe('leetcode', () => {
  const KNOWN_ANS = '1221121221221121122';
  const known = (n: number) => {
    const ans = KNOWN_ANS.slice(0, n);
    let count = 0;
    for (let i = 0; i < ans.length; i++) {
      if (ans[i] == '1') count++;
    }
    return count;
  };

  test('works', () => {
    for (let i = 0; i <= KNOWN_ANS.length; i++) {
      expect(magicalString(i)).toBe(known(i));
    }
  });
});

describe('sample', () => {
  const KNOWN_ANS = '1221121221221121122';
  const known = (n: number) => KNOWN_ANS.slice(0, n);

  test('works', () => {
    for (let i = 0; i <= KNOWN_ANS.length; i++) {
      expect(sample(i)).toBe(known(i));
    }
  });
});
