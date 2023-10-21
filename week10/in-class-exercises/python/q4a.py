# Nicholas Ong - Q4(a): News

def solve(query, file):
    infile = open(file, "r")
    result = []
    lines = infile.readlines()

    for line in lines:
        if query.lower() in line.lower(): result.append(line)

    if not result:
        print("There is no matching line")
        
    for i in range(len(result)):
        print(f"{i+1}. {result[i]}")

    infile.close()
    return 0

def main():
    query = input("Enter a keyword or a keyphrase: ")
    solve(query, "../src/news.txt")
    return 0

if __name__ == "__main__":
    main()
