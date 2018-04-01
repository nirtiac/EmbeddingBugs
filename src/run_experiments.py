#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataProcessor import DataProcessor


def deal_with_bugreport_data():
    dp = DataProcessor()
    base_path = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/"
    projects = ["Birt", "Eclipse_Platform_UI", "SWT", "JDT"]
    for project in projects:
        file_path = base_path + project + ".xlsx"
        out_file = base_path + project + ".txt"
        reports = dp.process_bug_report_data(file_path, out_file, project)

def test():
    print "hi"

def main():
    test()

    deal_with_bugreport_data()

if __name__ == "__main__":
    main()