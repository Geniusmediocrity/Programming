def find_max_substring(string: str) -> str:
    words = string.split()
    subs_set = set()
    word = words[0]
    length = len(word)
    for i in range(length):
        for j in range(i+1, length):
            subs_set.add(word[i:j+1])
                
    result = {}
    for sub in subs_set:
        for word in words:
            if sub in word:
                result[sub] = result.get(sub, 0) + 1
    
    result = (sorted(result.items(), key= lambda seq: (seq[1], len(seq[0]), seq[0]), reverse=True))[0][0]
    print(subs_set)
    return result
    
    
    
print(find_max_substring("ABACDAQ BACDAQA ACDAQAW XYZCDAQ"))
