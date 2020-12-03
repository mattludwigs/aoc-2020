from collections import Counter
import functools


class PasswordEntry():
    def __init__(self, entry_str):
        cleaned = self.__clean_chars(entry_str)
        splitted = cleaned.split()
        self.min_times = int(splitted[0])
        self.max_times = int(splitted[1])
        self.letter = splitted[2]
        self.password = splitted[3]

    def is_valid(self):
        counter = Counter(self.password)
        num_times = counter[self.letter]

        if self.min_times <= num_times <= self.max_times:
            return True
        else:
            return False

    def __clean_chars(self, entry_str):
        no_newline = entry_str.replace("\n", "")
        no_colon = no_newline.replace(":", "")
        hyphen_to_space = no_colon.replace("-", " ")
        return hyphen_to_space


def count_valid(count, password_entry):
    if password_entry.is_valid():
        return count + 1
    else:
        return count


with open("../input/day2") as f:
    entries = [PasswordEntry(line)
               for line in f.read().splitlines() if line != ""]

    valid_count = functools.reduce(count_valid, entries, 0)
    print(valid_count)
