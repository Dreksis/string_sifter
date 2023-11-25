import os

def find_pid_for_addresses(result_file_path, memprocfs_root):
    """
    This function takes two arguments: a file path to a file containing memory addresses and a path to the memprocfs
    root directory. It searches the memory maps of all running processes to find those that have memory regions
    containing the specified addresses. It returns a dictionary where the keys are the PIDs of the matching processes
    and the values are lists of the matching memory addresses.
    """
    # Open the file containing the memory addresses and read its contents into a list
    with open(result_file_path, 'r') as file:
        found_addresses = [int(line.strip(), 16) for line in file.readlines()]

    # Create an empty dictionary to store the results of the search
    pid_map = {}

    # Iterate over the contents of the memprocfs root directory
    for pid in os.listdir(memprocfs_root):
        pid_path = os.path.join(memprocfs_root, pid)

        # Check if the current subdirectory is a valid PID (i.e., a valid integer)
        if os.path.isdir(pid_path):
            try:
                int(pid)
            except ValueError:
                continue

            # Open the memory map file for the current PID and iterate over its contents
            with open(os.path.join(pid_path, 'memmap.txt'), 'r') as file:
                for line in file:
                    # Split each line into a list of strings using whitespace as the delimiter
                    parts = line.split(' ')

                    # If the line has at least two elements, assume they are the starting and ending memory
                    # addresses for a memory region and convert them to integers in base 16 format
                    if len(parts) >= 2:
                        start_addr, end_addr = int(parts[0], 16), int(parts[1], 16)

                        # Iterate over the list of found memory addresses and check if each one falls within the
                        # current memory region. If it does, add it to the list of addresses associated with the
                        # current PID in the pid_map dictionary.
                        for addr in found_addresses:
                            if start_addr <= addr <= end_addr:
                                pid_map.setdefault(pid, []).append(addr)

    # Return the pid_map dictionary
    return pid_map

# Prompt the user to enter the path to the file containing memory addresses and the path to the memprocfs root directory
result_file_path = input("Enter the path to the file containing memory addresses: ")
memprocfs_root = input("Enter the path to the memprocfs root directory: ")

# Call the find_pid_for_addresses function with the user-specified paths and print the resulting pid_map dictionary
pid_map = find_pid_for_addresses(result_file_path, memprocfs_root)
for pid, addresses in pid_map.items():
    print(f"PID: {pid}, Addresses: {addresses}")
