
class connect4:
    width = 0
    height = 0
    board = []
    def __init__(self,boardwidth,boardheight):
        if( boardheight >= 4 and boardwidth>=4 ):
            self.width = boardwidth
            self.height = boardheight
            self.board = chess[boardheight][boardwidth]
            for i in range(0,boardheight):
                for j in range(0,boardwidth):
                    chess[i][j] = chess(0)
        else:
            print("size of the board should be greater than 4 x 4")
     
    def put_chess(self, state, col):
        pos = 0
        while pos < self.height:
            if chess[pos][col].get_state !=0:
                if pos !=0:
                    chess[pos-1][col].set_state(state)
                    break
                else:
                    print("select a new location, the col is full")
            else:
                pos += 1
        
        pos += 1

        for i in range(1,4):
            if pos+i > 0 and pos+i < self.height:
                if chess[pos+i][col].get_state ==state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break
        for i in range(1,4):
            if col+i > 0 and col+i < self.width:
                if chess[pos][col+i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break
        for i in range(1,4):
            if col-i > 0 and col-i < self.width:
                if chess[pos][col-i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break

        for i in range(1,4):
            if col-i > 0 and col-i < self.width and pos+i > 0 and pos+i < self.height:
                if chess[pos+i][col-i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break

        for i in range(1,4):
            if col+i > 0 and col+i < self.width and pos+i > 0 and pos+i < self.height:
                if chess[pos+i][col+i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break

        for i in range(1,4):
            if col+i > 0 and col+i < self.width and pos-i > 0 and pos-i < self.height:
                if chess[pos-i][col+i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break

        for i in range(1,4):
            if col-i > 0 and col-i < self.width and pos-i > 0 and pos-i < self.height:
                if chess[pos-i][col-i].get_state == state:
                    if i == 3 :
                        return [True,state]
                    continue
                else:
                    break
        

        return [False,state]
    

class chess:
    state = 0
    
    def __init__(self,state):
        self.state=state

    def get_state(self):
        return self.state

    def set_state(self,state):
        if state == 0 or state == 1 or state ==2:
            self.state = state
        else:
            print("state should be 0, 1, 2. which 0 for no chess, 1 for black, 2 for white")
    