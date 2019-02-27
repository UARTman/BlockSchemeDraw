#!/usr/bin/env python
# coding: utf-8

# In[127]:


InputStr = ''
print(InputStr)
OutputArray = []


# # Функция - стартовый парсер

# In[ ]:


# # Функция - парсер Begin/End

# In[128]:


def FParseBE(start=0, end='end', out=OutputArray, inp=InputStr):
    i = start #Index
    print(i, inp, len(inp))
    
    while True:
        if i>=len(inp):
            return None
        
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        if inp[i:i+5] == 'begin':
            out.append(['block',[]])
            k=FParseBE(start=i+5,out=out[-1][1])
            i=k
            continue
        if inp[i:i+2] == 'if':
            out.append(['if',[],[],[]])
            k=FParseIf(start=i+2,out=out[-1][1],out1=out[-1][2],out2=out[-1][3])
            i=k
            continue
        
        if inp[i:i+5] == 'while':
            out.append(['while',[],[]])
            k=FParseWhile(start=i+5,out=out[-1][1],out1=out[-1][2])
            i=k
            continue
        
        if inp[i:i+3] == 'for':
            out.append(['for',[],[],[],[]])
            k=FParseFor(start=i+3,out=out[-1][1],out1=out[-1][2],out2=out[-1][3],typ=out[-1][4])
            i=k
            continue
        
        if inp[i] == "'":
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
            k=FParseStr(start=i+1,out=out)
            i=k
            out[-1]+="'"
            continue
            
        if inp[i:i+6] == 'repeat':
            out.append(['repeat',[],[]])
            k=FParseRU(start=i+6,out=out[-1][1],out1=out[-1][2])
            i=k
            continue
        
        
        
        
        if len(out)==0:         
            out.append('')
        if type(out[-1])==str:
            out[-1]+=inp[i]
        else:
            out.append(inp[i])
        
        i+=1


# # Парсер Строк

# In[129]:


def FParseStr(start=0,end="'",out=OutputArray,inp=InputStr):
    i = start #Index
    
    while True:
        if i>=len(inp):
            return None
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        
        
        
        
        if i<len(inp):   #Добавляем символ в выводную структуру
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
        else:
            return None
        
        i+=1


# # Парсер If

# In[130]:


