"""Programm for check user ticket number id lucky."""


def get_ticket_number() -> list[int]:
    """Return ticket number with left zeros.

    Raises:
        ValueError: if ticket nomber is not integer.

    Returns:
        list[int]: list with separated ticket digits.
    """
    ticket_number = input('Enter ticket number: ').zfill(6)
    try:
        return list(map(int, ticket_number))
    except ValueError:
        raise ValueError('ticket_number must be a int')


def check_ticket_digits(ticket_digits: list[int] | tuple[int]) -> None:
    """Validate ticket number.

    Args:
        ticket_digits (list[int] | tuple[int]): list with separated \
            ticket digits.

    Raises:
        TypeError: if ticket_digits not a list or not a list of integers.
        ValueError: if ticket_digits contain less than 6 digits.
    """
    if not isinstance(ticket_digits, (list, tuple)):
        raise TypeError('ticket_digits must be a list')
    for digit in ticket_digits:
        if not isinstance(digit, int):
            raise TypeError('ticket_digits must be a list of integers')
    if len(ticket_digits) < 6:
        raise ValueError('ticket_digits must contain 6 digits')


def check_lucky_ticket(ticket_digits: list[int] | tuple[int]) -> bool:
    """Check if ticket is a lucky.

    Args:
        ticket_digits (list[int] | tuple[int]): list with separated \
            ticket digits.

    Returns:
        bool: is ticket a lucky.
    """
    check_ticket_digits(ticket_digits)
    left_part = ticket_digits[:3]
    right_part = ticket_digits[-3:]
    return sum(left_part) == sum(right_part)


def get_lucky_ticket_message(is_lucky_ticket: bool) -> str:
    """Get the message of a lucky or not lucky ticket.

    Args:
        is_lucky_ticket (bool): is ticket a lucky.

    Raises:
        TypeError: if is_ticket_lucky not boolean.

    Returns:
        str: message for ticket.
    """
    if not isinstance(is_lucky_ticket, bool):
        raise TypeError('is_lucky_ticket must be a bool')
    if is_lucky_ticket:
        return 'Yahooo! Your ticket is lucky! Congratulations!'
    return 'Hmmm, your ticket is not lucky :('


if __name__ == '__main__':
    ticket_number = get_ticket_number()
    is_lucky_ticket = check_lucky_ticket(ticket_number)
    message = get_lucky_ticket_message(is_lucky_ticket)
    print(message)
