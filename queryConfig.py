def deviceInfoQuery(data):
    device_info_query = (
        "INSERT INTO deviceInformation (deviceID, deviceAddress, deviceLocationName) "
        "VALUES (%s, %s, %s) AS new_data "
        "ON DUPLICATE KEY UPDATE deviceID = new_data.deviceID"
    )
    device_info_data = (data['Device ID'], 'Not Available', 'Not Available')
    return device_info_query, device_info_data


def readingStoreQuery(data):
    reading_store_query = (
        "INSERT INTO readingStore "
        "(deviceID, timeStamp, temperature, humidity, battery_level, signal_strength, motion_detected, "
        "light_level, pressure, status, event_count, error_code, data_usage) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) AS new_data "
        "ON DUPLICATE KEY UPDATE "
        "timeStamp = new_data.timeStamp, temperature = new_data.temperature, humidity = new_data.humidity, "
        "battery_level = new_data.battery_level, signal_strength = new_data.signal_strength, "
        "motion_detected = new_data.motion_detected, light_level = new_data.light_level, "
        "pressure = new_data.pressure, status = new_data.status, event_count = new_data.event_count, "
        "error_code = new_data.error_code, data_usage = new_data.data_usage"
    )

    motion_detected = 1 if data['Motion Detected'] == "True" else 0
    error_code = int(data['Error Code'])
    reading_store_data = (
        data['Device ID'], data['Timestamp'], data['Temperature'], data['Humidity'],
        data['Battery Level'], data['Signal Strength'], motion_detected,
        data['Light Level'], data['Pressure'], data['Status'],
        data['Event Count'], error_code, data['Data Usage']
    )

    return reading_store_query, reading_store_data
