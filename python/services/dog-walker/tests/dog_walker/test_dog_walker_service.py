import pytest
from dog_walker.service import DogWalker

def test_constructor():
    walker = DogWalker()

    assert walker is not None
