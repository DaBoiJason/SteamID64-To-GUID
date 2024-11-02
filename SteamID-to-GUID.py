import hashlib

def uid2guid(uid):
    if uid is None:
        return None
    parts = [0x42, 0x45, 0, 0, 0, 0, 0, 0, 0, 0]
    steam_id = uid
    for i in range(2, 10):
        parts[i] = steam_id % 256
        steam_id //= 256
    byte_array = bytearray(parts)
    md5_hash = hashlib.md5(byte_array).hexdigest()
    return md5_hash
print ("Enter the STEAM ID 64 to convert to GUID for ARMA and DAY-Z")
uid = int(input())
hash_output = uid2guid(uid)
print(f"The MD5 hash of the SteamID64 {uid} for ARMA and DAY-Z is:\nGUI : {hash_output}\n")
input("Press Enter to close the tab")