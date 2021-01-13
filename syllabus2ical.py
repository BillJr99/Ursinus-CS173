import frontmatter
import sys
from datetime import datetime,timedelta
import uuid
from dateutil import tz
import os

uidseed = -1

def genuid():
    # https://pynative.com/python-uuid-module-to-generate-universally-unique-identifiers/
    global uidseed
    global coursenum
    
    if uidseed == -1:
        # https://stackoverflow.com/questions/17888152/parse-string-to-int-when-string-contains-a-number-extra-characters
        uidseed = int(''.join(c for c in coursenum if c.isdigit())) * 10000000000
    
    UUID_x = uuid.UUID(int=uidseed)
    uidseed = uidseed + 1
    return UUID_x 

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
    
def getDateString(dt):
    return dt.strftime('%Y%m%d')
    
def getTimeStringAsZulu(t, timedate=None):
    # Convert from Eastern Time/Local Time Zone to Zulu Time
    # https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local-datetime
    
    from_zone = tz.tzlocal() # tz.gettz('America/New_York')
    to_zone = tz.tzutc() # tz.gettz('UTC')
    
    # Check for dst
    dstoffset = None
    if timedate:
        timedate = timedate.replace(tzinfo=from_zone)
        dstoffset = timedate.dst()
    
    t = t.replace(tzinfo=from_zone)
    t = t.astimezone(to_zone)
    
    if dstoffset:
        t = t + timedelta(dstoffset)
    
    return t.strftime('%H%M%S')
    
def getTimeString(t):   
    return t.strftime('%H%M%S')    
    
def parseDate(dt):
    return datetime.strptime(dt, '%Y/%m/%d')
    
def parseTime(t):
    return datetime.strptime(t, '%I:%M %p')
    
def adddays(dt, n):
    return dt + timedelta(days=n)
    
def addweeks(dt, n):
    return dt + timedelta(days=7*n)
    
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

def geticalday(d):
    if d == 'M':
        return 'MO'
    elif d == "T":
        return "TU"
    elif d == "W":
        return "WE"
    elif d == "R":
        return "TH"
    elif d == "F":
        return "FR"
    elif d == "S":
        return "SA"
    elif d == "U":
        return "SU"
    else:
        return ""
    
if len(sys.argv) <= 1:
    fname = "_pages/syllabus.md"
else:
    fname = sys.argv[1]
    
f = open(fname, 'r')
mdcontents = f.read()

post = frontmatter.loads(mdcontents)
postdict = post.to_dict()

if not os.path.exists("files"):
    try:
        os.makedirs("files")
    except:
        pass

coursenum = postdict['info']['course_number']
        
outfname = 'files/' + coursenum + '.ics'
outf = open(outfname, 'w+')

coursename = postdict['info']['course_title']
startdate = postdict['info']['course_start_date']
enddate = postdict['info']['course_end_date']
homepage = postdict['info']['course_homepage']
isM = postdict['info']['class_meets_days']['isM']
isT = postdict['info']['class_meets_days']['isT']
isW = postdict['info']['class_meets_days']['isW']
isR = postdict['info']['class_meets_days']['isR']
isF = postdict['info']['class_meets_days']['isF']
isS = postdict['info']['class_meets_days']['isS']
isU = postdict['info']['class_meets_days']['isU']

outf.write("BEGIN:VCALENDAR\r\nVERSION:2.0\r\n")

# DST Timezone Information for Recurring Times under current time zone rules
outf.write("BEGIN:VTIMEZONE\r\nTZID:US-Eastern\r\nLAST-MODIFIED:20070101T000000Z\r\nTZURL:http://zones.stds_r_us.net/tz/US-Eastern\r\nBEGIN:STANDARD\r\nDTSTART:19671029T020000\r\nRRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=11\r\nTZOFFSETFROM:-0400\r\nTZOFFSETTO:-0500\r\nTZNAME:EST\r\nEND:STANDARD\r\nBEGIN:DAYLIGHT\r\nDTSTART:19870405T020000\r\nRRULE:FREQ=YEARLY;BYDAY=2SU;BYMONTH=3\r\nTZOFFSETFROM:-0500\r\nTZOFFSETTO:-0400\r\nTZNAME:EDT\r\nEND:DAYLIGHT\r\nEND:VTIMEZONE\r\n")

