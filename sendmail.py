#! /usr/bin/python
# -*- coding: utf-8 -*-
import logging.handlers, logging, sys

def readxls(filename, sheetname):
    ''' this is for read the excel2003 message.'''
    import xlrd
    wb = xlrd.open_workbook(filename)
    return wb.sheet_by_name(sheetname)

def sendmail(toaddr, msg):
    ''' this is for send a mail.'''
    import smtplib
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com:25')
    smtp.login('zhao_weien', 'wayne@78')
    smtp.sendmail('zhao_weien@163.com', toaddr, msg)
    smtp.quit()

def retrieve_to_address():
    '''' Return the email address according the bank account.'''
    import csv
    csvRdr = csv.reader(open('addresses.csv'))
    addresses = {}
    for row in csvRdr:
        addresses[row[0]] = row[1]
    return addresses

def build_mail(toaddr, items, row):
    ''' Build the email address, items and row content.'''
    from email.mime.text import MIMEText
    crnl = '\r\n'
    content = '薪酬明细：' + crnl
    for i in range(len(items)):
        content = content + items[i].encode('utf-8') + ': ' + \
        unicode(row[i]).encode('utf-8') + crnl
    msg = MIMEText(content)
    msg['Subject'] = '薪酬单'
    msg['From'] = u'花都区成人教育培训中心财务室'
    msg['To'] = toaddr
    msg.set_charset('utf-8')
    sendmail(toaddr, msg.as_string())

def main():
    # open the xls file.
    sh = readxls('lessonpayment.xls','Sheet1')

    # search and retrieve all items.
    match = u'身份证姓名'
    for i in range(sh.nrows):
        matched = False
        row = sh.row_values(i)
        for j in range(len(row)):
            if match == row[j]:
                items = row
                matched = True
                break
        if matched:
            break
    
    # send messages
    addresses = retrieve_to_address()
    log = []
    for i in range(i + 2, sh.nrows):
        try:
            address = addresses[sh.row_values(i)[0]].encode()
            build_mail(address, items, sh.row_values(i))
        except KeyError, e:
            log.append('account ' + e.args[0].encode() + \
                       " doesn't map to an address.")
    sendlog('\r\n'.join(log))

def sendlog(msg):
    smtphdl = logging.handlers.SMTPHandler(mailhost='smtp.163.com',\
           fromaddr='zhao_weien@163.com', toaddrs=['zhao_weien@163.com'],\
           subject='log', credentials=('zhao_weien','wayne@78'))
    log = logging.getLogger('logger')
    log.addHandler(smtphdl)
    log.warning(msg)

if __name__ == '__main__':
    main()