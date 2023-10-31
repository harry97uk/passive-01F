import argparse
import os
from full_name import recognize_full_name
from ip_address import recognize_ip_address
from username import recognize_username

# Define the directory where results will be saved
result_directory = "results"

# Ensure the result directory exists
if not os.path.exists(result_directory):
    os.makedirs(result_directory)

# Define the argparse configuration
parser = argparse.ArgumentParser(description="Passive Recognition Tool v1.0.0")

# Add options for full name, IP address, and username
parser.add_argument("-fn", metavar="FULL NAME", type=str, help="Search with full name")
parser.add_argument("-ip", metavar="IP ADDRESS", type=str, help="Search with IP address")
parser.add_argument("-u", metavar="USERNAME", type=str, help="Search with username")

# Parse the command-line arguments
args = parser.parse_args()

# Determine which option is chosen and handle accordingly
if args.fn:
    last_name, first_name, address, number = recognize_full_name(args.fn)
    result_file = "result.txt"
    with open(os.path.join(result_directory, result_file), "w") as file:
        file.write(f"First name: {first_name}\n")
        file.write(f"Last name: {last_name}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Number: {number}\n")
    print(f"Saved in {result_file}")
elif args.ip:
    position = recognize_ip_address(args.ip)
    result_file = "result2.txt"
    with open(os.path.join(result_directory, result_file), "w") as file:
        #file.write(f"ISP: {isp}\n")
        file.write(f"{position}\n")
    print(f"Saved in {result_file}")
elif args.u:
    social_networks = recognize_username(args.u)
    result_file = "result3.txt"
    with open(os.path.join(result_directory, result_file), "w") as file:
        for network, presence in social_networks.items():
            file.write(f"{network} : {presence}\n")
    print(f"Saved in {result_file}")
else:
    print("No recognized option provided. Use -fn, -ip, or -u to perform a search.")
