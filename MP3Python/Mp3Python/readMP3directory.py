def readMP3directory(inPath, inMap):
    import os 
    '''
    Created on 3 Sep 2016

    @author: mark dwyer
    '''
    index=inMap[0]
    print('['+inPath+','+str(index)+']')
    files = os.listdir(inPath)
    print(files)
    for f in files:
        thisFile=inPath+'/'+f
        print ('os.path.isdir(f)'+str(os.path.isdir(thisFile))+inPath+f)
        if os.path.isdir(str(thisFile)):
            inMap[0]=index
            inMap=readMP3directory(thisFile,inMap)  
        else:
            print(f+':'+str(os.path.isfile(thisFile)));
            if os.path.isfile(thisFile):
                fileSize=os.path.getsize(thisFile)
                if (fileSize< 1000000):
                    print('Skipping .. too small')
                else:
                    index=index+1
                    print('['+str(index)+']:'+thisFile+',size:'+str(fileSize))    
                    inMap[index]=[thisFile,fileSize]
    return inMap

i=1
mp3files={}
mp3files[0]=0
inputPath='/Users/mark/Music'
mp3files = readMP3directory(inputPath,mp3files)
g=mp3files[0]
print('all loaded ...'+str(g)+' items')
jj=0

for xx in mp3files.keys():
    fileName = mp3files[xx]
    jj=jj+1
    #print('['+str(jj)+':'+str(fileName)+']')
    
print('Number of file found:'+str(jj))



