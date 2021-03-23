def top_3_words(text):
    '''
    given a string of text (possibly with punctuation and line-breaks), 
    returns an array of the top-3 most occurring words, 
    in descending order of the number of occurrences
    '''
    from string import ascii_letters
    scan = ''
    words = {}
    r_words = []
    
    for l in text:
        if l in ascii_letters or l == "'":
            scan = scan+l.lower()
        elif len(scan)>0:
            if scan in words:
                words[scan] += 1
                scan = ''
            else:
                words[scan] = 1
                scan = ''
    
    
    
    for index in range(2):
        maximum = max(words.values())
        for word in words:
            if words[word] == maximum:
                r_words.append(word)
                words[word] = 0
            
    
    return r_words
