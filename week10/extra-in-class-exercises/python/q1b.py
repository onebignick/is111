# Nicholas Ong - Q1(b): Grades
import collections

def solve(file_name):
    infile = open(file_name, "r")
    lines = infile.readlines()
    graph = collections.defaultdict(set)
    
    for line in lines:
        line = line.strip().split("#")
        graph[line[0]].add(line[1]+line[2])

    keys = [key for key in graph]
    for i in range(len(keys)-1):
        for j in range(i+1,len(keys)):
            tmp=graph[keys[i]]&graph[keys[j]]
            if len(tmp)>=1: print(f"{keys[i]}, {keys[j]}")

    infile.close()

def main():
    solve("../src/grades.txt")

main()
