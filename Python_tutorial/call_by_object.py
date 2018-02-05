import copy

def showid(show_list):
    print (" ")
    print ("list id is : ",id(show_list))
    for ele in show_list:
        print (ele," --> ",id(ele))


if __name__=="__main__":
    will = ["will",28,["python","c#","js"]]
    
    #test1
    #wilber = will 
    #will[1]="hahaha"
    #will[-1].append('gagaga')

    #test2
    wilber = will[:]
    will[1]="hahaha"
    will[-1].append('gagaga')
    
    #test3
    #wilber = copy.copy(will)

    #test4
    #wilber  = copy.deepcopy(will)

    showid(will)
    showid(wilber)

