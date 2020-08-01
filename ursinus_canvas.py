# https://canvasapi.readthedocs.io/en/stable/
# https://canvas.instructure.com/doc/api/

# canvasapi on pip is out of date, might need to install from https://github.com/ucfopen/canvasapi (git+https://github.com/ucfopen/canvasapi.git)

from canvasapi import Canvas, exceptions
import getopt
import sys
import frontmatter
from datetime import datetime, timedelta
import threading

# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/course.py
# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/canvas.py

# CONSIDERATION
# Add assignment rubrics and point values (course.create_rubric) from assignment pages to facilitate grading (also to update point values)
## https://canvas.instructure.com/doc/api/rubrics.html
# course.create_course_section - separate calendar?  duplicate assignments, etc?
# Change course calendar entries to timetables: which can possibly be done on a per-section basis
## https://canvas.instructure.com/doc/api/calendar_events.html#method.calendar_events_api.set_course_timetable
# Tie to learning outcomes
# Hide unused links

API_URL = "https://ursinus.instructure.com/"
# Generate key at API_URL + profile/settings
# Obtain User ID from API_URL + /api/v1/users/self

CANVAS_TIME_ZONE = "America/New_York"
DUE_TIME = "T045959Z" # this time is no earlier than 11:59PM Eastern Time during EST or EDT
DUE_DATE_OFFSET = 1 # add 1 day to make things due the next morning per the due time above

child_threads = []

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
    
def stripnobool(val):
    if type(val) is bool:
        result = ""
    else:
        result = str(val)
    
    return result.strip()

def dodelete(item):
    try:
        item.delete()
    except exceptions.ResourceDoesNotExist:
        print("Deleting: Resource Does Not Exist")
    
def delete_all_events(canvas, coursecontext):
    events = canvas.get_calendar_events(all_events = True, context_codes = [coursecontext])
    
    for event in events:
        t = threading.Thread(target=dodelete, args=(event,))
        child_threads.append(t)
        t.start()

def delete_all_assignments(course):
    assignments = course.get_assignments()

    for assignment in assignments:        
        t = threading.Thread(target=dodelete, args=(assignment,))
        child_threads.append(t)
        t.start()           
        
def delete_all_modules(course):
    modules = course.get_modules()
    
    itemthreads = []
    
    for module in modules:
        items = module.get_module_items()
        
        for item in items:
            t = threading.Thread(target=dodelete, args=(item,))
            child_threads.append(t)
            t.start()                 
        
        for t in itemthreads:
            t.join()
            
        t = threading.Thread(target=dodelete, args=(module,))
        child_threads.append(t)
        t.start()   
            
def delete_all_assignment_groups(course):
    groups = course.get_assignment_groups()
    
    for group in groups:
        t = threading.Thread(target=dodelete, args=(group,))
        child_threads.append(t)
        t.start()   

def delete_assignment_group_by_name(course, name):
    groups = course.get_assignment_groups()
    
    for group in groups:
        if group.name == name:
            t = threading.Thread(target=dodelete, args=(group,))
            child_threads.append(t)
            t.start()         
    
def delete_old_data(course, canvas, coursecontext):
    t1 = threading.Thread(target=delete_all_assignments, args=(course,))
    t2 = threading.Thread(target=delete_all_events, args=(canvas,coursecontext,))
    t3 = threading.Thread(target=delete_all_modules, args=(course,))
    t4 = threading.Thread(target=delete_all_assignment_groups, args=(course,))
    
    child_threads.append(t1)
    child_threads.append(t2)
    child_threads.append(t3)
    child_threads.append(t4)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
def add_grading_standard(course, inputdict):
    course.add_grading_standards(inputdict)
    
def countWeeks(d1, d2):
    # https://stackoverflow.com/questions/14191832/how-to-calculate-difference-between-two-dates-in-weeks-in-python
    monday1 = (d1 - timedelta(days=d1.weekday()))
    monday2 = (d2 - timedelta(days=d2.weekday()))
    return (monday2 - monday1).days / 7

def getDayCodeNum(daycode):
    if daycode == 'M':
        return 0
    elif daycode == 'T':
        return 1
    elif daycode == 'W':
        return 2
    elif daycode == 'R':
        return 3
    elif daycode == 'F':
        return 4
    elif daycode == 'S':
        return 5
    elif daycode == 'U':
        return 6
    else:
        return -1

