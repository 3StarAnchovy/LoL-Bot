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
        sum_Lev = res.json().get('summonerLevel')
        sum_ID = res.json().get('id')
        print("소환사 레벨 : ", sum_Lev)
        print("summonerID : ", sum_ID)

    
    def getChampRotation(self): #챔프 로테이션
        url = self.url + "/lol/platform/v3/champion-rotations"+"?api_key="+self.api_key
        res = requests.get(url)
        rotation_list = res.json().get('freeChampionIds') #type = list
        print("챔피언 리스트 배열 : ",rotation_list,"\n")
        
        url = self.DataDragon + "/champion.json"
        res = requests.get(url)
        champ_data = res.json().get('data')
        for champ_name , chame_des in champ_data.items():
            #print(champ_data.get(champ_name).get('key'))
            for rotation in rotation_list:
                #print(rotation)
                if champ_data.get(champ_name).get('key') == str(rotation):
                    print(champ_data.get(champ_name).get('name'))
        #return champ_data

userID = input("userID : ")
test = RiotData(userID)
test.getUserData()
print("\n")
test.getChampRotation()

#test1

#api_key = "RGAPI-e829d34c-823a-48e2-8496-f25301e2ceee"
#url ="https://kr.api.riotgames.com"+"/lol/summoner/v4/summoners/by-name/"+"HongJiMin"+"?api_key="+api_key
#res = requests.get(url)
#브런치 힘들어,,