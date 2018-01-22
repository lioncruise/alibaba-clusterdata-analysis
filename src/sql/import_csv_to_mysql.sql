-- Before you run this SQL script, you should make sure all CSV file in /alibaba_cluster_csv/ directory.

LOAD DATA LOCAL infile '/alibaba_cluster_csv/server_event.csv'
INTO TABLE server_event
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7)
SET
timestamp = nullif(@c1,''),
machine_id = nullif(@c2,''),
event_type = nullif(@c3,''),
event_detail = nullif(@c4,''),
cpu = nullif(@c5,''),
memory = nullif(@c6,''),
disk = nullif(@c7,'');


LOAD DATA LOCAL infile '/alibaba_cluster_csv/server_usage.csv'
INTO TABLE server_usage
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7, @c8)
SET
timestamp = nullif(@c1,''),
machine_id = nullif(@c2,''),
cpu = nullif(@c3,''),
memory = nullif(@c4,''),
disk = nullif(@c5,''),
cpu_1min = nullif(@c6,''),
cpu_5min = nullif(@c7,''),
cpu_15min = nullif(@c8,'');


LOAD DATA LOCAL infile '/alibaba_cluster_csv/container_event.csv'
INTO TABLE container_event
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7, @c8)
SET
timestamp = nullif(@c1,''),
event_type = nullif(@c2,''),
instance_id = nullif(@c3,''),
machine_id = nullif(@c4,''),
cpu_requested = nullif(@c5,''),
memory_requested = nullif(@c6,''),
disk_requested = nullif(@c7,''),
cpu_ids = nullif(@c8,'');


LOAD DATA LOCAL infile '/alibaba_cluster_csv/container_usage.csv'
INTO TABLE container_usage
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7, @c8, @c9, @c10, @c11, @c12)
SET
timestamp = nullif(@c1,''),
instance_id = nullif(@c2,''),
cpu = nullif(@c3,''),
memory = nullif(@c4,''),
disk = nullif(@c5,''),
cpu_1min = nullif(@c6,''),
cpu_5min = nullif(@c7,''),
cpu_15min = nullif(@c8,''),
avg_cycles_per_instruction = nullif(@c9,''),
avg_cache_miss_per_1000_instruction = nullif(@c10,''),
max_cycles_per_instruction = nullif(@c11,''),
max_cache_miss_per_1000_instruction = nullif(@c12,'');


LOAD DATA LOCAL infile '/alibaba_cluster_csv/batch_task.csv'
INTO TABLE batch_instance
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7, @c8)
SET
create_time = nullif(@c1,''),
end_time = nullif(@c2,''),
job_id = nullif(@c3,''),
task_id = nullif(@c4,''),
num_of_instances = nullif(@c5,''),
status = nullif(@c6,''),
cpu_per_instance = nullif(@c7,''),
memory_per_instance = nullif(@c8,'');


LOAD DATA LOCAL infile '/alibaba_cluster_csv/batch_instance.csv'
INTO TABLE batch_instance
fields terminated BY ','
lines terminated BY '\n'
(@c1, @c2, @c3, @c4, @c5, @c6, @c7, @c8, @c9, @c10, @c11, @c12)
SET
start_time = nullif(@c1,''),
end_time = nullif(@c2,''),
job_id = nullif(@c3,''),
task_id = nullif(@c4,''),
machine_id = nullif(@c5,''),
status = nullif(@c6,''),
sequence_no = nullif(@c7,''),
total_sequence_num = nullif(@c8,''),
max_cpu_num = nullif(@c9,''),
avg_cpu_num = nullif(@c10,''),
max_memory_usage = nullif(@c11,''),
avg_memory_usage = nullif(@c12,'');
