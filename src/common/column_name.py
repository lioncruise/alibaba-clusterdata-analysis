server_event_column_name = ['timestamp', 'machine_id', 'event_type', 'event_detail', 'cpu', 'memory', 'disk']
server_usage_column_name = ['timestamp', 'machine_id', 'cpu', 'memory', 'disk', 'cpu_load_1min', 'cpu_load_5min',
                            'cpu_load_15min']
# container_event.csv's last column is useless, but we have to write it to the list otherwise pandas goes to wrong.
container_event_column_name = ['timestamp', 'event_type', 'instance_id', 'machine_id', 'cpu_requested',
                               'memory_requested', 'disk_requested', 'cpu_ids', 'useless_column']
container_usage_column_name = ['timestamp', 'instance_id', 'cpu', 'memory', 'disk', 'cpu_load_1min', 'cpu_load_5min',
                               'cpu_load_15min', 'avg_cycles_per_instruction', 'avg_cache_miss_per_1000_instruction',
                               'max_cycles_per_instruction', 'max_cache_miss_per_1000_instruction']
batch_task_column_name = ['create_time', 'end_time', 'job_id', 'task_id', 'num_of_instances', 'status',
                          'cpu_per_instance', 'memory_per_instance']
batch_instance_column_name = ['start_time', 'end_time', 'job_id', 'task_id', 'machine_id', 'status', 'sequence_no',
                              'total_sequence_num', 'max_cpu_num', 'avg_cpu_num', 'max_memory_usage', 'avg_memory_usage']
