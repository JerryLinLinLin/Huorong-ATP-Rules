# -*- coding: utf-8 -*-
# @Author: JerryLinLinLin
# @Date:   2022-06-16 17:47:09
# @Last Modified by:   JerryLinLinLin
# @Last Modified time: 2022-06-17 17:45:15

'''
Merge all rule.json into one file.
Merge all auto.json into one file.
'''

import os
import json
import argparse


def main(input_path, output_path):

    # sum of rules and auto
    rule_sum_dict = dict(json.loads(
        '{"ver":"5.0","tag":"hipsuser","data":[]}'))
    auto_sum_dict = dict(json.loads(
        '{"ver":"5.0","tag":"hipsuser_auto","data":{}}'))

    for path, dirs, files in os.walk(input_path):
        for filename in files:

            if filename == "rule.json":
                rule_full_path = os.path.join(path, filename)
                rule_dict = json.load(open(rule_full_path))
                print("Merging file: %s" % rule_full_path)
                # loop each rule in sub rule files
                for each_rule in rule_dict["data"]:
                    rule_sum_dict["data"] = rule_sum_dict["data"] + \
                        [each_rule]  # add them up

            if filename == "auto.json":
                auto_full_path = os.path.join(path, filename)
                auto_dict = json.load(open(auto_full_path))
                print("Merging file: %s" % auto_full_path)
                # loop each auto in sub auto files
                for each_key in dict(auto_dict["data"]).keys():
                    # check if key already exist
                    if dict(auto_sum_dict["data"]).get(each_key) is None:
                        # frist one
                        auto_sum_dict["data"][each_key] = auto_dict["data"][each_key]
                    else:
                        auto_sum_dict["data"][each_key] = auto_sum_dict["data"][each_key] + \
                            auto_dict["data"][each_key]  # add list to key

    # dump json
    os.makedirs(output_path, exist_ok=True)
    with open(os.sep.join([output_path, "Rule.json"]), 'w') as f:
        json.dump(rule_sum_dict, f, indent=4, sort_keys=True)
    with open(os.sep.join([output_path, "Auto.json"]), 'w') as f:
        json.dump(auto_sum_dict, f, indent=4, sort_keys=True)

    print("Output Rule file to %s" % os.sep.join([output_path, "Rule.json"]))
    print("Output Rule file to %s" % os.sep.join([output_path, "Auto.json"]))


if __name__ == "__main__":
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True,
                        help="rule folder path to merge")
    parser.add_argument("--output", type=str, required=True,
                        help="output folder path")
    args = parser.parse_args()
    main(args.path, args.output)
    exit(0)
