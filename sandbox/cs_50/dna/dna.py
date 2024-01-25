import csv
from sys import argv


# how to run:
# python dna.py '.csv_file_dir' 'txt_file_dir'
def main():
    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Missing command-line argument")
        exit(1)

    # TODO: Read database file into a variable
    rows = []
    with open(f"{argv[1]}") as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(f"{argv[2]}") as sequence_file:
        dna = sequence_file.readline()

    # TODO: Find longest match of each STR in DNA sequence
    strs = [key for key in rows[0] if key != "name"]
    result = [longest_match(dna, key) for key in strs]

    # TODO: Check database for matching profiles
    for row in rows:
        if all(int(row[key]) == value for key, value in zip(strs, result)):
            print(row["name"])
            exit(0)

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
