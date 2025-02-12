import socket
import time


server_adrr = ('0.0.0.0', 12000)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_adrr)
print(f"connection running and waiting for connections on {server_adrr}...")


last_seq = 0  # Track the last received packet
last_received_time = time.time()  # last packet arriving time
time_threshold = 3  # if no packet is received within 3 seconds assume client stopped


try:
    while True:
        # Detecting client failure
        server_socket.settimeout(time_threshold)

        try:
            # Receive data
            data, client_addr = server_socket.recvfrom(1024)
            received_time = time.time()
            seq_no, timestamp = data.decode().split(",")
            seq_no = int(seq_no)
            timestamp = float(timestamp)

            # calculate delay
            delay = received_time - timestamp

            # check lost packets
            if last_seq and seq_no > last_seq + 1:
                lost_packets = seq_no - last_seq - 1
                print(f"Lost packet(s): {lost_packets}")

            print(f"Received heartbeat {seq_no} from {
                  client_addr} | Delay: {delay:.6f}sec")

            # update the tracking variable
            last_seq = seq_no
            last_received_time = received_time

        except socket.timeout:
            print(f"No heartbeat received for 3 seconds. Client maybe down")


except KeyboardInterrupt:
    print("\n Server closed by user")

finally:
    server_socket.close()
