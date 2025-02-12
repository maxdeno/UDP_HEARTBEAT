import random
import socket
import time

# server address and port
server_addr = ("127.0.0.1", 12000)

# Define the variables
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

seq_number = 1


try:
    while True:
        if random.random() > 0.3:
            # Timestamp for sending the message
            timestamp = time.time()
            message = f"{seq_number}, {timestamp}"

            # sending the heartbeat packet
            client.sendto(message.encode(), server_addr)
            print(f"Sent Heartbeat {seq_number} at {timestamp:.6f}")

        else:
            print(f"Packet {seq_number} lost!")

        seq_number += 1  # increament the seq_number by 1
        time.sleep(1)   # wait 1 sec before sending another heartbeat

except KeyboardInterrupt:
    print("\n Client stooped by the user")

finally:
    client.close()
