#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataProcessor import DataProcessor
from EBModel import EBModel
import os
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
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed_split/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    reports = dp.read_and_process_report_data(path_to_reports_data, "swt")
    dp.process_all_files(path_to_starter_repo, reports, path_to_processed_repo, path_to_temp)

def test_reading_in():
    dp = DataProcessor()

    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/birt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse-jdt/")
    dp.get_stackoverflow_data("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/")


def test_train():

    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt/"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 1
    train_split_index_end = 20
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project)
    eb.train()
def get_model_stats():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/swt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/SWT.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 1
    train_split_index_end = 1
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project)
    eb.train()

def get_model_stats_eclipse():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Eclipse_Platform_UI.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.ui"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 1
    train_split_index_end = 1
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project)
    print "ECLIPSE"
    eb.train()

def get_model_stats_jdt():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/eclipse-jdt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/JDT.xlsx.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.jdt.ui_temp/"
    train_split_index_start = 1
    train_split_index_end = 1
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "jdt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project)
    print "JDT"
    eb.train()

def get_model_stats_birt():
    path_to_stackoverflow_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/birt/"
    path_to_reports_data = "/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/Birt.xlsx"
    path_to_starter_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt"
    path_to_processed_repo = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_processed/"
    path_to_temp = "/home/ndg/users/carmst16/EmbeddingBugs/resources/source_files/test/eclipse.platform.swt_temp/"
    train_split_index_start = 1
    train_split_index_end = 1
    final_model = "/home/ndg/users/carmst16/EmbeddingBugs/resources/model/test.py"
    project = "swt"
    eb = EBModel(path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project)
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

def main():

    #test_reading_in()
    #test_read_reports()
    #test_train()
    process_files_swt()
    #get_model_stats()
    #get_model_stats_jdt()
    #get_model_stats_birt()
    #get_model_stats_eclipse()

if __name__ == "__main__":
    main()