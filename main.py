import subprocess

def get_wifi_profiles():
    try:
        # Run the command to get the list of Wi-Fi profiles
        profiles_data = subprocess.check_output('netsh wlan show profiles', shell=True, text=True)
        profiles = [line.split(":")[1].strip() for line in profiles_data.split('\n') if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Wi-Fi profiles: {e}")
        return []

def get_wifi_password(profile):
    try:
        # Run the command to get the Wi-Fi password for a specific profile
        profile_data = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True, text=True)
        for line in profile_data.split('\n'):
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for profile {profile}: {e}")
        return None

def main():
    profiles = get_wifi_profiles()
    if profiles:
        print("Saved Wi-Fi profiles and passwords:")
        for profile in profiles:
            password = get_wifi_password(profile)
            print(f"Profile: {profile}, Password: {password if password else 'None'}")
    else:
        print("No Wi-Fi profiles found.")

if __name__ == "__main__":
    main()