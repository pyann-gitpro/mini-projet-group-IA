# tests/test_zorglangue.py

import pytest
from app.components.zorglangue import inverser_mot, inverser_phrase

def test_inverser_mot():
    assert inverser_mot("Bonjour") == "ruojnoB"
    assert inverser_mot("Zorglub") == "bulgroZ"
    assert inverser_mot("!") == "!"
    assert inverser_mot("Salut!") == "tulaS!"

def test_inverser_phrase():
    assert inverser_phrase("Bonjour Zorglub !") == "ruojnoB bulgroZ !"
    assert inverser_phrase("Ceci est un test.") == "iceC tse un tset."
