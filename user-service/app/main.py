from fastapi import FastAPI, HTTPException
from app.database import create_user_db, update_user_db, delete_user_db
from app.kafka_producer import publish_event

app = FastAPI()

@app.post("/users")
async def create_user(user: dict):
    create_user_db(user)
    publish_event("user-events", {"action": "create", "user": user})
    return {"status": "User created"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: dict):
    update_user_db(user_id, user)
    publish_event("user-events", {"action": "update", "user_id": user_id, "user": user})
    return {"status": "User updated"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    delete_user_db(user_id)
    publish_event("user-events", {"action": "delete", "user_id": user_id})
    return {"status": "User deleted"}
