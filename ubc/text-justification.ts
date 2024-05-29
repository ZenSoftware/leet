/**
 * https://leetcode.com/problems/text-justification/description/
 */
export { fullJustify, lineCharCount, spaces };

function fullJustify(words: string[], maxWidth: number): string[] {
  const result: string[] = [];
  let nextIndex = 0;
  let line: string[] = [];

  while (nextIndex < words.length) {
    const nextWord = words[nextIndex];
    const charCountWithoutSpaces = lineCharCount(line);
    const charCountWithSpaces = charCountWithoutSpaces + line.length + nextWord.length;
    if (charCountWithSpaces <= maxWidth) {
      // Word fits on the line
      line.push(nextWord);
    } else {
      // Ran out of space for the line, now compute the spaces
      if (line.length > 1) {
        // More than one word on the current line
        const remainingWidth = maxWidth - charCountWithoutSpaces;
        const numberOfSpaces = line.length - 1;
        const spaceWidth = Math.floor(remainingWidth / numberOfSpaces);
        for (let i = 0; i < line.length - 1; i++) {
          line[i] = line[i] + spaces(spaceWidth);
        }

        const usedSpaces = spaceWidth * numberOfSpaces;
        let remainingSpaces = maxWidth - (usedSpaces + charCountWithoutSpaces);
        for (let i = 0; i < remainingSpaces; i++) {
          line[i] = line[i] + ' ';
        }

        const computedLine = line.join('');
        result.push(computedLine);
      } else {
        // One word on the current line, buffer spaces on the end.
        const remainingWidth = maxWidth - charCountWithoutSpaces;
        const computedLine = line[0] + spaces(remainingWidth);
        result.push(computedLine);
      }

      // Initialize the next line now that the current line is done
      line = [nextWord];
    }

    nextIndex++;
  }

  // Evaluate the last line
  if (line.length > 1) {
    // More than one word on the last line
    for (let i = 0; i < line.length - 1; i++) {
      line[i] = line[i] + ' ';
    }

    let lastLine = line.join('');
    const remainingWidth = maxWidth - lastLine.length;
    lastLine += spaces(remainingWidth);
    result.push(lastLine);
  } else {
    // One word on the last line
    let lastLine = line[0];
    const remainingWidth = maxWidth - lastLine.length;
    lastLine += spaces(remainingWidth);
    result.push(lastLine);
  }

  return result;
}

function lineCharCount(line: string[]): number {
  let charCount = 0;
  for (let word of line) {
    charCount += word.length;
  }
  return charCount;
}

function spaces(count: number): string {
  let spaces = '';
  for (let i = 1; i <= count; i++) {
    spaces += ' ';
  }
  return spaces;
}
