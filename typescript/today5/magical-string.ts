// https://leetcode.com/problems/magical-string/description/
export { magicalString, sample };

function magicalString(n: number): number {
  if (n == 0) return 0;

  let toggler = false;
  let history = [true];
  let count = 1;

  for (let i = 1; i < n; i++) {
    if (history[i] === true) {
      if (toggler) history.push(true);
      else history.push(false);
      count++;
    } else {
      if (toggler) history.push(true, true);
      else history.push(false, false);
    }
    toggler = !toggler;
  }

  return count;
}

function sample(n: number): string {
  if (n == 0) return "";

  let one = false;
  let result = ["1"];
  let count = 1;

  for (let i = 1; i < n; i++) {
    if (result[i] === "1") {
      if (one) result.push("1");
      else result.push("2");
      count++;
    } else {
      if (one) result.push("1", "1");
      else result.push("2", "2");
    }
    one = !one;
  }

  return result.slice(0, n).join("");
}
