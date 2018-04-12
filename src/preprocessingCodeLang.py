import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
#from nltk.corpus import words
import enchant
import string

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
        d = enchant.Dict("en_US")
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
            temp = self.camel_case_split(w)
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

    #TODO: figure out if you also want an implementation without sentence boundaries
    def preprocessLang(self, lang):
        '''
            This method preprocesses the Natural language in the post.
            :param code: all the natural language from one post
            :return: preprocessed language tokens
            '''

        # OK IN THIS INSTANCE YOU ARE RETURNING A LIST OF LISTS
        # AKA SENTENCE BOUNDADRIES
        preLang=[]
        lang = lang.encode('ascii', 'ignore')

        sent_text = nltk.sent_tokenize(lang)
        d = enchant.Dict("en_US")
       # print "SENT TEXT", sent_text
        for s in sent_text:
            s= s.strip()
            s = re.sub('[^0-9a-zA-Z]+', ' ', s)
            s = re.sub('<[^<]+?>', '', s)
            s = re.sub(r"\p{P}+", " ", s)

            word_list = nltk.word_tokenize(s)
            #print "'WORD_LIST", word_list
            word_list = [word.lower() for word in word_list if word.isalnum()]
            for i in range(len(word_list)):
                if not d.check(word_list[i]):
                    word_list[i] = "@" + word_list[i] + "@"
            word_list = [w for w in word_list if (w not in stopwords.words('english') or "@" in w)]
            word_list = [w for w in word_list if not len(w) <= 2]
            ps = PorterStemmer()
            preLang.append([ps.stem(w).encode('ascii', 'ignore') for w in word_list])
        return preLang

def readXMLFile():
        '''
        This method creates different files for each post, which will have language token and code tokens as @codetoken@ after preprocessing.
        :return:
        '''
        ## Change this path according to your machine before running.
        path = "/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/"
        files = ['birt.xml', 'eclipse.xml', 'eclipse-jdt.xml', 'swt.xml']
        pp = Preprocessor()
        for file in files:
            filepath = path+file
            tree = ET.parse(filepath)
            root = tree.getroot()
            i=0
            project = file[:-4]
            for child in root:

                i=i+1

                ## Change this path according to your machine before running.
                file = open("/home/ndg/users/carmst16/EmbeddingBugs/resources/stackexchangedata/"+project+"/"+str(i)+".txt", "w")
                print(project+"-post"+str(i)+".txt")
                if (child.attrib['Body'] is not None):
                    body = child.attrib['Body'].encode('ascii', 'ignore').decode('ascii')

                    str_idx = body.find('<pre><code>')
                    strt_of_strng = 0
                    lang=""
                    code =""
                    if str_idx == -1:
                        lang= body
                        preLang = pp.preprocessLang(lang)
                        for token in preLang:
                            if len(token) >= 1:
                                file.write(",".join(token))
                               # file.write("\n")
                    else:
                        while (str_idx != -1):
                            str_idx = body[strt_of_strng:].find('<pre><code>')
                            lst_idx = body[strt_of_strng:].find('</code></pre>')
                            if str_idx != -1:
                                lang = body[strt_of_strng:strt_of_strng + str_idx]
                                preLang = pp.preprocessLang(lang)
                                for token in preLang:
                                    if len(token) >= 1:
                                        file.write(",".join(token))
                                       # file.write("\n")

                                code=body[strt_of_strng + str_idx:strt_of_strng + lst_idx + 13]
                                preCode = pp.preprocessCode(code)
                                file.write(",".join(preCode))
                               # file.write("\n")


                            else:
                                lang = body[strt_of_strng:]
                                preLang = pp.preprocessLang(lang)
                                for token in preLang:
                                    if len(token) >= 1:
                                        file.write(",".join(token))

                                       # file.write("\n")
                            #TODO: why is this 13???
                            strt_of_strng = strt_of_strng + lst_idx + 13

                    #preCode = Preprocessor.preprocessCode(code)
                    #preLang =Preprocessor.preprocessLang(lang)
                    #for token in preLang:
                    #    if len(token)>=1:
                    #        file.write("[")
                    #        for t in token:
                    #            file.write(t)
                    #            file.write(",")
                    #        file.write("]")
                    #        file.write(",")
                    #file.write("\n")
                    #for token in preCode:
                    #    file.write(token)
                    #    file.write(",")

                file.close()

def main():

    readXMLFile()

if __name__ == "__main__":
    main()
