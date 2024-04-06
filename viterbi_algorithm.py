import math 

def viterbi_algorithm():
    
 best_path=[]
 prob={"a":[],"b":[]}
 for i in states:
   
    prob[i].append(s_prob[i]+e_prob[i][S[0]]) 

 for k in range(1,len(S)):
     n=1 
     for j in states:
      num=max(prob[j][k-1]+t_prob[j][j],prob[j][k-1]+t_prob[states[n]][j])   
      prob[j].append(e_prob[j][S[k]]+num)
      n=n-1 #switch from one state to the other
 for i in range(0,4):
     if(prob["a"][i]>=prob["b"][i]): 
         best_path.append("a")
     else:
         best_path.append("b")
 for i in range(0,4):
     print("Symbol",S[i],"{","a:",prob["a"][i],",","b:",prob["b"][i],"}")
 best_sequence=''.join(best_path)
 print("The best path is:",best_sequence)

obs=['A','G','T','C']
states=['a','b']

s_prob={"a":0.5,"b":0.5} #initial probabilities
t_prob={"a":{"a":9/10,"b":1/10},"b":{"a":1/10,"b":9/10}} #transition probabilities,probability from current state to next
e_prob={"a":{"A":0.4,"G":0.4,"C":0.1,"T":0.1},"b":{"A":0.2,"G":0.2,"C":0.3,"T":0.3}} 
'''
emission probabilities,probability for the emission 
of a symbol from one of the states 
'''
for s in states:
    s_prob[s]=math.log2(s_prob[s])
    for j in states:
        t_prob[s][j]=math.log2(t_prob[s][j])
    for k in obs:
        e_prob[s][k]=math.log2(e_prob[s][k])

seq='GGCT'
S=[]
for c in seq:
    S.append(c)
viterbi_algorithm()