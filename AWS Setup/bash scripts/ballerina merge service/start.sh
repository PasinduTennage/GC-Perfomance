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


heap_size=$1
num_users=$2 
target_gc_logs_path=$3
gc=$4
size=$5




mkdir -p ${target_gc_logs_path}

killall java

echo "Starting Ballerina"
ballerina run /home/ubuntu/Pasindu/merge_service.bal $heap_size $num_users $target_gc_logs_path $gc $size
