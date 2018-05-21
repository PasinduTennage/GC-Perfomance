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



mkdir dasboards



for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        
        total_users=$(($u))
        report_location=/home/wso2/pasindu/apache-jmeter-4.0/bin/dashboards/${total_users}_users/${heap}_heap
        echo "Report location is ${report_location}"
        mkdir -p $report_location
	
	/home/wso2/pasindu/apache-jmeter-4.0/bin/jmeter -g  /home/wso2/pasindu/apache-jmeter-4.0/bin/results/${total_users}_users/${heap}_heap/results.jtl   -o $report_location	
        
    done
done


echo "Completed"
