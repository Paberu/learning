def BiggerGreater(word):
    output = ''
    if word == max(word)*len(word):
        return ''

    for i in range(len(word)-1, 1, -1):
        if word[i] > word[i-1]:
            output = word[:i-1] + word[i] + word[i-1]
            return output

    the_letter = max(word)
    for curr_letter in word:
        if curr_letter > word[0] and curr_letter < the_letter:
            the_letter = curr_letter

    temp_word = sorted(word)
    temp_word.remove(the_letter)
    output = the_letter + ''.join(temp_word)

    if output <= word:
        return ''
    else:
        return output
