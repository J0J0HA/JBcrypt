import random
import string


class Encoder:
    def _random_letter(self, not_in=""):
        result = "A"
        while result in not_in:
            result = random.choice(string.ascii_letters)
        return result

    def encode(self, msg: str) -> str:
        msg_len = len(msg)
        msg_ltrs = ""
        for msg_ltr in msg:
            if msg_ltr not in msg_ltrs:
                msg_ltrs += msg_ltr
        msg_dif = len(msg_ltrs)
        key = msg_ltrs
        key_list = list(key)
        for index in range(0, 3):
            key += self._random_letter(not_in=key)
        random.shuffle(key_list)
        key_dict = {}
        for index in range(len(key_list)):
            key_dict[key_list[index]] = key_list[len(key_list) - index - 1]
            key_dict[key_list[len(key_list) - index - 1]] = key_list[index]
        msg_list = list(msg)
        for index in range(len(msg)):
            msg_list[index] = key_dict[msg_list[index]]
        for index in range(0, 3):
            msg_list.insert(random.randint(0, len(msg_list) - 1), self._random_letter(not_in=msg + key))
        msg = "".join(msg_list)
        result = ""
        key_pos = False
        real_index = 0
        for index in range(len(key) + len(msg)):
            if key_pos:
                result += key[real_index]
                real_index += 1
            else:
                result += msg[real_index]
            key_pos = not key_pos
        return result
