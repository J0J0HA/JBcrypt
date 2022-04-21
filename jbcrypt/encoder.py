import random
import string


class Encoder:
    opt_msg_ext_rnd_ltr = 0
    opt_key_ext_rnd_ltr = 0
    opt_rnd_alw_ltrs = string.ascii_letters + string.digits

    def __init__(self, **options):
        for option in options.items():
            if option[0] in ["rxl", "random_extra_letters", "brxl", "both_rxl", "both_random_extra_letters"]:
                self.opt_key_ext_rnd_ltr = option[1]
                self.opt_msg_ext_rnd_ltr = option[1]
            if option[0] in ["msg_rxl", "msg_random_extra_letters", "mrxl"]:
                self.opt_msg_ext_rnd_ltr = option[1]
            if option[0] in ["key_rxl", "key_random_extra_letters", "krxl"]:
                self.opt_key_ext_rnd_ltr = option[1]

    def _random_letter(self, not_in=""):
        usable = ""
        for letter in self.opt_rnd_alw_ltrs:
            if letter not in not_in:
                usable += letter
        try:
            result = random.choice(usable)
        except IndexError:
            result = ""
        return result

    def encode(self, msg: str) -> str:
        msg_ltrs = ""
        for msg_ltr in msg:
            if msg_ltr not in msg_ltrs:
                msg_ltrs += msg_ltr
        key = msg_ltrs
        for index in range(len(msg) - len(key)):
            key += self._random_letter(not_in=key)
        for index in range(self.opt_key_ext_rnd_ltr):
            key += self._random_letter(not_in=key)
        key_list = list(key)
        random.shuffle(key_list)
        key_dict = {}
        for index in range(len(key_list)):
            key_dict[key_list[index]] = key_list[len(key_list) - index - 1]
        msg_list = []
        for letter in msg:
            msg_list.append(key_dict[letter])
        for index in range(self.opt_msg_ext_rnd_ltr):
            msg_list.insert(random.randint(0, len(msg_list) - 1), self._random_letter(not_in=msg + key))
        rnd_msg = "".join(msg_list)
        result = ""
        key_pos = False
        real_index = 0
        for index in range(len(key) + len(rnd_msg)):
            if key_pos:
                result += list(key_dict.keys())[real_index]
                real_index += 1
            else:
                result += rnd_msg[real_index]
            key_pos = not key_pos
        return result
