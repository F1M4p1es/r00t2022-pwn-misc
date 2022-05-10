FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/asia-east1.gce.archive.ubuntu.com/g' /etc/apt/sources.list && apt update && apt-get install -y lib32z1 xinetd && rm -rf /var/lib/apt/lists/ && rm -rf /root/.cache && apt-get autoclean && rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*
#apt update && apt-get install -y lib32z1 xinetd && rm -rf /var/lib/apt/lists/ && rm -rf /root/.cache && apt-get autoclean && rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*

COPY ./pwn.xinetd /etc/xinetd.d/pwn

COPY ./service.sh /service.sh

RUN chmod +x /service.sh

# useradd and put flag
RUN useradd -m pwn4 && useradd -m pwn5 && useradd -m pwn6 && echo 'flag{80162462-c4ce-4b72-85ce-a9c333c4815e}' > /home/pwn4/flag.txt && echo 'flag{af949d19-054a-4346-a4b0-4b7a6eadd3e9}' > /home/pwn5/flag.txt && echo 'flag{c79520dd-2306-4687-81fa-16099e627c2e}' > /home/pwn6/flag.txt

# copy bin
COPY ./bin/pwn4 /home/pwn4/pwn4
COPY ./catflag /home/pwn4/bin/sh
COPY ./bin/pwn5 /home/pwn5/pwn5
COPY ./catflag /home/pwn5/bin/sh
COPY ./bin/pwn6 /home/pwn6/pwn6
COPY ./catflag /home/pwn6/bin/sh


# chown & chmod
RUN chown -R root:pwn4 /home/pwn4 && chmod -R 750 /home/pwn4 && chmod 740 /home/pwn4/flag.txt && chown -R root:pwn5 /home/pwn5 && chmod -R 750 /home/pwn5 && chmod 740 /home/pwn5/flag.txt && chown -R root:pwn6 /home/pwn6 && chmod -R 750 /home/pwn6 && chmod 740 /home/pwn6/flag.txt

# copy lib,/bin 
RUN cp -R /lib* /home/pwn4 && cp -R /usr/lib* /home/pwn4 && mkdir /home/pwn4/dev && mknod /home/pwn4/dev/null c 1 3 && mknod /home/pwn4/dev/zero c 1 5 && mknod /home/pwn4/dev/random c 1 8 && mknod /home/pwn4/dev/urandom c 1 9 && chmod 666 /home/pwn4/dev/* && cp /bin/sh /home/pwn4/bin && cp /bin/ls /home/pwn4/bin && cp /bin/cat /home/pwn4/bin && cp -R /lib* /home/pwn5 && cp -R /usr/lib* /home/pwn5 && mkdir /home/pwn5/dev && mknod /home/pwn5/dev/null c 1 3 && mknod /home/pwn5/dev/zero c 1 5 && mknod /home/pwn5/dev/random c 1 8 && mknod /home/pwn5/dev/urandom c 1 9 && chmod 666 /home/pwn5/dev/* && cp /bin/sh /home/pwn5/bin && cp /bin/ls /home/pwn5/bin && cp /bin/cat /home/pwn5/bin && cp -R /lib* /home/pwn6 && cp -R /usr/lib* /home/pwn6 && mkdir /home/pwn6/dev && mknod /home/pwn6/dev/null c 1 3 && mknod /home/pwn6/dev/zero c 1 5 && mknod /home/pwn6/dev/random c 1 8 && mknod /home/pwn6/dev/urandom c 1 9 && chmod 666 /home/pwn6/dev/* && cp /bin/sh /home/pwn6/bin && cp /bin/ls /home/pwn6/bin && cp /bin/cat /home/pwn6/bin

CMD ["/service.sh"]
