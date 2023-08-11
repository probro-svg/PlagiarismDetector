import docx
import nltk
from tkinter import *
from tkinter import messagebox

# reading the list of names of students present in the class
file1 = open("list.txt", "r")
text1 = file1.readlines()
str1 = ''.join(text1)
str = str1.split(' ')
print(str)  # str renders each name


def getme():
    if(flag == 1):
        messagebox.showinfo("Result", "THE DOCUMENT IS PLAGIARISED")
    else:
        messagebox.showinfo("Result", "THE DOCUMENT IS NOT PLAGIARISED")


# returns each word file in form of a list separated by full stops
def ReadingTextDocuments(testPython):
    doc = docx.Document(testPython)

    completedText = []
    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
    s = '\n'.join(completedText)
    s1 = s.split('.')
    return s1


name = input("Enter the name of the first document\t")
name1 = name+'.docx'
flag = 0
doc1 = ReadingTextDocuments(name1)
doc1.pop()  # Reads the user input file, splits it into a list with . as a delimiter
LOC = len(doc1)
for out in str:
    name2 = out+'.docx'

    doc2 = ReadingTextDocuments(name2)
    doc2.pop()
    cnt1 = 0
    for i in doc1:
        for j in doc2:
           # print(i,j)
            if(i == j):
                cnt1 += 1
    # print(cnt1,LOC)
    per = (cnt1/LOC)*100
    if(per > 55 and out != name):
        flag = 1
    if(out != name):
        print("The percentage of document that has been copied from ",
              out, "is: ", per, "% \n")
getme()


root = Tk()
button = Button(root, command=getme)
button.pack()
root.geometry("400x400")
root.mainloop()
