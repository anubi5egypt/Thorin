import requests
import re
import random
from core import nano
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def inject(link,pay):
    b_link=link.split('?')[0]
    params=link.split('?')[1]
    if len(params) >0:
        param_list=[]
        Plenth=params.split('&')
        for z in Plenth:
            param=z.split('=')[0]
            val=z.split('=')[1]
            if param not in param_list:
                param_list.append(param)
            payload=(b_link+'?')
            for y in param_list:
                payload=(payload+y+'='+val+pay+'&')
            payload=payload[:-1]
        return payload



def response_time(url):
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    try:
        r = requests.get(url,headers=headers)   
        r_time = int(r.elapsed.total_seconds())
        return r_time
    except:
        pass
    



def bolian_base(url):
    state=False
    try:
        r1=requests.get(inject(url,'test')).text
        r2=requests.get(inject(url,'test')).text
        if len(r1)==len(r2) :
            for god,bad in regex.SQL_INJECTION_ERROR_BASE.items():
                r1=requests.get(inject(url,god))
                god_r=r1.content
                sr1=r1.status_code
                r2=requests.get(inject(url,bad))
                bad_r=r2.content
                sr2=r2.status_code
                if len(god_r) != len(bad_r) and sr1 == sr2:
                    state=True
                    print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                    print(inject(url,god)+' | response Length:'+str(len(god_r))+'\n'+inject(url,bad)+' | response Length:'+str(len(bad_r)))
                    break
                    
    except:
        pass
    return state


def time_base(url): 
        
    try:
        for x in regex.SQL_INJECTION_BLIND_BASE:
            r1=inject(url,str(x).format('3'))
            rs1=response_time(r1)
            r2=inject(url,str(x).format('6'))
            rs2=response_time(r2)
            r3=inject(url,str(x).format('9'))
            rs3=response_time(r3)
            if int(rs1) >= 3 and int(rs2) >= 6 and int(rs3) >= 9:
                if int(rs1) >= int(rs2)/2 and int(rs1) >= int(rs3)/3:
                      if int(rs2) >= int(rs1)*2 and int(rs3) >=int(rs1)*3:
                           t=bolian_base(url)
                           if t==True:
                               print(r1+' | Response time:'+'\033[32m'+str(rs1)+'\033[00m'+'\n'+r2+' | Response time:'+'\033[32m'+str(rs2)+'\033[00m'+'\n'+r3+' | Response time:'+'\033[32m'+str(rs3)+'\033[00m')
                               break
                           
                           else:
                               print('\033[33;1mWarning can be false positives\033[00m') 
                               print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                               print(r1+' | Response time:'+'\033[32m'+str(rs1)+'\033[00m'+'\n'+r2+' | Response time:'+'\033[32m'+str(rs2)+'\033[00m'+'\n'+r3+' | Response time:'+'\033[32m'+str(rs3)+'\033[00m')
                           break
    except:
        pass
    
def semple(url):
    state=False
    done=0
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    payload=["'",'"',";","#","-","--","--+"]
    
    for i in payload: 
        if done ==1 :
            break
        try:
            url=inject(url,i)
            r = requests.get(url,headers=headers,verify=False)
            cont = r.content
            for x in regex.SQL_ERROR:
                if(re.search(x, str(cont))):
                    url_=nano.inject_param(url,"x")
                    r_ = requests.get(url_,headers=headers,verify=False)
                    cont_ = r_.content
                    if(re.search(x, str(cont_))):
                        pass
                    else:
                        state=True
                        print("\033[91mPossibly SQL injection vulnerability\033[00m  "+url)
                        done=1
                        break
        except:
            pass
               
    return state
                
                
def sqlinjection_(url):
    task1=semple(url)
    if task1 == False:
        time_base(url)
