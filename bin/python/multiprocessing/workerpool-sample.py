#!/usr/bin/env python3

import multiprocessing
import time
import os

multiprocessing.set_start_method('fork')
input_file = 'hostlist.csv'

def split_list(list_target, workernum):
    return [list_target[i::workernum] for i in range(workernum)]

def build_list(target_file):
    target_list = list()
    with open(target_file) as input_file:
        input_lines = [input_line.rstrip() for input_line in input_file]
        target_list += input_lines
        for target in target_list:
            print('PUT: {}'.format(target))
    return target_list

def worker(item):
    print('GOT: {}'.format(item))

def work_handler():
    workqueue = multiprocessing.Pool(workerpool)
    workqueue.map(worker, target_list)

workerpool = 20
target_list = build_list(input_file)
work_handler()
