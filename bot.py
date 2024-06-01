import discord,Confidential,time

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
            message_id = message.id
            
              # Do something with the message ID (e.g., print it)
            print(f"Message ID: {message_id}")
            
            channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
            filterd_message  = await channel.fetch_message(message_id)
            fetched_message = filterd_message.clean_content()
            print(f"Fetched message content: {fetched_message.content}")
            dm_message += f" You were mentioned by {message.author.mention}({message.author.name})\n {message.channel.name}:\n {fetched_message.content}"
        #   

        elif owner_role_mentioned:
            message_id = message.id
            
              # Do something with the message ID (e.g., print it)
            print(f"Message ID: {message_id}")
            
            channel = self.get_channel(message.channel.id)  # Assuming you have the channel ID
            fetched_message = await channel.fetch_message(message_id)
            print(f"Fetched message content: {fetched_message.content}")
            dm_message += f" You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}: {fetched_message.content}\n"
            
            t = time.localtime()
            notification_channel = self.get_channel(NOTIFICATION_CHANNEL_ID)
            # Construct the notification message
            notification_message = f"**Hey!** You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name} on {time.strftime('%H %M %S || %p')}:\n"
            notification_message += f"{fetched_message.content}"
                    # Access other message attributes like author, embeds, attachments, etc.
                
            # Send the notification message
            await notification_channel.send(notification_message)
          
        
        await dm_channel.send(dm_message)
      except discord.HTTPException as e:
        # Handle potential errors (e.g., DMs disabled)
        print(f"Failed to send DM: {e}")

# Run the bot
client = MyBot(intents=intents)
client.run(bot_token)
