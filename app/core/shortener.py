import random
import string

BASE62_CHARACTERS = string.ascii_letters + string.digits  # 62 chars: a-z, A-Z, 0-9
CODE_LENGTH = 6


def generate_short_code() -> str:
    """Generates a random Base62 short code, e.g. 'aZ3kD9'."""
    return "".join(random.choices(BASE62_CHARACTERS, k=CODE_LENGTH))
