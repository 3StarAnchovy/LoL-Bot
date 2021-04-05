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
        self.userID = userID
        self.api_key = json_data['Riot_Key'] #로컬에 있는 json 파일의 value로 키 세팅
        self.url = "https://kr.api.riotgames.com"
        self.DataDragon = "http://ddragon.leagueoflegends.com/cdn/11.6.1/data/ko_KR"
    
    def getUserData(self): #유저 정보
        url = self.url+"/lol/summoner/v4/summoners/by-name/"+self.userID+"?api_key="+self.api_key
        res = requests.get(url)
        sum_Lev = res.json().get('summonerLevel') #유저 레벨
        sum_ID = res.json().get('id')  #전적검색 위한 소환사ID
        print("소환사 레벨 : ", sum_Lev)
        print("summonerID : ", sum_ID)

        url_League = self.url + "/lol/league/v4/entries/by-summoner/" + sum_ID + "?api_key=" + self.api_key
        res_League = requests.get(url_League)
        queue_List = res_League.json()  #소환사 티어, 승률, json파일 파싱
        
        for i in range(len(queue_List)):
            que_Type = queue_List[i].get('queueType')
            if(que_Type == "RANKED_SOLO_5x5"):
                print("솔로랭크 정보입니다.")  #솔랭 전적 출력
                print("티어 : ", queue_List[0].get('tier'), queue_List[0].get('rank'), queue_List[0].get('leaguePoints'), "포인트")
                #티어, 랭크, 리그포인트 출력
                win = int(queue_List[0].get('wins'))
                lose = int(queue_List[0].get('losses'))
                print("승률 : ", round((win/(lose+win))*100, 1), "%")  #승률 출력
            elif(que_Type == "RANKED_FLEX_SR"):
                print("자유랭크 정보입니다.")  #자랭 전적 출력
                print("티어 : ", queue_List[1].get('tier'), queue_List[1].get('rank'), queue_List[1].get('leaguePoints'), "포인트")
                #티어, 랭크, 리그포인트 출력
                win = int(queue_List[1].get('wins'))
                lose = int(queue_List[1].get('losses'))
                print("승률 : ", round((win/(lose+win))*100, 1), "%")  #승률 출력
            else:
                print("자료가 없습니다.")

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
#test.getChampRotation()