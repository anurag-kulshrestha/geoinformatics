def extract(a): #Q2
    d={}
    for i in a:
        d[i]=0
    return d.keys()

def trace(a):
    count,result=0,0
    for i in a:
        result+=i[count]
        count+=1
    return result

def freq(a):
    d={}
    for i in a:
        if(i not in d.keys()):
            d[i]=a.count(i)
    return d
#def corr(a):
    
            

if __name__=='__main__':
    #print(extract((2,3,6,2,5,4,1,2,3,6,5,2,6,3,1,4,5,2,3,6,2,1)))
    #print(trace([[1,2,3],[4,5,6],[7,8,9]]))
    print(freq([2,3,6,2,3,2,3,6,2,5,3,2,6,2,3,6,5]))