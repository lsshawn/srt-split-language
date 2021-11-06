import pysrt
subs = pysrt.open('./data.srt')

with open('en.srt','w') as englishOutput, open('cn.srt', 'w') as chineseOutput:
    for sub in subs:
        index = str(sub.index)
        englishOutput.write(index + '\n')
        chineseOutput.write(index + '\n')

        time = str(sub.start) + ' --> ' + str(sub.end)
        englishOutput.write(time + '\n')
        chineseOutput.write(time + '\n')

        text = sub.text.split('\n')
        cn = text[0]
        chineseOutput.write(cn + '\n\n')

        if len(text) == 2:
            en = text[1]
            englishOutput.write(en + '\n\n')
        else:
            englishOutput.write('\n')

