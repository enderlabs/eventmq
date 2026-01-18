"""
derp subscriber
"""
import zmq


if __name__ == "__main__":
    sockets = []
    for i in range(100):
        ctx = zmq.Context()
        s = ctx.socket(zmq.SUB)
        s.linger = 0
        s.setsockopt(zmq.SUBSCRIBE, str(i).encode('utf-8'))
        s.connect('tcp://127.0.0.1:47299')
        sockets.append(s)

    while True:
        # block until something comes in. normally you'd do something with
        # this in another thread or something
        for s in sockets:
            print(s.recv_multipart())  # noqa