def getDayNum(dayidx, M, T, W, R, F, S, U):
    result = 0
    
    if M:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 0
    
    if T:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 1

    if W:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 2

    if R:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 3

    if F:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 4

    if S:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 5

    if U:
        dayidx = dayidx - 1
        
        if dayidx == -1:
            result = 6

    return result
    
def getTimeString(t):   
    return t.strftime('%H%M%S')    
    
def parseDate(dt):
    return datetime.strptime(dt, '%Y/%m/%d')
    
def parseTime(t):
    return datetime.strptime(t, '%I:%M %p')
    
def parseDateTimeCanvas(dt):
    return datetime.strftime(dt, '%Y-%m-%dT%H:%M:%SZ')
    
def adddays(dt, n):
    return dt + timedelta(days=n)
    
def addweeks(dt, n):
    return dt + timedelta(days=7*n)
    
def getDateString(dt):
    return dt.strftime('%Y%m%d')    
    
def getCourseDate(startdate, weeknum, dayidx, M, T, W, R, F, S, U, tostring=True):
    dt = parseDate(startdate)
    weeknum = int(weeknum)
    dayidx = int(dayidx)
    
    dt = addweeks(dt, weeknum)
    daynum = getDayNum(dayidx, M, T, W, R, F, S, U)
    dt = adddays(dt, daynum)
    
    if tostring:
        return getDateString(dt)
    else:
        return dt
    
# Create Assignment Shells: https://canvasapi.readthedocs.io/en/stable/examples.html#create-an-assignment
def create_assignment(course, inputdict):
    asmt = course.create_assignment(inputdict)
    return asmt
    
# Create Assignment Group: https://canvas.instructure.com/doc/api/assignment_groups.html#method.assignment_groups_api.create
def create_assignmentgroup(course, inputdict):
    asmtgroup = course.create_assignment_group(**inputdict)
    return asmtgroup

# Create a Module: https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.create
def create_module(course, inputdict):
    module = course.create_module(inputdict)
    return module
    
# Add an item to an existing module: https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.create
def add_module_item(module, inputdict):
    moduleitem = module.create_module_item(inputdict)
    module.edit(module={'published': True})
    return moduleitem
    
def get_assignment_group_containing_label(groups, label):
    for group in groups:
        name = group.name
        
        if label in name:
            return group
    
    return None
    
def add_assignments_to_groups(course):
    # Get all the assignments
    assignments = course.get_assignments()
    
    # Get all the assignment groups
    groups = course.get_assignment_groups()
    
    # If Lab, Project, Assignment (etc...) is in the name, add it to the weight column with Lab, Project, or Assignment (etc...) in the name
    for assignment in assignments:
        name = assignment.name
        asmtid = assignment.id
        
        if 'Lab:' in name:
            group = get_assignment_group_containing_label(groups, 'Lab')
        elif 'Programming Assignment:' in name:
            group = get_assignment_group_containing_label(groups, 'Programming Assignment')
        elif 'Written Assignment:' in name:
            group = get_assignment_group_containing_label(groups, 'Written Assignment')            
        elif 'Project:' in name:
            group = get_assignment_group_containing_label(groups, 'Project')
        elif 'Exercise:' in name:
            group = get_assignment_group_containing_label(groups, 'Exercise')
            
        if not (group is None):
            groupid = group.id
            
            assignment.edit(assignment={'assignment_group_id': groupid})
    
# Create Calendar: https://canvasapi.readthedocs.io/en/stable/canvas-ref.html (canvas.create_calendar_event, dict from https://canvas.instructure.com/doc/api/calendar_events.html)
def create_calendar_event(canvas, inputdict):
    try:
        canvas.create_calendar_event(inputdict)
    except exceptions.ResourceDoesNotExist:
        print("Calendar Event Creation: Resource Does Not Exist")
    
