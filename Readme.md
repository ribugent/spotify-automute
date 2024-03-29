# Spotify automute for Linux

Spotify is an amazing service and it worths paying for it, but if you wouldn't pay for it and/or you feel that ads are annoying and does not match your interests, this utility is for you.

## Motivation

For a long time I used [Spotify-AdKiller](https://github.com/SecUpwN/Spotify-AdKiller) and I think that's an amazing project, personally I feel some kind of admiration for projects written in bash.

But, in the last months I experienced some issues, the first was that for some reason it does not works when you use pipewire pulseaudio drop-in replacement, and the second is that the script does not detects ads anymore (or it seems)

My bash skills are not high as the original creator, so I challenged myself to write my replacement in python, of course, the original project has a lot of more amazing features, but my objective is to focus only on muting ads.

## Dependencies

- Linux
- Python 3.6 or higher

## Installation

```sh
pip install git+https://github.com/ribugent/spotify-automute.git
```

## Starting

Run:

```sh
spotify-automute
```

Currently, the process runs in foreground mode, so keeping in a separate terminal on in screen/tmux is recommended.

## FAQ

**Does it work with Spotify flatpak/AppImage/snap versions?**

To be clear, I haven't tried it, but since this script uses dbus it should work.

**Does it work with pipewire pulseaudio drop-in replacement?**

Yes, it does.

**Does this project blocks/skips playing ads?**

No, only mutes spotify, I don't plan to implement that feature.

## TODO

- [x] Write a simple one-shot script
- [x] Create initial Readme
- [x] Make repo public
- [x] Avoid crashes when Spotify is not running
- [x] Add logs
- [x] Turn script as a long-running process
- [ ] Allow start as a service/background process
- [x] Respect last users action if they mute/unmute Spotify manually
- [x] Improve install
- [ ] Use dbus signaling to retrieve track changes
- [ ] Evaluate uploading to pypi

## License

This small project is licensed under the terms of [GPLv3](LICENSE)

**Spotify is a registered trademark by Spotify Technology S.A., and this project is not endorsed, not approbated, and related with them, use at your own risk.**
