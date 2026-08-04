import random
import string

CHARACTERS = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
CODE_LENGTH = 6


def generate_short_code() -> str:
    """Generates a random alphanumeric short code (e.g. 'aZ3kD9')."""
    return "".join(random.choices(CHARACTERS, k=CODE_LENGTH))