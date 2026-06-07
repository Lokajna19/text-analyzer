while True:
    text=input("Enter or paste your text\n")
    if len(text) > 1:
        words = text.split()
    else:
        words=[]
    words_length = len(words)
    characters_length = len(text)
    fullstops = text.count('.')
    print("Here is your detailed Analysis")
    print(f"Your text has {words_length} words in it.")
    print(f"Your text has {characters_length} characters in it.")
    if fullstops > 1:
        print(f"Your text has {fullstops} fullstops\n")
    elif fullstops == 1:
        print("Your text has only one fullstop\n")
    else:
        print("Your text has no fullstops\n")
    
    
    