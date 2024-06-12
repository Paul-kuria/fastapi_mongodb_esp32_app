#!/usr/bin/env python

import os

from dotenv import load_dotenv

load_dotenv()

# find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class
    """

    # Settings applicable to all environmennts
    MONGO_DB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGO_DB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGO_DB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")

    db_url = f"mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}/{MONGODB_DB}?retryWrites=true&w=majority"
    MONGO_URI = db_url


class DevelopmentConfig(Config):
    DEBUG = True
