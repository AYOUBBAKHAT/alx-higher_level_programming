#!/usr/bin/python3
"""contains the class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
