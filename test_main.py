"""Tests for main code."""

from unittest.mock import patch

import pytest

from main import (check_lucky_ticket, check_ticket_digits,
                  get_lucky_ticket_message, get_ticket_number)


def test_get_ticket_number():
    """Test get_ticket_number function.

    Tests:
        - Correctly handles a short ticket number by padding with zeros.
        - Correctly handles a full-length ticket number.
        - Raises ValueError when input is not a number.
    """
    with patch('builtins.input', return_value='123'):
        assert get_ticket_number() == [0, 0, 0, 1, 2, 3]
    with patch('builtins.input', return_value='123456'):
        assert get_ticket_number() == [1, 2, 3, 4, 5, 6]
    with patch('builtins.input', return_value='abc'):
        with pytest.raises(ValueError):
            get_ticket_number()


def test_check_ticket_digits():
    """Test check_ticket_digits function.

    Tests:
        - Correctly handles a valid ticket number.
        - Raises TypeError when input is not a list or tuple.
        - Raises TypeError when input contains non-integer values.
        - Raises ValueError when input contains fewer than 6 digits.
    """
    check_ticket_digits([1, 2, 3, 4, 5, 6])
    with pytest.raises(TypeError):
        check_ticket_digits('123456')
    with pytest.raises(TypeError):
        check_ticket_digits([1, 2, 3, 4, 5, '6'])
    with pytest.raises(ValueError):
        check_ticket_digits([1, 2, 3, 4, 5])


def test_check_lucky_ticket():
    """Test check_lucky_ticket function.

    Tests:
        - Correctly identifies a non-lucky ticket.
        - Correctly identifies a lucky ticket.
        - Raises TypeError when input contains non-integer values.
    """
    assert check_lucky_ticket([1, 2, 3, 4, 5, 6]) is False
    assert check_lucky_ticket([1, 2, 3, 3, 2, 1]) is True
    with pytest.raises(TypeError):
        check_lucky_ticket([1, 2, 3, 4, 5, '6'])


def test_get_lucky_ticket_message():
    """Test get_lucky_ticket_message function.

    Tests:
        - Returns the correct message for a lucky ticket.
        - Returns the correct message for a non-lucky ticket.
        - Raises TypeError when input is not a boolean.
    """
    assert get_lucky_ticket_message(True) == 'Yahooo! Your ticket is lucky! Congratulations!'
    assert get_lucky_ticket_message(False) == 'Hmmm, your ticket is not lucky :('
    with pytest.raises(TypeError):
        get_lucky_ticket_message('True')
