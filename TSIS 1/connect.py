import psycopg2     # translater, for move code from python to SQL 
from config import DB_CONFIG


def get_connection():
    """Return a new psycopg2 connection using DB_CONFIG."""
    return psycopg2.connect(**DB_CONFIG)