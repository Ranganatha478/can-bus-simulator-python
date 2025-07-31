import can
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Initialize CAN bus (virtual interface for simulation)
bus = can.interface.Bus(bustype='virtual', channel='vcan0', bitrate=500000)

# Function to send CAN messages
def send_can_messages():
    messages = [
        can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33, 0x44], is_extended_id=False),
        can.Message(arbitration_id=0x124, data=[0x55, 0x66, 0x77, 0x88], is_extended_id=False),
        can.Message(arbitration_id=0x125, data=[0x99, 0xaa, 0xbb, 0xcc], is_extended_id=False),
    ]

    for msg in messages:
        bus.send(msg)
        print(f"Sent: {msg}")
        time.sleep(1)

# Function to receive CAN messages and log to CSV
def log_can_messages(duration=10):
    start_time = time.time()
    records = []
    while time.time() - start_time < duration:
        message = bus.recv(timeout=1)
        if message:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            record = {
                'timestamp': timestamp,
                'arbitration_id': hex(message.arbitration_id),
                'data': message.data.hex()
            }
            records.append(record)
            print(f"Received: {record}")
    # Save records to CSV
    df = pd.DataFrame(records)
    df.to_csv('can_log.csv', index=False)
    return df

# Simulate sending and logging messages
if __name__ == "__main__":
    print("Starting CAN message transmission...")
    send_can_messages()
    print("Logging incoming CAN messages...")
    df = log_can_messages(15)  # record for 15 seconds

    # Simple analysis: count messages per arbitration ID
    count_series = df['arbitration_id'].value_counts()
    print("Message count per Arbitration ID:")
    print(count_series)

    # Plot distribution
    count_series.plot(kind='bar', title='CAN Message Count per ID')
    plt.xlabel('Arbitration ID')
    plt.ylabel('Message Count')
    plt.show()
