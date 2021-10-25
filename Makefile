PREFIX?=/usr/local

install:
	@echo "Installing to ${PREFIX}"
	mkdir -p ${PREFIX}/bin
	install -m 755 main.py ${PREFIX}/bin/spotify-automute

uninstall:
	@echo "Uninstalling from ${PREFIX}"
	rm -f ${PREFIX}/bin/spotify-automute
