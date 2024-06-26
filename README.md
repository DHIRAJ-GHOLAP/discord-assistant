# Discord Mention Assistant (DM Assistant)

This Python bot streamlines workflow for server owners and admins by efficiently handling mentions.

## Features

### DM Notifications
Receive instant Direct Messages (DMs) whenever someone mentions you (the server owner/admin), even if you're unavailable. These DMs include:

- **Author Information**: Name and ID of the member who mentioned you.
- **Channel Context**: Name and ID of the channel where the mention occurred.
- **Message Content**: The complete message containing the mention, providing full context.

### Optional Forwarded Notifications (Configurable)
The bot can optionally send a formatted notification message to a designated server channel, keeping other admins or moderators informed about your mentions. This message includes the same details as the DM.

## Benefits

- **Improved Availability**: Stay informed about mentions even when not actively monitoring the server.
- **Enhanced Context**: Gain valuable insights into mentions with channel and message details.
- **Streamlined Workflow**: Reduce the need for manual checking for mentions, freeing up time for other tasks.
- **Increased Visibility (Optional)**: Optionally share mentions with other admins or moderators for broader awareness.

## Installation

### Obtain Discord Bot Token
Create a Discord bot application in the [Discord Developer Portal](https://discord.com/developers/docs) and generate a bot token. Never share your bot token publicly. Store it securely!

### Install Dependencies
Use the following command to install the required `discord.py` library:
```bash
pip install discord.py
```

### Configure Script
1. Replace `BOT_OWNER_ID` in the `MyBot` class with your actual user ID.
2. Replace `NOTIFICATION_CHANNEL_ID` in the `MyBot` class with the ID of the desired channel for forwarded notifications (optional).

### Run the Bot
Execute the Python script using:
```bash
python bot.py
```

## Additional Notes

- Consider including a LICENSE file to specify the license under which you distribute your code.
- Explore adding further customization options using configuration files or environment variables.

## Get Started Today!

This Discord Mention Assistant empowers you to manage mentions effectively, enhancing your server administration experience. Clone this repository, follow the setup instructions, and gain a valuable assistant for your Discord server.

---

### Example Bot Code

Here's an example of what the bot code might look like:


### License

Include a `LICENSE` file to specify the license under which you distribute your code. 

---

Enhance your Discord server management with this Mention Assistant. Set it up now and enjoy a streamlined workflow and improved availability!

### u can use this bot for ur personal use but after liking the repo and forking it other wise not
