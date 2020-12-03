import functools


class PasswordEntry():
    def __init__(self, entry_str):
        print(entry_str)
        cleaned = self.__clean_chars(entry_str)
        splitted = cleaned.split()
        self.index_one = int(splitted[0]) - 1
        self.index_two = int(splitted[1]) - 1
        self.letter = splitted[2]
        self.password = splitted[3]

    def is_valid(self):
        pos_count = 0
        if self.password[self.index_one] == self.letter:
            pos_count += 1

        if self.password[self.index_two] == self.letter:
            pos_count += 1

        if pos_count == 1:
            return True
        else:
            return False

    def __clean_chars(self, entry_str):
        no_newline = entry_str.replace("\n", "")
        no_colon = no_newline.replace(":", "")
        hyphen_to_space = no_colon.replace("-", " ")
        return hyphen_to_space


def count_valid(count, entry):
    if entry.is_valid():
        return count + 1
    else:
        return count


with open("../input/day2") as f:
    entries = [PasswordEntry(line)
               for line in f.read().splitlines() if line != ""]

    valid_count = functools.reduce(count_valid, entries, 0)

    print(valid_count)
