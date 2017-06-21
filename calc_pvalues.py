#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations
import argparse
import numpy as np


def main(args):
    mat = np.loadtxt(args.path_matrix)
    avgs = [(i, v) for i, v in enumerate(mat.mean(axis=0))]

    minmax = np.loadtxt(args.path_minmax)
    sysl = np.loadtxt(args.path_sysl, dtype=object)

    n_items = minmax.shape[0]
    for system_pair in combinations(avgs, 2):
        diff = abs(system_pair[0][1] - system_pair[1][1])
        count = sum(minmax[:, 2] >= diff)
        pvalue = count / n_items
        sys1 = sysl[system_pair[0][0]]
        sys2 = sysl[system_pair[1][0]]
        print('{} {} {} {}'.format(sys1, sys2, diff, pvalue))

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_matrix', help='path to matrix file')
    parser.add_argument('path_minmax', help='path to minmax file')
    parser.add_argument('path_sysl', help='path to system label')
    parser.add_argument('-v', '--verbose',
                        action='store_true', default=False,
                        help='verbose output')
    args = parser.parse_args()
    main(args)
