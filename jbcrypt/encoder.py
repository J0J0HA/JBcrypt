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
        for index in range(0, 3):
            msg += self._random_letter(not_in=msg)
        if msg_dif > msg_len:
            for index in range(0, msg_dif - msg_len):
                key += self._random_letter(not_in=key)
        random.shuffle(key_list)
        key = "".join(key_list)
        print("KEY", key)
        print("MSG", msg)
        return msg
