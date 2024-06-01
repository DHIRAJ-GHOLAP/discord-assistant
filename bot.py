import discord,Confidential

intents = discord.Intents.default()
intents.members = True  #

bot_token = Confidential.token
NOTIFICATION_CHANNEL_ID = 1241812772279418920
class MyBot(discord.Client):
  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')

  async def on_message(self, message):
    if message.author == self.user:  # Prevent bot from replying to itself
      return

    bot_owner_mentioned = message.author.mention in message.content

    
    owner_role_mentioned = False
    for role in message.role_mentions:
      if role.name.lower() == "owner":  
        owner_role_mentioned = True
        break

    if bot_owner_mentioned or owner_role_mentioned:
      try:
        
        bot_owner = await self.fetch_user(738739339969822730)

        
        dm_channel = await bot_owner.create_dm()

       
        dm_message = f"**Hey!**"
        notification_channel = self.get_channel(NOTIFICATION_CHANNEL_ID)
        
        if bot_owner_mentioned:
          dm_message += f" You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
        #   notification_message = f"**Hey!** You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
        #   notification_message += f"{message.content}"                   
        #   await notification_channel.send(notification_message)
          

        elif owner_role_mentioned:
            dm_message += f" You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
            
            notification_channel = self.get_channel(NOTIFICATION_CHANNEL_ID)
            # Construct the notification message
            notification_message = f"**Hey!** You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
            notification_message += f"{message.content}"

            # Send the notification message
            await notification_channel.send(notification_message)
          
        #   dm_message += f" You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
        #   notification_message = f"**Hey!** You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
        #   notification_message += f"{message.content}"                   
        #   await notification_channel.send(notification_message)
        #   dm_message += f" The Owner role was mentioned in {message.channel.name} by {message.author.mention}({message.author.name}):\n {message.content}"
        # Send the DM message
        await dm_channel.send(dm_message)
      except discord.HTTPException as e:
        # Handle potential errors (e.g., DMs disabled)
        print(f"Failed to send DM: {e}")

# Run the bot
client = MyBot(intents=intents)
client.run(bot_token)
