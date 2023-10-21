# Nicholas Ong - Q3(b): Phone Number
import collections

def solve(file_name):
    infile = open(f"../src/{file_name}", "r")
    outfile = open("phone_book_reorganized.txt", "w")

    cache = collections.defaultdict(list)
    lines = infile.readlines()
    for line in lines:
        line = line.strip().split("|")
        cache[line[0]].append(line[1])
    
    result = []
    for key in cache:
        temp = key+'\n'
        for value in cache[key]: temp = temp + value + '\n'
        result.append(temp+'\n')
    outfile.writelines(result)

    infile.close()
    outfile.close()

def main():
    test_cases = ["phone_book.txt"]
    for test_case in test_cases:
        solve(test_case)
    return

if __name__ == "__main__":
    main()
