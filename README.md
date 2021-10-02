# Project Setup

Follow the steps below to set up the project on your environment.

## Mac Setup

Homebrew requires the Xcode command-line tools from Apple's Xcode. Install the Xcode command-line tools by running the 
following command in your macOS Terminal:
```
xcode-select --install
```

Install brew using the official [Homebrew installation instructions](https://brew.sh/#install).

Install MongoDB by running the following commands in your macOS Terminal:
```
brew tap mongodb/brew
brew install mongodb-community@5.0
```

Use the following commands to run and stop MongoDB (i.e. the mongod process) as a macOS service:
```
brew services start mongodb-community@5.0
brew services stop mongodb-community@5.0
```

Create the initial structure in MongoDB:
- Database: `discord-db`
- Collection: `users`

## Local Development

Create a virtual environment with Python 3.7 or higher.

Install required packages:
```
pip3 install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the projects root directory with the following variables set:
```
DISCORD_TOKEN=ODg0MTU1MDg1NDUyNjExNjQ2.YTUXlw.LrDNHvwYo3VeHdpgRzN0Jq8DzXg
```

## Community

Join the community to stay updated on the most recent developments.

- [thenewboston.com](https://thenewboston.com/)
- [Discord](https://discord.gg/thenewboston)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Instagram](https://www.instagram.com/thenewboston_official/)
- [LinkedIn](https://www.linkedin.com/company/thenewboston-developers/)
- [Reddit](https://www.reddit.com/r/thenewboston/)
- [Twitch](https://www.twitch.tv/thenewboston/videos)
- [Twitter](https://twitter.com/thenewboston_og)
- [YouTube](https://www.youtube.com/user/thenewboston)
