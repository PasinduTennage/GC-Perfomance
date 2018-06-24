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


minutes=$1

killall java


export JVM_MEM_OPTS="-Xms500m -Xmx500m "
        
echo "Starting MS4J Hello World"
/opt/jdk1.8.0_162/bin/java -Xloggc:/home/wso2/Pasindu/GCLogs/${minutes}_Minutes_GCLog.txt  -verbose:gc -XX:+PrintGCDateStamps -Xms500m -Xmx500m  -jar /home/wso2/Pasindu/Hello-Service-*.jar
