import { simplifyPath, removeExtraSlashes, removeUpLevels } from './simplify-path';

describe('Simplify Path', () => {
  it('evaluates simplifyPath correctly', () => {
    expect(simplifyPath('/.//a///b//././')).toEqual('/a/b');
    expect(simplifyPath('/.//a///b//././.../')).toEqual('/a/b/...');
    expect(simplifyPath('/.//a///b//././.../.')).toEqual('/a/b/...');
    expect(simplifyPath('/.//a///b.//././.../.')).toEqual('/a/b./...');
  });

  it('evaluates removeExtraSlashes correctly', () => {
    expect(removeExtraSlashes('///a///b////')).toEqual('/a/b');
    expect(removeExtraSlashes('/')).toEqual('/');
  });

  it('evaluates removeUpLevels correctly', () => {
    expect(removeUpLevels('../../a')).toEqual('/a');
  });
});
