import report
import random
import datetime
import time

def delayReport (reportDays,submitDelay=0.0):
    reportData = {"date": "", "temperature": "", "county": "宝山区",
                  "campusLocation": "宝山", "Time_1or2": "1", "location": "具体地址"}
    reportDateList=[]
    studentInfoList = [["18100000","password"],["18000000","password"] ]
    timeUTC = datetime.datetime.utcnow()
    timeLocal = timeUTC + datetime.timedelta(hours=8)
    reportTime = timeLocal
    for i in range(1,reportDays+1):
        reportTime = reportTime - datetime.timedelta(days=1)
        reportDateList.append( reportTime.strftime('%Y - %m - %d'))



    for studentInfo in studentInfoList:
        reportData.update({'temperature': str(round(random.uniform(36, 36.5), 2))})  # 随机温度
        try:
            cookie =report.get_cookies(studentInfo)
        except:
            print("无法获取学号  " + studentInfo[0] + "  的cookie,可能是账号密码错误")
            continue

        for reportDate in reportDateList:
            reportData.update({"date":reportDate})
            for Time_1or2 in ["1", "2"]:
                reportData.update({"Time_1or2": Time_1or2})
                reportSuccess = report.daily_report(cookie, reportData)
                if (reportSuccess) == -1:
                    print(str(studentInfo[0] +"   "+reportDate + "   补报失败，可能已经报送过"))
                else:
                    print(str(studentInfo[0] +"   "+ reportDate + "   提交成功"))
                time.sleep(submitDelay)

if __name__ == '__main__':

    delayReport(50) #补报天数,补报延时(s)