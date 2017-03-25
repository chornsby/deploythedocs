import React from 'react';

/**
 * Split a given array into an array of arrays where the length of each chunk is
 * given by the parameter "number".
 *
 * chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
 *
 * @param array The array to split into chunks
 * @param number The length of each chunk
 */
export function chunk(array, number) {
  // Guard against infinite while loop
  if (number < 1) {
    throw new Error('number must be > 0');
  }

  const result = [];

  for (let index = 0; index < array.length; index += number) {
    result.push(array.slice(index, index + number));
  }

  return result;
}


export const VersionType = {
  api: React.PropTypes.string,
  url: React.PropTypes.string.isRequired,
  version: React.PropTypes.string.isRequired,
};

export const ProjectType = {
  api: React.PropTypes.string,
  name: React.PropTypes.string.isRequired,
  url: React.PropTypes.string.isRequired,
  versions: React.PropTypes.arrayOf(VersionType).isRequired,
};
