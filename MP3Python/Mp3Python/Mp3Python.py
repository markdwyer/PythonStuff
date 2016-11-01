'''
Created on 25 Aug 2016

@author: mark dwyer
'''
import ConfigParser
import glob
import random
import Mp3Python.readMP3directory

config = ConfigParser.ConfigParser()
config.read('/Users/mark/Documents/workspace-sts-3.4.0.RELEASE/MP3Python/Config.cfg')
inputPath = config.get('main', 'input_path')
outputPath = config.get('main','output_path')
outputSize = config.get('main','output_size')

print("Config Read for run: input_path="+inputPath+", output_path="+outputPath+", output_size="+outputSize+"GB")

#print(os.listdir(inputPath))

#L=os.listdir(inputPath)
#print(L)


i=1
mp3files={}

mp3files = Mp3Python.readMP3directory(inputPath,mp3files)

for filename in glob.iglob(inputPath+'/**/*.*'):
    print('['+str(i)+']:'+filename)
    mp3files[str(i)]=filename
    i=i+1
    

for j in mp3files:
#   print(j)
    print('**['+j+']'+mp3files[j])

usedSpace=0
songCount=0
outputSizeBytes = int(outputSize) * 1024 * 1024 * 1024 
while (usedSpace < outputSizeBytes):
    anotherSong = random.randint(1, i-1)
    print(str(anotherSong))
    fileName=mp3files[str(anotherSong)]
    try :
        f = open(fileName,'r')
    except IOError :
        print('Skipping directory : '+fileName)
    
    data = f.read()
    z=len(data)
    songCount=songCount+1
    print('('+str(songCount)+')'+str(usedSpace)+'#'+str(outputSizeBytes)+'['+str(anotherSong)+'] '+fileName+':['+str(z)+']');
    usedSpace = usedSpace + z 
    
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    