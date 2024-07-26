# Wi-Fi Profile and Password Retriever

This Python script retrieves and displays saved Wi-Fi profiles and their passwords on a Windows machine.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [get_wifi_profiles](#get_wifi_profiles)
  - [get_wifi_password](#get_wifi_password)
  - [main](#main)
- [Disclaimer](#disclaimer)

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository or download the script file.
    ```sh
    git clone https://github.com/yourusername/wifi-profile-retriever.git
    cd wifi-profile-retriever
    ```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory containing the script.
3. Run the script using Python:
    ```sh
    python wifi_profile_retriever.py
    ```

The script will display a list of saved Wi-Fi profiles and their associated passwords.

## Functions

### get_wifi_profiles

Retrieves a list of saved Wi-Fi profiles on the machine.

**Returns:**
- A list of Wi-Fi profile names.

### get_wifi_password

Retrieves the password for a given Wi-Fi profile.

**Parameters:**
- `profile` (str): The name of the Wi-Fi profile.

**Returns:**
- The password for the Wi-Fi profile, or `None` if no password is found.

### main

The main function that orchestrates the retrieval and display of Wi-Fi profiles and passwords.

## Disclaimer

This script is intended for educational purposes and should only be used on machines where you have explicit permission to retrieve Wi-Fi profiles and passwords. Unauthorized use of this script may violate privacy and security policies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.