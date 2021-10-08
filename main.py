#!/usr/bin/env python3
import dbus
import re
import pulsectl

session_bus = dbus.SessionBus()
pulse = pulsectl.Pulse('spotify-automute')


def main():
	spotify_track_id = get_spotify_track_id()
	if spotify_track_id is None:
		return

	spotify_sinks = get_spotify_sinks()
	is_ad = track_is_ad(spotify_track_id)
	sinks_mute(spotify_sinks, is_ad)


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
	return re.match(r"^spotify:ad:", track_id) != None


def get_spotify_sinks():
	input_sinks = pulse.sink_input_list()
	return filter(lambda sink: sink.proplist.get('application.process.binary'), input_sinks)


def sinks_mute(sinks, mute):
	for sink in sinks:
		pulse.sink_input_mute(sink.index, mute)


main()
