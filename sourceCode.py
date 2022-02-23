import numpy as np
import string
file=open('input.txt','r')
keywords=[i for x in [x.split() for x in open("keywords.txt","r").readlines()] for i in x]
operator=[i for x in [x.split() for x in open("operators.txt","r").readlines()] for i in x]
saperator=[i for x in [x.split() for x in open("saperator.txt","r").readlines()] for i in x]
data=[' '.join(i.strip().split()) for i in file.readlines()]
sp=open('saperator.txt','r')
s=set(sp.readlines()[0].split(' '))
d=[];pre=0;check=False;cS=False
for i,j in enumerate(data):
    data[i]=data[i]+" "
for p,v in enumerate(data):
    for p1,v1 in enumerate(v):
        if check==True:
            check=False
            continue
        if v1=='#':
            d.append(v)
            break
        if v1==' ':
            d.append(v[pre:p1])
            pre=p1+1
            continue
        if v1 in s:
            d.append(v[pre:p1])
            d.append(v1)
            pre=p1+1
            continue
        if v1=='<':
            if v[p1+1]=='<':
                d.append(v[pre:p1])
                d.append('<<')
                pre=p1+2
                check=True
                continue
            elif v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('<=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('<')
                pre=p1+1
        if v1=='>':
            if v[p1+1]=='>':
                d.append(v[pre:p1])
                d.append('>>')
                pre=p1+2
                check=True
                continue
            elif v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('>=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('>')
                pre=p1+1
        if v1=='+':
            if v[p1+1]=='+':
                d.append(v[pre:p1])
                d.append('++')
                pre=p1+2
                check=True
                continue
            elif v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('+=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('+')
                pre=p1+1
        if v1=='-':
            if v[p1+1]=='-':
                d.append(v[pre:p1])
                d.append('--')
                pre=p1+2
                check=True
                continue
            elif v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('-=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('-')
                pre=p1+1
        if v1=='!':
            if v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('!=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('!')
                pre=p1+1
        if v1=='=':
            if v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('==')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('=')
                pre=p1+1
        if v1=='*':
            if v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('*=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('*')
                pre=p1+1
        if v1=='/':
            if v[p1+1]=='/':
                d.append(v[p1:])
                break
        if v1=='/':
            if v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('/=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('/')
                pre=p1+1
        if v1=='%':
            if v[p1+1]=='=':
                d.append(v[pre:p1])
                d.append('%=')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('%')
                pre=p1+1
        if v1=='&':
            if v[p1+1]=='&':
                d.append(v[pre:p1])
                d.append('&&')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('&')
                pre=p1+1
        if v1=='|':
            if v[p1+1]=='|':
                d.append(v[pre:p1])
                d.append('||')
                pre=p1+2
                check=True
                continue
            else:
                d.append(v[pre:p1])
                d.append('|')
                pre=p1+1
    pre=0
tokens=[i for i in d if i!='']
temp='';tempP=[];tempStr=[];tempPos=[]
for i,j in enumerate(tokens):
    j=j.strip()
    if cS==True and (j[0]!='"' and j[-1]!='"'):
        temp=temp+' '+j
        continue
    if cS==False and j[0]=='"' and j[-1]=='"' and len(j)>1:
        continue
    elif cS==False and j[0]=='"':
        temp=temp+j
        tempP.append(i)
        cS=True
        continue
    elif  cS==True:
        temp=temp+' '+j
        tempStr.append(temp)
        tempPos.append([tempP[0],i])
        tempP=[]
        temp=''
        cS=False
        continue
for i,j in enumerate(tempStr):
    tokens[tempPos[i][0]]=j
    tempPos[i][0]+=1
tokens=np.array(tokens)
tempPos=[j for i in tempPos for j in range(i[0],i[1]+1)]
data=np.delete(tokens,tempPos)
data=data.tolist()
def constantAndFloatNfa(lexeme):
    file=[x.split() for x in open("ConstantAndFloat.txt","r").readlines()]
    for pos,val in enumerate(file):
        for p,v in enumerate(val):
            if v=='0-9':
                s=set()
                s.update({str(x) for x in range(0,10)})
                file[pos][p]=s
    if lexeme[0]=='.':
        lexeme='0'+lexeme
    final_state=2
    state={0}
    for inp in lexeme:
        empty_set=set() 
        for ter in state:
            for pos,val in enumerate(file[ter]):
                if (val==inp or (type(val)==set and (inp in val)) or (val=="$")):
                    empty_set.add(pos)
            state=empty_set
                                
    if (final_state in state) :
        return 1
    else:
        return 0
def identifierNfa(lexeme):
    file=[x.split() for x in open("identifier.txt","r").readlines()]
    for pos,val in enumerate(file):
        for p,v in enumerate(val):
            if v=='0-9,a-z,A-Z,_':
                s=set()
                s.update(string.ascii_lowercase)
                s.update(string.ascii_uppercase)
                s.update({str(x) for x in range(0,10)})
                s.update('_')
                file[pos][p]=s
            elif v=='A-Z,a-z,_':
                s=set()
                s.update(string.ascii_lowercase)
                s.update(string.ascii_uppercase)
                s.update('_')
                file[pos][p]=s
    final_state=1
    state={0}
    for inp in lexeme:
        empty_set=set() 
        for ter in state:
            for pos,val in enumerate(file[ter]):
                if (val==inp or (type(val)==set and (inp in val))) and (val!='-'):
                    empty_set.add(pos)
            state=empty_set
                                
    if (final_state in state) and len(lexeme)<31 and (lexeme not in keywords):
        return 1
    else:
        return 0
def stringsNfa(input):
    file=[x.split() for x in open("String.txt","r").readlines()]
    keywords=[i for x in [x.split() for x in open("keywords.txt","r").readlines()] for i in x]
    for pos,val in enumerate(file):
        for p,v in enumerate(val):
            if v=='all':
                s=set()
                s.update(string.ascii_letters+string.punctuation)
                s.update({str(x) for x in range(0,10)})
                file[pos][p]=s
    final_state=3
    state={0}
    for inp in input:
        empty_set=set() 
        for ter in state:
            for pos,val in enumerate(file[ter]):
                if val==inp or (type(val)==set and (inp in val) or (val=="$")):
                    empty_set.add(pos)
            state=empty_set
                                
    if (final_state in state):
        return 1
    else:
        return 0
print('TOKEN_TYPE --------> TOKEN_VALUE')
for j,i in enumerate(data):
    if i[0]=='#':
        print(j+1,': Preprocessor Directive ','---->',i)
    elif i in keywords:
        print(j+1,': C++ Keyword ','---->',i)
    elif i in operator:
        print(j+1,': C++ Operator ','---->',i)
    elif i in saperator:
        print(j+1,': C++ Special Character ','---->',i)
    elif constantAndFloatNfa(i):
        print(j+1,': C++ Constant or Float ','---->',i)
    elif i[0]=='"' and i[-1]=='"':
        print(j+1,': C++ String ','---->',i)
    elif identifierNfa(i):
        print(j+1,': Identifier ','---->',i)
    elif i[0]=='/':
        print(j+1,': Single Line Comment ','---->',i)
