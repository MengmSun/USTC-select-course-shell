import requests
import time


class PickCourse(object):
    def __init__(self):
        """
        复制粘贴请求头
        将下面值不一样的换掉即可
        """
        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '你的Cookie',
            'origin': 'https://jw.ustc.edu.cn',
            'referer': '你的referer',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "macOS",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.session = requests.Session()

    def add(self, course_id):
        """
        发起选课请求
        """
        url = 'https://jw.ustc.edu.cn//ws/for-std/course-select/add-request'
        payload = {
            'studentAssoc': '你的studentAssoc',
            'lessonAssoc': course_id, # 要选择的课程id
            'courseSelectTurnAssoc': '481', # 根据实际情况填写对应数值
            'scheduleGroupAssoc': '',
            'virtualCost': '0'
        }
        r = self.session.post(url, data=payload, headers=self.headers)
        #print(r.text)
        return r.text

    def add_result(self, id):
        """
        发起是否选课成功请求
        """
        url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/add-drop-response'
        payload = {
            'studentId': '你的studentId',
            'requestId': id # 发起选课请求后的返回值
        }
        r = self.session.post(url, data=payload, headers=self.headers)
        #print(r.json())
        return r.json()

    def pick(self, course_id):
        while(True):
            id = self.add(course_id=course_id)
            result = self.add_result(id=id)
            if result is not None:
                if(result['success'] == False ):
                    print("课程:"+ course_id+ "选择失败!")
                    time.sleep(0.5)  # 每隔0.5秒发起一次选课请求
                elif(result['success'] == True):
                    print("课程:"+ course_id+ "选择成功!")
                    break

if __name__ == "__main__":
    pick_course = PickCourse()
    pick_course.pick(course_id='137459')

# 137459 软件体系结构                               

