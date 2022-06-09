from typing import Iterable, Tuple


def line_iterator(content: str) -> Iterable[Tuple[int, str, int, int]]:
    end = 0
    for idx, line in enumerate(content.splitlines()):
        start = end + int(idx != 0)
        end = start + len(line)
        yield idx, line, start, end
