/**
 * https://leetcode.com/problems/simplify-path/
 */
export { simplifyPath, removeExtraSlashes, removeUpLevels };

function simplifyPath(path: string): string {
  path = removeCurrentDirectory(path);
  path = removeExtraSlashes(path);
  path = removeUpLevels(path);

  return path;
}

function removeExtraSlashes(path: string): string {
  if (path.length < 2) return path;

  let cleaned = '';
  for (let i = 0; i < path.length; i++) {
    if (path[i] === '/' && path[i + 1] === '/') continue;
    cleaned += path[i];
  }

  if (cleaned[cleaned.length - 1] === '/') {
    return cleaned.substring(0, cleaned.length - 1);
  }

  return cleaned;
}

function removeCurrentDirectory(path: string): string {
  while (path.includes('/./')) {
    path = path.replaceAll('/./', '/');
  }
  if (path.endsWith('/.')) {
    return path.substring(0, path.length - 2);
  }
  return path;
}

function removeUpLevels(path: string): string {
  let splitPath = path.split('/');

  // remove leading '..'
  let i = 0;
  while (splitPath[i] === '..') {
    i++;
  }
  splitPath = splitPath.slice(i);

  // Add back leading  /
  path = splitPath.join('/');
  if (path[0] !== '/') path = '/' + path;

  return path;
}
