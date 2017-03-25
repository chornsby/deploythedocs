import { chunk } from '../utils';

describe('The chunk() utility function', () => {
  it('splits an array into doubles', () => {
    expect(chunk([1, 2, 3, 4], 2)).toEqual([[1, 2], [3, 4]]);
  });

  it('include leftovers in the final chunk', () => {
    expect(chunk([1, 2, 3, 4, 5], 2)).toEqual([[1, 2], [3, 4], [5]]);
  });

  it('includes everything in the first chunk if not enough', () => {
    expect(chunk([1], 2)).toEqual([[1]]);
  });

  it('returns an empty array if given one', () => {
    expect(chunk([], 2)).toEqual([]);
  });

  it('rejects numbers below 1', () => {
    expect(() => chunk([1, 2, 3, 4], 0)).toThrowError('number must be > 0');
  });
});
