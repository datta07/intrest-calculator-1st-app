import time
k=[]
def time1(p,date,month,year,no):
            a=list(map(int,p.split('-')))
            b=[int(date),int(month),int(year)]
            c=[]
            for k in range(0,3):
                  c.append(a[k]-b[k])
            c[2]=12*c[2]  
            c[2]=c[2]+c[1] 
            if (c[0]<0):
                  c[2]-=1
                  c[0]+=30  
            s= str(c[2])+' months & '+str(c[0])+' days'
            if (c[2]<0):
                 return 'k'
            if (no==1):
                 return s  
            c[0]=float(c[0])
            if c[0]==0 :
                return c[2]-1
            return c[2]+(c[0]/30)
            
def intrest(p,t,i):
            global k
            k=[]
            k.append(p)
            p=int(p)
            t1=t//6
            t1=t1*6
            t2=t%6
            t=0
            while (t<t1):
                      p=p*(1+i*6)
                      t=t+6
                      k.append("{0:0.2f}".format(p))
            p=p*(1+(i*(t2)))
            k.append("{0:0.2f}".format(p))
            return "{0:0.2f}".format(p)+'/-'
            
def intrest1(p,t,i):
            global k
            k=[]
            k.append(p)
            p=int(p)
            t1=t//6
            t1=t1*6
            t=0
            ans=p
            while (t<t1):
                      ans+=p*(i*6)
                      k.append("{0:0.2f}".format(ans))
                      t=t+6
            p=p*(1+(i*t))
            return str(p)+'/-'
            
def value():
            global k
            return k

