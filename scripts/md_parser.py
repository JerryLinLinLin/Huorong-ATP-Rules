# -*- coding: utf-8 -*-
# @Author: JerryLinLinLin
# @Date:   2022-06-17 16:46:42
# @Last Modified by:   JerryLinLinLin
# @Last Modified time: 2023-04-09 12:47:03

import argparse
import hashlib
import os
import json
from mdutils.mdutils import MdUtils
from mdutils import Html

'''
This script is to generate markdown doc for all rule sets.
Genertate each rule description under ./rule/name/
Generate statistic under ./rule/
'''


def get_file_sha256(file_path: str) -> str:
    """Get a file sha256 checksum

    Args:
        file_path (str): file to check

    Returns:
        str: sha256
    """
    with open(file_path, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash


def get_action_type_dict(action_type: int) -> dict:
    """Get action type dict format of a policy

    Args:
        action_type (int): action type int in a policy

    Returns:
        dict: status of action type
    """
    action_type_dict = dict()
    action_type_dict["Create"] = (action_type >> 0) & 1
    action_type_dict["Read"] = (action_type >> 1) & 1
    action_type_dict["Write"] = (action_type >> 2) & 1
    action_type_dict["Delete"] = (action_type >> 3) & 1
    action_type_dict["Execute"] = (action_type >> 4) & 1
    return action_type_dict


def get_action_type_string_zh_cn(action_type: int) -> str:
    """zh_cn: Get action type string description

    Args:
        action_type (int): action type int in a policy

    Returns:
        str: string description
    """
    action_type_dict = get_action_type_dict(action_type)
    action_type_string = str()
    action_type_string = action_type_string + \
        ("创建、" if action_type_dict["Create"] == 1 else "")
    action_type_string = action_type_string + \
        ("读取、" if action_type_dict["Read"] == 1 else "")
    action_type_string = action_type_string + \
        ("写入、" if action_type_dict["Write"] == 1 else "")
    action_type_string = action_type_string + \
        ("删除、" if action_type_dict["Delete"] == 1 else "")
    action_type_string = action_type_string + \
        ("执行、" if action_type_dict["Execute"] == 1 else "")
    action_type_string = action_type_string[0:len(action_type_string) - 1]
    return action_type_string


def get_montype_string_zh_cn(montype: int) -> str:
    """zh_cn: Get montype string description

    Args:
        montype (int): montype int in a policy

    Returns:
        str: string description
    """
    if (montype == 0):
        return "程序"
    if (montype == 1):
        return "文件"
    if (montype == 2):
        return "注册表"


def readme_zh_cn(rule_set_path: str, rule_dict: dict, mdFile: MdUtils):
    """zh_cn: Generate readme for each ruleset, option for generate sum readme

    Args:
        rule_set_path (str): current rule set path
        rule_dict (dict): json content of a rule set
        mdFile (MdUtils): pass if cumulative, otherwise pass None
    """
    rule_set_name = str(rule_set_path)[str(rule_set_path).rindex(
        os.path.sep) + 1:len(str(rule_set_path))]
    isCumulative = True
    if mdFile is None:
        isCumulative = False
        mdFile = MdUtils(file_name=os.sep.join([rule_set_path, "README"]))
        mdFile.new_line("简体中文 | [English](README_en_us.md)")
        mdFile.new_line()
        mdFile.new_line()
        mdFile.create_marker("table of content")
    mdFile.new_header(level=1, title=rule_set_name)
    for each_rule in rule_dict["data"]:
        mdFile.new_header(level=2, title=each_rule["name"])
        mdFile.new_line(
            text="状态：" + ("启用" if int(each_rule["power"]) == 1 else "未启用"))
        mdFile.new_paragraph(text="行为描述：源程序`{src_proc}`做出以下操作时，{action}".format(
            src_proc=each_rule["procname"], action="提示用户处理" if int(each_rule["treatment"]) == 1 else "自动阻止"))
        policy_list = list()
        for each_action in each_rule["policies"]:
            policy_list.append("对路径为`{action_path}`的{type}进行**{action}**操作".format(action_path=each_action["res_path"], type=get_montype_string_zh_cn(
                each_action["montype"]), action=get_action_type_string_zh_cn(each_action["action_type"])))
        mdFile.new_list(policy_list)

    mdFile.new_line(text="rule.json hash: {_sha256}".format(
        _sha256=get_file_sha256(os.path.join(rule_set_path, "rule.json"))), bold_italics_code='bi')
    if (isCumulative is False):
        mdFile.new_table_of_contents(table_title='目录', depth=2, marker="##--[table of content]--##")
        mdFile.create_md_file()

def get_action_type_string_en_us(action_type: int) -> str:
    """en_us: Get action type string description

    Args:
        action_type (int): action type int in a policy

    Returns:
        str: string description
    """
    action_type_dict = get_action_type_dict(action_type)
    action_type_string = str()
    action_type_string = action_type_string + \
        ("Create, " if action_type_dict["Create"] == 1 else "")
    action_type_string = action_type_string + \
        ("Read, " if action_type_dict["Read"] == 1 else "")
    action_type_string = action_type_string + \
        ("Write, " if action_type_dict["Write"] == 1 else "")
    action_type_string = action_type_string + \
        ("Delete, " if action_type_dict["Delete"] == 1 else "")
    action_type_string = action_type_string + \
        ("Execute, " if action_type_dict["Execute"] == 1 else "")
    action_type_string = action_type_string[0:len(action_type_string) - 2]
    return action_type_string


def get_montype_string_en_us(montype: int) -> str:
    """en_us: Get montype string description

    Args:
        montype (int): montype int in a policy

    Returns:
        str: string description
    """
    if (montype == 0):
        return "program"
    if (montype == 1):
        return "file"
    if (montype == 2):
        return "registry"


def readme_en_us(rule_set_path: str, rule_dict: dict, mdFile: MdUtils):
    """en_us: Generate readme for each ruleset, option for generate sum readme

    Args:
        rule_set_path (str): current rule set path
        rule_dict (dict): json content of a rule set
        mdFile (MdUtils): pass if cumulative, otherwise pass None
    """
    rule_set_name = str(rule_set_path)[str(rule_set_path).rindex(
        os.path.sep) + 1:len(str(rule_set_path))]
    isCumulative = True
    if mdFile is None:
        isCumulative = False
        mdFile = MdUtils(file_name=os.sep.join([rule_set_path, "README_en_us"]))
        mdFile.new_line("[简体中文](README.md) | English")
        mdFile.new_line()
        mdFile.new_line()
        mdFile.create_marker("table of content")
    mdFile.new_header(level=1, title=rule_set_name)
    for each_rule in rule_dict["data"]:
        mdFile.new_header(level=2, title=each_rule["name"])
        mdFile.new_line(
            text="Status: " + ("Enabled" if int(each_rule["power"]) == 1 else "Disabled"))
        mdFile.new_paragraph(text="Behavioral Description: ")
        mdFile.new_line(text="When the source process`{src_proc}`initializes the following actions, {action}".format(
            src_proc=each_rule["procname"], action="HIPS module should let the user decide them." if int(each_rule["treatment"]) == 1 else "HIPS module should automatically block them."))
        policy_list = list()
        for each_action in each_rule["policies"]:
            policy_list.append("`{action}` the {type} under the path `{action_path}`".format(action_path=each_action["res_path"], type=get_montype_string_en_us(
                each_action["montype"]), action=get_action_type_string_en_us(each_action["action_type"])))
        mdFile.new_list(policy_list)

    mdFile.new_line(text="rule.json hash: {_sha256}".format(
        _sha256=get_file_sha256(os.path.join(rule_set_path, "rule.json"))), bold_italics_code='bi')
    if (isCumulative is False):
        mdFile.new_table_of_contents(table_title='Contents', depth=2, marker="##--[table of content]--##")
        mdFile.create_md_file()

def main(folder_path:str):
    """Main

    Args:
        folder_path (str): rule folder
    """
    mdFile_zh_cn = MdUtils(file_name=os.sep.join([folder_path, "README"]))
    mdFile_en_us = MdUtils(file_name=os.sep.join([folder_path, "README_en_us"]))

    mdFile_zh_cn.new_line("简体中文 | [English](README_en_us.md)")
    mdFile_zh_cn.new_line()
    mdFile_zh_cn.new_line()
    mdFile_en_us.new_line("[简体中文](README.md) | English")
    mdFile_en_us.new_line()
    mdFile_en_us.new_line()

    mdFile_zh_cn.create_marker("table of content")
    mdFile_en_us.create_marker("table of content")

    for path, dirs, files in sorted(os.walk(folder_path)):
        for filename in files:
            if filename == "rule.json":
                rule_full_path = os.path.join(path, filename)
                rule_dict = json.load(open(rule_full_path))
                readme_zh_cn(path, rule_dict, None)
                readme_zh_cn(path, rule_dict, mdFile_zh_cn)

                readme_en_us(path, rule_dict, None)
                readme_en_us(path, rule_dict, mdFile_en_us)

    mdFile_zh_cn.new_table_of_contents(table_title='目录', depth=2, marker="##--[table of content]--##")
    mdFile_zh_cn.create_md_file()

    mdFile_en_us.new_table_of_contents(table_title='Contents', depth=2, marker="##--[table of content]--##")
    mdFile_en_us.create_md_file()



if __name__ == "__main__":
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True,
                        help="rule folder path to generate markdown")
    args = parser.parse_args()
    main(args.path)
    exit(0)
