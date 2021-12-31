import pandas as pd
import requests
from bs4 import BeautifulSoup


class crawling_data():
    def __init__(self):
        self.now_datetime = []
        self.temperature = []
        self.sensible = []



    def crawling(self, day_hour):

        # 초기 datetime
        tmp_datetime = day_hour

        print(tmp_datetime)


        str_datetime = tmp_datetime.strftime("%Y.%m.%d.%H") 
        url = f"https://www.weather.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&reg=100&auto_man=m&tm={str_datetime}%3A00"
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.select('#content_weather > table > tbody > tr:nth-child(42)>td')

            # 기온 추출
            temp_now = temp[5].text
            sensible_now = temp[7].text
            print(tmp_datetime)
            
            return tmp_datetime, temp_now, sensible_now
#             self.now_datetime.append(tmp_datetime)
#             self.temperature.append(temp_now)
#             self.sensible.append(sensible_now)
#             print(self.sensible)

        # 시간 추가
    #             tmp_datetime = tmp_datetime + datetime.timedelta(hours=1)


        else : 
            print(response.status_code)
            print(tmp_datetime)

    #         if count % 10 == 0:
    #             time.sleep(0.12)
    #             print(count)
    #             print(tmp_datetime)
    def hi(self, h):
        print(h)
        
    
    def save_csv(self):
        result = pd.DataFrame()
        result['시간'] = self.now_datetime
        result['온도'] = self.temperature
        result['체감온도'] = self.sensible
        
        result.to_csv('temp.csv', index=False)
    
    

def worker(x): 
    return x * x