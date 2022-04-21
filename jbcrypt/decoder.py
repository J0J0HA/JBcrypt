class Decoder:
    def __init__(self, **options):
        for option in options.items():
            setattr(self, option[0], option[1])

    def decode(self, encrypted_msg: str):
        key = ""
        msg = ""
        key_pos = False
        for ltr in encrypted_msg:
            if key_pos:
                key += ltr
            else:
                msg += ltr
            key_pos = not key_pos
        key_list = list(key)
        key_dict = {}
        for index in range(len(key_list)):
            key_dict[key_list[index]] = key_list[len(key_list) - index - 1]
        msg_list = list(msg)
        result = []
        for letter in msg_list:
            if letter in key_dict.keys():
                result.append(key_dict[letter])
        return "".join(result)