# Write the lecture schedule as a recurring event - recurring events do not account for rescheduled or designated dates, which will be updated on the syllabus; designated dates will be excepted from the recurring rule
for i in range(len(postdict['info']['class_meets_locations'])):
    section = postdict['info']['course_sections'][i]['section']
    for meeting in postdict['info']['class_meets_locations'][i]['section']:
        dtstart = getDateString(parseDate(startdate))
        dtstart = dtstart + "T"
        dtstart = dtstart + getTimeString(parseTime(meeting['starttime'])) # leave in local time, timezone info given above assuming Eastern Time
        
        dtend = getDateString(parseDate(startdate)) # assume no event overlaps a day boundary, ends on start date
        dtend = dtend + "T"
        dtend = dtend + getTimeString(parseTime(meeting['endtime'])) # leave in local time, timezone info given above assuming Eastern Time
        
        dtuntil = getDateString(parseDate(enddate)) # for recurrence rule
        dtuntil = dtuntil + "T"
        dtuntil = dtuntil + "235959"
        dtuntil = dtuntil + "Z" 

        location = meeting['place']
        
        repeatday = geticalday(meeting['day'])
        
        rrule = "RRULE:FREQ=WEEKLY;BYDAY=" + repeatday + ";INTERVAL=1;UNTIL=" + dtuntil
        
        # Write Holiday Exceptions
        if postdict['university']['semester'] == "Fall":
            hdatekey = 'fallholidays'
        elif postdict['university']['semester'] == "Spring":
            hdatekey = 'springholidays'
        else:
            hdatekey = None
            
        if not (hdatekey is None):      
            for holiday in postdict['university'][hdatekey]:
                dtholiday = getDateString(parseDate(holiday['date']))       
                rrule = rrule + "\r\nEXDATE:" + dtholiday

        # Write Key Date Exceptions
        if postdict['university']['semester'] == "Fall":
            kdatekey = 'fall'
        elif postdict['university']['semester'] == "Spring":
            kdatekey = 'spring'
        else:
            kdatekey = None
            
        if not (kdatekey is None):
            for keydate in postdict['university'][kdatekey]:
                dtkeydate = getDateString(parseDate(keydate['kdate']))
                keydescription = keydate['kname']    

                if keydescription.lower().startswith("designated"):
                    rrule = rrule + "\r\nEXDATE:" + dtkeydate

        outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + dtstart + "\r\nDTSTART;TZID=US-Eastern:" + dtstart + "\r\nDTEND;TZID=US-Eastern:" + dtend + "\r\n" + rrule + "\r\nSUMMARY:" + coursenum + " " + coursename + " Section " + section + " Class Meeting\r\nLOCATION:" + location + "\r\nDESCRIPTION:\r\nPRIORITY:3\r\nEND:VEVENT\r\n")

for item in postdict['schedule']:   
    weekidx = item['week']
    dayidx = item['date']
    if 'title' in item:
        title = item['title']
    else:
        title = "N/A"
    if 'link' in item:
        link = item['link']
        
        if not link.startswith("http"): 
            link = rchop(homepage, '/') + '/' + stripnobool(link)
    else:
        link = ""
     
    startd = getCourseDate(startdate, weekidx, dayidx, isM, isT, isW, isR, isF, isS, isU)
    description = stripnobool(link)
    
    if 'readings' in item:
        for reading in item['readings']:      
            rtitle = reading['rtitle']
            
            if 'rlink' in reading:
                rlink = reading['rlink']
            else:
                rlink = ""
                
            if rlink:
                if not rlink.startswith("http"): 
                    rlink = rchop(homepage, '/') + '/' + stripnobool(rlink)
            else:
                rlink = stripnobool(rlink)
            
            description = stripnobool(description) + "\\nReading: " + stripnobool(rtitle) + " " + stripnobool(rlink) 
        
    if 'deliverables' in item:
        for deliverable in item['deliverables']:        
            dtitle = deliverable['dtitle']
            
            if 'dlink' in deliverable:
                dlink = deliverable['dlink']
            else:
                dlink = ""
            
            if dlink:
                if not dlink.startswith("http"): 
                    dlink = rchop(homepage, '/') + '/' + stripnobool(dlink)
            else:
                dlink = stripnobool(dlink)
            
            description = stripnobool(description) + "\\nDeliverable: " + stripnobool(dtitle) + " " + stripnobool(dlink) 
        
            # Write the Assignment as an all-day event
            outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + startd + "T000000Z" + "\r\nDTSTART;VALUE=DATE:" + startd + "\r\nSUMMARY:" + coursenum + " " + coursename + ": " + stripnobool(dtitle) + "\r\nLOCATION:\r\nDESCRIPTION:\r\nPRIORITY:3\r\nEND:VEVENT\r\n")        
    # Write the lecture as an all-day event:
    outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + startd + "T000000Z" + "\r\nDTSTART;VALUE=DATE:" + startd + "\r\nSUMMARY:" + coursenum + " " + coursename + ": Class Meeting\r\nLOCATION:\r\nDESCRIPTION:" + stripnobool(description) + "\r\nPRIORITY:3\r\nEND:VEVENT\r\n")
    
