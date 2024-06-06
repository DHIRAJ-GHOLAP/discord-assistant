import time
import discord
from discord.ext import commands
import Confidential
intents = discord.Intents.default()
intents.members = True  

bot_token = Confidential.token
owner_usr_id = 738739339969822730
gali_counter = []
founder_id = 1141700782027194470


class MyBot(discord.Client):
   async def on_ready(self):
      print(f'Logged in as {self.user} (ID: {self.user.id})')

   async def on_message(self, message):
      try:
         founder = await self.fetch_user(founder_id)
         if message.author == self.user:  # Prevent bot from replying to itself
            return
         bot_owner = await self.fetch_user(owner_usr_id) 
         message_id = message.id
         channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
         fetched_message = await channel.fetch_message(message_id)
         dm_channel = await bot_owner.create_dm()
         founder_dm_channel = await founder.create_dm()
         if ('https://tenor.com' ) in fetched_message.content  :  # This will ignore the GIF links
            pass
         elif f'<@{owner_usr_id}>' in fetched_message.content : 
               print ("Owner has tagged")
               dm_message = f"**Hey!**"
               channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
               fetched_message = await channel.fetch_message(message_id)
               print(f" {fetched_message.content}")
               
               dm_message += f" You were mentioned by {message.author.mention} in {message.channel.name}: TIME = {time.strftime(' %I:%M %p')} {fetched_message.clean_content} \n"
               await dm_channel.send(dm_message) 
               print(message.author.name," - ",fetched_message.clean_content )
         
         if (message.author.name == 'flash.homies') and (fetched_message.clean_content == '!b'):
            await fetched_message.delete()
            time.sleep(3)
            for i in range(20):
               await message.channel.send("I am a suside bomber")
         if (message.author.name == founder or bot_owner)and(fetched_message.clean_content.startswith('create staff')):
            founder_dm_message = '! '
            founder_dm_message += f"Sucessfully assign role to "
            cm = fetched_message.content
            role_user = cm[15:-1]
            assigning = await self.fetch_user(role_user)
            
            # await founder_dm_channel.send(founder_dm_channel) 
            role = discord.utils.get(message.guild.roles, name="Staff")  # Replace "Member" with the actual role name
            if role:
                await assigning.add_role(role)
                await message.channel.send(f"Role '{role.name}' assigned to {await self.fetch_user(role_user)}")
            else:
                await message.channel.send("Role not found.")
      except Exception as e:
         print("something went wrong")
         print(e)
         




client = MyBot(intents=intents)
client.run(bot_token)


