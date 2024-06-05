import discord,time
import re
import Confidential
# import TextBlob
intents = discord.Intents.default()
intents.members = True  #

bot_token = Confidential.token
class MyBot(discord.Client):
   async def on_ready(self):
      print(f'Logged in as {self.user} (ID: {self.user.id})')

   async def on_message(self, message):
      if message.author == self.user:  # Prevent bot from replying to itself
         return
      bot_owner = await self.fetch_user(738739339969822730) 
      message_id = message.id
      channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
      fetched_message = await channel.fetch_message(message_id)
      dm_channel = await bot_owner.create_dm()
      if ('https://tenor.com' ) in fetched_message.content  :  # This will ignore the GIF links
         pass
      elif '<@738739339969822730>' in fetched_message.content : 
            print ("Owner has tagged")
            dm_message = f"**Hey!**"
            channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
            fetched_message = await channel.fetch_message(message_id)
            print(f" {fetched_message.content}")
            
            dm_message += f" You were mentioned by {message.author.mention} in {message.channel.name}: {fetched_message.clean_content} \n"
            await dm_channel.send(dm_message) 
            print(message.author.name," - ",fetched_message.clean_content )
      else:
         print(message.author.name," - ",fetched_message.clean_content )
            

client = MyBot(intents=intents)
client.run(bot_token)


