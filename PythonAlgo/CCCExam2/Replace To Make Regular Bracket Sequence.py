import sys
import heapq
import bisect
import math
import random

INF = 10 ** 9 + 7
OFFLINE = 0
N = 101010
sys.setrecursionlimit(INF)


def fi():
    return int(sys.stdin.readline())


def fi2():
    return map(int, sys.stdin.readline().split())


def fi3():
    return sys.stdin.readline().rstrip()


def fo(*args):
    for s in args:
        sys.stdout.write(str(s) + " ")
    sys.stdout.write("\n")


##
if OFFLINE:
    sys.stdin = open("fin.txt", "r")
    sys.stdout = open("fout.txt", "w")
##


##main

stack = []
s = fi3().rstrip()

res = 0

closing = '}])>'
opening = '<({['

revert = {'}': '{', ')': '(', ']': '[', '>': '<'}

for char in s:

    if char in opening:
        stack.append(char)

    if char in closing:
        if len(stack) == 0:
            fo('Impossible')
            exit(0)

        if stack[-1] != revert[char]:
            res += 1

        k = stack.pop(-1)

if len(stack) != 0:
    fo('Impossible')
    exit(0)

fo(res)
