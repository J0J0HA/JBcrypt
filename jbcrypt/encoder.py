class Encoder:
    def encode(self, msg: str) -> str:
        msg_len = len(msg)
        msg_ltrs = ""
        for msg_ltr in msg:
            if not msg_ltr in msg_ltrs:
                msg_ltrs += msg_ltr
        msg_dif = len(msg_ltrs)
        if msg_dif > msg_len:
            pass
        return msg
