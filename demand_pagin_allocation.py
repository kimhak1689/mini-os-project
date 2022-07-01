class DemandPaging:
    def __init__(self,sequence_input,page_frame):
        super().__init__()
        self._page_frame=page_frame
        self._sequence_input=sequence_input
        self._page_frame_list=list()
        self._page_interrupt = 0
        self._timesnapshot = 0
    '''
    setter and getter 
    '''
    def set_page_frame_list_to_empty_list(self):
        for i in range(0,self._page_frame):
            self._page_frame_list.append("")

    def get_page_frame_list(self):
        return self._page_frame_list

    def set_seq_to_page_frame_list(self,i,seq):
        self._page_frame_list[i]=seq

    def set_page_frame(self,page_frame):
        self._page_frame = page_frame

    def set_sequence_input(self,sequence_input):
        self._sequence_input= sequence_input

    def get_sequence_input(self):
        return self._sequence_input

    def set_page_interrupt(self,page_interrupt):
        self._page_interrupt = page_interrupt

    def get_page_interrupt(self):
        return self._page_interrupt
    
    def set_timesnapshot(self,timesnapshot):
        self._timesnapshot = timesnapshot
    
    def get_timesnapshot(self):
        return self._timesnapshot


    '''
    Find FIFO
    '''
    def find_fifo(self):
        '''
        Technical to finalize the input and output by ref exercise so:
        -Use loop to set empty array that we get like how many page_frame
        -set count list to zero (I am not good at math or something . I think this is the best way tracking the element that I want to set or make them like fifo)
        -Use loop in sequence for example we have alphabet or whatever
        -Use another loop check if in that list of page frame have or not by using count
        -if not just set symbol to page frame list from 0 -> lastindex
        -check if it is last index so make it -1 cus there outside if statement like +1 and they will return to origin as 0
        -so It looks like fifo but just weird way
        '''
        #set list to empty
        self.set_page_frame_list_to_empty_list()
        #tracking with count_list
        count_list = 0
        for i in self.get_sequence_input():
            count=0
            for j in range(0,len(self.get_page_frame_list())):
                if(self.get_page_frame_list()[j]==i):
                    count=1
            if(count==0):
                self.set_seq_to_page_frame_list(count_list,i) #we set symbol to pageframe_list and count interrupt
                #if it equal to last index so just set count_list to -1 cus there is count_list+=1 when next update we get from 0
                if(count_list==len(self.get_page_frame_list())-1):
                    count_list=-1
                count_list+=1
                self.set_page_interrupt(self.get_page_interrupt()+1)
            else:
                #set count to 0 to check again is there any the same symbol in page frame
                count =0
            #show seq change as row not column I guess
            print(self.get_page_frame_list())
            self.set_timesnapshot(self.get_timesnapshot()+1)
        print("FIFO or First in First out")
        print("Page Interrupt:",self.get_page_interrupt())
        print("Timesnapshot:",self.get_timesnapshot())
        _failure = float(self.get_page_interrupt()/self.get_timesnapshot())
        print("failure: %.2f"%(_failure))
        print("Success: %.2f"%(1-_failure))

    def find_least_recently_used(self):
        '''
        Find LRU first just using more tracking index to make sure like go up and go down(decrease or increase) or constant element to change symbol in page_frame
        -tracking used for if like they find the symbol that has in page_frame list so they just modify the order of LRU
        Like in lru if after change last element then if there is the same symbol in the next and we find another next is no symbol so we can use the same last element and change
        symbol,but if u see tracking change to 1 or increase so we assume that we have to go up or down 
        - and we set go up to true for the first time so it will descrease element to change the value
        for example we have 3 page _frame
        we have a b c in list already and already change c to d
        [a,b,c]
        so result [a.b,d] and then next there no f so need to change again 
        -so tracking start value 1 and set go up true so it start decrease and change from last index to lastindex-1
        result [a,f,d]
        -So that is how I finalize
        -If index reach to 0 so I just set go up false and it will increase or go down and it increases until last index but if tracking =1 it will still the same index and change that part
        example [a,b,c]
                [a,b,d]
                [a,b,d] tracking 1
                [a,b,f] still the same index and change that part
                one more example
                [a,b,c]
                [a,b,d]
                [a,f,d]
                [a,f,d] tracking 1
                [a,c,d] still the same index and just change that part
        -one more just like above count the page interrupt and find the failure and success
        '''
        self.set_page_frame_list_to_empty_list()
        count_list=0  
        tracking=0
        another_count_list=0
        go_up=True
        for i in self.get_sequence_input():
            count=0
            for j in range(0,len(self.get_page_frame_list())):
                if(self.get_page_frame_list()[j]==i):
                    count=1
                    tracking+=1
            if(count==0):
                if(count_list<len(self.get_page_frame_list())-1):
                    self.set_seq_to_page_frame_list(count_list,i)
                    count_list+=1
                elif(count_list==len(self.get_page_frame_list())-1):
                    another_count_list = count_list
                    self.set_seq_to_page_frame_list(count_list,i)
                    count_list+=1
                else:
                    if(tracking!=0):
                        tracking=0
                        self.set_seq_to_page_frame_list(another_count_list,i)
                    else:
                        if(go_up):
                            another_count_list-=1
                            self.set_seq_to_page_frame_list(another_count_list,i)
                            if(another_count_list==0):
                                go_up=False
                        else:
                            another_count_list+=1
                            self.set_seq_to_page_frame_list(another_count_list,i)
                            if(another_count_list==len(self.get_page_frame_list())-1):
                                go_up=True
                self.set_page_interrupt(self.get_page_interrupt()+1)
            else:
                count=0
            print(self.get_page_frame_list())
            self.set_timesnapshot(self.get_timesnapshot()+1)
        print("LRU or Least recently used")
        print("Page Interrupt",self.get_page_interrupt())
        print("Timesnapshot:",self.get_timesnapshot())
        _failure = float(self.get_page_interrupt()/self.get_timesnapshot())
        print("failure: %.2f"%(_failure))
        print("Success rate: %.2f"%(1-_failure))

                
if __name__ == "__main__":
    while(True):
        print("1.Find FIFO")
        print('2.Find LRU')
        print('3.Exit')
        choice = int(input("Input your choice:"))
        if(choice==1 or choice==2):
            page_frame = int(input("How many page frame?:")) #3 page frame
            sequence_input = list(input("Input sequence:")) #Example ababfdfcgfgbde ABACABDBACD
            if(choice==1):
                Fifo = DemandPaging(sequence_input,page_frame)
                Fifo.find_fifo()
            else:
                Lru = DemandPaging(sequence_input,page_frame)
                Lru.find_least_recently_used()
        elif(choice==3):
            print("Bye bye")
            break
        else:
            print("Wrong operator")

        