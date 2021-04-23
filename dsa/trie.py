class Trie:
    def __init__(self, special_char='~'):
        self.special_char = special_char
        self.children = {}

    def insert(self, input_str, value=None):
        if len(input_str) == 0:
            return False

        curr = self.children
        for char in input_str:
            if char not in curr:
                curr[char] = {}

            curr = curr[char]

        curr[self.special_char] = value
        return True

    def search(self, input_str):
        if len(input_str) == 0:
            return False, None

        curr = self.children
        for char in input_str:
            if char in curr:
                curr = curr[char]
            else:
                return False, None

        if self.special_char not in curr:
            return False, None
        else:
            return True, curr[self.special_char]
