from devices import Device,Firewall, Switch
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Micks attempt
from devices import Switch
# creat instance of switch
Cisco_01 = Switch(24)
# Configure the subclass
Cisco_01.configure_switch()

my_devices = Device()
my_devices.calculate_crc("dummy")

# call main class variables to see if we can access them here (yes we can)
print(my_devices.pi)
#this should be vlan 200
print(f"The Vlan used for printing from device class is {my_devices.switch_print_vlan}")

#lets change the value of vlan from my subclass to on the main device class and print it now
Cisco_01.change_vlan_in_device()
# should print vlan 400
print(f"The Vlan used for printing from device class changed to {my_devices.switch_print_vlan}")

# I will send in a valus to the main class and get its return value
# The main class will pverwrite what I sent in on its return
print(f'this is a test {my_devices.calculate_crc("Dummy Mick Data....Ha Ha")}')

