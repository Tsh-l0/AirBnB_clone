#!/usr/bin/python3
"""
Initializes the storage engine and reloads the storage objects
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
