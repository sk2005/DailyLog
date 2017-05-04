import sys
import string
import json

InputFile="TODAY.sk"

MyFile = open(InputFile,"r+")
CurrentTodayLine = ""
DateStr = ""
DateTag = "Date"
TopicTag = "Topic"
TopicsList = []
TopicFileName = ""
TopicsObj = {"topics":[]}
TopicsListObj = TopicsObj["topics"]
TopicObj = {"name":"","dates":[]}
TopicDateObj = {"Date":""}
TopicDateBody = ""
inTopic = False
TopicName = "temp"
TopicFile = open("temp.sk",'a+')
try:

    for CurrentTodayLine in MyFile:

        if CurrentTodayLine.find("<") != -1:
            # Found a tag
            print CurrentTodayLine
            InnerStr = Tagtr = TagValueStr = ""
            InnerStr = (CurrentTodayLine.split("<")[1]).split(">")[0]
            print "Inner: "+InnerStr

            if InnerStr and InnerStr.find(":") != -1:
                # The Inner string should be of Tag:Value form
                TagStr = (InnerStr.split(":")[0]).strip()
                TagValueStr = (InnerStr.split(":")[1]).strip()

            if TagStr and TagValueStr:
                # Valid Tag
                print "<%s : %s >" % (TagStr, TagValueStr)
                if TagStr.lower() == DateTag.lower():
                    # This is a Date tag
                    DateStr = TagValueStr
                    inTopic = False
                elif TagStr.lower() == TopicTag.lower():
                    # Found a Topic beginning. Close the existing file
                    TopicName = TagValueStr
                    TopicFile.close()
                    inTopic = True
                    TopicFileName = "%s.txt" % (TopicName)
                    print "Intopic: "+TopicName + "------" + TopicFileName
                    TopicFile = open(TopicFileName,'a')
                    # Ready to starting the Topic Body in file
                    TopicFile.write("Date: "+DateStr+'\n')
                    TopicFile.write("---------------------------\n")
                    #print "Date: "+DateStr+'\n'
                else:
                    # This is a SubTopic. Write to topic file
                    TopicFile.write(CurrentTodayLine+'\n')
                    #print TopicName+"OOOO"+TagStr
                    continue
            else:
                # is a "<  >" found within the lines of boby
                TopicFile.write(CurrentTodayLine+'\n')
                print "Other <> tags found"
                continue

        else:
            # This is a body. Write to topic file
            TopicFile.write(CurrentTodayLine+'\n')
            #print "Topic:"+TopicName+":"+DateStr+":"+CurrentTodayLine
            continue

    TopicFile.close()
    MyFile.close()

except:
        errStr = sys.exc_info()
        print TopicFileName
        sys.exit(errStr)
