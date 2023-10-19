import bcrypt


def hash_password(password: str) -> (str, str):
    """
    Hashes a password and returns the salt and hashed password.
    :param password: The password to hash.
    :return: A tuple containing the salt and hashed password.

    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return salt.decode("utf-8"), hashed.decode("utf-8")
