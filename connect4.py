
class connect4:
    width = 0
    height = 0
    board = []
    def __init__(self,boardwidth,boardheight):
        self.width = boardwidth
        self.height = boardheight
        self.board = chess[boardheight][boardwidth]
        for i in range(0,boardheight):
            for j in range(0,boardwidth):
                chess[i][j] = chess(0)
    
    def check_connect_four(self):
        pass

    def put_chess(self, state, col):
        pos = 0
        while pos < self.height:
            if chess[col][pos].get_state !=0:
                chess[col][pos-1].set_state(state)
            else:
                pos += 1

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
    