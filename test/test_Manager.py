import pytest
from dcache.Manager import Manager

def test_init():
    mgr = Manager() 
    
def test_connect():  # Will not work in the DB is not up!!
    mgr = Manager()
    mgr.connect()

def test_insert():
    mgr = Manager()
    mgr.connect()
    mgr.insert({"_id": "lala"})

def test_find():
    mgr = Manager()
    mgr.connect()
    mgr.find({"_id": "lala"})