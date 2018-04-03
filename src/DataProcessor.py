__author__ = 'Caitrin'
import os
import itertools
from openpyxl import load_workbook
import cPickle as pickle
import xml.etree.ElementTree as ET

class BugReport:
    def __init__(self, reportID=None, bug_id=None, summary=None, description=None, report_time=None, report_timestamp=None, status=None, commit=None, commit_timestamp=None, files=None, filesLong=None):
        self.reportID = reportID
        self.bug_id = bug_id
        self.summary = summary
        self.description = description
        self.report_time = report_time
        self.report_timestamp = report_timestamp
        self.status = status
        self.commit = commit
        self.commit_timestamp = commit_timestamp
        self.files = files
        self.filesLong = filesLong



class DataProcessor:

    def __init__(self):
        pass


    def get_stackoverflow_data(self, directory):
        sent = []
        for f_path in os.listdir(directory):
            with open(f_path, 'r') as content_file:
                content = content_file.read()
                tokens = content.split()
                code = [s for s in tokens if "@" in s]
                nl = [s for s in tokens if "@" not in s]
                sent.extend([zip(x, nl) for x in itertools.permutations(code, len(nl))])
                sent.append(tokens)

        return sent


    def process_bug_report_data(self, file_name, out_file, project, gitpath, newDir):
        wb = load_workbook(filename=file_name)
        sheetname = project.lower()
        ws = wb[sheetname]
        #header = [cell.value for cell in wb.rows[0]]

        reports = []

        for row in ws.rows[1:]:
            args = [cell.value for cell in row]
            report = BugReport(*args)
            reports.append(report)

        os.chdir(gitpath)
        first_commit = str(reports[0].commit)
        first_report_id = str(reports[0].reportID)

        os.system("git checkout " + first_commit+"~1")
        newDirPath = newDir + first_report_id + "/"
        os.makedirs(newDirPath)
        os.system("cp -r * " + newDir)
        last_commit = first_commit + "~1"


        #because reports is an ordered list, as inserted, so we're inserting as they are in the dataset.
        #really have to go and verify this when you build your reconstruction function

        for report in reports[1:]:
            new_commit = str(report.commit) + "~1"
            new_report_id = str(report.reportID)
            newDirPath = newDir + new_report_id + "/"
            os.makedirs(newDirPath)
            os.system("git checkout " + new_commit)
            print ('git diff --name-status %s %s | grep ".java$" | grep "^A"' %(last_commit, new_commit))

            #print os.system('git diff --name-status %s %s | grep ".java$" | grep "^A"' %(last_commit, new_commit))
            #ok I guess I  now only care about any file not about sorting them eh

            os.system('git diff --name-status %s %s | grep ".java$" | grep "^A" | cut -f2 | xargs -I "{}" cp {} %s' %(last_commit, new_commit, newDirPath))
            os.system('git diff --name-status %s %s | grep ".java$" | grep "^M" | cut -f2 | xargs -I "{}" cp {} %s' %(last_commit, new_commit, newDirPath))
            os.system('git diff --name-status %s %s | grep ".java$" | grep "^D"| cut -f2| xargs -I "{}" touch %sDEL_{}' %(last_commit, new_commit, newDirPath))

            last_commit = new_commit


        #with open(out_file, "wb") as f:
        #    for report in reports:
        #        f.write(str(report.reportID) + "," + str(report.commit) + "\n")

        reportOutFile = project + "_reports_processed.pkl"
        pickle.dump(reports, open("/home/ndg/users/carmst16/EmbeddingBugs/resources/bugreport/" + reportOutFile))

        return reports


def readBugReport():
    bug_reports = []
    total = 0
    i=0
    path = "dataset/"
    #project_files = ['Birt.xml', 'Eclipse_Platform_UI.xml', 'JDT.xml', 'SWT.xml']
    project_files = ['Birt.xml', 'Eclipse_Platform_UI.xml']
    for file in project_files:
        tree = ET.parse(path+file)
        root = tree.getroot()
        for table in root.iter('table'):
            i=i+1
            for column in table.findall('column'):
                if column is not None:
                    name = column.get('name')
                    if name == "id":
                        reportID = column.text
                        #print(reportID)
                    if name=="bug_id":
                        bug_id = column.text
                        #print(bug_id)
                    if name == "summary":
                        summary = column.text
                        #print(summary)
                    if name=="description":
                        description = column.text
                        #print(description)
                    if name == "report_time":
                        report_time = column.text
                        #print(report_time)
                    if name=="report_timestamp":
                        report_timestamp = column.text
                        #print(report_timestamp)
                    if name == "status":
                        status = column.text
                        #print(status)
                    if name=="commit":
                        commit = column.text
                        #print(commit)
                    if name == "commit_timestamp":
                        commit_timestamp = column.text
                        #print(commit_timestamp)
                    if name=="files":
                        files = column.text
                        #print(files)

            #1.Bug reports with status marked as resolved fixed, veri- fied fixed, or closed fixed were collected for evaluation
            if (status=="resolved fixed" or status =="closed fixed" or status=="verified fixed"):
                ## 3.  Bug reports without fixed files are also ignored because they are considered not functional
                if (files is not None):
                    total= total+1
                    bug_reports.append(BugReport(reportID,bug_id,summary,description,report_time,report_timestamp,status,commit,commit_timestamp,files))
    print("all Total:"+str(i))
    print("final report Total:" + str(total))
    return(bug_reports)

bug_reports = readBugReport()
##### This is just for reference, how you can access each bug report !!!
#for bug_report in bug_reports:
    #print(bug_report.bug_id +" "+bug_report.summary)
