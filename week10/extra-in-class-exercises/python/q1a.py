# Nicholas Ong - Q1(a): Grades
import collections

def solve(filename):
    infile = open(filename, "r")
    outfile = open("course_info.txt", "w")

    lines = infile.readlines()
    cache = collections.defaultdict(list)

    for line in lines:
        line = line.strip().split("#")
        if line[-1] == "A": cache[line[1]].append(line[0])

    results = []
    for key in cache:
        result = key+'\n'
        for value in cache[key]: result = result + value + '\n'
        results.append(result +'\n')
    results[-1] = results[-1].strip()
    outfile.writelines(results)

    infile.close()
    outfile.close()

def main():
    solve("../src/grades.txt")
    return 0

if __name__ == "__main__":
    main()
