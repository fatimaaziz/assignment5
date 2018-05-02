print('round robin algorithum')
arival_time=[0,3,2]
process=['p1','p2','p3']
burst_time=[13,3,7]
rP_time=[0]*3
wait_time=[0]*3
start_time=[0]*3
finishtime=[0]*3
timeslice=3
turnaround=[0]*3



for i in range (2):
     for j in range (2-i):
             if(arival_time[j]>arival_time[j+1]):
                     temp=burst_time[j]
                     burst_time[j]=burst_time[j+1]
                     burst_time[j+1]=temp
                     temp1=arival_time[j]
                     arival_time[j]=arival_time[j+1]
                     arival_time[j+1]=temp1
                     temp2=process[j]
                     process[j]=process[j+1]
                     process[j+1]=temp2

               
#sort according to arrival time
for i in range(3):
     rP_time[i]=burst_time[i]                  
numofprocess=3
iter=0#for iteration
time=arival_time[0] 
print(time,':')
while (numofprocess!=0):
     if(rP_time[iter]>timeslice):
          time=time+timeslice
          rP_time[iter]=rP_time[iter]-timeslice
          print (process[iter],':',time)   
     elif(rP_time[iter]<=timeslice and rP_time[iter]>0):
                time=time+rP_time[iter]
                rP_time[iter]=0
                print (process[iter],':',time)
                finishtime[iter]=time
                turnaround[iter]=finishtime[iter]-arival_time[iter]
                wait_time[iter]=finishtime[iter]-arival_time[iter]-burst_time[iter]
                numofprocess=numofprocess-1

     iter=iter+1
     if(iter==3):
           iter=0     

               
         
        
    

  
print ("processname  A_T   W_T   TA_T")  
for i in range(3):
    print (process[i],"          ",arival_time[i],"  ",wait_time[i]," ",turnaround[i])
                  
          
                  
