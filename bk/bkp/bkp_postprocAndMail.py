import smtplib
from email.message import EmailMessage
import sys
import re
from openpyxl import Workbook
from pathlib import Path
import datetime as dt

re0 = re.compile('(20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ([0-9][0-9]:[0-9][0-9]:[0-9][0-9])')
re3 = re.compile('Latency: +([0-9.]+)(.+)$')
re4 = re.compile('Download: +([0-9.]+)(.+)$')
re5 = re.compile('Upload: +([0-9.]+)(.+)$')


#def main(fn):
fn = 'bbk.log'
if True:
    fp = Path(fn)
    xlp = fp.with_suffix('.xlsx')
    if (xlp.exists()):
        newName = "old_" + dt.datetime.now().strftime("%Y-%m-%d_%H%M%S_") + xlp.name
        xlp.rename(xlp.with_name(newName))
    wb = Workbook()
    wb.active.append(['dag', 'tid_hms', 'tid_hm', 'latens', 'enhet latens', 'ner', 'enhet ner', 'upp', 'enhet upp'])
    with open(fp) as fh:
        for n,l in enumerate(fh):
            nm7 = n % 7
            if (0 == nm7):
                m = re0.search(l)
                row = [m[1],m[2], m[2][:-3]]
            elif (1 == nm7):
                pass
            elif (2 == nm7):
                pass
            elif (3 == nm7):
                m = re3.search(l)
                row.append(float(m[1]))
                row.append(m[2])
            elif (4 == nm7):
                m = re4.search(l)
                row.append(float(m[1]))
                row.append(m[2])
            elif (5 == nm7):
                m = re5.search(l)
                row.append(float(m[1]))
                row.append(m[2])
            elif (6 == nm7):
                wb.active.append(row)
    wb.save(xlp)
    fp.rename(fp.with_name("done" + dt.datetime.now().strftime("%Y-%m-%d_%H%M%S_") + fp.name))
    textfile='mail.txt'

    with open(textfile) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())

    msg['Subject'] = f'The contents of {textfile}'
    msg['From'] = 'system@wengle.se'
    msg['To'] = 'boe@wengle.se'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    
#if '__main__' == __name__:
#    if (2 == len(sys.argv)):
#        main(sys.argv[1])
#    else:
#        print(f'Usage: {sys.argv[0]} <bbk.log> ')
