def alphabetapart(state,alpha,beta,maximizing,depth,maxp,minp):
    
    if depth==0:
        return utilityOfState(state),state
    
    rowsLeft,columnsLeft=np.where(state==0)
    returnState=copy(state)
    if rowsLeft.shape[0]==0:
        return utilityOfState(state),returnState
        
    if maximizing==True:
        utility=neg_inf
        for i in range(0,rowsLeft.shape[0]):
            nextState=copy(state)
            nextState[rowsLeft[i],columnsLeft[i]]=maxp
            #print 'in max currently the Nextstate is ',nextState,'\n\n'
            Nutility,Nstate=minimax(nextState,alpha,beta,False,depth-1,maxp,minp)
            if Nutility > utility:
                utility=Nutility
                returnState=copy(nextState)
            if utility>alpha:
                alpha=utility
            if alpha >=beta :
                #print 'pruned'
                break;
        
        #print 'for max the best move is with utility ',utility,' n state ',returnState
        return utility,returnState

    else:
        utility=inf
        for i in range(0,rowsLeft.shape[0]):
            nextState=copy(state)
            nextState[rowsLeft[i],columnsLeft[i]]=minp
            #print 'in min currently the Nextstate is ',nextState,'\n\n'
            Nutility,Nstate=minimax(nextState,alpha,beta,True,depth-1,maxp,minp)
            if Nutility < utility:
                utility=Nutility
                returnState=copy(nextState)
            if utility< beta:
                beta=utility
            if alpha >=beta :
                #print 'pruned'
                break;
        return utility,returnState
