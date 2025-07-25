import { evalRPN } from './evaluate-reverse-polish-notation';

describe('Evaluate Reverse Polish Notation', () => {
  it('evaluates correctly', () => {
    expect(evalRPN(['2', '1', '+', '3', '*'])).toEqual(9);
    expect(evalRPN(['4', '13', '5', '/', '+'])).toEqual(6);
    expect(evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])).toEqual(
      22
    );
  });
});
