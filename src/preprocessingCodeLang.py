import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
from nltk.corpus import words

class Preprocessor:
    def __init__(self):
        pass

    def camel_case_split(self, identifier):
        '''

        :param identifier: the Camel casing word we want to split
        :return: the list which has splitted the Camel Case word
        '''
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        return [m.group(0) for m in matches]

    def preprocessCode(self, code):
        '''
        This method preprocesses the Code in the post.
        :param code: all the code from one post
        :return: preprocessed code tokens
        '''
        preCode = []
        word_list=[]
        i=0
        stopwords = ['code', 'lt', 'gt', 'pre', 'xx']
        if type(code) == list:
            for sen in code:
                word_list.extend(nltk.word_tokenize(sen))
        else:
            word_list = nltk.word_tokenize(code)
        word_list = [word for word in word_list if word.isalpha()]
        word_list = [w for w in word_list if not w in stopwords]
        word_list = [w for w in word_list if not len(w)==1]
        for w in word_list:
            temp = camel_case_split(w)
            if len(temp)>1:
                for t in temp:
                    t = "@"+t+"@"
                    if (len(t)!=1) :
                        t=t.lower()
                        preCode.append(t)
                w="@"+w+"@"
                w=w.lower()
                #if w not in preCode:
                preCode.append(w)
            else:
                w=w.lower()
                w = "@"+w+"@"
                #if w not in preCode:
                preCode.append(w)
        i = i+1
        return preCode


    def preprocessLang(self, lang):
        '''
            This method preprocesses the Natural language in the post.
            :param code: all the natural language from one post
            :return: preprocessed language tokens
            '''
        preLang=[]
        other_words = ['http']
        sent_text = nltk.sent_tokenize(lang)
        for s in sent_text:
            word_list = nltk.word_tokenize(s)
            word_list = [word.lower() for word in word_list if word.isalpha()]
            word_list = [w for w in word_list if not w in stopwords.words('english')]
            word_list = [w for w in word_list if not w in other_words]
            word_list = [w for w in word_list if not len(w) == 1]

            ps = PorterStemmer()
            preLang.append([ps.stem(w) for w in word_list])
        #### Decided to skip this, due to several issues and huge slow down in execution speed.
        #for w in word_list:
        #    if w in words.words():
        #        preLang.append(w)
        #    else:
        #        preLang.append("@"+w+"@")
        return preLang


    def readXMLFile():
        '''
        This method creates different files for each post, which will have language token and code tokens as @codetoken@ after preprocessing.
        :return:
        '''
        files = ['birt.xml', 'eclipse.xml', 'eclipse-jdt.xml', 'swt.xml']
        for file in files:
            tree = ET.parse(file)
            root = tree.getroot()
            i=0
            project = file[:-4]
            for child in root:
                i=i+1
                file = open(project+"-post"+str(i)+".txt", "w")
                print(project+"-post"+str(i)+".txt")
                if (child.attrib['Body'] is not None):
                    body = child.attrib['Body']
                    str_idx = body.find('<pre><code>')
                    strt_of_strng = 0
                    lang=""
                    code =""
                    if str_idx == -1:
                        lang= lang+body
                    else:
                        while (str_idx != -1):
                            str_idx = body[strt_of_strng:].find('<pre><code>')
                            lst_idx = body[strt_of_strng:].find('</code></pre>')
                            if str_idx != -1:
                                code= code+ body[strt_of_strng + str_idx:strt_of_strng + lst_idx + 13]
                                lang = lang + body[strt_of_strng:strt_of_strng + str_idx]
                            else:
                                lang = lang + body[strt_of_strng:]
                            strt_of_strng = strt_of_strng + lst_idx + 13

                    preCode = preprocessCode(code)
                    preLang =preprocessLang(lang)
                    for token in preLang:
                        if len(token)>=1:
                            file.write("[")
                            for t in token:
                                file.write(t)
                                file.write(",")
                            file.write("]")
                            file.write(",")
                    file.write("\n")
                    for token in preCode:
                        file.write(token)
                        file.write(",")

                file.close()

readXMLFile()