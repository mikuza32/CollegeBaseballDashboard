import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os 

load_dotenv()


def initialize_firebase():
    credDir = os.environ.get("FIREBASE_CREDENTIALS_PATH")
    if not credDir:
        raise Exception("FIREBASE_CREDENTIALS_PATH is not set in the dev environment")
    
    cred = credentials.Certificate(credDir)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
    return firestore.client()


def store_data(df, collection_name):
    db = initialize_firebase()
    collection_reference = db.collection(collection_name)
    for _, row in df.iterrows():
        collection_reference.add(row.to_dict())
    return f"Stored {len(df)} data in the {collection_name} collection"


if __name__ == "__main__":
    pass
