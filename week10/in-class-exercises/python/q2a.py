# Nicholas Ong - Q2a: Books
def get_books_cheaper_than(input_file_name, price_limit, output_file_name):
    infile = open(f"../src/{input_file_name}", "r")
    outfile = open(output_file_name, "w")

    result = []
    lines = infile.readlines()
    for line in lines:
        a = line.strip().split()
        try:
            if float(a[-1][1:]) < price_limit:
                result.append(line)
        except Exception as e:
            print(e)
    outfile.writelines(result)

    infile.close()
    outfile.close()

def main():
    test_cases = [["books-1.txt","books-1-output.txt", 15.0], ["books-2.txt", "books-2-output.txt", 7.0]]
    for input_file_name, output_file_name, price_limit in test_cases:
        get_books_cheaper_than(input_file_name, price_limit, output_file_name)

if __name__ == "__main__":
    main()
