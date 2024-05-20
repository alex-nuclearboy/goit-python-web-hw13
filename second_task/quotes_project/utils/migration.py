import os
import sys
import django

# Append parent directory to sys.path to access Django project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_project.settings')
django.setup()

import configparser
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from quotesapp.models import Author, Tag, Quote

# Read MongoDB connection configuration from config.ini file
config = configparser.ConfigParser()
config.read('utils/config.ini')

# MongoDB connection parameters
mongodb_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
mongodb_domain = config.get('DB', 'domain')
db_name = config.get('DB', 'db_name')

# MongoDB connection URI
URI = (
    f'mongodb+srv://{mongodb_user}:{mongodb_pass}'
    f'@{mongodb_domain}/?retryWrites=true&'
    'w=majority&appName=Cluster0'
)


def get_mongodb():
    """
    Establish connection to the MongoDB database.

    Returns:
        db: A MongoDB database instance.

    Raises:
        ConnectionFailure: If MongoDB cannot be reached.
        PyMongoError: If an error occurs in the connection process.
    """
    try:
        client = MongoClient(URI)
        db = client[db_name]
        # Attempt to retrieve the server info to confirm connection
        client.server_info()
        print("Connected to MongoDB")
        return db
    except ConnectionFailure:
        print("Failed to connect to MongoDB: Connection failed.")
        raise
    except PyMongoError as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        raise

def import_authors(db):
    """Import athors from MongoDB into Postgres.

    Arg:
        db: MongoDB database instance.
    """
    try:
        authors = db.authors.find()
        for author in authors:
            Author.objects.get_or_create(
                fullname=author['fullname'],
                birth_date=author['born_date'],
                birth_location=author['born_location'],
                description=author['description']
            )
        print("Authors imported successfully")
    except Exception as e:
        print(f"An error occurred while importing authors: {e}")


def import_quotes(db):
    """
    Import quotes from MongoDB into Postgres.

    Arg:
        db: MongoDB database instance.
    """
    try:
        quotes = db.quotes.find()
        for quote in quotes:
            # Import tags associated with each quote
            tags = []
            for tag in quote['tags']:
                t, *_ = Tag.objects.get_or_create(name=tag)
                tags.append(t)
                
            # Check if quote already exists
            exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

            # Create quote if it does not exist
            if not exist_quote:
                author = db.authors.find_one({'_id': quote['author']})
                a = Author.objects.get(fullname=author['fullname'])
                q = Quote.objects.create(
                    quote=quote['quote'],
                    author=a,
                )
                # Associate tags with the quote
                for tag in tags:
                    q.tags.add(tag)
        print("Quotes imported successfully")
    except Exception as e:
        print(f"An error occurred while importing quotes: {e}")


if __name__ == "__main__":
    # Establish MongoDB connection
    db = get_mongodb()

    # Import authors and quotes
    import_authors(db)
    import_quotes(db)

    print("Migration completed successfully")
