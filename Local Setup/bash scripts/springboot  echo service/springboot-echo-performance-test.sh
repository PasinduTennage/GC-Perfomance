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


concurrent_users=(1000 1) #to be changed 1 50 100 200 
heap_sizes=(100m 4g) #to be changed  200m 500m 1g 2g 4g 8g
message_sizes=(1024 10240) # 400 1600
garbage_collectors=(UseSerialGC UseParallelGC) #UseSerialGC UseParallelGC UseConcMarkSweepGC  

jtl_location=/home/wso2/pasindu/jtls

springboot_host_user=wso2@192.168.32.11 
springboot_host=192.168.32.11

target_uptime_path=/home/wso2/Pasindu/uptime_dir

uptime_path=/home/wso2/pasindu/uptime_dir

target_script=/home/wso2/Pasindu/start.sh

target_uptime_script=/home/wso2/Pasindu/uptime_script.sh

target_gc_logs_path=/home/wso2/Pasindu/GCLogs

gc_logs_path=/home/wso2/pasindu/GCLogs

gc_logs_report_path=/home/wso2/pasindu/gcReports

jmx_file=/home/wso2/pasindu/jmx/springboot_echo.jmx

jtl_splitter_path=/home/wso2/pasindu/Jmeter-Split

dashboards_path=/home/wso2/pasindu/dashboards

jmeter_path=/home/wso2/pasindu/apache-jmeter-4.0/bin

performance_report_python_file=/home/wso2/pasindu/performance/performance-report.py

payload_generator_python_file=/home/wso2/pasindu/performance/payloadGenarator.py

performance_report_output_file=/home/wso2/pasindu/SpringBootEchoPerformance.csv

payloads_output_file_root=/home/wso2/pasindu/payloads

payload_files_prefix=payload

gc_viewer_jar_file=/home/wso2/pasindu/gc_viewer/gcviewer-1.36-SNAPSHOT.jar

test_duration=120	 #to be changed to ___

split_time=1 #to be changed to 5

rm -r $gc_logs_path/
rm -r $dashboards_path/
rm -r $gc_logs_report_path/
rm -r $jtl_location
rm -r $payloads_output_file_root/
rm -r $uptime_path/
rm $performance_report_output_file

echo "Generating Payloads"
mkdir -p $payloads_output_file_root

python3 ${payload_generator_python_file} ${payloads_output_file_root}/${payload_files_prefix}

echo "Finished generating payloads"

for size in ${message_sizes[@]}
do

    for heap in ${heap_sizes[@]}
    do
        for u in ${concurrent_users[@]}
        do
        
            for gc in ${garbage_collectors[@]}
    	    do
        	    total_users=$(($u))
                    
        	    report_location=$jtl_location/${total_users}_users/${heap}_heap/${gc}_collector/${size}_message
        	    echo "Report location is ${report_location}"
        	    mkdir -p $report_location

		    nohup sshpass -p 'javawso2' ssh -n -f ${springboot_host_user} "/bin/bash $target_script ${heap} ${total_users} ${target_gc_logs_path} ${gc} ${size}" &
	
		    while true 
		    do
			    echo "Checking service"
    			    response_code=$(curl -s -o /dev/null -w "%{http_code}" http://${springboot_host}:9000/echo?message=m)
    			    if [ $response_code -eq 200 ]; then
        			    echo "Springboot started"
        			    break
    			    else
        			    sleep 10
    			    fi
		    done
                    
		    message=$(<${payloads_output_file_root}/${payload_files_prefix}${size})
                    
	        	

        	    # Start JMeter server
        	    ${jmeter_path}/jmeter  -Jgroup1.host=${springboot_host}  -Jgroup1.port=9000 -Jgroup1.threads=$u -Jgroup1.seconds=${test_duration} -Jgroup1.data=${message} -n -t ${jmx_file} -l ${report_location}/results.jtl
                    
                    echo "Running Uptime command"	

                    nohup sshpass -p 'javawso2' ssh -n -f ${springboot_host_user} "/bin/bash $target_uptime_script ${heap} ${total_users} ${target_uptime_path} ${gc} ${size}" &
		    
            done
	
        
        done
    done
done

echo "Completed Generating JTL files"



echo "Copying GC logs to Jmeter server machine"


mkdir -p ${gc_logs_path}
sshpass -p 'javawso2' scp -r $springboot_host_user:${target_gc_logs_path} ${gc_logs_path}

echo "Finished Copying GC logs to server machine"

echo "Copying uptime logs to Jmeter server machine"


mkdir -p ${uptime_path}
sshpass -p 'javawso2' scp -r $springboot_host_user:${target_uptime_path} ${uptime_path}

echo "Finished Copying uptime logs to server machine"

echo "Splitting JTL"

for size in ${message_sizes[@]}
do

    for heap in ${heap_sizes[@]}
    do
        for u in ${concurrent_users[@]}
        do
            for gc in ${garbage_collectors[@]}
    	    do
        	    total_users=$(($u))
        	    jtl_file=${jtl_location}/${total_users}_users/${heap}_heap/${gc}_collector/${size}_message/results.jtl        
		    java -jar ${jtl_splitter_path}/jtl-splitter-0.1.1-SNAPSHOT.jar -f $jtl_file -t $split_time -d	
            done
        done
    done
done

echo "Completed Splitting jtl files"

echo "Generating Dash Boards"

for size in ${message_sizes[@]}
do
    for heap in ${heap_sizes[@]}
    do
        for u in ${concurrent_users[@]}
        do
            for gc in ${garbage_collectors[@]}
    	    do    
        	    total_users=$(($u))
        	    report_location=${dashboards_path}/${total_users}_users/${heap}_heap/${gc}_collector/${size}_message
        	    echo "Report location is ${report_location}"
        	    mkdir -p $report_location
	
                    ${jmeter_path}/jmeter -g  ${jtl_location}/${total_users}_users/${heap}_heap/${gc}_collector/${size}_message/results-measurement.jtl   -o $report_location	
            done
        
        done
    done
done


echo "Completed generating dashboards"

echo "Generating GC reports"

mkdir -p $gc_logs_report_path


for size in ${message_sizes[@]}
do
    for heap in ${heap_sizes[@]}
    do
        for u in ${concurrent_users[@]}
        do
            for gc in ${garbage_collectors[@]}
    	    do    
        	    total_users=$(($u))
        	    gc_file=${gc_logs_path}/GCLogs/${heap}_Heap_${total_users}_Users_${gc}_collector_${size}_size_GCLog.txt
                    gc_report_file=$gc_logs_report_path/${heap}_Heap_${total_users}_Users_${gc}_collector_${size}_size_GCReport.csv
                    java -jar $gc_viewer_jar_file $gc_file $gc_report_file
	
            done
        
        done
    done
done


echo "Completed generating GC reports"


echo "Generating the CSV file"

python3 $performance_report_python_file  $jtl_location $gc_logs_report_path $uptime_path $dashboards_path $performance_report_output_file

echo "Finished generating CSV file"
