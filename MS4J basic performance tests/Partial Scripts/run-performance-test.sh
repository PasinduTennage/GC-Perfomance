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


concurrent_users=(10 50 100 200 500 1000 1500 2000)
heap_sizes=(100m 200m 500m 1g 2g 4g 8g)

ms4j_host=192.168.32.11

# Test Duration in seconds
test_duration=2 #to be changed to 900


mkdir results



for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        
        total_users=$(($u))
        report_location=$PWD/results/${total_users}_users/${heap}_heap
        echo "Report location is ${report_location}"
        mkdir -p $report_location

	nohup sshpass -p 'javawso2' ssh -n -f wso2@192.168.32.11 "/bin/bash /home/wso2/Pasindu/start.sh ${heap} ${total_users}" &
	
	while true 
	do
		echo "Checking service"
    		# Check service
    		response_code=$(curl -s -o /dev/null -w "%{http_code}" http://192.168.32.11:9090/hello/wso2)
    		if [ $response_code -eq 200 ]; then
        		echo "MS4j started"
        		break
    		else
        		sleep 10
    		fi
	done
	
	


        # Start JMeter server
        ./jmeter  -Jgroup1.threads=$u  -n -t MS4J_Hello_Wso2.jmx -l ${report_location}/results.jtl	
        
	
        
    done
done


echo "Completed"
