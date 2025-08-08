# FallenRobot

## Project Overview
FallenRobot is a powerful, multi-purpose Telegram group management bot written in Python. It offers rich management, entertainment, and utility features for automated group administration and interaction.

- [中文说明 (Chinese)](README.zh.md)

## Main Features
- Group management (ban, mute, blacklist, warn, etc.)
- Entertainment (truth or dare, memes, couple pairing, etc.)
- Utilities (translation, Wikipedia, Google search, currency conversion, etc.)
- Multi-level user permissions
- Modular plugin system

## Quick Start
### Install Dependencies
```bash
pip install -r requirements.txt
# For development
pip install -r requirements-dev.txt
```

### Configuration
1. Copy `.env.example` to `.env` and fill in your values:
```
API_ID=xxxx
API_HASH=xxxx
TOKEN=xxxx
OWNER_ID=xxxx
DATABASE_URL=xxxx
...
```
2. Or set environment variables directly.

### Run
```bash
python -m FallenRobot
```

## Usage Examples
- Add the bot to your group and send `/help` to see all commands
- Admins can use `/ban`, `/mute`, `/warn`, etc. to manage members
- Regular users can use `/truth`, `/dare`, `/meme`, `/translate`, and other fun/utility commands

## FAQ
**Q: How do I get API_ID and API_HASH?**  
A: Register an app at [my.telegram.org](https://my.telegram.org/apps).

**Q: Invalid TOKEN error on startup?**  
A: Make sure your `.env` file contains the correct Bot Token from @BotFather.

**Q: How to add custom modules?**  
A: Add a new Python file in `FallenRobot/modules/` and follow the structure of existing modules.

## Contributing
1. Fork this repo and create a new branch
2. Follow PEP8 style, use `black` and `flake8` for checks
3. Add type hints and docstrings where appropriate
4. Ensure all tests pass with pytest before submitting a PR
5. Contributions for docs, bugfixes, and new features are welcome!

## Security Advice
- Never share your `.env` file or Bot Token
- Enable 2FA for your bot account
- Regularly update dependencies to patch vulnerabilities
- Only add trusted users as admins

## Community & Support
- Telegram Support Group: [Join here](https://t.me/DevilsHeavenMF)
- Open issues or PRs to contribute

## Multilingual
- [中文说明 (Chinese)](README.zh.md)

---
For more questions, open an issue or join the support group.