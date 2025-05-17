# 01_reverse_string.py

def reverse_string(s: str) -> str:
    return s[::-1]

# Example usage
if __name__ == "__main__":
    print(reverse_string("hello"))  # Output: "olleh"
    print(reverse_string("python"))  # Output: "nohtyp"
    print(reverse_string("algorithm"))  # Output: "mhtirogla"
    print(reverse_string("data structure"))  # Output: "erutcurts atad"
    print(reverse_string("binary search"))  # Output: "hcraes yranib"
    print(reverse_string("linked list"))  # Output: "tsil deknil"
