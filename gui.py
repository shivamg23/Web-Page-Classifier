from tkinter import *
from functools import partial
import requests
import re
from bs4 import BeautifulSoup
import tkinter.messagebox
import os


#-----Functions for calculations-----
def analyse_web_page(name,input1):
    file1=open("files/"+name+"1.txt","r")
    file2=open("files/"+name+"2.txt","r")
    text1=file1.read().split("$$$$$")
    text2=file2.read().split("$$$$$")
    file1.close()
    file2.close()
    text1.pop()
    text2.pop()
    v1=len(text1)
    v2=len(text2)
    text11=[]
    text22=[]
    for i in range(len(text1)):
        text1[i]=text1[i].split()
    for i in range(len(text2)):
        text2[i]=text2[i].split()
    for i in range(len(text1)):
        for j in range(len(text1[i])):
            for k in range(len(text1)):
                if (k==i):
                    continue
                for l in range(len(text1[k])):
                    if(text1[i][j].lower()==text1[k][l].lower()):
                        text11.append(text1[i][j])
    for i in range(len(text2)):
        for j in range(len(text2[i])):
            for k in range(len(text2)):
                if (k==i):
                    continue
                for l in range(len(text2[k])):
                    if(text2[i][j].lower()==text2[k][l].lower()):
                        text22.append(text2[i][j])
    text_1=list(set(text11))
    text_2=list(set(text22))
    try:
        html = requests.get(input1.get())
        soup = BeautifulSoup(html.content, "html.parser")
        y = [re.sub(r'<.+?>', r'', str(a)) for a in soup]
        text=[]
        y=" ".join(y)
        y=y.split()
        special=["+",",","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'",'"',"<",",",".",">","?","/","|","`","~","1","2","3","4","5","6","7","8","9","0"]
        y1=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","following","1","2"]
        for i in range(len(y)):
            word=y[i].lower()
            if(word not in y1 and word not in text and word not in special):
                j = 0
                while j < len(word):
                    if (word[j] in special):
                        if (j == 0):
                            word = word[1:]
                        elif (j == len(word) - 1):
                            word = word[0:j]
                        else:
                            word = word[0:j] + word[j + 1:]
                    else:
                        j += 1
                if(word!="" and len(word)<=20):
                    text.append(word)
        text_url=[]
        count_url=[]
        c=0
        for i in range(len(text)):
            for j in range(len(text_1)):
                if(text[i].lower()==text_1[j].lower() and text[i] not in text_url and text[i]!="1" ):
                    text_url.append(text[i])
                    count_url.append(text.count(text[i]))
                    c=1
                    break
            if(c==0):
                for j in range(text_2):
                    if (text[i].lower() == text_2[j].lower() and text[i] not in text_url and text[i]!="1"):
                        text_url.append(text[i])
                        count_url.append(text.count(text[i]))
                        c = 1
                        break
        #---class1 probability---
        pob=[]
        down=v1+v2
        for i in text_url:
            down+=text11.count(i)
        for i in text_url:
            up=text11.count(i)+1
            prob=float(up)/float(down)
            pob.append(prob)
        class1_prob=float(v1)/float(v1+v2)
        for i in range(len(count_url)):
            class1_prob*=pob[i]**count_url[i]
        print(pob)
        #---class2 probability---
        pob = []
        down = v2+v1
        for i in text_url:
            down += text22.count(i)
        for i in text_url:
            up = text22.count(i)+1
            prob = float(up) / float(down)
            pob.append(prob)
        class2_prob = float(v2) / float(v1 + v2)
        for i in range(len(count_url)):
            class2_prob *= pob[i] ** count_url[i]
        print(pob)
        file=open("files/classifiaction_names.txt","r")
        t=file.read().split()
        i=t.index(name)
        file.close()
        file=open("files/classes.txt","r")
        t=file.read().split()
        file.close()
        c1=t[i*2]
        c2=t[i*2+1]
        if(class1_prob>class2_prob):
            print(c1)
            result(c1,name)
        else:
            print(c2)
            result(c2,name)
        print(class2_prob)
        print(class1_prob)
        print(text_url)
        print(count_url)
    except:
        tkinter.messagebox.showerror("Error!","Incorrect URL")
        analyse(name)



