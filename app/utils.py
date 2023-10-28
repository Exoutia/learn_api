import bcrypt


def hash_password(password: str) -> (str, str):
    """
    Hashes a password and returns the salt and hashed password.
    :param password: The password to hash.
    :return: A tuple containing the salt and hashed password.

    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hash: str) -> bool:
    """
    Verifies a password against a hash.
    :param password: The password to verify.
    :param hash: The hash to verify against.
    :return: True if the password matches the hash, False otherwise.

    """
    return bcrypt.checkpw(password.encode("utf-8"), hash.encode("utf-8"))
