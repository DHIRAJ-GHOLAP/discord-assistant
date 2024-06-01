import discord,Confidential

intents = discord.Intents.default()
intents.members = True  # Required to access member information

# Replace with your actual bot token (obtain from Discord Developer Portal)
bot_token = Confidential.token
NOTIFICATION_CHANNEL_ID = 1241812772279418920
class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if message.author == self.user:  # Prevent bot from replying to itself
            return

        # Check if you (bot owner) are directly mentioned
        bot_owner_mentioned = message.author.mention in message.content

        if bot_owner_mentioned:
            try:
                # Replace with the ID of the channel where you want notifications
                notification_channel = self.get_channel(NOTIFICATION_CHANNEL_ID)

                if notification_channel:
                    # Construct the notification message
                    notification_message = f"**Hey!** You were mentioned by {message.author.mention}({message.author.name}) in {message.channel.name}:\n"
                    notification_message += f"{message.content}"

                    # Send the notification message
                    await notification_channel.send(notification_message)
                else:
                    print(f"Notification channel not found: {NOTIFICATION_CHANNEL_ID}")
            except discord.HTTPException as e:
                # Handle potential errors (e.g., DMs disabled)
                print(f"Failed to send notification: {e}")

# Run the bot
client = MyBot(intents=intents)
client.run(bot_token)