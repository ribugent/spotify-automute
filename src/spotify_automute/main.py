#!/usr/bin/env python3
import dbus
import logging
import re
import time
import pulsectl

logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
session_bus = dbus.SessionBus()
pulse = pulsectl.Pulse('spotify-automute')


def main():
	spotify_track_id = None
	while True:
		spotify_track_id = automute(spotify_track_id)
		time.sleep(1)

def automute(previous_spotify_track_id=None):
	spotify_track_id = get_spotify_track_id()
	if spotify_track_id is None:
		logging.debug("Spotify is not running")
		return None
	elif spotify_track_id == previous_spotify_track_id:
		logging.debug("Spotify is playing the same track")
		return spotify_track_id

	is_ad = track_is_ad(spotify_track_id)
	logging.info("Spotify track id is '%s' and the ad detection result is %s", spotify_track_id, is_ad)

	spotify_sinks = get_spotify_sinks()
	sinks_mute(spotify_sinks, is_ad)

	return spotify_track_id


def get_spotify_track_id():
	try:
		spotify_bus = session_bus.get_object(
		"org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
	except dbus.exceptions.DBusException:
		return None

	spotify_properties = dbus.Interface(
		spotify_bus, "org.freedesktop.DBus.Properties")

	metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	return metadata["mpris:trackid"]


def track_is_ad(track_id):
	return re.match(r"^/com/spotify/ad/", track_id) != None


def get_spotify_sinks():
	input_sinks = pulse.sink_input_list()
	return filter(lambda sink: sink.proplist.get('application.process.binary') == 'spotify', input_sinks)


def sinks_mute(sinks, mute):
	verb = "Muting" if mute else "Unmutting"
	for sink in sinks:
		logging.info("%s sink %i:%s", verb, sink.index, sink.name)
		pulse.sink_input_mute(sink.index, mute)

if __name__ == "__main__":
	main()
