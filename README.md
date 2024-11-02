# Steam ID 64 to GUID Converter

This Python program is designed for server administrators who need to convert Steam ID 64 (a unique identifier for Steam accounts) into GUIDs (Globally Unique Identifiers) used in games like ARMA and DayZ. The GUIDs are derived from the MD5 hash of the Steam ID 64, allowing server admins to manage player identities more efficiently.

## Features

- Convert Steam ID 64 to GUID using MD5 hashing
- Simple command-line interface
- Quick and easy to use for server management

## Prerequisites

- Python 3.x
- `hashlib` module (included with Python standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DaBoiJason/SteamID64-To-GUID
   ```

2. Navigate to the project directory:

   ```bash
   cd SteamID64-To-GUID
   ```

3. You can run the script directly if you have Python installed on your machine.

## USAGE

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script:

   ```bash
   python SteamID to GUID.py
   ```

4. You will be prompted to enter the Steam ID 64. Enter the ID and press Enter.

5. The program will output the corresponding GUID.

## Example

   ```text
   Enter the STEAM ID 64 to convert to GUID for ARMA and DAY-Z
   76561198000000000
   The MD5 hash of the SteamID64 76561198000000000 for ARMA and DAY-Z is:
   GUI : edc48a4a45cdc3e925dc160020c42595

   Press Enter to close the tab
   ```

## Contributing

Contributions are welcome!

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.