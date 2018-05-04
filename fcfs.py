print('first come first serve')
arival_time=[0,3,2]
burst_time=[13,4,7]
wait_time=[0]*3
start_time=0
finishtime=0
turnaround=[0]*3
avgturn=0
waittime=0
for index in range(3):
print("GANTT CHART")
     print 'process:',index
     
     finishtime=finishtime+burst_time[index]
     wait_time[index]=start_time-arival_time[index]
  
     print 'time for wating',wait_time[index]
     turnaround[index]=finishtime-arival_time[index]
    
     print 'turnaroundtime',turnaround[index]
     start_time=start_time+burst_time[index]
for index in range(3)
      waittime=waittime+wait_time[index]
	  avgturn=avgturn+turnaround[index]
avgturn=avgturn/3
waittime=waittime/3
print("average time",avgturn)
print("wait time",waittime)



