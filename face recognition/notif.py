from pushbullet import Pushbullet
API_KEY="your-key"


file="Alert text.txt"

with open(file,mode='r') as f:
    text=(f.read())

pb=Pushbullet(API_KEY)
push=pb.push_note('Checking',text)