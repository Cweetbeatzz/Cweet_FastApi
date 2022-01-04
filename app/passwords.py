from passlib.context import CryptContext

##################################################################


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

##################################################################


def hash_password(password: str):
    result = password_context.hash(password)
    return result


def compare_passwords(plain_password1, hash_password2):
    result = password_context.verify(plain_password1, hash_password2)
    return result
