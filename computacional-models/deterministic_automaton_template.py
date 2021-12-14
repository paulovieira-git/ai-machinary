final_states=[3]                                    # < ---------
print("introduza um valor (-1 para terminar): ")
word = input()
state=1 # estado inicial
while(word!="-1"):
    counter=-1 # contador
    state=1
    while(counter<len(word)-1):
        counter=counter+1
        match state:
            case 1:                                 
                if(word[counter]=="a"):
                    state=1
                if (word[counter] == "b"):
                    state=2
                if (word[counter] != "a" and word[counter] != "b"): # quando nao occorem os anteriores
                    state=4
            case 2:
                if (word[counter] == "a"):
                    state = 3
                if (word[counter] != "a"):
                    state=4
            case 3:
                if (word[counter] == "b"):
                    state = 3
                if (word[counter] != "b"):
                    state = 4
            case 4:
                    state=4                      
    if(counter==len(word)-1 and state in final_states):
        print("palavra aceite,",word)
    else:
        print("palavra nao aceite,",word)

    print("********************")
    print("introduza um valor (-1 para terminar): ")
    word = input()
state=1  #initial state
if(word=="-1" and state in final_states):
    print("palavra vazia aceite")
else:
    print("palavra vazia não aceite")
