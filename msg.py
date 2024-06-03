import discord,time
import re
intents = discord.Intents.default()
intents.members = True  #

bot_token_msg = ''
userNames = []
owo = 1226390402953908355 
TnD = 1226448741582635059
pok = 1226481087966875728
pkB = 1226481983631392778
no2 = 1228218537764716545

class MyBot(discord.Client):
  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')

  async def on_message(self, message):
    if message.author == self.user:  # Prevent bot from replying to itself
      return
    message_id = message.id
    channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
    fetched_message = await channel.fetch_message(message_id)
    
    if ('https://tenor.com' ) in fetched_message.content  :  # This will ignore the GIF links
        pass
    else :
        if message.channel.id == owo :
           pass
        elif message.channel.id == pkB :
           pass
        elif message.channel.id == pok :
           pass
        elif message.channel.id == no2 :
           pass
        elif message.channel.id == TnD :
           pass
        
        else:
          print(message.author.name," - ",fetched_message.clean_content )
          with open(f"dta.txt",'a') as chatDTA :
             tempMSG = fetched_message.clean_content
             encoded_msg = tempMSG.encode("utf-8")
             chatDTA.write(f"{message.author.name} - {encoded_msg}\n")
             
     



    # Assigning the users to there name
    if message.author in userNames:  # This will add the username to the list 
        pass
    else:
        userNames.append(message.author.name)
    

client = MyBot(intents=intents)
client.run(bot_token_msg)
def filter_msg():
    with open("dta.txt", 'r') as f:
        data = f.read()
        filtering_data=re.findall('b \'', data)
        z = re.sub("b'", "", data)
        with open('filterdata.txt', 'w')as g :
            g.write(z)
filter_msg()

