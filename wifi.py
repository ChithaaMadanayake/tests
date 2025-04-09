import subprocess
import re

def get_wifi_password(profile_name):
    try:
        # Run netsh command for the specific WiFi profile
        command = f'netsh wlan show profile name="{profile_name}" key=clear'
        profile_info = subprocess.check_output(command, shell=True, text=True, errors="ignore")

        # Extract the WiFi password
        password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info)
        if password_match:
            print(f"WiFi: {profile_name}\nPassword: {password_match.group(1)}\n{'-'*30}")
        else:
            print(f"WiFi: {profile_name}\nPassword: No password set\n{'-'*30}")

    except subprocess.CalledProcessError as e:
        print(f"Error accessing WiFi profile '{profile_name}':", e)

# Get the password for "ZIMBA RULES"
get_wifi_password("ZIMBA RULES")
