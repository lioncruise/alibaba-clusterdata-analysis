import json


def node_conversion():
    file_path = 'E:/nodeinfo.json'
    new_file_path = 'E:/newnodeinfo.json'

    with open(file_path) as old_file, open(new_file_path, 'w+') as new_file:
        for line in old_file:
            old_json = json.loads(line)
            uid = list(old_json.keys())[0]
            cpu = old_json[uid]["resources"]["cpu"]
            mem = old_json[uid]["resources"]["mem"]
            disk_size = old_json[uid]["resources"]["disk_size"]
            max_key_instances = old_json[uid]["resources"]["max_key_instances"]
            match_tag = old_json[uid]["labels"]["match_tag"]
            exclude_tag = old_json[uid]["labels"]["exclude_tag"]

            new_json = {
                "uid": uid,
                "cpu": cpu,
                "memory": mem,
                "disk_size": disk_size,
                "max_key_instances": max_key_instances,
                "match_tag": match_tag,
                "exclude_tag": exclude_tag
            }

            new_line = json.dumps(new_json) + '\n'
            new_file.write(new_line)


if __name__ == '__main__':
    node_conversion()
