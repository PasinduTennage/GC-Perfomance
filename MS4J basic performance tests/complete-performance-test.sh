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


concurrent_users=(10 50 100 200 500 1000)


mkdir results_8g



for u in ${concurrent_users[@]}
do
        
    total_users=$(($u))
    report_location=$PWD/results_8g/${total_users}
    echo "Report location is ${report_location}"
    mkdir -p $report_location
    	
    
    sshpass -p 'javawso2' ssh wso2@192.168.32.11	

     # Start JMeter server
    ./jmeter  -Jgroup1.threads=$u  -n -t MS4J_Hello_Wso2.jmx -l ${report_location}/results.jtl	
        
	
        
done



echo "Completed"
