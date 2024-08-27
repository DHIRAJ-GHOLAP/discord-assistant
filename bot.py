print('change the info in config.json file and if you have any queries the join my server link - discord.gg/invites/homies-here')
import time
import discord
from discord.ext import commands
import json  

with open('config.json', 'r') as f:
    config = json.load(f)



bot_token = config['BOT_TOKEN']
owner_usr_id = config['OWNER_USER_ID']
founder_id = config['FOUNDER_ID']
gc = config['GC_CHANNEL_ID']
admins = config['ADMINS']
compliments = config['COMPLIMENTS']
log = config['logchannel']



intents = discord.Intents.default()
intents.members = True

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        try:
            ###########################################################################
            ##################### Main code ###########################################
            ###########################################################################
            bot_owner = await self.fetch_user(owner_usr_id)
            founder = await self.fetch_user(founder_id)

            if message.author == self.user:  
                return

            message_id = message.id
            channel = self.get_channel(message.channel.id) 
            fetched_message = await channel.fetch_message(message_id)
            dm_channel = await bot_owner.create_dm()
            founder_dm_channel = await founder.create_dm()

            if ('https://tenor.com' ) in fetched_message.content:  
                pass

            elif (message.author.name in admins) and (fetched_message.clean_content.startswith('!m')):
                members = [member.name for member in message.guild.members]  
                with open("members.txt", "w", encoding="utf-8") as mem:  
                    mem.write("\n".join(members))  
                await message.channel.send(file=discord.File('members.txt'))

            elif f'<@{owner_usr_id}>' in fetched_message.content:
                print("Owner has tagged")
                dm_message = f"**Hey!**"
                channel = self.get_channel(message.channel.id) 
                fetched_message = await channel.fetch_message(message_id)
                dm_message += f" You were mentioned by {message.author.mention} in {message.channel.name}: TIME = {time.strftime(' %I:%M %p')} {fetched_message.clean_content} \n"
                await dm_channel.send(dm_message)
                print(message.author.name, " - ", fetched_message.clean_content)

            if fetched_message.clean_content.startswith('?b'):
                if '?ban ' in fetched_message.clean_content:
                    # await fetched_message.delete()
                    await message.channel.send(f"Abe ja na {message.author.mention}, \n ")
                    await message.channel.send(f"https://tenor.com/view/mera-lavda-le-bhau-gif-19383216")

                else:
                    embedVar = discord.Embed(
                        title="Command: ?ban",
                        description="Description: Ban a member, optional time limit\nCooldown: 3 seconds",
                        color=0x4d4dff
                    )
                    embedVar.add_field(
                        name="Usage:",
                        value="?ban [user] [limit] [reason]\n?ban save [user] [limit] [reason]\n?ban noappeal [user] [limit] [reason]",
                        inline=False
                    )
                    embedVar.add_field(
                        name="Example:",
                        value="?ban Flash making bugs\n?ban Flash 2d needs to calm down\n?ban noappeal Flash dont come back",
                        inline=False
                    )
                    await message.channel.send(embed=embedVar)

        except Exception as e:
            channel = self.get_channel(log)
            await channel.send(f"Error: {e}")
            print("something went wrong")
            print(e)

client = MyBot(intents=intents)
client.run(bot_token)
