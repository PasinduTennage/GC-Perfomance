seconds=(900 3600 18000)

for second in ${seconds[@]}
do
    
        
        jtl_file=/home/wso2/pasindu/apache-jmeter-4.0/bin/results/${second}_seconds/results.jtl
        
	java -jar jtl-splitter-0.1.1-SNAPSHOT.jar -f $jtl_file -t 5 -d	
        
    
done


echo "Completed Splitting jtl files"





for second in ${seconds[@]}
do
    
        
        
        report_location=/home/wso2/pasindu/apache-jmeter-4.0/bin/dashboards/${second}_seconds
        echo "Report location is ${report_location}"
        mkdir -p $report_location
	
	/home/wso2/pasindu/apache-jmeter-4.0/bin/jmeter -g  /home/wso2/pasindu/apache-jmeter-4.0/bin/results/${second}_seconds/results-measurement.jtl   -o $report_location	
        
    
done


echo "Completed"
