# -*- coding: utf-8 -*-
# @Author: JerryLinLinLin
# @Date:   2022-06-15 23:23:26
# @Last Modified by:   JerryLinLinLin
# @Last Modified time: 2022-06-27 17:48:41

'''
This script is to validate hips rules with schema from https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema
'''

import os
import json
import argparse
from jsonschema import validate
from urllib.request import urlopen


def main(folder_path:str) -> int:
    """Validate rules

    Args:
        folder_path (str): rule folder path

    Returns:
        int: 0 if succeed
    """
    rule_schema_url = "https://raw.githubusercontent.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema/master/rule_schema.json"
    auto_schema_rul = "https://raw.githubusercontent.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema/master/auto_schema.json"

    print("Open schema urls")
    rule_schema_res = urlopen(rule_schema_url).read()
    auto_schema_res = urlopen(auto_schema_rul).read()

    print("Load shcema")
    rule_schema = json.loads(rule_schema_res.decode('utf-8'))
    auto_schema = json.loads(auto_schema_res.decode('utf-8'))

    # walk through rule sets
    for path, dirs, files in sorted(os.walk(folder_path)):
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

    print("PASS! validate_rules.py")
    return 0


if __name__ == "__main__":
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True,
                        help="folder path to check")
    args = parser.parse_args()
    main(args.path)
    exit(0)
