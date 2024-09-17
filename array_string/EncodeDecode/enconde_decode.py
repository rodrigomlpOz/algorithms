class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.
        
        We encode each string by storing its length followed by a delimiter
        to ensure we can safely decode later. We choose a delimiter that won't
        appear in the strings, such as ':', so the format is length:word.
        """
        encoded_str = ""
        for s in strs:
            # Append length of the string, a delimiter (':'), and the string itself
            encoded_str += str(len(s)) + ':' + s
        return encoded_str

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string to a list of strings.
        
        We parse the encoded string by reading the length, then extracting the
        appropriate substring.
        """
        decoded_list = []
        i = 0
        
        while i < len(s):
            # Find the position of the next ':' to extract the length of the string
            j = s.find(':', i)
            length = int(s[i:j])  # This gives us the length of the next string
            i = j + 1  # Move the pointer to the start of the actual string
            decoded_list.append(s[i:i + length])  # Extract the string of that length
            i += length  # Move the pointer to the next encoded string
        
        return decoded_list
