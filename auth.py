


from jose import jwt , JWTError
from fastapi.security import OAuth2PasswordBearer
from datetime import timezone , datetime , timedelta
from fastapi import HTTPException , Depends

SECRET_KEY = "mysecret"
ALGORITH = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

auth_response = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data : dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})

    return jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITH)


def verify_token(token : str = Depends(auth_response)):
    try :
        payload = jwt.decode(token ,SECRET_KEY ,algorithms=ALGORITH )


    except JWTError :
       raise HTTPException(
            status_code=404,
            detail="error not found"
        )

    return payload

