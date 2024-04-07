# Modules: Modules are very simple. Just create a file and you can import into another file.
# step1: create a python package : "database_utils"
# Step2: create a python file i.e. "Readfromdb.py" in "database_utils" package.

from database_utils import Readfromdb

Readfromdb.read_from_db()
ref = Readfromdb.utilisDB()
ref.readDBMySQL()
