from bid import Bid
from ask import Ask
import datetime

class Packet:
    def __init__(self, data):
        self.package_time = self.get_package_time(data)
        self.captured_packet_length = self.get_captured_packet_length(data)
        self.original_packet_length = self.get_original_packet_length(data)
        self.packet_data = self.get_packet_data(data)
        self.total_size = 32 + self.captured_packet_length * 2
        self.flag = self.is_valid(self.packet_data)

        if self.flag:
            self.packet_data = self.get_packet_data_cutoff(self.packet_data)
            self.data_type = self.get_data_type(self.packet_data)
            self.info_type = self.get_info_type(self.packet_data)
            self.market_type = self.get_market_type(self.packet_data)
            self.issue_code = self.get_issue_code(self.packet_data)
            self.market_status_type = self.get_market_status_type(self.packet_data)
            self.total_bid_quote_vol = self.get_bid_quote_volume(self.packet_data)
            self.bids = self.get_bids(self.packet_data)
            self.total_ask_quote_vol = self.get_ask_quote_volume(self.packet_data)
            self.asks = self.get_asks(self.packet_data)
            self.num_valid_bids = self.get_num_valid_bids(self.packet_data)
            self.num_valid_asks = self.get_num_valid_asks(self.packet_data)
            self.accept_time = self.get_accept_time(self.packet_data)

    def is_valid(self, packet_data):
        if self.captured_packet_length != self.original_packet_length:
            return False
        elif '4236303334' not in packet_data:
            return False
        else:
            return True

    def get_package_time(self, packet_header):
        seconds = self.translate_big_endian(packet_header[:8])
        nanoseconds = self.translate_big_endian(packet_header[8:16])
        if len(str(nanoseconds)) < 10:
            x = 10 - len(str(nanoseconds))
            ns_str = '0.' + x*'0' + str(nanoseconds)
        else:
            ns_str = str(nanoseconds)

        seconds = float(seconds) + 32400 # the added number adjusts from UTC to Tokyo time
        nanoseconds = float(ns_str)
        time = seconds + nanoseconds
    # convert the time from unix time to the date time one
        date_time = datetime.datetime.fromtimestamp(time)
        return date_time

    def translate_big_endian(self, time_raw):
        chunks, chunk_size = len(time_raw), 2
        time = [time_raw[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        time.reverse()
        time = ''.join(time)
        time_pairs = [(hex,count) for count,hex in enumerate(time[::-1])]
        hex_2_dec_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        epoch = sum([hex_2_dec_dict.get(hex)*(16**count) for (hex,count) in time_pairs])

        # epoch_sec = 0
        return epoch

    # size is in the number of octets -> 2 hex nums == 1 octet
    def get_captured_packet_length(self,data):
        captured_packet_length = self.translate_big_endian(data[16:24])
        return captured_packet_length

    # size is in the number of octets -> 2 hex nums == 1 octet
    def get_original_packet_length(self,data):
        original_packet_length = self.translate_big_endian(data[24:32])
        return original_packet_length

    def get_packet_data(self,data):
        end_point = 32 + self.captured_packet_length * 2
        packet_data = data[32:end_point]
        return packet_data


# ---------------------------------------------------------------------
    def get_data_type(self,packet_data):
        data_type = self.hex_2_ascii(packet_data[:4])
        return data_type

    def get_info_type(self,packet_data):
        info_type = self.hex_2_ascii(packet_data[4:8])
        return info_type

    def get_market_type(self,packet_data):
        market_type = self.hex_2_ascii(packet_data[8:10])
        return market_type

    def get_packet_data_cutoff(self,packet_data):
        return packet_data[packet_data.find('42363033'):]

    def get_accept_time(self, data_packet_raw):
        # print(data_packet_raw)
        # -2 because the last two characters are 'ff' - end of file!
        time = self.hex_2_ascii(data_packet_raw[-18:-2])
        return time


    def get_issue_code(self,data_packet_raw):
        issue_code = self.hex_2_ascii(data_packet_raw[10:34])
        return issue_code

    def get_market_status_type(self,data_packet):
        market_status_type = self.hex_2_ascii(data_packet[40:44])
        return market_status_type

    def get_bid_quote_volume(self,data_packet):
        total_bid_quote_vol = data_packet[44:58]
        return self.hex_2_ascii(total_bid_quote_vol)


    def get_bids(self,data_packet_raw):
        bid_data_raw = data_packet_raw[58:178]
        bids = Bid(bid_data_raw)
        return bids

    def get_ask_quote_volume(self,data_packet):
        total_ask_quote_volume = data_packet[178:192]
        return self.hex_2_ascii(total_ask_quote_volume)

    def get_asks(self,data_packet_raw):
        ask_data_raw = data_packet_raw[192:312]
        asks = Ask(ask_data_raw)
        return asks

    def get_num_valid_bids(self,data_packet):
        num_valid_bids = data_packet[312:322]
        return self.hex_2_ascii(num_valid_bids)

    def get_num_valid_asks(self,data_packet):
        num_valid_asks = data_packet[362:372]
        return self.hex_2_ascii(num_valid_asks)

    def hex_2_ascii(self,hex_string):
        try:
            bytes_object = bytes.fromhex(hex_string)
            ascii_str = bytes_object.decode("ASCII")
            return ascii_str
        except:
            return (hex_string,'no bueno!')










