import pytest
from burrowsWheeler import encode, decode

def test_encode():
    assert(encode("bananabar") == ("nnbbraaaa", 4))
    assert(encode("Humble Bundle") == ("e emnllbduuHB", 2))
    assert(encode("Mellow Yellow") == ("ww MYeelllloo", 1))
    #Test no string
    assert(encode("")[0] == "")

def test_decode():
    assert(decode("nnbbraaaa", 4) == "bananabar")
    assert(decode("e emnllbduuHB", 2) == "Humble Bundle")
    assert(decode("ww MYeelllloo", 1) == "Mellow Yellow")


