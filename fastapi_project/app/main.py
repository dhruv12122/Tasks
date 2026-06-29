from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from jose import JWTError
from fastapi import HTTPException, status

load_dotenv()
app = FastAPI()
security = HTTPBearer()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)

conn = sqlite3.connect(
    "smart_file_vault.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()

# Home page
@app.get("/")
def home():
    return {
        "message": "Smart File Vault Running"
    }


class UserRegister(BaseModel):
    name: str
    email: str
    password: str

# For user regestration
@app.post("/register")
def register(user: UserRegister):

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (user.email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        return {
            "message": "User already exists"
        }

    password_bytes = user.password.encode()
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    ).decode()

    cursor.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (
            user.name,
            user.email,
            hashed_password
        )
    )

    conn.commit()

    return {
        "message": "User registered successfully"
    }

# JWT
def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes= ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload["exp"] = expire

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

@app.get("/profile")
def profile(
    credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    user_id = payload["user_id"]

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id = ?
        """,
        (user_id,)
    )
    
    user = cursor.fetchone()

    if not user:
        raise HTTPException(
        status_code=404,
        detail="User not found"
        )
    else:
        return{
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }

# Authentication
class Login(BaseModel):
    email: str
    password: str

@app.post("/login")
def user_login(user: Login):
    cursor.execute(
        '''SELECT * FROM users
           WHERE email = ?''',
           (user.email,)
    )
    current_user = cursor.fetchone()

    if not current_user:
        return{
            "message": "Invalid email or password"
        }
    
    entered_password = user.password.encode()
    stored_hash = current_user[3].encode()

    if not bcrypt.checkpw(entered_password, stored_hash):
        return {
            "message": "Invalid password"
        }

    access_toekn = create_access_token(
        {
            "user_id": current_user[0],
            "email": current_user[2]
        }
    )

    return {
        "access_token": access_toekn,
        "token_type": "bearer"
    }


# To get all users
@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    results = []
    results.append(
        {
            "id": users[0],
            "name": users[1],
            "email": users[2]
        }
    )
    return results

# To get a single user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        return {
            "message": "User not found"
        }

    results = []

    for user in user:
        results.append(
            {
                "id": user[0],
                "name": user[1],
                "email": user[2]
            }
        )
    return results


class UserUpdate(BaseModel):
    name: str

# For updating name 
@app.put("/users/{user_id}")
def update_name(user_id: int, user:UserUpdate):
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )
    existing_user = cursor.fetchone()

    if not existing_user:
        return {
            "message": "User not found"
        }
    
    cursor.execute(
        '''
        UPDATE users SET name = ?
        WHERE id = ? 
        ''',
        (user.name, user_id)
    )
    conn.commit()

    return {
        "message": "User updated successfully"
    }

# For deleting user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    current_user = cursor.fetchone()

    if not current_user:
        return {
            "message": "User not found"
        }

    cursor.execute(
        '''DELETE FROM users
           WHERE id = ?''',
            (user_id,)
    )
    conn.commit()
    return {
        "message": "User deleted successfully"
    }

@app.get("/profile")
def profile(credentials: HTTPAuthorizationCredentials = Depends(security)):
     return {
        "token": credentials.credentials
    }