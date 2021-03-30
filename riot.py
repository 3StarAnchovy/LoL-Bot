#라이엇 api

#todo
# 1. 각자 데이터 출력하게끔 메소드 생성 및 주석 작성
# 2. 키 분리
# 3. 모듈화 후 디스코드 봇에서 사용
import requests
class RiotData:
    def __init__(self,userID): #set
        self.userID=userID
        self.api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
        self.url="https://kr.api.riotgames.com"
    def getUserData(self): #유저 정보
        url = self.url+"/lol/summoner/v4/summoners/by-name/"+self.userID+"?api_key="+self.api_key
        res = requests.get(url)
        return res

userID = input("userID : ")
test = RiotData(userID)
print(test.getUserData().json())

#api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
#url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
#res = requests.get(url)