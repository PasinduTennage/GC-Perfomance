concurrent_users=(10 50 100 200 500 1000 1500 2000)
heap_sizes=(100m 200m 500m 1g 2g 4g 8g)

for heap in ${heap_sizes[@]}
do
    for u in ${concurrent_users[@]}
    do
        
        total_users=$(($u))
        jtl_file=/home/wso2/pasindu/apache-jmeter-4.0/bin/results/${total_users}_users/${heap}_heap/results.jtl
        
	java -jar jtl-splitter-0.1.1-SNAPSHOT.jar -f $jtl_file -t 5 -d	
        
    done
done


echo "Completed Splitting jtl files"








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
