#!/usr/bin/python3
"""
Module for initializing storage system.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
