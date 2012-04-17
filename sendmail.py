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
    smtp.login('cat1599', '790811')
    smtp.sendmail('cat1599@163.com', toaddr, msg)
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
    content = '薪酬明细（测试）：' + crnl
    for i in range(len(items)):
        content = content + items[i].encode('utf-8') + ': ' + \
        unicode(row[i]).encode('utf-8') + crnl
    content = content + '如有问题，请回复此邮件，或致电财务室徐小慧咨询。'
    msg = MIMEText(content)
    msg['Subject'] = '薪酬单（测试）'
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
            if address=='':
                logmsg='account ' + sh.row_values(i)[0] + \
                       " hasn't an address."
                log.append(logmsg)
            else:
                build_mail(address, items, sh.row_values(i))
                print '账号'+sh.row_values(i)[0].encode('utf-8')+\
                    '的薪酬单已发送到' + address.encode('utf-8')
        except KeyError, e:
            logmsg='account ' + e.args[0].encode() + \
                       " doesn't map to an address."
            log.append(logmsg)
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
