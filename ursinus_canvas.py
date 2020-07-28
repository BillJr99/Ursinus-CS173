# https://canvasapi.readthedocs.io/en/stable/
from canvasapi import Canvas, exceptions
import getopt
import sys
import frontmatter
from datetime import datetime, timedelta

# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/course.py
# https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/canvas.py

# CONSIDERATION
# course.create_course_section - separate calendar?  duplicate assignments, etc?
# Change course calendar entries to timetables: which can possibly be done on a per-section basis
## https://canvas.instructure.com/doc/api/calendar_events.html#method.calendar_events_api.set_course_timetable
# Handle content export (also download?)
# Handle exporting discussions
# Add assignment rubrics and point values (course.create_rubric) from assignment pages to facilitate grading (also to update point values)
## # https://canvas.instructure.com/doc/api/rubrics.html
# Tie to learning outcomes

API_URL = "https://ursinus.instructure.com/"
# Generate key at API_URL + profile/settings
# Obtain User ID from API_URL + /api/v1/users/self
CANVAS_TIME_ZONE = "America/New_York"

def stripnobool(val):
    if type(val) is bool:
        result = ""
    else:
        result = str(val)
    
    return result.strip()
    
def delete_all_events(canvas, coursecontext):
    events = canvas.get_calendar_events(all_events = True, context_codes = [coursecontext])
    
    for event in events:
        event.delete()

def delete_all_assignments(course):
    assignments = course.get_assignments()

    for assignment in assignments:
        assignment.delete()
        
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
    
def getCourseDate(startdate, weeknum, dayidx, M, T, W, R, F, S, U):
    dt = parseDate(startdate)
    weeknum = int(weeknum)
    dayidx = int(dayidx)
    
    dt = addweeks(dt, weeknum)
    daynum = getDayNum(dayidx, M, T, W, R, F, S, U)
    dt = adddays(dt, daynum)
    
    return getDateString(dt)
    
# Create Assignment Shells: https://canvasapi.readthedocs.io/en/stable/examples.html#create-an-assignment
def create_assignment(course, inputdict):
    course.create_assignment(inputdict)
    
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
    
    course.update(course={'time_zone': CANVAS_TIME_ZONE}) # Set time zone to Eastern Time
    course.update(course={'syllabus_body': "<iframe src=\"" + homepage + "\" title=\"Course Homepage\" width=\"1024\" height=\"768\"></iframe>"}) # Set Syllabus to Course Webpage
    
    # Delete All Assignments and Events, Re-Initialize Here
    delete_all_assignments(course)
    delete_all_events(canvas, coursecontext)
    
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
            
        if 'deliverables' in item:
            for deliverable in item['deliverables']:        
                dtitle = deliverable['dtitle']
                if 'stripnobool(dlink)' in deliverable:
                    dlink = deliverable['stripnobool(dlink)']
                else:
                    dlink = ""
                
                description = dtitle.strip() 
            
                # Write the Assignment as an all-day event
                inputdict = {}
                inputdict['context_code'] = coursecontext
                inputdict['title'] = description.strip()
                inputdict['description'] = description.strip()
                inputdict['start_at'] = startd 
                inputdict['time_zone_edited'] = CANVAS_TIME_ZONE 
                inputdict['all_day'] = True
                
                create_calendar_event(canvas, inputdict) 

                # Create an Assignment Shell
                if not (' handed out' in description.lower()):
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
                    inputdict['points_possible'] = 100
                    inputdict['description'] = description + " (" + homepage + stripnobool(dlink) + ")"
                    inputdict['due_at'] = parseDateTimeCanvas(datetime.strptime(startd + "T235900Z", "%Y%m%dT%H%M%SZ"))
                    
                    create_assignment(course, inputdict)
            
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
    
# Instantiate Canvas and Course
canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user(USER_ID)

if courseid == -1:
    courseid = get_courseid(canvas, user)
if markdownfile is None:
    markdownfile = input("Enter path to course syllabus markdown file: ")
if coursehomepage is None:
    coursehomepage = input("Enter course website (https://...): ")
    
course = canvas.get_course(courseid)

# Read Course Markdown File
process_markdown(markdownfile, canvas, course, courseid, coursehomepage)

# Export Course Content
# course.export_content("zip")

# Gather all Discussion Topics    
topics = course.get_discussion_topics()
for topic in topics:
    entries = topic.get_entries()
        
    parse_discussions(entries)
            
