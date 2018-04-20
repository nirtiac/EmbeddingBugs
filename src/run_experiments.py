#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataProcessor import DataProcessor
from EBModel import EBModel
import os
import sys
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

def process_files_swt():
    dp = DataProcessor()
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split_text_trial/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp_again/"
    reports = dp.read_and_process_report_data(path_to_reports_data, "swt")
    dp.process_all_files(path_to_starter_repo, reports, path_to_processed_repo, path_to_temp)


def process_files_birt():
    dp = DataProcessor()
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Birt.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt_temp/"
    reports = dp.read_and_process_report_data(path_to_reports_data, "birt")
    dp.process_all_files(path_to_starter_repo, reports, path_to_processed_repo, path_to_temp)


def process_files_jdt():
    dp = DataProcessor()
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/JDT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_temp/"
    reports = dp.read_and_process_report_data(path_to_reports_data, "jdt")
    dp.process_all_files(path_to_starter_repo, reports, path_to_processed_repo, path_to_temp)


def process_files_eclipse():
    dp = DataProcessor()
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Eclipse_Platform_UI.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui_temp/"
    reports = dp.read_and_process_report_data(path_to_reports_data, "eclipse_platform_ui")
    dp.process_all_files(path_to_starter_repo, reports, path_to_processed_repo, path_to_temp)

def test_reading_in():
    dp = DataProcessor()

    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/birt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse-jdt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/")


def test_train():

    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split_text/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 20
    train_split_index_end = 24
    accuracy_at_k_value = 25
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    eb.train()

def get_vocab_coverage():

    #who the fuck made this many params
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split_text/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 20
    train_split_index_end = 24
    accuracy_at_k_value = 25
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    eb.get_model_coverage()

def get_model_stats_swt():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split_text/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 11
    train_split_index_end = 40
    accuracy_at_k_value = 100

    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    eb.train()

def get_model_stats_eclipse():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Eclipse_Platform_UI.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 11
    train_split_index_end = 40
    accuracy_at_k_value = 100

    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "eclipse_platform_ui"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    print "ECLIPSE"
    eb.train()

def get_model_stats_jdt():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse-jdt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/JDT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_temp/"
    train_split_index_start = 11
    train_split_index_end = 40
    accuracy_at_k_value = 100

    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "jdt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    print "JDT"
    eb.train()

def get_model_stats_birt():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/birt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Birt.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/birt_temp/"
    train_split_index_start = 11
    train_split_index_end = 40
    accuracy_at_k_value = 100

    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "birt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)
    print "BIRT"
    eb.train()

def test_read_reports():
    bug_file_path = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    project = "swt"
    #path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/"
    dp = DataProcessor()

    already_processed = False
    previous_commit = None
    all_scores = []
    path_to_starter = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    #print dp.get_stackoverflow_data(path_to_stackoverflow_data)
    reports = dp.read_and_process_report_data(bug_file_path, project)
    print "finished processing"
    for report in reports[1:2]:
        report_text = report.processed_description
        if not already_processed:
            dp.create_file_repo(path_to_starter, report, path_to_processed)
            already_processed = True
            previous_commit = report.commit
        else:
            dp.update_file_repo(previous_commit, report.commit, path_to_starter, path_to_temp, path_to_processed)
            previous_commit = report.commit

        report_text = report.processed_description

        for dir_, _, files in os.walk(path_to_processed):
            for fileName in files:
                relDir = os.path.relpath(dir_, path_to_processed)
                relFile = os.path.join(relDir, fileName)
                full_path = path_to_processed + relFile
                with open(full_path, 'r') as content_file:
                    content = content_file.readlines()
                    for line in content:
                        l = line.split(",")
                        l_content.append(l)

def test_scoring():


    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split_text/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 20
    train_split_index_end = 50
    accuracy_at_k_value = 25
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value)

    print eb.MAP([[0,0,0,0], [0,0,0,0], [0,0,0,0]])

def main():

    #test_scoring()

    #test_train()
    #get_vocab_coverage()
    # comm = sys.argv[1]
    # if comm == "test":
    #     test_train()
    #
    # if comm == "process_swt":
    #     process_files_swt()
    #
    # if comm == "process_birt":
    #     process_files_birt()
    #
    # if comm == "process_eclipse":
    #     process_files_eclipse()
    #
    # if comm == "process_jdt":
    #     process_files_jdt()

    #test_reading_in()
    #test_read_reports()
    #process_files_swt()
    #process_files_birt()
    #process_files_eclipse()
    #process_files_jdt()
    get_model_stats_swt()
    #get_model_stats_jdt()
    #get_model_stats_birt()

    #get_model_stats_eclipse()

if __name__ == "__main__":
    main()