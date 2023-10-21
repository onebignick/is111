# Nicholas Ong - Q4b: News

# AHO CORASICK???

def solve(query, file):
    infile = open(file, "r")
    result = []
    lines = infile.readlines()

    for line in lines:
        if query.lower() in line.lower(): result.append(line)

    if not result:
        print("There is no matching line")
        print()
    else:
        print(f"There are {len(result)} matching headlines")
    for i in range(len(result)):
        print(f"{i+1}. {result[i]}")
    infile.close()
    return 0

def main():
    flag = input("Do you want to search our news database? [Y|N] :")
    while flag=="Y":
        query = input("Enter a keyword or a keyphrase :")
        print()
        solve(query, "../src/news.txt")
        flag = "Y" if input("Do you want to search again? [Y|N] :")=="Y" else "N"
    print("Good-bye!")
    return 0

if __name__ == "__main__":
    main()   
