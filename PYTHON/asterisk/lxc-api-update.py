#!/usr/bin/python
import lxc
import sys

for container in lxc.list_containers(as_object=True):
    # Старт контейнера (если он не запущен)
    started=False
    if not container.running:
        if not container.start():
            continue
        started=True

    if not container.state == "RUNNING":
        continue

    # ждать соединения с контейнером
    if not container.get_ips(timeout=30):
        continue

    # выполнить команду обновления
    container.attach_wait(lxc.attach_run_command,
                          ["apt-get", "update"])
#    container.attach_wait(lxc.attach_run_command,
                          ["apt-get", "dist-upgrade", "-y"])
    container.attach_wait(lxc.attach_run_command,
                          ["apt-get", "upgrade", "-y"])

    # завершить работу контейнера
    if started:
        if not container.shutdown(30):
            container.stop()
