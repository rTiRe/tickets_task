from unittest.mock import patch

import pytest

from main import (check_lucky_ticket, check_ticket_digits,
                  get_lucky_ticket_message, get_ticket_number)


def test_get_ticket_number():
    with patch('builtins.input', return_value='123'):
        assert get_ticket_number() == [0, 0, 0, 1, 2, 3]
    with patch('builtins.input', return_value='123456'):
        assert get_ticket_number() == [1, 2, 3, 4, 5, 6]
    with patch('builtins.input', return_value='abc'):
        with pytest.raises(ValueError):
            get_ticket_number()


def test_check_ticket_digits():
    check_ticket_digits([1, 2, 3, 4, 5, 6])
    with pytest.raises(TypeError):
        check_ticket_digits('123456')
    with pytest.raises(TypeError):
        check_ticket_digits([1, 2, 3, 4, 5, '6'])
    with pytest.raises(ValueError):
        check_ticket_digits([1, 2, 3, 4, 5])


def test_check_lucky_ticket():
    assert check_lucky_ticket([1, 2, 3, 4, 5, 6]) is False
    assert check_lucky_ticket([1, 2, 3, 3, 2, 1]) is True
    with pytest.raises(TypeError):
        check_lucky_ticket([1, 2, 3, 4, 5, '6'])


def test_get_lucky_ticket_message():
    assert get_lucky_ticket_message(True) == 'Yahooo! Your ticket is lucky! Congratulations!'
    assert get_lucky_ticket_message(False) == 'Hmmm, your ticket is not lucky :('
    with pytest.raises(TypeError):
        get_lucky_ticket_message('True')
