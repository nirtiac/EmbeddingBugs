#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataProcessor import DataProcessor


#def deal_with_bugreport_data():
    #dp = DataProcessor()
    #base_path = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/"
    #projects = ["Birt", "Eclipse_Platform_UI", "SWT", "JDT"]
    #gitpaths = ["birt/", "eclipse.jdt.ui/", "eclipse.platform.swt/", "eclipse.platform.ui/"]
    #base_gitpath = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/"

    #for counter, project in enumerate(projects):
        #file_path = base_path + project + ".xlsx"
        #out_file = base_path + project + ".txt"
        #git_full_path = base_gitpath + gitpaths[counter]
        #processed_path = base_gitpath + gitpaths[counter][:-1] + "processed/"
        #reports = dp.process_bug_report_data(file_path, out_file, project, git_full_path, processed_path)

#TODO: call train here
def call_train_on_small_sample():
    path_to_stackoverflow_data = ""
    path_to_reports_data = ""
    path_to_starter_repo = ""

    EBM = EBMModel()

    return EBM


def call_train_birt():
    pass

def call_train_eclipse_platform_ui():
    pass

def call_train_jdt():
    pass

def call_train_swt():
    pass

def test_reading_in():
    dp = DataProcessor()

    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/birt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse-jdt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/")



def main():

    test_reading_in()

if __name__ == "__main__":
    main()