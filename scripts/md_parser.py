# -*- coding: utf-8 -*-
# @Author: JerryLinLinLin
# @Date:   2022-06-17 16:46:42
# @Last Modified by:   JerryLinLinLin
# @Last Modified time: 2022-06-21 18:13:05

import argparse
from mdutils.mdutils import MdUtils
from mdutils import Html

'''
This script is to generate markdown doc for all rule sets.
Genertate each rule description under ./rule/name/
Generate statistic under ./rule/
'''

def main(folder_path):
    for path, dirs, files in os.walk(folder_path):
        for filename in files:
            print("TO-DO")



if __name__ == "__main__":
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True,
                        help="rule folder path to generate markdown")
    args = parser.parse_args()
    main(args.path)
    exit(0)
