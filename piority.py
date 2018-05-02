
print ("priority\n")
arival_time=[0,2,3]
process=['p1','p2','p3']
pri=[8,3,1]
burst_time=[13,6,3]
wait_time=[0]*3
start_time=0
finishtime=0
time=0
turnaround=[0]*3
for i in range(3):
     for j in range(2-i):
            if (arival_time[j]>time and pri[j]>pri[j+1]):
                temp=burst_time[j]
                burst_time[j]=burst_time[j+1]
                burst_time[j+1]=temp
                temp1=arival_time[j]
                arival_time[j]=arival_time[j+1]
                arival_time[j+1]=temp1
                temp2=process[j]
                process[j]=process[j+1]
                process[j+1]=temp2
                temp3=pri[j]
                pri[j]=pri[j+1]
                pri[j+1]=temp3
     time=burst_time[i]+time

time=0
print("gang chart")
for index in range(3):
     print (time,':',process[index],':',time+burst_time[index])
     time=time+burst_time[index]    

for index in range(3):
     print (process[index])
     
     finishtime=finishtime+burst_time[index]
     wait_time[index]=start_time-arival_time[index]
  
     print ('time for wating',wait_time[index])
     turnaround[index]=finishtime-arival_time[index]
    
     print ('turnaroundtime',turnaround[index])
     start_time=start_time+burst_time[index]


    
	 

