
## Homies Discord Bot

Homies Discord Bot is a custom-built bot designed to manage various tasks and activities in the "Homies" Discord server. The bot includes features like member management, message handling, commands execution, and automated notifications.

### Features

- **Automated Member Management**: Fetch and manage member data.
- **Message Handling**: Responds to specific commands and messages.
- **Fun Commands**: Includes commands for banning members, sending notifications, and more.
- **Custom Notifications**: Sends notifications to server owner and admins based on specific triggers.
- **Error Logging**: Automatically logs errors to a specified log channel.
  
### Prerequisites

- Python 3.8+
- `discord.py` library

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/homies-discord-bot.git
    cd homies-discord-bot
    ```

2. **Install the required Python libraries**:
    ```bash
    pip install discord.py
    ```

3. **Create the `config.json` file**: Copy the content below and replace the placeholders with your actual data.

    ```json
    {
        "BOT_TOKEN": "YOUR_BOT_TOKEN_HERE",
        "OWNER_USER_ID": 738739339969822730, 
        "FOUNDER_ID": 1141700782027194470,
        "GC_CHANNEL_ID": 1227470902388719666,
        "ADMINS": ["thedevil1624", "flash.homies"],
        "COMPLIMENTS": [
            "You're an awesome friend.",
            "You're a gift to those around you.",
            "You're a smart cookie.",
            "You are awesome!",
            // More compliments...
        ],
        "logchannel" : 0000000
    }
    ```

4. **Run the bot**:
    ```bash
    python bot.py
    ```

### Configuration

Update the `config.json` file with your bot's configuration:

- `BOT_TOKEN`: Your Discord bot token.
- `OWNER_USER_ID`: The user ID of the bot owner.
- `FOUNDER_ID`: The user ID of the server founder.
- `GC_CHANNEL_ID`: The ID of the general chat channel.
- `ADMINS`: List of usernames of the server admins.
- `COMPLIMENTS`: List of compliments that the bot can use.
- `logchannel`: The ID of the log channel where errors and logs are sent.

### Usage

- The bot listens for specific commands prefixed with `!` or `?`.
- Admin commands include banning members and notifying the server owner.
- Logs errors and messages in the specified log channel.

### Commands

- `!m`: Save a list of members to a text file and send it to the channel.
- `?b`, `?ban`: Ban a member with optional parameters.
- Auto-responses and mentions are configured for specific user actions and messages.

### Error Handling

If an error occurs, the bot sends a detailed message to the log channel specified in `config.json`.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request with any features or bug fixes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Support

If you have any questions or need support, feel free to join our [Discord server](https://discord.gg/invites/homies-here).
