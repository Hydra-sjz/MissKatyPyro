# below code is taken from USERGE-X repo
# all credits to the respective author (dunno who wrote it will find later
# n update)


__all__ = ["get_collection"]

#from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
#from motor.motor_asyncio import AsyncIOMotorClient

from async_pymongo import AsyncClient
from pymongo import MongoClient
from Emilia import MONGO_DB_URL

_MGCLIENT: AgnosticClient = AsyncClient(MONGO_DB_URL)

_DATABASE: MongoClient = _MGCLIENT["Emilia"]


def get_collection(name: str):
    """Create or Get Collection from your database"""
    return _DATABASE[name]
