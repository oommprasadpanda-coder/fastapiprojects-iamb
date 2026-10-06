# from jose import jwt , JWTError
# from datetime import timedelta , timezone , datetime 
# from fastapi import HTTPException , Depends 
# from fastapi.security import OAuth2PasswordBearer

from jose import jwt , JWTError 
from datetime import timedelta , timezone , datetime 
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI , Depends , HTTPException 

SECRET_KEY = "mysecret"
ALGORITH = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30 

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data : dict):

    to_encode = data.copy()


    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})


    return jwt.encode(to_encode , SECRET_KEY ,algorithm=ALGORITH )

def verify_token(token : str = Depends(oauth2_schema)):
    try: 
        payload = jwt.decode(token , SECRET_KEY ,algorithms=ALGORITH )
    except JWTError:
        HTTPException(
            status_code=404,
            detail="payload not found"
        )

    return payload






# SECRET_KEY = "mysecret"
# ALGORITH =  "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# def create_token(data: dict):
#     to_encode = data.copy()

#     expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

#     to_encode.update({"exp"  : expire})

#     return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITH)

# 


