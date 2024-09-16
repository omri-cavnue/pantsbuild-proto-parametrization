"""Dog Walker Service."""

import datetime as dt
import logging
import sys

from definitions.messages.human.v1 import person_pb2
from definitions.messages.animal.v1 import dog_pb2

class DogWalker():
    def __init__(self) -> None:
        self.human = person_pb2.Person()
        self.dog = dog_pb2.Dog()