def WordSearch(length, s, subs):
    parts = []

    while len(s) > length:
        short_str = s[:length].strip()
        if s[len(short_str)] != ' ':
            piece_of_string = short_str.rsplit(maxsplit=1)[0]
        else:
            piece_of_string = short_str
        s = s.replace(piece_of_string, '', 1).strip()
        parts.append(piece_of_string)
    parts.append(s)

    result = []
    for part in parts:
        if subs not in part:
            result.append(0)
        else:
            if part.find(subs) == 0:
                result.append(1)
            else:
                result.append(0)
    return result
