def crc_remainder(data: str, generator: str) -> str:
    padded_data = list(data + '0' * (len(generator) - 1))
    generator = list(generator)

    for i in range(len(data)):
        if padded_data[i] == '1':
            for j in range(len(generator)):
                padded_data[i + j] = str(
                    int(padded_data[i + j] != generator[j])
                )

    remainder = ''.join(padded_data[-(len(generator) - 1):])
    return remainder


def verify_crc(frame: str, generator: str) -> str:
    padded_data = list(frame)
    generator = list(generator)

    for i in range(len(frame) - len(generator) + 1):
        if padded_data[i] == '1':
            for j in range(len(generator)):
                padded_data[i + j] = str(
                    int(padded_data[i + j] != generator[j])
                )

    remainder = ''.join(padded_data[-(len(generator) - 1):])
    return remainder


if __name__ == "__main__":
    data = "1101011011"
    generator = "10011"

    remainder = crc_remainder(data, generator)
    transmitted = data + remainder

    print("CRC:", remainder)
    print("Transmitted frame:", transmitted)

    error_frame = list(transmitted)
    error_frame[5] = '1' if error_frame[5] == '0' else '0'
    error_frame = ''.join(error_frame)

    print("Error frame:", error_frame)
    print("Verification remainder:", verify_crc(error_frame, generator))