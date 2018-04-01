__author__ = 'Caitrin'
import os
import itertools
from openpyxl import load_workbook


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
        first_commit = reports[0].commit
        first_report_id = reports[0].reportID

        os.system("git checkout " + first_commit+"~1")
        newDirPath = newDir + first_report_id + "/"
        os.mkdir(newDirPath)
        os.system("cp -r * " + newDir)
        for report in reports:
            new_commit = report.commit
            new_report_id = report.reportID
            'git diff --name-status 2143203 602d549 | grep ".java$" | grep "^A"'
            'git diff --name-status 2143203 602d549 | grep ".java$" | grep "^M"'
            'git diff --name-status 2143203 602d549 | grep ".java$" | grep "^D"'



        with open(out_file, "wb") as f:
            for report in reports:
                f.write(str(report.reportID) + "," + str(report.commit) + "\n")