FROM ubuntu:22.04

# Don't wait for user input
ENV DEBIAN_FRONTEND=noninteractive
# Use UTC as the timezone
ENV TZ=UTC

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade \
    && apt-get install -y \
        build-essential \
        git `# Only needed for git+https pip commands` \
        ntp \
        libssh-dev \
        libffi-dev \
        libssl-dev \
        zlib1g-dev `# Pillow (compressed png)` \
        wget \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# install python 3.9.5
RUN wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
RUN tar -xvf Python-3.9.5.tgz
RUN cd Python-3.9.5/ && ./configure --enable-optimizations && make && make altinstall

# Make Symbolic link of Python 3.9
RUN ln -sf /usr/local/bin/python3.9 /usr/bin/python

# Use a virtualenv to isolate dependencies.
RUN python -m venv /venv

# activate virtualenv
# RUN source /venv/bin/activate

# Wheel is needed to build wheel packages. You'll get ignorable errors
# without this.
RUN /venv/bin/python3.9 -m pip install --upgrade wheel

RUN mkdir -p /eventmq

ADD . /eventmq

WORKDIR /eventmq

RUN /venv/bin/python3.9 -m pip install -e .

ADD etc/eventmq.conf-dist /etc/eventmq.conf

# Symlink emq commands into PATH so you don't have to know about venv
RUN ln -s /venv/bin/emq-router /usr/bin/emq-router \
    && ln -s /venv/bin/emq-scheduler /usr/bin/emq-scheduler