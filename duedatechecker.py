import frontmatter
import sys
from datetime import datetime,timedelta
import uuid
from dateutil import tz
import os
from mailjet_rest import Client # pip install mailjet_rest
from email.mime.text import MIMEText
import smtplib

HEADER = 'Early Warning: https://campusweb.ursinus.edu/intranet/apps/AcademicWarning/default.aspx\nExam grades\nGrading\nMidterm checkin\nAttendance Reports: https://ursinus-edu.zoom.us/account/my/report?from=11/01/2020&to=11/30/2020'

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
    print("Specify md file")
    sys.exit(0)

fname = sys.argv[1]
f = open(fname, 'r')
mdcontents = f.read()

post = frontmatter.loads(mdcontents)
postdict = post.to_dict()

coursenum = postdict['info']['course_number']
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

message = ''

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
    description = stripnobool(link)
        
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
            
            description = stripnobool(dtitle) + "\n" + stripnobool(dlink) 
            description = stripnobool(description)
            
            # Date is yyyymmdd format
            yesterday = datetime.now() - timedelta(days=1) 
            currentdate = getDateString(yesterday)
            
            # Any deliverables due/handed out yesterday?
            if currentdate == startd:
                message = message + startd + ": " + description + "\n\n"
            
message = message.strip()
            
if len(message) > 0:
    message = HEADER + '\n\n' + message
    
    #print(message)
    
    if 'MAILJET_KEY' in os.environ and 'MAILJET_SECRET' in os.environ:
        MAILJET_KEY = os.environ['MAILJET_KEY']
        MAILJET_SECRET = os.environ['MAILJET_SECRET']
    
        #print(MAILJET_KEY)
        #print(MAILJET_SECRET)
        
        mailjet = Client(auth=(MAILJET_KEY, MAILJET_SECRET), version='v3.1')

        data = {
          'Messages': [
            {
              "From": {
                "Email": "wmongan@ursinus.edu",
                "Name": "William Mongan"
              },
              "To": [
                {
                "Email": "wmongan@ursinus.edu",
                "Name": "William Mongan"
                }
              ],
              "Subject": "Ursinus Deliverables Reminder",
              "TextPart": message,
              "HTMLPart": message.replace('\n', '<br>')
            }
          ]
        }
        
        result = mailjet.send.create(data=data)
        #print(result.status_code)
        #print(result.json())
    else:
        SMTP_SERVER = os.environ['SMTP_SERVER'] # smtp.ursinus.edu
        SMTP_PORT = os.environ['SMTP_PORT'] # 25
        
        msg = MIMEText(message)
        msg['Subject'] = "Ursinus Deliverables Reminder"
        msg['From'] = "wmongan@ursinus.edu"
        msg['To'] = "wmongan@ursinus.edu"
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:            
            server.sendmail("wmongan@ursinus.edu", "wmongan@ursinus.edu", msg.as_string())  
        
f.close()