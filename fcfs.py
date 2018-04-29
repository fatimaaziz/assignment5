print('first come first serve')
arival_time=[0,3,2]
burst_time=[13,4,7]
wait_time=[0]*3
start_time=0
finishtime=0
turnaround=[0]*3

for index in range(3):
     print 'process:',index
     
     finishtime=finishtime+burst_time[index]
     wait_time[index]=start_time-arival_time[index]
  
     print 'time for wating',wait_time[index]
     turnaround[index]=finishtime-arival_time[index]
    
     print 'turnaroundtime',turnaround[index]
     start_time=start_time+burst_time[index]




