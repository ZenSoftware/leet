/**
 * https://leetcode.com/problems/gas-station/description/
 */
export { canCompleteCircuit };

function canCompleteCircuit(gas: number[], cost: number[]): number {
  for (let i = 0; i < gas.length; i++) {
    if (checkCircuit(gas, cost, i)) return i;
  }

  return -1;
}

function checkCircuit(gas: number[], cost: number[], station: number): boolean {
  let current = station;
  let tank = 0;

  do {
    tank += gas[current];
    tank -= cost[current];
    if (tank < 0) return false;
    current = nextIndex(current, gas.length);
  } while (current !== station);

  return true;
}

function nextIndex(current: number, circuitLength: number) {
  if (current + 1 === circuitLength) return 0;
  else return current + 1;
}
