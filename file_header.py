
class Header:
    def __init__(self, header_packet_raw):
        self.time_format = self.get_time_format(header_packet_raw)

    def get_time_format(self,header_packet_raw):
        time_format_raw = header_packet_raw[:8]
        time_format_reanged = time_format_raw[6:8]+time_format_raw[4:6]+time_format_raw[2:4]+time_format_raw[:2]
        if time_format_reanged == 'a1b2c3d4':
            return 'seconds and microseconds'
        return 'seconds and nanoseconds'
