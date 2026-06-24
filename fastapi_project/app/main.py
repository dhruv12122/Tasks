from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

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


@app.get("/")
def home():
    return {
        "message": "Smart File Vault Running"
    }


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


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

    cursor.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (
            user.name,
            user.email,
            user.password
        )
    )

    conn.commit()

    return {
        "message": "User registered successfully"
    }