def process_markdown(fname, canvas, course, courseid, homepage):
    f = open(fname, 'r')
    mdcontents = f.read()
    
    post = frontmatter.loads(mdcontents)
    postdict = post.to_dict()
    
    coursecontext = 'course_' + str(courseid)

    coursenum = postdict['info']['course_number']
    coursename = postdict['info']['course_title']
    startdate = postdict['info']['course_start_date']
    enddate = postdict['info']['course_end_date']    
    isM = postdict['info']['class_meets_days']['isM']
    isT = postdict['info']['class_meets_days']['isT']
    isW = postdict['info']['class_meets_days']['isW']
    isR = postdict['info']['class_meets_days']['isR']
    isF = postdict['info']['class_meets_days']['isF']
    isS = postdict['info']['class_meets_days']['isS']
    isU = postdict['info']['class_meets_days']['isU']
    
    printlog("Replacing Syllabus Page with Course Homepage...")
    
    course.update(course={'time_zone': CANVAS_TIME_ZONE}) # Set time zone to Eastern Time
    course.update(course={'syllabus_body': "<iframe src=\"" + homepage + "\" title=\"Course Homepage\" width=\"1024\" height=\"768\"></iframe>"}) # Set Syllabus to Course Webpage
    
    printlog("Deleting Old Data...")
    
    # Delete All Assignments, Events, etc.; Re-Initialize Here
    delete_old_data(course, canvas, coursecontext)
       
    printlog("Writing Lecture Schedule...")
    
    # Write the lecture schedule as a recurring event
    for i in range(len(postdict['info']['class_meets_locations'])):
        section = postdict['info']['course_sections'][i]['section']
        for meeting in postdict['info']['class_meets_locations'][i]['section']:
            day = meeting['day']
            daynum = getDayCodeNum(meeting['day'])
            
            dt = parseDate(startdate)
            dt = adddays(dt, daynum)
            
            dtstart = getDateString(dt)
            dtstart = dtstart + "T"
            dtstart = dtstart + getTimeString(parseTime(meeting['starttime'])) 
            
            dtend = getDateString(dt) # Assume event ends on the same day
            dtend = dtend + "T"
            dtend = dtend + getTimeString(parseTime(meeting['endtime'])) # leave in local time

            location = meeting['place']
            summary = coursenum + " " + coursename + " Section " + section + " Class Meeting"
            
            inputdict = {}
            inputdict['context_code'] = coursecontext
            inputdict['title'] = summary.strip()
            inputdict['description'] = summary.strip()
            inputdict['location_name'] = location.strip()
            inputdict['start_at'] = dtstart
            inputdict['end_at'] = dtend            
            inputdict['time_zone_edited'] = CANVAS_TIME_ZONE 
            inputdict['all_day'] = False
            inputdict['duplicate'] = {}
            inputdict['duplicate']['frequency'] = "weekly"
            inputdict['duplicate']['count'] = countWeeks(parseDate(startdate), parseDate(enddate))
            
            create_calendar_event(canvas, inputdict)

    printlog("Writing Assignments...")
    for item in postdict['schedule']:   
        weekidx = item['week']
        dayidx = item['date']
        if 'title' in item:
            title = item['title']
        else:
            title = "N/A"
        if 'link' in item:
            link = item['link']
        else:
            link = ""
   
        startd = getCourseDate(startdate, weekidx, dayidx, isM, isT, isW, isR, isF, isS, isU)
        
        coursedt = getCourseDate(startdate, weekidx, dayidx, isM, isT, isW, isR, isF, isS, isU, tostring=False)
        coursedtstr = coursedt.strftime('%a, %b %d, %Y')
        weekdayidx = "(Week " + str(int(weekidx)+1) + " Day " + str(int(dayidx)+1) + ")"
        
        # Create a module for this entry
        inputdict = {}
        inputdict['name'] = coursedtstr + " - " + title   
        inputdict['published'] = True
        module = create_module(course, inputdict)
        
        # Create a Module Entry for Class Notes Link
        if 'link' in item:
            inputdict = {}
            inputdict['title'] = title
            inputdict['type'] = "ExternalUrl"
            inputdict['external_url'] = addslash(homepage) + stripnobool(link)
            inputdict['new_tab'] = True
            inputdict['published'] = True
            add_module_item(module, inputdict)
            
        if 'deliverables' in item:
            for deliverable in item['deliverables']:        
                dtitle = deliverable['dtitle']
                if 'dlink' in deliverable:
                    dlink = deliverable['dlink']
                else:
                    dlink = ""
                    
                if 'points' in deliverable:
                    points = int(deliverable['points'])
                else:
                    points = 100                    
                
                description = dtitle.strip() 
                
                description = rchop(description, " Due")

                # Create an Assignment Shell
                if not (' handed out' in description.lower()):
                    duedate = getCourseDate(startdate, weekidx, dayidx, isM, isT, isW, isR, isF, isS, isU, tostring=False)
                    duedate = getDateString(adddays(duedate, DUE_DATE_OFFSET)) # offset the due date as needed for the due time which is in UTC
                    
                    inputdict = {}
                    inputdict['name'] = description
                    inputdict['submission_types'] = []
                    inputdict['submission_types'].append('online_upload')
                    inputdict['allowed_extensions'] = []
                    inputdict['allowed_extensions'].append('zip')
                    inputdict['allowed_extensions'].append('bz2')
                    inputdict['allowed_extensions'].append('tar')
                    inputdict['allowed_extensions'].append('gz')
                    inputdict['allowed_extensions'].append('rar')
                    inputdict['allowed_extensions'].append('7z')
                    inputdict['notify_of_update'] = True
                    inputdict['published'] = True
                    inputdict['points_possible'] = points
                    inputdict['description'] = description + " (" + addslash(homepage) + stripnobool(dlink) + ")"
                    inputdict['due_at'] = parseDateTimeCanvas(datetime.strptime(duedate + DUE_TIME, "%Y%m%dT%H%M%SZ")) 
                    
                    assignment = create_assignment(course, inputdict)
                    
                    # Create a Module Entry for the Assignment
                    inputdict = {}
                    inputdict['title'] = description
                    inputdict['type'] = 'Assignment'
                    inputdict['content_id'] = assignment.id
                    inputdict['published'] = True
                    add_module_item(module, inputdict)
                    
        if 'readings' in item:
            for reading in item['readings']:    
                rtitle = reading['rtitle']
                if 'rlink' in reading:
                    rlink = reading['rlink']
                else:
                    rlink = ""  
                
                # Create a Module Entry for the Reading Activity
                inputdict = {}
                inputdict['title'] = rtitle
                inputdict['type'] = "ExternalUrl"
                inputdict['external_url'] = addslash(homepage) + stripnobool(rlink)
                inputdict['new_tab'] = True            
                inputdict['published'] = True
                add_module_item(module, inputdict)                  
    
    printlog("Writing Office Hours...")
    
    # Write Office Hours as a Recurring Event
    for instructor in postdict['instructors']:
        instructorname = instructor['name']
        
        for officehour in instructor['officehours']:     
            day = officehour['day']
            daynum = getDayCodeNum(officehour['day'])
            
            dt = parseDate(startdate)
            dt = adddays(dt, daynum)
            
            dtstart = getDateString(dt)
            dtstart = dtstart + "T"
            dtstart = dtstart + getTimeString(parseTime(officehour['starttime'])) 

            dtend = getDateString(dt) # assume no event overlaps a day boundary, ends on start date
            dtend = dtend + "T"
            dtend = dtend + getTimeString(parseTime(officehour['endtime'])) # leave in local time

            location = officehour['location']
            
            summary = coursenum + " " + coursename + " Office Hours with " + instructorname
            
            inputdict = {}
            inputdict['context_code'] = coursecontext
            inputdict['title'] = summary.strip()
            inputdict['description'] = summary.strip()
            inputdict['location_name'] = location.strip()
            inputdict['start_at'] = dtstart
            inputdict['end_at'] = dtend
            inputdict['time_zone_edited'] = CANVAS_TIME_ZONE 
            inputdict['all_day'] = False
            inputdict['duplicate'] = {}
            inputdict['duplicate']['frequency'] = "weekly"
            inputdict['duplicate']['count'] = countWeeks(parseDate(startdate), parseDate(enddate))
            
            create_calendar_event(canvas, inputdict)  

    printlog("Writing Exams...")
    
    # Write Exam Dates 
    for i in range(len(postdict['info']['class_meets_locations'])):
        section = postdict['info']['course_sections'][i]['section']       

        if not (postdict['info']['midtermexam'][i]['mdate'] == "TBD"):
            startd = getDateString(parseDate(postdict['info']['midtermexam'][i]['mdate']))
            startd = startd + "T"
            startd = startd + getTimeString(parseTime(postdict['info']['midtermexam'][i]['mstarttime'])) # leave in local time
            
            endd = getDateString(parseDate(postdict['info']['midtermexam'][i]['mdate']))
            endd = endd + "T"
            endd = endd + getTimeString(parseTime(postdict['info']['midtermexam'][i]['mendtime'])) # leave in local time
            
            dtitle = "Midterm Exam"
            location = postdict['info']['midtermexam'][i]['mroom']
            
            # Write the exam:
            inputdict = {}
            inputdict['context_code'] = coursecontext
            inputdict['title'] = dtitle.strip()
            inputdict['description'] = dtitle.strip()
            inputdict['location_name'] = location.strip()
            inputdict['start_at'] = dtstart
            inputdict['end_at'] = dtend 
            inputdict['time_zone_edited'] = CANVAS_TIME_ZONE 
            inputdict['all_day'] = False
            
            create_calendar_event(canvas, inputdict)  

        if not (postdict['info']['finalexam'][i]['fdate'] == "TBD"):
            startd = getDateString(parseDate(postdict['info']['finalexam'][i]['fdate']))
            startd = startd + "T"
            startd = startd + getTimeString(parseTime(postdict['info']['finalexam'][i]['fstarttime'])) # leave in local time, timezone info given above assuming Eastern Time
            
            endd = getDateString(parseDate(postdict['info']['finalexam'][i]['fdate']))
            endd = endd + "T"
            endd = endd + getTimeString(parseTime(postdict['info']['finalexam'][i]['fendtime'])) # leave in local time, timezone info given above assuming Eastern Time
            
            dtitle = "Final Exam"
            location = postdict['info']['finalexam'][i]['froom']
            
            # Write the exam:
            inputdict = {}
            inputdict['context_code'] = coursecontext
            inputdict['title'] = dtitle.strip()
            inputdict['description'] = dtitle.strip()
            inputdict['location_name'] = location.strip()
            inputdict['start_at'] = dtstart
            inputdict['end_at'] = dtend 
            inputdict['time_zone_edited'] = CANVAS_TIME_ZONE 
            inputdict['all_day'] = False
            
            create_calendar_event(canvas, inputdict)    
    
    printlog("Creating Assignment Groups...")
    
    # Write Out Assignment Groups   
    if 'grade_breakdown' in postdict:
        for breakdown in postdict['grade_breakdown']:
            inputdict = {} 
            
            inputdict['name'] = breakdown['category']
            inputdict['group_weight'] = float(rchop(breakdown['weight'], '%'))
            
            # The Assignments group might exist by default - don't call anything that in breakdown just in case
            create_assignmentgroup(course, inputdict)
            
        add_assignments_to_groups(course)

