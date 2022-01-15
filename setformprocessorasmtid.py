# https://canvasapi.readthedocs.io/en/stable/
# https://canvas.instructure.com/doc/api/

# canvasapi on pip is out of date, might need to install from https://github.com/ucfopen/canvasapi (git+https://github.com/ucfopen/canvasapi.git)
# pip install python-frontmatter

from canvasapi import Canvas, exceptions
import getopt
import sys
import frontmatter
from datetime import datetime, timedelta
import threading
import time
import random
from urllib import request, parse
import requests
import json
import os

# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/course.py
# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/canvas.py

API_URL = "https://ursinus.instructure.com/"
# Generate key at API_URL + profile/settings
# Obtain User ID from API_URL + /api/v1/users/self

def canvas_http_request(endpoint, inputdict=None, method="GET"):
    header = {"Authorization": "Bearer %s" % API_KEY}

    if not (inputdict is None):
        data = parse.urlencode(inputdict).encode()
        header['Content-Type'] = 'application/x-www-form-urlencoded'
    else:
        data = None
    
    req =  request.Request(rchop(API_URL, '/') + endpoint, data=data, headers=header, method=method) 
    resp = request.urlopen(req)   
    return resp
    
def makelink(base, url):
    if url.startswith("http"):
        return url
    else:
        return base + url

def addslash(str):
    if not (str.endswith("/")):
        return str + "/"
    else:
        return str

def printlog(msg, output=True):
    if output:
        print(msg)
        
# https://stackoverflow.com/questions/3663450/remove-substring-only-at-the-end-of-string
def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s
    
# https://stackoverflow.com/questions/16891340/remove-a-prefix-from-a-string
def lchop(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text   
    
def stripnobool(val):
    if type(val) is bool:
        result = ""
    else:
        result = str(val)
    
    return result.strip()
    
def asmtid_by_title(title):
    coursecontext = 'course_' + str(courseid)  

    # Get all the assignments
    assignments = course.get_assignments()

    for assignment in assignments:
        assignmentid = assignment.id    
        assignmenttitle = assignment.name
        
        if assignmenttitle == title:
            print("Found assignment " + title + " on canvas with id " + str(assignmentid))
            return assignmentid
    
    print("Assignment " + title + " not found on canvas")
    
    return None # not found
    
def find_canvas_assignment(exerciselink, syllabusfile):
    f = open(syllabusfile, 'r')
    mdcontents = f.read()
    
    post = frontmatter.loads(mdcontents)
    postdict = post.to_dict()    
    
    match = False
    for scheditem in postdict['schedule']:
        if 'deliverables' in scheditem:
            for deliverable in scheditem['deliverables']:
                title = deliverable['dtitle']
                link = deliverable['dlink']
                
                if link == exerciselink:
                    match = True
                else:
                    if link and not str(link).lower() == 'false':
                        linkparts = link.split('/')
                        exerciselinkparts = exerciselink.split('/')
                        match = True
                        if linkparts[-1].lower() == "module":
                            linkparts[-1] = "Exercise"
                        if exerciselinkparts[-1].lower() == "module":
                            exerciselinkparts[-1] = "Exercise"
                        if len(linkparts) != len(exerciselinkparts):
                            match = False
                        else:
                            for i in range(min(len(linkparts), len(exerciselinkparts))):
                                if linkparts[i] != exerciselinkparts[i]:
                                    match = False
                
                if match == True:
                    print("Matched " + link + " and " + exerciselink)
                    
                    # Get the assignment id for this title and return
                    asmtid = asmtid_by_title(title)
                    
                    return asmtid
                    
    return None # not found
                
def process_exercises(dirpath, syllabusfile, canvas, course, courseid):
    for fname in os.listdir(os.getcwd() + os.sep + dirpath):
        if fname.endswith(".md"):
            fpath = os.getcwd() + os.sep + dirpath + os.sep + fname
            f = open(fpath, 'r')
            mdcontents = f.read()
            
            post = frontmatter.loads(mdcontents)
            postdict = post.to_dict()
            
            # canvasasmtid can be empty for now, set canvasasmtid and canvaspoints
            if 'canvasasmtid' in postdict and 'canvaspoints' in postdict:            
                if 'permalink' in postdict:
                    if not str(postdict['permalink']).lower() == 'false':
                        exerciselink = str(lchop(postdict['permalink'], '/'))
                        asmtid = find_canvas_assignment(exerciselink, syllabusfile)
                        
                        if asmtid:
                            lines = []
                            f2 = open(fpath, 'r')
                            for line in f2:
                                if line.startswith("canvasasmtid:"):
                                    lines.append("canvasasmtid: \"" + str(asmtid) + "\"\n")
                                else:
                                    lines.append(line)
                        
                            # save
                            print("Saving " + fname)
                            fout = open(fpath, 'w')
                            for line in lines:
                                fout.write(line)
                            fout.close()
                        else:
                            print("*** Exercise not matched for " + exerciselink + " in file " + fname)

def get_courseid(canvas, user):
    courses = user.get_courses()
    
    for course in courses:
        print(course)
        
    courseid = input("Which Course ID? ")

    return int(courseid)

def usage():
    print("Usage:")
    print("\t[-h | --help]\tUsage Documentation")
    print("\t[-c | --courseid]\tCanvas Course ID number (can be found using canvas link after logging in); omit for a course listing here")
    print("\t[-m | --markdown]\tPath to syllabus markdown file")      
    print("\t[-p | --markdowndir]\tPath to course exercise modules markdown directory")  
    print("\t[-a | --apikey]\tAPI Key (get from API_URL + /profile/settings)")
    print("\t[-u | --userid]\tUser ID Number (get from API_URL + /api/v1/users/self)")
    
# Parse user options
# https://docs.python.org/3/library/getopt.html
try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:m:p:a:u:", ["help", "courseid=", "markdowndir=", "markdown=", "apikey=", "userid="])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -z not recognized"
    usage()
    sys.exit(2)

courseid = -1
markdownfile = None
USER_ID = None
API_KEY = None

for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    elif o in ("-c", "--courseid"):
        courseid = int(a)
    elif o in ("-m", "--markdown"):
        markdown = a        
    elif o in ("-p", "--markdowndir"):
        markdowndir = a
    elif o in ("-a", "--apikey"):
        API_KEY = a
    elif o in ("-u", "--userid"):
        USER_ID = a 

if USER_ID is None:
    USER_ID = input("Enter User ID (get from API_URL + /api/v1/users/self): ")
if API_KEY is None:
    API_KEY = input("Enter API Key (get from API_URL + /profile/settings): ")
    
printlog("Instantiating Canvas...")
# Instantiate Canvas and Course
canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user(USER_ID)

if courseid == -1:
    courseid = get_courseid(canvas, user)
if markdowndir is None:
    markdowndir = input("Enter path to course exercise module markdown directory: ")
if markdown is None:
    markdown = input("Enter path to course syllabus markdown file: ")
    
course = canvas.get_course(courseid)

printlog("Reading Markdown...")

process_exercises(markdowndir, markdown, canvas, course, courseid)

printlog("Finished")
