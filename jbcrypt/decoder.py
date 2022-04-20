class Decoder:
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
            key_dict[key_list[len(key_list) - index - 1]] = key_list[index]
        msg_list = list(msg)
        for index in range(len(msg)):
            if msg_list[index] in key_dict:
                msg_list[index] = key_dict[msg_list[index]]
        msg = "".join(msg_list)
        return msg