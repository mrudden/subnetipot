# subnetipot.py
# SubnetiPot
# Developed on Python 3.5.2
# Michael Rudden, 2016


# Purpose: group subnets into larger subnets, take parameter like /24 or /16, then process a list and produce all the specific bigger subnets that the smaller ones are contained in.


import argparse
import csv
import ipaddress


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~\n  Welcome to SubnetiPot \n\n ~irrigate your subnets~\n~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# Test data
test_subnet_list = [
  ipaddress.ip_network('192.168.1.0/28'),
  ipaddress.ip_network('192.168.1.16/28'),
  ipaddress.ip_network('192.168.1.32/28'),
  ipaddress.ip_network('192.168.1.242/32'),
  ipaddress.ip_network('192.168.24.48/28'),
  ipaddress.ip_network('192.168.24.16/28'),
  ipaddress.ip_network('192.168.24.144/28'),
  ipaddress.ip_network('192.168.116.200/29'),
  ipaddress.ip_network('192.168.116.32/27'),
  ipaddress.ip_network('192.168.116.64/26'),
  ipaddress.ip_network('10.10.10.64/26'),
  ipaddress.ip_network('10.10.10.128/26'),
  ipaddress.ip_network('10.10.10.192/28'),
  ipaddress.ip_network('10.10.220.64/26'),
  ipaddress.ip_network('10.10.220.128/26'),
  ipaddress.ip_network('10.10.220.192/28'),
  ipaddress.ip_network('10.10.222.64/26'),
  ipaddress.ip_network('10.10.222.128/26'),
  ipaddress.ip_network('10.10.222.192/28'),
  ipaddress.ip_network('10.12.111.64/26'),
  ipaddress.ip_network('10.12.111.128/26'),
  ipaddress.ip_network('10.12.111.192/28'),
  ]

test_range = "192.168.7.0-192.168.7.255"


def import_list(filename):
  #open CSV, read column into list_of_subnets. break down range as needed and flagged.
  imported_list = []
  with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ' ', quotechar='|')
    for row in csvreader:
      print(row)
      if args.range:
        ip_address = rangesplitter(row[0])[0]
      else:
        ip_address = ipaddress.ip_network(row[0])
      imported_list.append(ip_address)
#      print(ip_address)
  return imported_list


# Split a range of IPs if that's the input given. *Beta!
def rangesplitter(ip_range):
  split_range = ip_range.split('-')
  #print(split_range)
  first_ip = ipaddress.IPv4Address(split_range[0])
  second_ip = ipaddress.IPv4Address(split_range[1])
  #print(ipaddress.summarize_address_range(first_ip, second_ip))
  return [ipaddr for ipaddr in ipaddress.summarize_address_range(first_ip, second_ip)]

#print(rangesplitter(test_range))


def supernetter(subnet, netmask):
  if netmask == 0: return subnet.supernet(new_prefix=0)
  elif netmask == 1: return subnet.supernet(new_prefix=1)
  elif netmask == 2: return subnet.supernet(new_prefix=2)
  elif netmask == 3: return subnet.supernet(new_prefix=3)
  elif netmask == 4: return subnet.supernet(new_prefix=4)
  elif netmask == 5: return subnet.supernet(new_prefix=5)
  elif netmask == 6: return subnet.supernet(new_prefix=6)
  elif netmask == 7: return subnet.supernet(new_prefix=7)
  elif netmask == 8: return subnet.supernet(new_prefix=8)
  elif netmask == 9: return subnet.supernet(new_prefix=9)
  elif netmask == 10: return subnet.supernet(new_prefix=10)
  elif netmask == 11: return subnet.supernet(new_prefix=11)
  elif netmask == 12: return subnet.supernet(new_prefix=12)
  elif netmask == 13: return subnet.supernet(new_prefix=13)
  elif netmask == 14: return subnet.supernet(new_prefix=14)
  elif netmask == 15: return subnet.supernet(new_prefix=15)
  elif netmask == 16: return subnet.supernet(new_prefix=16)
  elif netmask == 17: return subnet.supernet(new_prefix=17)
  elif netmask == 18: return subnet.supernet(new_prefix=18)
  elif netmask == 19: return subnet.supernet(new_prefix=19)
  elif netmask == 20: return subnet.supernet(new_prefix=20)
  elif netmask == 21: return subnet.supernet(new_prefix=21)
  elif netmask == 22: return subnet.supernet(new_prefix=22)
  elif netmask == 23: return subnet.supernet(new_prefix=23)
  elif netmask == 24: return subnet.supernet(new_prefix=24)
  elif netmask == 25: return subnet.supernet(new_prefix=25)
  elif netmask == 26: return subnet.supernet(new_prefix=26)
  elif netmask == 27: return subnet.supernet(new_prefix=27)
  elif netmask == 28: return subnet.supernet(new_prefix=28)
  elif netmask == 29: return subnet.supernet(new_prefix=29)
  elif netmask == 30: return subnet.supernet(new_prefix=30)
  elif netmask == 31: return subnet.supernet(new_prefix=31)
  elif netmask == 32: return subnet.supernet(new_prefix=32)
  else: return "Error: Invalid netmask supplied."


# Takes an ip_network value, like 10.10.0.0/16, converts it to a string and splits on the "/", returning just the mask.
def get_mask(subnet):
  return int(str(subnet).split('/')[1])


# Let's handle arguments better than before, using argparse!
parser = argparse.ArgumentParser(description='Get bigger subnets that contain the ones being input')
parser.add_argument("netmask", type=int, help="Set netmask, must be a number from 1-32")
parser.add_argument("-f", "--filename", help="Specify CSV file to read. Data should be in column 1")
parser.add_argument("-r", "--range", help="Set input type to range. Input must be in format \"#.#.#.#-#.#.#.#\"", action="store_true")
args = parser.parse_args()


# Let's store the inputs and print out some helpful to show us our parameters.
try:
  cidr_netmask = args.netmask
  if cidr_netmask < 33:
    print("Parameters\n----------")
    print("Subnet Mask: " + str(cidr_netmask))
  else:
    raise
except:
  print("You need to put an argument after the script name.\nIt should be a number between 0 and 32.\n\nExample:\n>python subnetipot.py 16\n\nExiting.")
  exit(0)

if args.range:
  print("Mode: Range")
else:
  print("Mode: CIDR")

if args.filename:
  file_to_open = args.filename
  print("Filename: " + args.filename)
  # Open the CSV list, read it and process it into the list
  list_of_subnets = import_list(file_to_open)
else:
  print("Filename: Not specified, so test data will be used.")
  list_of_subnets = test_subnet_list


#list_of_subnets = file_to_open
list_of_supernets = []

# This is where the output comes from! The Meat and Potatoes, so to speak.
for subnet in list_of_subnets:
# For testing:
#  print(get_mask(subnet))
  if get_mask(subnet) >= cidr_netmask:
    supernet = supernetter(subnet, cidr_netmask)
    if supernet not in list_of_supernets:
      list_of_supernets.append(supernet)
    else: continue
  else:
    print("Mask requested is greater than " + str(subnet) + ". Skipping.")


print("\n--------------------------------------\n Here are those ranges you requested! \n--------------------------------------\n")

for bignet in list_of_supernets:
# Tasty bignets just like in Louisiana
  print(bignet)

print("\n--------------------------------------\n      ~you can now breathe easy~ \n--------------------------------------\n")
