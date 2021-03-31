#라이엇 api

#todo
# 1. 각자 데이터 출력하게끔 메소드 생성 및 주석 작성
# 2. 키 분리
# 3. 모듈화 후 디스코드 봇에서 사용
import requests
import json
class RiotData:
    def __init__(self,userID): #set
        with open('key.json') as json_file:
            json_data = json.load(json_file)
        self.userID=userID
        self.api_key = json_data['Riot_Key'] #로컬에 있는 json 파일의 value로 키 세팅
        self.url = "https://kr.api.riotgames.com"
        self.DataDragon = "http://ddragon.leagueoflegends.com/cdn/11.6.1/data/ko_KR"
    
    def getUserData(self): #유저 정보
        url = self.url+"/lol/summoner/v4/summoners/by-name/"+self.userID+"?api_key="+self.api_key
        res = requests.get(url)
        return res
    
    def getChampRotation(self): #챔프 로테이션
        url = self.url + "/lol/platform/v3/champion-rotations"+"?api_key="+self.api_key
        res = requests.get(url)
        rotation_list = res.json().get('freeChampionIds') #type = list
        print("챔피언 리스트 배열 : ",rotation_list,"\n")
        
        url = self.DataDragon + "/champion.json"
        res = requests.get(url)
        champ_data = res.json().get('data')
        return champ_data

userID = input("userID : ")
test = RiotData(userID)
print(test.getUserData().json(),"\n")
print(type(test.getChampRotation()))

#test1

#api_key = "RGAPI-cce887fb-67e8-487a-a70d-2476970599c2"
#url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
#res = requests.get(url)
#브런치 힘들어,,