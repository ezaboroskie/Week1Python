def vowel_count(sentence):
	
    countA = 0
    countE = 0
    countI = 0
    countO = 0
    countU = 0
	
    vowelA = set("Aa")
    vowelE = set("Ee")
    vowelI = set("Ii")
    vowelU = set("Uu")
    vowelO = set("Oo")
    
    
    for index in sentence:
	    if index in vowelA:
		    countA = countA + 1
	
    print("No. of A's: ", countA)

    for index in sentence: 
        if index in vowelE:
            countE = countE + 1

    print("No. of E's: ", countE)

    for index in sentence: 
        if index in vowelI:
            countI = countI + 1

    print("No. of I's: ", countI)

    for index in sentence: 
        if index in vowelO:
            countO = countO + 1

    print("No. of O's: ", countO)

    for index in sentence: 
        if index in vowelU:
            countU = countU + 1

    print("No. of U's: ", countU)

	

sentence = input("Write a sentence: ")


vowel_count(sentence)
