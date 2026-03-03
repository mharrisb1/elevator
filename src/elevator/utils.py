def validate_floor(n: int) -> int:
    """
    Validate floor number

    Args:
        n: Floor number

    Returns:
        Passed through floor number

    Raises:
        ValueError: If floor is not a positive integer greater than zero
    """
    if n <= 0:
        msg = "Floor number must be greater than zero"
        raise ValueError(msg)

    return n


def parse_csv(s: str) -> list[int]:
    """
    Parse in-memory CSV stream

    Args:
        s: In-memory CSV

    Returns:
        1D list of parsed values

    Raises:
        ValueError: If element in stream cannot be casted to int
        ValueError: If element in stream is not a valid floor number (greater than zero)
    """
    return [validate_floor(int(floor)) for floor in s.split(",")]
