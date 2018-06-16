#!/bin/bash
# Copyright 2018 WSO2 Inc. (http://wso2.org)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------
# Run Performance Tests for MS4J
# ----------------------------------------------------------------------------


concurrent_users=(1  5) #to be changed
heap_sizes=(50m 100m) #to be changed
garbage_collectors=(UseSerialGC UseParallelGC) #add UseConcMarkSweepGC UseG1GC
message_size=(50 1024 10240 102400) #to be checked later

jtl_location=/home/wso2/pasindu/jtls

ms4j_host_user=wso2@192.168.32.11 
ms4j_host=192.168.32.11

target_script=/home/wso2/Pasindu/start.sh

target_gc_logs_path=/home/wso2/Pasindu/GCLogs

gc_logs_path=/home/wso2/pasindu/GCLogs

jmx_file=/home/wso2/pasindu/jmx/MS4J_Hello_Wso2.jmx

jtl_splitter_path=/home/wso2/pasindu/Jmeter-Split

dashboards_path=/home/wso2/pasindu/dashboards

jmeter_path=/home/wso2/pasindu/apache-jmeter-4.0/bin


test_duration=120 #to be changed to ___

split_time=1 #to be changed to 5



for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        
        for gc in ${garbage_collectors[@]}
    	do
        	total_users=$(($u))
        	report_location=$jtl_location/${total_users}_users/${heap}_heap/${gc}_collector
        	echo "Report location is ${report_location}"
        	mkdir -p $report_location

		nohup sshpass -p 'javawso2' ssh -n -f ${ms4j_host_user} "/bin/bash $target_script ${heap} ${total_users} ${target_gc_logs_path} ${gc}" &
	
		while true 
		do
			echo "Checking service"
    			response_code=$(curl -s -o /dev/null -w "%{http_code}" http://${ms4j_host}:9090/hello/wso2)
    			if [ $response_code -eq 200 ]; then
        			echo "MS4j started"
        			break
    			else
        			sleep 10
    			fi
		done
	        	

        	# Start JMeter server
        	${jmeter_path}/jmeter  -Jgroup1.threads=$u -Jgroup1.seconds=${test_duration} -n -t ${jmx_file} -l ${report_location}/results.jtl	
        done
	
        
    done
done

echo "Completed Generating JTL files"



echo "Copying GC logs to Jmeter server machine"


mkdir -p ${gc_logs_path}
sshpass -p 'javawso2' scp -r $ms4j_host_user:${target_gc_logs_path} ${gc_logs_path}

echo "Finished Copying GC logs to server machine"

echo "Splitting JTL"

for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        for gc in ${garbage_collectors[@]}
    	do
        	total_users=$(($u))
        	jtl_file=${jtl_location}/${total_users}_users/${heap}_heap/${gc}_collector/results.jtl        
		java -jar ${jtl_splitter_path}/jtl-splitter-0.1.1-SNAPSHOT.jar -f $jtl_file -t $split_time -d	
        done
    done
done


echo "Completed Splitting jtl files"

echo "Generating Dash Boards"


for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        for gc in ${garbage_collectors[@]}
    	do    
        	total_users=$(($u))
        	report_location=${dashboards_path}/${total_users}_users/${heap}_heap/${gc}_collector
        	echo "Report location is ${report_location}"
        	mkdir -p $report_location
	
		${jmeter_path}/jmeter -g  ${jtl_location}/${total_users}_users/${heap}_heap/${gc}_collector/results-measurement.jtl   -o $report_location	
        done
        
    done
done


echo "Completed generating dashboards"
