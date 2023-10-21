# Nicholas Ong - Q2: Most Frequent Words
import collections
import heapq

def solve(filename):
    infile = open(f"../src/{filename}","r")
    tmp = []
    lines = infile.readlines()
    for line in lines:
        tmp += line.lower().split()
    r = collections.Counter(tmp)
    heap = []
    for key in r:
        heapq.heappush(heap, (-r[key], key))

    for i in range(3):
        tmp = heapq.heappop(heap)
        print(f"{tmp[1]}: {-tmp[0]}")
    infile.close()

def main():
    test_cases = ["article-1.txt", "article-2.txt"]
    for test in test_cases:
        solve(test)

main()
