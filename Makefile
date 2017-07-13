SERVICE_DIR = $(DESTDIR)/usr/lib/obs/service/

install:
	[ -d $(SERVICE_DIR) ] || mkdir -p $(SERVICE_DIR)
	cp container_checks $(SERVICE_DIR)
	cp container_checks.service $(SERVICE_DIR)
