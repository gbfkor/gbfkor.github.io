#-*- coding:utf-8 -*- 
import generatePost
import mergesheets

def extractPosts(inputPath="./data/cache/", outputPath="./base/_posts/"):
    fullCSVlist = mergesheets.FindListCSV(inputPath,"quest")
    for filename in fullCSVlist:
        generatePost.GeneratePost(filename,outputPath)

if(__name__ == '__main__'):
    extractPosts()