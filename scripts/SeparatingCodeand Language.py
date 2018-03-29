import xml.etree.ElementTree as ET
import xml.etree.cElementTree as CET

rootCode = CET.Element("posts")
rootLanguage = CET.Element("posts")

def readXMLFile():
    files = ['birt.xml', 'eclipse.xml', 'eclipse-jdt.xml', 'swt.xml']
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        #print(root)
        for child in root:
            print( child.attrib['Id']+" "+child.attrib['Title']+" "+child.attrib['Body'])
            str_idx=child.attrib['Body'].find('<pre><code>')
            strt_of_strng=0
            body=""
            code=[]
            if str_idx==-1:
                body = child.attrib['Body']
            else:
                while(str_idx!=-1):
                    str_idx = child.attrib['Body'][strt_of_strng:].find('<pre><code>')
                    lst_idx = child.attrib['Body'][strt_of_strng:].find('</code></pre>')
                    if str_idx!=-1:
                        code.append(child.attrib['Body'][strt_of_strng+str_idx:strt_of_strng+lst_idx + 13])
                    if str_idx!=-1:
                        body = body + child.attrib['Body'][strt_of_strng:strt_of_strng+str_idx]
                    else:
                        body = body + child.attrib['Body'][strt_of_strng:]
                    strt_of_strng=strt_of_strng+lst_idx + 13
            if code!="":
                for i in code:
                    CET.SubElement(rootCode, "row", Id=child.attrib['Id'],Title=child.attrib['Title'], CreationDate= child.attrib['CreationDate'], Body=i )

            CET.SubElement(rootLanguage, "row", Id=child.attrib['Id'], Title=child.attrib['Title'],CreationDate= child.attrib['CreationDate'], Body=body)

    treeCode = CET.ElementTree(rootCode)
    treeCode.write("AllCode1.xml")

    treeLanguage = CET.ElementTree(rootLanguage)
    treeLanguage.write("AllLang1.xml")

#files = ['birt.xml','eclipse.xml','eclipse-jdt.xml','swt.xml']
readXMLFile()
