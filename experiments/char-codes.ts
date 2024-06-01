function getCharCodes() {
  const lower = 'abcdefghijklmnopqrstuvwxyz';
  const upper = lower.toUpperCase();
  const numeric = '0123456789';

  let result: number[] = [];
  for (let i = 0; i < lower.length; i++) {
    result.push(lower.charCodeAt(i));
  }
  console.log('Lower: ', result);

  result = [];
  for (let i = 0; i < upper.length; i++) {
    result.push(upper.charCodeAt(i));
  }
  console.log('Upper: ', result);

  result = [];
  for (let i = 0; i < numeric.length; i++) {
    result.push(numeric.charCodeAt(i));
  }
  console.log('Numeric: ', result);
}

getCharCodes();