def get_courseid(canvas, user):
    courses = user.get_courses()
    
    for course in courses:
        print(course)
        
    courseid = input("Which Course ID? ")

    return int(courseid)

def parse_discussions(entries):
    for entry in entries:
        print(entry)
        
        replies = entry.replies()
        
        parse_discussions(replies)

def usage():
    print("Usage:")
    print("\t[-h | --help]\tUsage Documentation")
    print("\t[-c | --courseid]\tCanvas Course ID number (can be found using canvas link after logging in); omit for a course listing here")
    print("\t[-m | --markdown]\tPath to course syllabus markdown file")  
    print("\t[-w | --webpage]\tURL of hosted course homepage (https://www.yourhomepage.com/course)")
    print("\t[-a | --apikey]\tAPI Key (get from API_URL + /profile/settings)")
    print("\t[-u | --userid]\tUser ID Number (get from API_URL + /api/v1/users/self)")
    print("\t[-t | --timezone]\tTime Zone (i.e. America/New_York)")
    
# Parse user options
# https://docs.python.org/3/library/getopt.html
try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:m:w:a:u:t:", ["help", "courseid=", "markdown=", "webpage=", "apikey=", "userid=", "timezone="])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

courseid = -1
markdownfile = None
coursehomepage = None
USER_ID = None
API_KEY = None

