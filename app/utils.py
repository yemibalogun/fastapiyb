from passlib.context import CryptContext
# passlib is used to hash passwords

#this is telling passlib what hashing algorithm is used. In this case we're using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function to hash the user's password
def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)