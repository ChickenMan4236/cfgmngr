install:
	mkdir -p /opt/cfgmngr
	cp src/main.py /opt/cfgmngr/main.py
	cp src/commands.py /opt/cfgmngr/commands.py
	cp src/files.py /opt/cfgmngr/files.py
	cp src/paths.py /opt/cfgmngr/paths.py
	cp src/repo.py /opt/cfgmngr/repo.py
	cp src/shell.py /opt/cfgmngr/shell.py
	cp src/env.py /opt/cfgmngr/env.py
	cp LICENSE.md /opt/cfgmngr/LICENSE.md
	cp src/cfgmngr.sh /usr/bin/cfgmngr
	sudo chmod +x /usr/bin/cfgmngr
	ln -f /usr/bin/cfgmngr /usr/bin/cfgm
