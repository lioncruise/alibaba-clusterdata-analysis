import json


def pod_conversion():
    file_path = 'E:/instanceinfo.json'
    new_file_path = 'E:/newinstanceinfo.json'

    with open(file_path) as old_file, open(new_file_path, 'w+') as new_file:
        for line in old_file:
            old_json = json.loads(line)
            uid = list(old_json.keys())[0]
            cpu = old_json[uid]["resources"]["cpu"]
            mem = old_json[uid]["resources"]["mem"]
            disk_size = old_json[uid]["resources"]["disk_size"]
            match_tag = old_json[uid]["labels"]["match_tag"]
            exclude_tag = old_json[uid]["labels"]["exclude_tag"]
            exclusive_tag = old_json[uid]["labels"]["exclusive_tag"]
            is_key_instance = old_json[uid]["is_key_instance"]
            app_group = old_json[uid]["app_group"]
            host_id = old_json[uid]["host_id"]

            new_json = {
                "uid": uid,
                "cpu": cpu,
                "memory": mem,
                "disk_size": disk_size,
                "match_tag": match_tag,
                "exclude_tag": exclude_tag,
                "exclusive_tag": exclusive_tag,
                "is_key_instance": is_key_instance,
                "app_group": app_group,
                "host_id": host_id
            }

            new_line = json.dumps(new_json) + '\n'
            new_file.write(new_line)


if __name__ == '__main__':
    pod_conversion()
