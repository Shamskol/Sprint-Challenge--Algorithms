'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if "th" not in word:
        return 0
    else:
        print("yes")
        word = word.replace("th", " ", 1)
        return 1 + count_th(word)
        

        


    # print(word)
        
    

print(count_th("abcthxthyzththTh"))
print(count_th("thhtthht")) 
    
