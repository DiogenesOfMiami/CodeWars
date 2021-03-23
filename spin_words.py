def spin_words(sentence):            
    
    wordList = sentence.split() # Split the sentence into a list of words    
    
    result = ''                 # Prepare final result

    wordCount = 1               # How many words in the sentence - so I can add a space or not
    
    for word in wordList:       # For each word in the list of words
        
        if len(word) >= 5:      # If the word is long enough to reverse
            word = word[::-1]   # Reverse it

        if wordCount == 1:
            result = result + word  # Then add that word to the result
        else:
            result = result + ' ' + word
        
        wordCount += 1
    

    return result      # Return the result

print(spin_words("Welcome"))
print(spin_words("Hello how might you be doing on this evening"))