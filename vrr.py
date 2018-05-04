print("round robbin with input output")
ready=[0]*100#making two queues
readyrear=0
readyfront=0
waitingqueue=[0]*50
waitingrear=0
waitingfront=0
axiliaryqueue=[0]*50
axxrear=0
axxfront=0
n=int(input("enter the number of process: "))
qt=int(input("time slice: "))
qt1=int(input("time of runing befor going to input: "))
qt2=qt1
inp=int(input("input time : "))
for i in range (n):
		process={}
		ready[i]=process
		ready[i]['proname']=input("enter process name : ")
		ready[i]['arrival']=int(input("enter the arival time"))
		ready[i]['brust']=int(input("enter the brust  time"))
		ready[i]['remaining time']=ready[i]['brust']
		ready[i]['turnaround']=0
		ready[i]['waiting']=0
		ready[i]['waitingqueuert']=0
		ready[i]['remaining qt']=0
		ready[i]['pro is what']=int(input("if even enter 0 or odd enter 1"))
		ready[i]['finish time']=0
		readyrear=readyrear+1#incrementing ready
		
for i in range(n-1):#sorting acorrding to arriva time
        for j in range(n-1-i):
				if(ready[j+1]['arrival']<ready[j]['arrival']):
					temp=ready[j]
					ready[j]=ready[j+1]
					ready[j+1]=ready[j]
 
time=ready[0]['arrival']
resultant=[0]*n
rp=n
while(rp!=0):
		if(ready[i]['pro is what']==1):#if odd proces
		       if(ready[readyfront]['remaining time']>qt):
                  time=time+qt
                  print (ready[readyfront]['proname'],':',time)
				  ready[readyfront]['remaining time']=ready[readyfront]['remaining time']-qt
				  ready[readyrear]=ready[readyfront]
				  readyrear=readyrear+1
               elif(ready[readyfront]['remaining time']<=qt and ready[readyfront]['remaining time']>0):
                  time=time+ready[readyfront]['remaining time']
                  ready[readyfront]['remaining time']=0
                  print (ready[readyfront]['proname'],':',time)
                  ready[readyfront]['finish time']=time
                  ready[readyfront]['turnaround']=ready[readyfront]['finish time']-ready[readyfront]['arrival']
                  ready[readyfront]['waiting']=ready[readyfront]['finish time']-ready[readyfront]['arrival']-ready[readyfront]['brust']
                  resultant[rp]=ready[readyfront]
				  rp=rp-1
		   readyfront=readyfront+1
		elif(ready[i]['pro is what']==0)
		     if(ready[readyfront]['remaining time']>qt1):
                  time=time+qt1
                  ready[readyfront]['remaining time'] =ready[readyfront]['remaining time']-timeslice
                  print (ready[readyfront]['proname'],':',time)
				  ready[readyfront]['remaining time']=ready[readyfront]['remaining time']-qt
				  ready[readyfront]['waitingqueuert']=time+inp
				  ready[readyfront]['remaining qt']=qt-qt1
				  waitingqueue[waitingrear]=ready[readyfront]
				  waitingrear=waitingrear+1
				  q1=0
				  
               elif(ready[readyfront]['remaining time']<=qt1 and ready[readyfront]['remaining time']>0):
                  time=time+ready[readyfront]['remaining time']
                  ready[readyfront]['remaining time']=0
                  print (ready[readyfront]['proname'],':',time)
                  ready[readyfront]['finish time']=time
                  ready[readyfront]['turnaround']=ready[readyfront]['finish time']-ready[readyfront]['arrival']
                  ready[readyfront]['turnaround']=ready[readyfront]['finish time']-ready[readyfront]['arrival']-ready[readyfront]['brust']
                  rp=rp-1
			readyfront=readyfront+1	  
			  
        	
        if(waitingqueue[waitingfront]['waitingqueuert']<=time)
		    ready[readyfront]['waitingqueuert']=0
		    axiliaryqueue[axxrear]=waitingqueue[waitingfront]
			if(axiliaryqueue[axxfront]['remaining time']>axiliaryqueue[axxfront]['remaining qt']):
                    time=time+axiliaryqueue[axxfront]['remaining qt']
					print (axiliaryqueue[axxfront]['proname'],':',time)
					axiliaryqueue[axxfront]['remaining time']=axiliaryqueue[axxfront]['remaining qt']-qt
					axiliaryqueue[axxfront]['waitingqueuert']=0
					axiliaryqueue[axxfront]['remaining qt']=0
					
					ready[readyrear]=axiliaryqueue[axxfront]
					readyrear=readyrear+1
				  
				  
               elif(axiliaryqueue[axxfront]['remaining time']<=axiliaryqueue[axxfront]['remaining qt'] and axiliaryqueue[axxfront]['remaining time']>0):
                  time=time+axiliaryqueue[axxfront]['remaining time']
                  axiliaryqueue[axxfront]['remaining time']=0
                  print (axiliaryqueue[axxfront],':',time)
                  axiliaryqueue[axxfront]['finish time']=time
                  axiliaryqueue[axxfront]['turnaround']=axiliaryqueue[axxfront]['finish time']-axiliaryqueue[axxfront]['arrival']
                  axiliaryqueue[axxfront]['waiting']=axiliaryqueue[axxfront]['finish time']-axiliaryqueue[axxfront]['arrival']-axiliaryqueue[axxfront]['brust']
                  resultant[rp-1]=axiliaryqueue[axxfront]
				  rp=rp-1
		
			waitingfront=waitingfront+1
		turnarround=0
wait=0
for i in range(n):
	 turnarround=resultant[rp]['turnaround']+turnarround 
	 wait=wait+resultant[rp]['waiting']

wait=wait/n
turnaround=turnaround/n
print("average trunouttime",turnarround)
print("average waitingtime",wait)
