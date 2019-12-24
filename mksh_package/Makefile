VERSION := R57

SH      := /sbin/sh
EQN     := /usr/freeware/bin/geqn
TBL     := /usr/freeware/bin/tbl
NROFF   := /usr/freeware/bin/groff

PROJECT_ROOT := $(shell pwd)
URL          := https://github.com/MirBSD/mksh/archive/mksh-R57.tar.gz

mksh-$(VERSION).tar.gz:
	curl --remote-name -L $(URL)

mksh/:
	tar xzf mksh-$(VERSION).tar.gz
	mv mksh-mksh-$(VERSION) mksh/

mksh/mksh: mksh/*.c mksh/*.h
	cd mksh && $(SH) ./Build.sh

mksh.z: mksh/mksh.1
	$(EQN) -Tascii $^ | $(TBL) | $(NROFF) -man -Tascii > mksh.cat
	pack -f mksh.cat
	mv mksh.cat.z $@

# Private Target: dist/stree
#
# Create the dist from the spec, idb and build artifacts.
dist/patchXX00001: mksh.z mksh/mksh patchXX00001.idb patchXX00001.spec
	/usr/sbin/gendist -verbose -sbase $(PROJECT_ROOT) -idb patchXX00001.idb -spec patchXX00001.spec -dist $(PROJECT_ROOT)/dist -all
