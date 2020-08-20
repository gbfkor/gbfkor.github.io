#-*- coding:utf-8 -*- 
import csv
from time import gmtime, strftime

def GeneratePost(inputCsvFile = "", outputFilePath = ""):
    postTitle = inputCsvFile.split('.csv')[0].split('quest_')[1]
    print(postTitle)

    outputFileName = f"2020-08-15-{postTitle}.markdown"
    if len(outputFileName) > 1:
        outputFileName = outputFilePath + outputFileName
    sceneCodes = []

    # 퀘스트 타입 체크
    tempname = inputCsvFile.encode('utf-8')
    cEvent_Mac = b'\xe1\x84\x8b\xe1\x85\xb5\xe1\x84\x87\xe1\x85\xa6\xe1\x86\xab\xe1\x84\x90\xe1\x85\xb3'
    cEvent = b'\xec\x9d\xb4\xeb\xb2\xa4\xed\x8a\xb8'
    cMain_Mac = b'\xe1\x84\x86\xe1\x85\xa6\xe1\x84\x8b\xe1\x85\xb5\xe1\x86\xab'
    cMain = b'\xeb\xa9\x94\xec\x9d\xb8'
    cFate_Mac = b'\xe1\x84\x91\xe1\x85\xa6\xe1\x84\x8b\xe1\x85\xb5\xe1\x84\x90\xe1\x85\xb3'
    cFate = b'\xed\x8e\x98\xec\x9d\xb4\xed\x8a\xb8'
    qType = "Etc"
    if (cEvent in tempname) or (cEvent_Mac in tempname):
        qType = "Event"
    elif (cMain in tempname) or (cMain_Mac in tempname):
        qType = "Main"
    elif (cFate in tempname) or (cFate_Mac in tempname):
        qType = "Fate"
    
    # sceneCode 를 불러오는 과정
    with open(inputCsvFile) as fin:
        csvReader = csv.DictReader(fin)
        for row in csvReader:
            if row["SceneCode"] not in sceneCodes:
                sceneCodes.append(row["SceneCode"])
    
    # sceneCode 를 스트링형식으로 변환
    textOutSceneCode = ''
    for code in sceneCodes:
        textOutSceneCode += f'"{code}", '
    textOutSceneCode += "end"
    textOutSceneCode = textOutSceneCode.replace(', end','')
    if textOutSceneCode == "end":
        textOutSceneCode = ""


    fout=open(outputFileName,"w")
    fout.write(f"""---
layout: post
title:  "{postTitle}"
date:   {strftime("%Y-%m-%d %H:00:00", gmtime())} +0000
categories: {qType}
Tags: Story {qType}
SceneCode: [{textOutSceneCode}]
---
""")
    fout.close()




if(__name__ == '__main__'):
    GeneratePost("cache/quest_메인_1장.csv")