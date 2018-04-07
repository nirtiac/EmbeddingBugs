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

from src import EBModel
from src import preprocessingCodeLang

def main():

    preprocessingCodeLang.readXMLFile()
    files = ['birt', 'eclipse', 'eclipse-jdt', 'swt']
    path = "/Users/shrutibhanderi/PycharmProjects/EmbeddingBugs/samplefiles/"
    i = 0
    for file in files:
        i=i+1
        content = open("/Users/shrutibhanderi/PycharmProjects/EmbeddingBugs/samplefiles/" + file + "-post" + str(i) + ".txt","r")
        EBModel.train(content)

if __name__ == "__main__":
    main()