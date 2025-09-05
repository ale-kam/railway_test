"""
Redis handler
"""
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

pprint(dict(os.environ.items()))