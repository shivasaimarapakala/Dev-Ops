import sys
#Checking if the Child branch is working properly to me

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
    logfile1 = sys.argv[1]
    logfile2 = sys.argv[2]    
    old_warnings = count_warnings_in_file(logfile1)
    new_warnings = count_warnings_in_file(logfile2)
    
    if new_warnings > old_warnings:
        print("Build is Rejected")
    else:
        print(" Build can be Promoted")

if __name__ == "__main__":
    main()
