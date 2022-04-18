from .decoder import Decoder
from .encoder import Encoder


def encode(msg: str, system: str = "MK") -> str:
    return Encoder().encode(msg)


def decode(msg, system="MK"):
    return Decoder().decode(msg)
