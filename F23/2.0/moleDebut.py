lyricLength = int(input())
wordsLength = int(input())
words = input().split()
pitches = list(map(int,input().split()))
lyrics = input().split()


wordPitch = {}
for word,pitch in zip(words,pitches):
    wordPitch[word] = pitch

#for lyric in lyrics:
#    print(wordPitch[lyric])

lms = [1] * lyricLength
for i in range(lyricLength-1,-1,-1):
    for j in range(i+1,lyricLength):
        if wordPitch[lyrics[i]] < wordPitch[lyrics[j]]:
            lms[i] = max(lms[i],1+lms[j])
print(max(lms))



