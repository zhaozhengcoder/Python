import copy

def showid(show_list):
    print (" ")
    print ("list id is : ",id(show_list))
    for ele in show_list:
        print (ele," --> ",id(ele))


if __name__=="__main__":
    xiaoming = ["will",28,["python","c#","js"]]
    
    #test1
    lilei = xiaoming 
    lilei[1]="edit!"
    lilei[-1].append('edit too !')

    #test2
    #lilei = xiaoming[:]
    #lilei[1]="edit!"
    #lilei[-1].append('edit too !')
    
    #test3
    #lilei = copy.copy(xiaoming)
    #lilei[1]="edit!"
    #lilei[-1].append('edit too !')

    #test4
    #lilei = copy.deepcopy(xiaoming)
    #lilei[1]="edit!"
    #lilei[-1].append('edit too !')

    showid(xiaoming)
    showid(lilei)