for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    elif o in ("-c", "--courseid"):
        courseid = int(a)
    elif o in ("-m", "--markdown"):
        markdownfile = a
    elif o in ("-w", "--webpage"):
        coursehomepage = a
    elif o in ("-a", "--apikey"):
        API_KEY = a
    elif o in ("-u", "--userid"):
        USER_ID = a
    elif o in ("-t", "--timezone"):
        CANVAS_TIME_ZONE = a

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
if markdownfile is None:
    markdownfile = input("Enter path to course syllabus markdown file: ")
if coursehomepage is None:
    coursehomepage = input("Enter course website (https://www.yourhomepage.com/course): ")
    
course = canvas.get_course(courseid)

printlog("Reading Markdown...")
# Read Course Markdown File
process_markdown(markdownfile, canvas, course, courseid, coursehomepage)

#printlog("Initiating Course Export...")
# Export Course Content
#course.export_content("zip")

printlog("Parsing Discussions...")
# Gather all Discussion Topics    
topics = course.get_discussion_topics()
for topic in topics:
    entries = topic.get_entries()
        
    parse_discussions(entries)

printlog("Cleaning Up...")

# Delete the default Assignments gradebook group
delete_assignment_group_by_name(course, "Assignments")

# Wait for any child threads to finish            
for t in child_threads:
    t.join()