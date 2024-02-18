def UFO(n, data, octal):
    if octal:
        base = 8
    else:
        base = 16
    translated_data = []
    for signal in data:
        signal = list(map(int, list(str(signal))))
        translated_signal = 0
        for i in range(-1, -len(signal)-1, -1):
            translated_signal += signal[i] * base**(-(i+1))
        translated_data.append(translated_signal)
    return translated_data
