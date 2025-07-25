/**
 * https://leetcode.com/problems/gas-station/description/
 */
export { canCompleteCircuit };

function canCompleteCircuit(gas: number[], cost: number[]): number {
  let result = 0;
  let total = 0;
  let tank = 0;
  for (let i = 0; i < gas.length; i++) {
    const val = gas[i] - cost[i];
    tank += val;
    total += val;
    if (total < 0) {
      total = 0;
      result = i + 1;
    }
  }

  if (tank < 0) return -1;
  else return result;
}
