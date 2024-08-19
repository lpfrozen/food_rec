import os
import certifi
import motor.motor_asyncio
import pandas as pd
from pymongo.errors import ServerSelectionTimeoutError
from bson import ObjectId
from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# show all columns
pd.set_option('display.max_columns', None)


print("Starting server...")

# load environment variables
from dotenv import load_dotenv

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"], tlsCAFile=certifi.where())
db = client.food_restaturent


async def fetch_users():
    try:
        # Access the users collection
        users_collection = db.users

        # Fetch all documents from the users collection
        users_cursor = users_collection.find({})

        # Convert cursor to list and then to DataFrame
        users_list = await users_cursor.to_list(length=None)
        users_df = pd.DataFrame(users_list)

        print("Users DataFrame:")
        print(users_df)

    except Exception as e:
        print("An error occurred while retrieving users:", e)

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstName: str
    lastName: str
    userName: str
    email: str
    dateOfBirth: str
    mobileNumber: str
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "userID": "60f4d5c5b5f0f0e5e8b2b5c9",
                "firstName": "John",
                "lastName": "Doe",
                "userName": "JohnDoe",
                "email": "johndoe@example.com",
                "dateOfBirth": "1990-01-01",
                "mobileNumber": "0712345678",
                "password": "password"
            }
        }



async def list_users():
    users = await db["users"].find().to_list(1000)
    print(users)
    return users

# To run this, you'll need to run the FastAPI app with an event loop
import asyncio

asyncio.run(list_users())