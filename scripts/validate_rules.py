import os
import json
from jsonschema import validate
from urllib.request import urlopen


def main():
    rule_schema_url = "https://raw.githubusercontent.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema/master/rule_schema.json"
    auto_schema_rul = "https://raw.githubusercontent.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema/master/auto_schema.json"

    print("Open schema urls")
    rule_schema_res = urlopen(rule_schema_url).read()
    auto_schema_res = urlopen(auto_schema_rul).read()

    print("Load shcema")
    rule_schema = json.loads(rule_schema_res.decode('utf-8'))
    auto_schema = json.loads(auto_schema_res.decode('utf-8'))

    # walk through rule sets
    for path, dirs, files in os.walk(os.getcwd() + "\\rules"):
        for filename in files:

            if filename == "rule.json":
                rule_full_path = os.path.join(path, filename)
                rule_json = json.load(open(rule_full_path))

                print("Validating rule: %s" % rule_full_path)
                validate(instance=rule_json, schema=rule_schema)
                continue

            if filename == "auto.json":
                auto_full_path = os.path.join(path, filename)
                auto_json = json.load(open(auto_full_path))

                print("Validating auto: %s" % auto_full_path)
                validate(instance=auto_json, schema=auto_schema)
                continue
            
            if filename != "":
                full_path = os.path.join(path, filename)
                print("Illegal filename: %s" % full_path)
                exit(-1)
            
    print("PASS! validate_rules.py")
    return 0

if __name__ == "__main__":
    main()
    exit(0)
