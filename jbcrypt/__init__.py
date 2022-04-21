from .decoder import Decoder
from .encoder import Encoder


def encode(msg: str, **options) -> str:
    return Encoder(**options).encode(msg)


def decode(msg, **options):
    return Decoder(**options).decode(msg)
