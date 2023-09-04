from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plainpassword, hashed_password):
    return pwd_context.verify(plainpassword, hashed_password)