# Write Office Hours as a Recurring Event - recurring events do not account for rescheduled or designated dates, which will be updated on the syllabus; designated dates will be excepted from the recurring rule
for instructor in postdict['instructors']:
    instructorname = instructor['name']
    
    for officehour in instructor['officehours']:        
        dtstart = getDateString(parseDate(startdate))
        dtstart = dtstart + "T"
        dtstart = dtstart + getTimeString(parseTime(officehour['starttime'])) # leave in local time, timezone info given above assuming Eastern Time

        dtend = getDateString(parseDate(startdate)) # assume no event overlaps a day boundary, ends on start date
        dtend = dtend + "T"
        dtend = dtend + getTimeString(parseTime(officehour['endtime'])) # leave in local time, timezone info given above assuming Eastern Time

        dtuntil = getDateString(parseDate(enddate)) # for recurrence rule
        dtuntil = dtuntil + "T"
        dtuntil = dtuntil + "235959"
        dtuntil = dtuntil + "Z" 

        location = officehour['location']
        
        repeatday = geticalday(officehour['day'])
        
        rrule = "RRULE:FREQ=WEEKLY;BYDAY=" + repeatday + ";INTERVAL=1;UNTIL=" + dtuntil
        
        # Write Holiday Exceptions
        if postdict['university']['semester'] == "Fall":
            hdatekey = 'fallholidays'
        elif postdict['university']['semester'] == "Spring":
            hdatekey = 'springholidays'
        else:
            hdatekey = None
            
        if not (hdatekey is None):      
            for holiday in postdict['university'][hdatekey]:        
                dtholiday = getDateString(parseDate(holiday['date']))       
                rrule = rrule + "\r\nEXDATE:" + dtholiday
                
        # Write Key Date Exceptions
        if postdict['university']['semester'] == "Fall":
            kdatekey = 'fall'
        elif postdict['university']['semester'] == "Spring":
            kdatekey = 'spring'
        else:
            kdatekey = None
            
        if not (kdatekey is None):
            for keydate in postdict['university'][kdatekey]:
                dtkeydate = getDateString(parseDate(keydate['kdate']))
                keydescription = keydate['kname']    

                if keydescription.lower().startswith("designated"):
                    rrule = rrule + "\r\nEXDATE:" + dtkeydate                

        outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + dtstart + "\r\nDTSTART;TZID=US-Eastern:" + dtstart + "\r\nDTEND;TZID=US-Eastern:" + dtend + "\r\n" + rrule + "\r\nSUMMARY:" + coursenum + " " + coursename + " Office Hours with " + instructorname + "\r\nLOCATION:" + location + "\r\nDESCRIPTION:\r\nPRIORITY:3\r\nEND:VEVENT\r\n")

# Write Exam Dates 
for i in range(len(postdict['info']['class_meets_locations'])):
    section = postdict['info']['course_sections'][i]['section']       

    if not (postdict['info']['midtermexam'][i]['mdate'] == "TBD"):
        startd = getDateString(parseDate(postdict['info']['midtermexam'][i]['mdate']))
        startd = startd + "T"
        startd = startd + getTimeString(parseTime(postdict['info']['midtermexam'][i]['mstarttime'])) # leave in local time, timezone info given above assuming Eastern Time
        
        endd = getDateString(parseDate(postdict['info']['midtermexam'][i]['mdate']))
        endd = endd + "T"
        endd = endd + getTimeString(parseTime(postdict['info']['midtermexam'][i]['mendtime'])) # leave in local time, timezone info given above assuming Eastern Time
        
        dtitle = "Midterm Exam"
        location = postdict['info']['midtermexam'][i]['mroom']
        
        # Write the exam:
        outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + startd + "\r\nDTSTART;VALUE=DATE:" + startd + "\r\nDTEND;VALUE=DATE:" + endd + "\r\nSUMMARY:" + coursenum + " " + coursename + ": " + stripnobool(dtitle) + "\r\nLOCATION:" + stripnobool(location) + "\r\nDESCRIPTION:\r\nPRIORITY:3\r\nEND:VEVENT\r\n") 

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
        outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + startd + "\r\nDTSTART;VALUE=DATE:" + startd + "\r\nDTEND;VALUE=DATE:" + endd + "\r\nSUMMARY:" + coursenum + " " + coursename + ": " + stripnobool(dtitle) + "\r\nLOCATION:" + stripnobool(location) + "\r\nDESCRIPTION:\r\nPRIORITY:3\r\nEND:VEVENT\r\n")     

# Write University Dates
if postdict['university']['semester'] == "Fall":
    kdatekey = 'fall'
elif postdict['university']['semester'] == "Spring":
    kdatekey = 'spring'
else:
    kdatekey = None
    
if not (kdatekey is None):
    for keydate in postdict['university'][kdatekey]:
        startd = getDateString(parseDate(keydate['kdate']))
        description = keydate['kname']
          
        # Write the key date as an all-day event:
        outf.write("BEGIN:VEVENT\r\nUID:" + stripnobool(genuid()) + "\r\nDTSTAMP:" + startd + "T000000Z" + "\r\nDTSTART;VALUE=DATE:" + startd + "\r\nSUMMARY:" + stripnobool(description) + "\r\nLOCATION:\r\nDESCRIPTION:" + stripnobool(description) + "\r\nPRIORITY:3\r\nEND:VEVENT\r\n")
               
outf.write("END:VCALENDAR\r\n")

f.close()
outf.close()