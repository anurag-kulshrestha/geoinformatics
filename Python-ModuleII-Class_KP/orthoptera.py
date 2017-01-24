import assignment_p4
#grasshopper
#a=open('orthoptera.txt', 'r')

def count_column(index):
    a=open('orthoptera.txt', 'r')
    count=0
    a.readline()
    readTxt=a.readlines()
    for i in readTxt:
        indi=i[-2].split(';')
        if(indi[index]!=''):
            count+=1
    a.close()
    return count

def column_List(index):
    a=open('orthoptera.txt', 'r')
    a.readline()
    readTxt=a.readlines()
    family=[]
    for i in readTxt:
        indi=i[:-2].split(';')
        if (indi[index]!=''):
            family.append(indi[index])
    a.close()
    return family

def count_Unique(index):
    List=column_List(index)
    d=assignment_p4.freq(List)
    return len(d)



def high_freq(index):
    List=column_List(index)
    d=assignment_p4.freq(List)
    max_freq=max_value_dict(d)
    return max_freq

def DICT(index_k,index_v):
    a=open('orthoptera.txt', 'r')
    a.readline()
    readTxt=a.readlines()
    d={}
    temp=0
    for i in readTxt:
        indi=i.split(';')
        if(indi[index_k]!=''):
            temp+=1
            if(indi[index_k] not in d.keys()):
                d[indi[index_k]]=indi[index_v]
    a.close()
    return d

def max_value_dict(d):
    max_freq=[]
    max_value=max(d.values())
    for k,v in d.iteritems():
        if(v==max_value):
            max_freq.append(k)
    max_freq.append(max_value)
    return max_freq

def count_without_sub():
    #a=open('orthoptera.txt', 'r')
    readTxt=a.readlines()
    for i in readTxt:
        indi=i.split(';')

def author_Count(auth_name):
    count=0
    auth_List=[]
    count_with_others=0
    auth=column_List(6)
    for i in auth:
        auth_List=[]
        spec=i.strip('()').split(',')
        for j in spec:
            auth_List+=j.strip().split('&')
        new_auth_list=stripList(auth_List)
        if (auth_name in new_auth_list):
            count+=1
            if(len(auth_List)>2):
                count_with_others+=1
    return([count,count_with_others])

def stripList(List):
    result=[]
    for i in List:
        result.append(i.strip())
    return result
    

if __name__=='__main__':
    #print(count_Unique(5)) #Q5
    #print(column_List(5)) #Q1
    #print(high_freq(0))#Q4
    '''Q6
    sub_spec_genus=DICT(5,2)
    d1=assignment_p4.freq(sub_spec_genus.values())
    print(max_value_dict(d1))
    '''
    #Q7#print(author_Count('La Greca'))
    