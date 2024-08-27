import numpy as np

# Function to generate CDMA code
def generate_cdma_code():
    n = int(input("Enter the number of stations: "))
    codes = []
    for i in range(1, n+1):
        code = list(map(int, input(f"Enter the code of station {i}: ").split()))
        print(f"The code of station-{i} C{i} is: {code}")
        codes.append(code)
    return codes

# Function to check if station wants to send data
def check_send_data(station):
    send_data = input(f"Is Station-{station} Wants to Send Anything: ").strip().lower()
    if send_data == 'yes':
        bit_value = int(input("Enter the Bit Value: "))
        return bit_value
    else:
        return None

# Function to send data on common channel
def send_on_common_channel(codes, bit_values):
    common_channel_data = np.zeros(len(codes[0]))
    for code, bit_value in zip(codes, bit_values):
        if bit_value is not None:
            common_channel_data += np.array(code) * bit_value
    return common_channel_data

# Function to decode data from common channel
def decode_data(common_channel_data, receiving_station_code):
    decoded_data = np.dot(common_channel_data, receiving_station_code)
    return decoded_data

# Main function
def main():
    codes = generate_cdma_code()
    bit_values = [check_send_data(i) for i in range(1, len(codes)+1)]
    common_channel_data = send_on_common_channel(codes, bit_values)
    print("Data on Common Channel is:", common_channel_data)
    
    sending_station = int(input("Enter the Sending Station: "))
    receiving_station = int(input("Enter the Receiving Station: "))
    receiving_station_code = codes[receiving_station - 1]
    if bit_values[sending_station - 1] is not None:
        print(f"Station-{sending_station} is sending Bit {bit_values[sending_station - 1]} to Station-{receiving_station}")
        decoded_data = decode_data(common_channel_data, receiving_station_code)
        print(f"Station-{receiving_station} received Bit {decoded_data}")

if __name__ == "__main__":
    main()
