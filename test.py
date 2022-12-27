from netmiko import ConnectHandler, NetmikoTimeoutException

ip = str(input('\nEnter the device ip address: '))
username = str(input('Enter the device name: '))
password = str(input('Enter the device password: '))
port = str(input('Enter the port number: '))

mikroTik = {
    "device_type": "mikrotik_routeros",
    "host": ip,
    "username": username,
    "password": password,
    "port": port
}

conn = ConnectHandler(**mikroTik)
print('\nConnection established successfully with ', ip)

print("""\n
Choose a command:
    1. System reboot
    2. System shutdown
    3. Show IP settings
    4. Show default configuration
    5. Show ARP table
    6. Show static routes
    7. Show interfaces
    8. Show MAC address table
    9. Display device name
    10. Display all users
    11. Change device name
    12. Change device password (firstly, device name must be changed)
    13. Other
    14. Disconnect\n""")

while True:
    choice = int(input('Enter your choice: '))

    try:
        if (choice == 1):
            output = conn.send_command('system reboot')
        elif (choice == 2):
            output = conn.send_command('system shutdown')
        elif (choice == 3):
            output = conn.send_command('ip address print')
        elif (choice == 4):
            output = conn.send_command('system default-configuration print')
        elif (choice == 5):
            output = conn.send_command('show ip arp')
        elif (choice == 6):
            output = conn.send_command('ip route print')
        elif (choice == 7):
            output = conn.send_command('interface print')
        elif (choice == 8):
            output = conn.send_command('interface bridge host print')
        elif (choice == 9):
            output = conn.send_command('system identity print')
        elif (choice == 10):
            output = conn.send_command('user print')
        elif (choice == 11):
            new_name = str(input('Enter new device name: '))
            output = conn.send_command('system set 0 name = {}'.format(new_name))  
        elif (choice == 12):
            new_password = str(input('Enter new password: '))
            output = conn.send_command('system set 0 password = "{}"'.format(new_password))
        elif (choice == 13):
            command = str(input('Enter command: '))
            output = conn.send_command(command)
        elif (choice == 14):
            conn.disconnect(**mikroTik)
            break
        else:
            print('Invalid input!')
            
        print(output)

    except NetmikoTimeoutException:
        print('Request timeout...')
