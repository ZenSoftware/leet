// https://github.com/type-challenges/type-challenges/blob/main/questions/00018-easy-tuple-length/README.md
{
  type tesla = ['tesla', 'model 3', 'model X', 'model Y'];
  type spaceX = ['FALCON 9', 'FALCON HEAVY', 'DRAGON', 'STARSHIP', 'HUMAN SPACEFLIGHT'];
  const tesla2 = ['tesla', 'model 3', 'model X', 'model Y'] as const;

  type Length<T extends readonly unknown[]> = T['length'];

  type teslaLength = Length<tesla>; // expected 4
  type spaceXLength = Length<spaceX>; // expected 5
  type tesla2Length = Length<typeof tesla2>; // expected 5
}
