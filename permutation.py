#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hashlib import md5
import argparse
import numpy as np


def main(args):
    MAX_SEED = 2**32 - 1
    if args.seed_by_name:
        filename = args.path_input + args.path_output
        seed = int(md5(filename.encode('utf_8')).hexdigest(), 16)
        seed %= MAX_SEED
        np.random.seed(seed)

    mat = np.loadtxt(args.path_input)

    # Permutation
    for i, row in enumerate(mat):
        mat[i] = np.random.permutation(row)

    matsum = mat.sum(axis=0)

    with open(args.path_output, 'w') as f:
        maxval = matsum.max()
        minval = matsum.min()
        diffavg = (maxval - minval) / mat.shape[0]
        f.write('{} {} {}\n'.format(maxval, minval, diffavg))

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_input', help='path to input file')
    parser.add_argument('path_output', help='path to input file')
    parser.add_argument('--seed-by-name', action='store_true',
                        help='set a random seed based on an input file\'s name')
    parser.add_argument('-v', '--verbose',
                        action='store_true', default=False,
                        help='verbose output')
    args = parser.parse_args()
    main(args)
