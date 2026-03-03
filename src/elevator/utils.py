import csv
import io


def parse_csv(s: str) -> list[int]:
    """
    Parse in-memory CSV stream

    Args:
        s: In-memory CSV

    Returns:
        1D list of parsed values

    Raises:
        ValueError: If element in stream cannot be casted to int
    """
    stream = io.StringIO(s)
    reader = csv.reader(stream, delimiter=",")
    return [int(val) for row in reader for val in row]


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
