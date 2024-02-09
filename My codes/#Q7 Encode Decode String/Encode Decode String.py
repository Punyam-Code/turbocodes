#Q7 encode decode string 

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return ''.join([f"{len(s)}:{s}" for s in strs])

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0

        while i < len(s):
            # Find the colon that separates length and string
            colon_index = s.find(':', i)
            # Extract the length of the current string
            length = int(s[i:colon_index])
            # Move the index after the colon
            i = colon_index + 1
            # Extract the string using the length
            decoded_strs.append(s[i:i + length])
            # Move the index after the current string
            i += length

        return decoded_strs

# Example usage:
codec = Codec()
original_strings = ["hello", "world", "leetcode"]

# Encode the list of strings
encoded_string = codec.encode(original_strings)
print(f"Encoded String: {encoded_string}")

# Decode the string to a list of strings
decoded_strings = codec.decode(encoded_string)
print(f"Decoded Strings: {decoded_strings}")


#type 2 
def encode(self, strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

    def decode(self, str):
    res, i = [], 0
    while i ‹ len(str):
        j゠i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append (str[j + 1: j+ 1 + length])
        i = j+ 1 + length
    return res
