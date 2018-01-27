CREATE DATABASE IF NOT EXISTS alibaba_cluster;
USE alibaba_cluster;


CREATE TABLE server_event
(
  id           INT AUTO_INCREMENT
    PRIMARY KEY,
  timestamp    INT          NULL,
  machine_id   INT          NULL,
  event_type   VARCHAR(255) NULL,
  event_detail VARCHAR(255) NULL,
  cpu          INT          NULL,
  memory       DOUBLE       NULL,
  disk         DOUBLE       NULL
)
  ENGINE = InnoDB;


CREATE TABLE server_usage
(
  id         INT AUTO_INCREMENT
    PRIMARY KEY,
  timestamp  INT    NULL,
  machine_id INT    NULL,
  cpu        DOUBLE NULL,
  memory     DOUBLE NULL,
  disk       DOUBLE NULL,
  cpu_1min   DOUBLE NULL,
  cpu_5min   DOUBLE NULL,
  cpu_15min  DOUBLE NULL
)
  ENGINE = InnoDB;


CREATE TABLE container_event
(
  id               INT AUTO_INCREMENT
    PRIMARY KEY,
  timestamp        INT          NULL,
  event_type       VARCHAR(255) NULL,
  instance_id      INT          NULL,
  machine_id       INT          NULL,
  cpu_requested    INT          NULL,
  memory_requested DOUBLE       NULL,
  disk_requested   DOUBLE       NULL,
  cpu_ids          VARCHAR(255) NULL
)
  ENGINE = InnoDB;


CREATE TABLE container_usage
(
  id                                  INT AUTO_INCREMENT
    PRIMARY KEY,
  timestamp                           INT    NULL,
  instance_id                         INT    NULL,
  cpu                                 DOUBLE NULL,
  memory                              DOUBLE NULL,
  disk                                DOUBLE NULL,
  cpu_1min                            DOUBLE NULL,
  cpu_5min                            DOUBLE NULL,
  cpu_15min                           DOUBLE NULL,
  avg_cycles_per_instruction          DOUBLE NULL,
  avg_cache_miss_per_1000_instruction DOUBLE NULL,
  max_cycles_per_instruction          DOUBLE NULL,
  max_cache_miss_per_1000_instruction DOUBLE NULL
)
  ENGINE = InnoDB;


CREATE TABLE batch_task
(
  id                  INT AUTO_INCREMENT
    PRIMARY KEY,
  create_time         INT          NULL,
  end_time            INT          NULL,
  job_id              INT          NULL,
  task_id             INT          NULL,
  num_of_instances    INT          NULL,
  status              VARCHAR(255) NULL,
  cpu_per_instance    INT          NULL,
  memory_per_instance DOUBLE       NULL
)
  ENGINE = InnoDB;


CREATE TABLE batch_instance
(
  id                 INT AUTO_INCREMENT
    PRIMARY KEY,
  start_time         INT          NULL,
  end_time           INT          NULL,
  job_id             INT          NULL,
  task_id            INT          NULL,
  machine_id         INT          NULL,
  status             VARCHAR(255) NULL,
  sequence_no        INT          NULL,
  total_sequence_num INT          NULL,
  max_cpu_num        DOUBLE       NULL,
  avg_cpu_num        DOUBLE       NULL,
  max_memory_usage   DOUBLE       NULL,
  avg_memory_usage   DOUBLE       NULL
)
  ENGINE = InnoDB;


/*
 2018/1/27 数据库变更脚本
 修改server_usage和container_usage中和CPU load average相关的列名
*/
ALTER TABLE server_usage CHANGE cpu_1min cpu_load_1min DOUBLE;
ALTER TABLE server_usage CHANGE cpu_5min cpu_load_5min DOUBLE;
ALTER TABLE server_usage CHANGE cpu_15min cpu_load_15min DOUBLE;
ALTER TABLE container_usage CHANGE cpu_1min cpu_load_1min DOUBLE;
ALTER TABLE container_usage CHANGE cpu_5min cpu_load_5min DOUBLE;
ALTER TABLE container_usage CHANGE cpu_15min cpu_load_15min DOUBLE;