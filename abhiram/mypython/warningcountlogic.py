import sys

def count_warnings_in_file(file_path):
    # Open file with 'r' mode
    file = open(file_path, 'r')
    count = 0
    # Loop through each line in the file
    for line in file:
        # Check if the line contains "WARNING" or "warning"
        if "WARNING" in line or "warning" in line:
            count += 1
    # Close the file
    file.close()
    return count

def main():
    print("Enter the path to the old build log file:")
    logfile1 = input().strip('"')
    print("Enter the path to the current build log file:")
    logfile2 = input().strip('"')
    
    old_warnings = count_warnings_in_file(logfile1)
    new_warnings = count_warnings_in_file(logfile2)
    
    if new_warnings > old_warnings:
        print("Buiild is Rejected")
    else:
        print(" Build can be Promoted")

if __name__ == "__main__":
    main()
