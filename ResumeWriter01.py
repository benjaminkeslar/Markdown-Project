import os

# This program takes several .txt files as inputs, and then assembles them into a single resume file.
# This resume file is then output as a .txt, .html, or .md file.
# I'll figure out how to make a .pdf or .tex output later.

resume = ""
name = ""
contactsS = ""
outList = []
contactsL = []

txt = False
html = False
md = False

inList = os.listdir("input")

print("Please type what you want the output to be as initials (t/h/m).")
print("For example, if you want to output both a .md and a .html, type 'mh' (or 'hm'; it's not position sensitive).")
input1 = input()

for c in input1:
    if c == 't':
        txt = True
    if c == 'h':
        html = True
        resumeH = ""
        
    if c == 'm':
        md = True
        resumeM = ""


if "Preamble.txt" in inList:
    inList.remove("Preamble.txt")
    with open("input/Preamble.txt") as f:
        name = f.readline()
        for x in f:
            contactsL.append(x[:-1])

    contactsS = " | ".join(contactsL)
    resume += (name + contactsS)
    
    if html:
        resumeH += ("<!DOCTYPE html>\n<html>\n<head>\n<title>" + name[:-1] + " Resume</title>\n</head>\n<body>\n")
        resumeH += ("<h1 style='text-align: center'>" + name[:-1] + "</h1>\n<p style='text-align: center'>" + contactsS + "</p>\n<hr>\n")
    if md:
        resumeM += ("# " + name + contactsS + "\n\n\n---\n")


print(inList)
print("Please type what order of sections you want by initials.")
print("For example, if you want (alpha, beta, gamma) type abg; pay attention to capitilization.")
input2 = input()
for i in input2:
    for n in inList:
        if i == n[0]:
            outList.append(n)
            inList.remove(n)

print(outList)

for i in outList:
    resume += ("\n\n\n\n")
    resumeH += ("\n<br>\n<br>\n")
    resumeM += ("  \n  \n  \n  \n")
    with open("input/" + i) as f:
        for n in f:
            resume += n
            if len(n) > 1 and html:
                n2 = n[:-1]
                if n2[-1] == ':':
                    resumeH += ("<h2>" + n2 + "</h2>\n")
                else:
                    resumeH += ("<p>" + n2 + "</p>\n")
                    
                    
            elif html: resumeH += "<br>\n"
            if md:
                if len(n) > 1:
                    if n[-2] == ':':
                        resumeM += ("#### " + n)
                    else: resumeM += n
                else: resumeM += ("  \n" + n)

        
resumeH += "</body>\n</html>"

if txt:
    with open((name[:-1] + " Resume.txt"), "w") as f:
        f.write(resume)
if html:
    with open ((name[:-1] + " Resume.html"), "w") as f:
        f.write(resumeH)
if md:
    with open ((name[:-1] + " Resume.md"), "w") as f:
        f.write(resumeM)

