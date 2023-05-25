from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, "paz")

    assert encrypt_message("paz", 2) == ("z_ap")
    assert encrypt_message("paz", 3) == ("zap")