def FParseIf(start=0,end=';',out=OutputArray,inp=InputStr,out1=[],out2=[]):
    i = start #Index
    
    while True:
        if i>=len(inp):
            return None
        
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        if inp[i:i+5] == 'begin':
            out.append(['block',[]])
            k=FParseBE(start=i+5,out=out[-1][1])
            i=k
            continue
        
        if inp[i:i+2] == 'if':
            out.append(['if',[],[],[]])
            k=FParseIf(start=i+2,out=out[-1][1],out1=out[-1][2],out2=out[-1][3])
            i=k-1
            continue
        
        if inp[i:i+5] == 'while':
            out.append(['while',[],[]])
            k=FParseWhile(start=i+5,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
            
        if inp[i:i+6] == 'repeat':
            out.append(['repeat',[],[]])
            k=FParseRU(start=i+6,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
            
        if inp[i:i+3] == 'for':
            out.append(['for',[],[],[],[]])
            k=FParseFor(start=i+3,out=out[-1][1],out1=out[-1][2],out2=out[-1][3],typ=out[-1][4])
            i=k-1
            continue
        
        if inp[i:i+4] == 'then':
            out=out1
            i=i+4
            continue
        if inp[i:i+4] == 'else':
            out=out2
            i=i+4
            continue
        
        if inp[i] == "'":
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
            k=FParseStr(start=i+1,out=out)
            i=k
            out[-1]+="'"
            continue
            
        
        
        
        
        if i<len(inp):#Добавляем символ в выводную структуру
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
        else:
            return None
        
        i+=1


# # Парсер While

# In[131]:


def FParseWhile(start=0,end=';',out=OutputArray,inp=InputStr,out1=[]):
    i = start #Index
    
    while True:
        if i>=len(inp):
            return None
        
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        if inp[i:i+5] == 'begin':
            out.append(['block',[]])
            k=FParseBE(start=i+5,out=out[-1][1])
            i=k
            continue
        
        if inp[i:i+2] == 'if':
            out.append(['if',[],[],[]])
            k=FParseIf(start=i+2,out=out[-1][1],out1=out[-1][2],out2=out[-1][3])
            i=k-1
            continue
        
        if inp[i:i+5] == 'while':
            out.append(['while',[],[]])
            k=FParseWhile(start=i+5,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
        
        if inp[i:i+6] == 'repeat':
            out.append(['repeat',[],[]])
            k=FParseRU(start=i+6,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
        
        if inp[i:i+3] == 'for':
            out.append(['for',[],[],[],[]])
            k=FParseFor(start=i+3,out=out[-1][1],out1=out[-1][2],out2=out[-1][3],typ=out[-1][4])
            i=k-1
            continue
            
            
        if inp[i:i+2] == 'do':
            out=out1
            i=i+2
            continue

        if inp[i] == "'":
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
            k=FParseStr(start=i+1,out=out)
            i=k
            out[-1]+="'"
            continue
            
        
        
        
        
        if i<len(inp):#Добавляем символ в выводную структуру
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
        else:
            return None
        
        i+=1


# # Парсер Repeat/Until

# In[132]:


def FParseRU(start=0,end=';',out=OutputArray,inp=InputStr,out1=[]):
    i = start #Index
    while True:
        if i>=len(inp):
            return None
        
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        if inp[i:i+5] == 'begin':
            out.append(['block',[]])
            k=FParseBE(start=i+5,out=out[-1][1])
            i=k
            continue
        
        if inp[i:i+2] == 'if':
            out.append(['if',[],[],[]])
            k=FParseIf(start=i+2,out=out[-1][1],out1=out[-1][2],out2=out[-1][3])
            i=k
            continue
        
        if inp[i:i+5] == 'while':
            out.append(['while',[],[]])
            k=FParseWhile(start=i+5,out=out[-1][1],out1=out[-1][2])
            i=k
            continue
            
        if inp[i:i+6] == 'repeat':
            out.append(['repeat',[],[]])
            k=FParseRU(start=i+6,out=out[-1][1],out1=out[-1][2])
            i=k
            continue
        
        if inp[i:i+3] == 'for':
            out.append(['for',[],[],[],[]])
            k=FParseFor(start=i+3,out=out[-1][1],out1=out[-1][2],out2=out[-1][3],typ=out[-1][4])
            i=k
            continue
            
        if inp[i:i+5] == 'until':
            out=out1
            i=i+5
            continue

        if inp[i] == "'":
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
            k=FParseStr(start=i+1,out=out)
            i=k
            out[-1]+="'"
            continue
            
        
        
        
        
        if i<len(inp):#Добавляем символ в выводную структуру
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
        else:
            return None
        
        i+=1


# # Парсер for

# In[133]:


def FParseFor(start=0,end=';',out=OutputArray,inp=InputStr,out1=[],out2=[],typ=[]):
    i = start #Index
    
    
    while True:
        if i>=len(inp):
            return None
        
        if inp[i:i+len(end)] == end: #
            return i+len(end)
        
        if inp[i:i+5] == 'begin':
            out.append(['block',[]])
            k=FParseBE(start=i+5,out=out[-1][1])
            i=k
            continue
        
        if inp[i:i+2] == 'if':
            out.append(['if',[],[],[]])
            k=FParseIf(start=i+2,out=out[-1][1],out1=out[-1][2],out2=out[-1][3])
            i=k-1
            continue
        
        if inp[i:i+5] == 'while':
            out.append(['while',[],[]])
            k=FParseWhile(start=i+5,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
            
        if inp[i:i+6] == 'repeat':
            out.append(['repeat',[],[]])
            k=FParseRU(start=i+6,out=out[-1][1],out1=out[-1][2])
            i=k-1
            continue
            
        if inp[i:i+3] == 'for':
            out.append(['for',[],[],[],[]])
            k=FParseFor(start=i+3,out=out[-1][1],out1=out[-1][2],out2=out[-1][3],typ=out[-1][4])
            i=k-1
            continue
            
        if inp[i:i+2] == 'to':
            out=out1
            i=i+2
            typ.append(1)
            continue
        
        if inp[i:i+6] == 'downto':
            out=out1
            i=i+6
            typ.append(2)
            continue
        
        if inp[i:i+2] == 'do':
            out=out2
            i=i+2
            continue
        
        if inp[i] == "'":
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
            k=FParseStr(start=i+1,out=out)
            i=k
            out[-1]+="'"
            continue
            
        
        
        
        
        if i<len(inp):#Добавляем символ в выводную структуру
            if len(out)==0:         
                out.append('')
            if type(out[-1])==str:
                out[-1]+=inp[i]
            else:
                out.append(inp[i])
        else:
            return None
        
        i+=1




# In[134]:


if __name__ == '__main__':
    try:
        print(FParseBE(start=0))
    except TypeError:
        pass
    print(OutputArray)


# In[135]:





# In[ ]:





# In[ ]:





# In[ ]:




