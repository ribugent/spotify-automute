# Spotify automute for Linux

Spotify is an amazing service and it worths paying for it, but if you wouldn't pay for it and/or you feel that ads are annoying and does not match your interests, this utility is for you.

## Motivation

For a long time I used [Spotify-AdKiller](https://github.com/SecUpwN/Spotify-AdKiller) and I think that's an amazing project, personally I feel some kind of admiration for projects written in bash.

But, in the last months I experienced some issues, the first was that for some reason it does not works when you use pipewire pulseaudio drop-in replacement, and the second is that the script does not detects ads anymore (or it seems)

My bash skills are not high as the original creator, so I challenged myself to write my replacement in python, of course, the original project has a lot of more amazing features, but my objective is to focus only on muting ads.

## (Dev) Dependencies

- Linux
- Python 3
- Python virtualenv

## Installation

Clone the repo

```sh
git clone git@github.com:ribugent/spotify-automute.git
```

Create virtualenv and install python modules

```sh
cd spotify-automute
virtualenv local
source local/bin/activate
pip install -r requirements.txt
```

## Starting

```sh
cd spotify-automute
source local/bin/activate
watch ./main.py
```

There's a lot to do, but at this time this is the only way to run it. If you have experience using screen or tmux, you can execute this process on it.

## TODO

- [x] Write a simple one-shot script
- [x] Create initial Readme
- [x] Make repo public
- [ ] Add logs
- [ ] Avoid crashes when Spotify is not running
- [ ] Turn script as a long-running process
- [ ] Allow start as a service/background process
- [ ] Respect last users action if they mute/unmute Spotify manually
- [ ] Improve install
- [ ] Use dbus signaling to retrieve track changes

## License

This small project is licensed under the terms of [GPLv3](LICENSE)

**Spotify is a registered trademark by Spotify Technology S.A., and this project is not endorsed, not approbated, and related with them, use at your own risk.**
