import regex as re


def HexToRgb(hx, hsl=False):
    """Converts a HEX code into RGB or HSL.

    Args:
        hx (str): Takes both short as well as long HEX codes.
        hsl (bool): Converts the given HEX code into HSL value if True.
    Return:
        Tuple of length 3 consisting of either int or float values.
    """
    # replaces # so we dont need to worry
    hx = str(hx).replace("#", "")
    # regex magic
    if re.compile(r"[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$").match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(
                int(hx[i] * 2, 16) / div if div else int(hx[i] * 2, 16)
                for i in (1, 2, 3)
            )
        return tuple(
            int(hx[i : i + 2], 16) / div if div else int(hx[i : i + 2], 16)
            for i in (1, 3, 5)
        )
    raise ValueError(f'"{hx}" is not a valid HEX code.')
