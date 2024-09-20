import string
def validIPAddress(self, queryIP: str) -> str:
    # Function to validate if queryIP is IPv4
    def is_valid_ipv4(ip: str) -> bool:
        parts = ip.split(".")
        for part in parts:
            # Check if part is a digit, and no leading zeros unless it's "0"
            if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                return False
        return True

    # Function to validate if queryIP is IPv6
    def is_valid_ipv6(ip: str) -> bool:
        parts = ip.split(":")
        for part in parts:
            # Check length and valid hex digits
            if not (1 <= len(part) <= 4) or not all(c in string.hexdigits for c in part):
                return False
        return True

    # Check if the input is a valid IPv4 or IPv6
    if queryIP.count(".") == 3 and is_valid_ipv4(queryIP):
        return "IPv4"
    elif queryIP.count(":") == 7 and is_valid_ipv6(queryIP):
        return "IPv6"
    else:
        return "Neither"