def add_class(classification,class1,class2):
    file1=open("files/classifiaction_names.txt","a")
    file2=open("files/classes.txt","a")
    file1.write(" "+classification.get())
    file2.write(" "+class1.get()+" "+class2.get())
    file1.close()
    file2.close()
    tkinter.messagebox.showinfo("Progress Status","The new class has been created!!")
    add_new_class()


def store(name,input1,button1,button2):
    url=input1.get()
    v1=button1.get()
    v2=button2.get()
    try:
        html = requests.get(input1.get())
        soup = BeautifulSoup(html.content, "html.parser")
        y = [re.sub(r'<.+?>', r'', str(a)) for a in soup]
        text=[]
        y=" ".join(y)
        y=y.split()
        special = ["+", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]",":", ";", "'", '"', "<", ",", ".", ">", "?", "/", "|", "`", "~", "1", "2", "3", "4", "5", "6", "7","8", "9", "0"]
        y1=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        for i in range(len(y)):
            word=y[i].lower()
            if(word not in y1 and word not in text and word not in special):
                j=0
                while j<len(word):
                    if(word[j] in special):
                        if(j==0):
                            word=word[1:]
                        elif(j==len(word)-1):
                            word=word[0:j]
                        else:
                            word=word[0:j]+word[j+1:]
                    else:
                        j+=1
                if(word!="" and len(word)<=20):
                    text.append(word)
        c=0
        print(text)
        text=" ".join(text)
        if(v1==0 and v2==0):
            tkinter.messagebox.showerror("Error!", "Please Select a class")
            c=1
        elif(v1==1 and v2==1):
            tkinter.messagebox.showerror("Error!", "Please Select only one class")
            c=1
        elif(v1==0 and v2==1):
            f=open("files/"+name+"2.txt","a")
            f.write(" "+text+" $$$$$")
            f.close()
            print("files/"+name+"2.txt")
            tkinter.messagebox.showinfo("Progress Status", "Web Page data classified and stored!")
        elif(v1==1 and v2==0):
            f = open("files/"+name + "1.txt", "a")
            f.write(" "+text+" $$$$$")
            f.close()
            print("files/"+name + "1.txt")
            tkinter.messagebox.showinfo("Progress Status", "Web Page data classified and stored!")
        if(c==0):
            classification(name)

    except:
        tkinter.messagebox.showerror("Error!","Incorrect URL")
        classification(name)

def delete_class(name):
    f=open("files/classifiaction_names.txt","r")
    text=f.read().split()
    index=text.index(name)
    print(text)
    print(index)
    del text[index]
    f.close()
    f = open("files/classifiaction_names.txt", "w")
    f.write(" ".join(text))
    f.close()
    f=open("files/classes.txt","r")
    text=f.read().split()
    print(text)
    del text[index*2]
    del text[index*2]
    f.close()
    f = open("files/classes.txt", "w")
    f.write(" ".join(text))
    f.close()
    if os.path.exists(name+"1.txt"):
        os.remove(name+"1.txt")
    if os.path.exists(name+"2.txt"):
        os.remove(name+"2.txt")
    tkinter.messagebox.showinfo("Progress Status", "Class has been deleted successfully!!")
    existing_class()




#*****End functions for calculations*****

#-----functions for frames------


def initialize():
    global frame
    frame = Frame(root)
    frame.grid(row=0)
    add_new_class()


def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()


def add_new_class():
    clear()
    frame = Frame(root,bg="#394140")
    frame.grid(row=0)
    label1 = Label(frame,text="Add New Classification",font=("comic sans ms", 20,"bold"),padx=20,pady=10,bg="#394140",fg="#E05238")
    label2=Label(frame,text="Classification Name",font=("comic sans ms", 14,"bold"),bg="#E05238",fg="White",padx=5,pady=3)
    label3 = Label(frame, text="Class 1 Name", font=("comic sans ms", 14,"bold"),bg="#E05238",fg="White",padx=5,pady=3)
    label4 = Label(frame, text="Class 2 Name", font=("comic sans ms", 14,"bold"),bg="#E05238",fg="White",padx=5,pady=3)
    input1 = Entry(frame)
    input2 = Entry(frame)
    input3 = Entry(frame)
    button=Button(frame,text="Create",fg="#E05238",bg="#29302F",padx=15,relief=FLAT,font=("comic sans ms", 14,"bold"),command=lambda: add_class(input1,input2,input3))
    label1.grid(columnspan=3,row=0,sticky=E)
    label2.grid(row=2,sticky=E)
    label3.grid(row=4,sticky=E)
    label4.grid(row=6,sticky=E)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid( row=1, column=1)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid( row=3, column=1)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid( row=5, column=1)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=7, column=1)
    input1.grid(row=2,column=2,ipady=8,ipadx=30,sticky=W)
    input2.grid(row=4, column=2,ipady=8,ipadx=30,sticky=W)
    input3.grid(row=6, column=2,ipady=8,ipadx=30,sticky=W)
    button.grid(row=8,column=2,sticky=W,ipadx=42)


def classification(name):
    clear()
    file=open("files/classes.txt","r")
    text=file.read().split()
    file.close()
    file=open("files/classifiaction_names.txt","r")
    text1=file.read().split()
    file.close()
    i=text1.index(name)
    class1=text[i*2]
    class2=text[i*2+1]
    frame = Frame(root,bg="#394140")
    frame.grid(row=0)
    v1=IntVar()
    v2=IntVar()
    label1 = Label(frame, text=name,font=("comic sans ms", 20,"bold"),bg="#394140",fg="#E05238", padx=20,pady=10)
    label2 = Label(frame, text="Enter URL",font=("comic sans ms", 14,"bold"),bg="#E05238",fg="White",padx=5,pady=3)
    label3 = Label(frame, text=class1,font=("comic sans ms", 14,"bold"), padx=20,pady=20, bg="#394140",fg="#889190")
    label4 = Label(frame, text=class2,font=("comic sans ms", 14,"bold"), padx=20,pady=20, bg="#394140",fg="#889190")
    button = Button(frame, text="Classify",fg="#E05238",bg="#29302F",padx=15,relief=FLAT,font=("comic sans ms", 14,"bold"),command=lambda: store(name,input1,v1,v2))
    input1 = Entry(frame)
    checkbutton1 = Checkbutton(frame,variable=v1,onvalue=1,offvalue=0, bg="#394140",relief=FLAT)
    checkbutton2 = Checkbutton(frame,variable=v2,onvalue=1,offvalue=0, bg="#394140",relief=FLAT)
    label1.grid(columnspan=2)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=1)
    label2.grid(row=2,sticky=E)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=3)
    label3.grid(row=4,sticky=E)
    label4.grid(row=4,column=2)
    input1.grid(row=2,column=1, ipady=8, ipadx=50,columnspan=2)
    checkbutton1.grid(row=4,column=1,sticky=W)
    checkbutton2.grid(row=4,column=3,)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=5)
    button.grid(row=6, column=1, sticky=W)


def existing_class():
    clear()
    frame = Frame(root, bg="#394140")
    frame.grid(row=0)
    Label(frame,text="Existing Classifications", font=("comic sans ms", 20,"bold"),bg="#394140",fg="#E05238", padx=20,pady=10).grid(columnspan=3,row=0)
    file=open("files/classifiaction_names.txt","r")
    text=file.read().split()
    for i in range(len(text)):
        Label(frame,text=str(i+1)+". "+str(text[i]),font=("comic sans ms", 14,"bold"),bg="#E05238",fg="White", padx=10,pady=10).grid(row=i*2+1,sticky=W)
        if(i>0):
            Label(frame,text="abc",fg="#394140", bg="#394140").grid(row=i*2)
        Button(frame, text="Classify", padx=5,pady=5, font=("comic sans ms", 12,"bold"),relief=FLAT,fg="#E05238",bg="#29302F",command=partial(classification,text[i])).grid(row=i*2+1,column=2)
        Button(frame, text="Delete", padx=5,pady=5, font=("comic sans ms", 12,"bold"),relief=FLAT,fg="#E05238",bg="#29302F",command=partial(delete_class,text[i])).grid(row=i*2+1,column=4)
        Button(frame, text="Analyse", padx=5,pady=5,fg="#E05238",bg="#29302F",relief=FLAT, font=("comic sans ms", 12,"bold"),command=partial(analyse,text[i])).grid(row=i*2+1,column=6)
        Label(frame, text="ab", fg="#394140", bg="#394140").grid(row=i * 2+1,column=1)
        Label(frame, text="ab", fg="#394140", bg="#394140").grid(row=i * 2+1,column=3)
        Label(frame, text="ab", fg="#394140", bg="#394140").grid(row=i * 2 + 1, column=5)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=len(text)*2)
    Button(frame, text="Create New", padx=15, font=("comic sans ms", 12,"bold"),relief=FLAT,fg="#E05238",bg="#29302F",command=lambda: add_new_class()).grid(row=len(text)*2+1,column=1,columnspan=2)
    file.close()


def analyse(name):
    clear()
    frame = Frame(root, bg="#394140")
    frame.grid(row=0)
    Label(frame, text="Analyse Web Page", font=("comic sans ms", 20, "bold"), bg="#394140", fg="#E05238",padx=20, pady=10).grid(columnspan=3, row=0)
    Label(frame, text="Enter URL", font=("comic sans ms", 14, "bold"), bg="#E05238", fg="White", padx=5, pady=3).grid(row=2,sticky=E)
    input1=Entry(frame)
    input1.grid(row=2,column=1, ipady=8, ipadx=50,columnspan=2)
    Label(frame, text="Classification Name :", font=("comic sans ms", 14, "bold"), bg="#E05238", fg="White", padx=5, pady=3).grid(row=4, sticky=E,columnspan=2)
    Label(frame, text=name, font=("comic sans ms", 14, "bold"), padx=20, pady=20, bg="#394140", fg="#889190").grid(row=4,column=2)
    Button(frame, text="Analyse", padx=15, font=("comic sans ms", 12, "bold"), relief=FLAT, fg="#E05238",bg="#29302F", command=lambda: analyse_web_page(name,input1)).grid(row=6,column=1,columnspan=2)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=1)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=3)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=5)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=4,column=3)
    Button(frame, text="Change Class", padx=15, font=("comic sans ms", 12, "bold"), relief=FLAT, fg="#E05238",bg="#29302F", command=lambda: existing_class()).grid(row=4,column=4,columnspan=2)

def result(c,name):
    clear()
    frame = Frame(root, bg="#394140")
    frame.grid(row=0)
    Label(frame, text="Analyse Web Page", font=("comic sans ms", 20, "bold"), bg="#394140", fg="#E05238",padx=20, pady=10).grid(columnspan=3, row=0)
    Label(frame, text="Enter URL", font=("comic sans ms", 14, "bold"), bg="#E05238", fg="White", padx=5, pady=3).grid(row=2,sticky=E)
    input1=Entry(frame)
    input1.grid(row=2,column=1, ipady=8, ipadx=50,columnspan=2)
    Label(frame, text="Classification Name :", font=("comic sans ms", 14, "bold"), bg="#E05238", fg="White", padx=5, pady=3).grid(row=4, sticky=E,columnspan=2)
    Label(frame, text=name, font=("comic sans ms", 14, "bold"), padx=20, pady=20, bg="#394140", fg="#889190").grid(row=4,column=2)
    Button(frame, text="Analyse", padx=15, font=("comic sans ms", 12, "bold"), relief=FLAT, fg="#E05238",bg="#29302F", command=lambda: analyse_web_page(name,input1)).grid(row=6,column=1,columnspan=2)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=1)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=3)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=5)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=4,column=3)
    Button(frame, text="Change Class", padx=15, font=("comic sans ms", 12, "bold"), relief=FLAT, fg="#E05238",bg="#29302F", command=lambda: existing_class()).grid(row=4,column=4,columnspan=2)
    Label(frame, text="Class", font=("comic sans ms", 14, "bold"), bg="#E05238", fg="White", padx=5, pady=3).grid(row=7, sticky=E)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=5)
    Label(frame, text="abc", fg="#394140", bg="#394140").grid(row=6)
    Label(frame, text=c, font=("comic sans ms", 14, "bold"), padx=20, pady=20, bg="#394140", fg="#889190").grid(row=7, column=1)
    Button(frame, text="OK", padx=15, font=("comic sans ms", 12, "bold"), relief=FLAT, fg="#E05238",bg="#29302F", command=lambda: analyse(name)).grid(row=9,column=1,columnspan=2)

#-----window declaration-----
root = Tk()
root.title('Web Page Classifier v1.0')
root.resizable(True, True)
root.geometry("600x350")
root.resizable(1, 1)


#-----menu-----

menu=Menu(root)
root.config(menu=menu,bg="#394140")

submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="Add New Classification",command=lambda: add_new_class())
submenu.add_command(label="Show Existing Classifications",command=lambda: existing_class())
submenu.add_separator()
submenu.add_command(label="Classify Web Page",command=lambda: existing_class())
submenu.add_command(label="Analyse Web Page",command=lambda: existing_class())


#*****End Menu*****


initialize()
root.mainloop()


#*****End Window Declaration*****

