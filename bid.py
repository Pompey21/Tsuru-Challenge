class Bid:
    def __init__(self,bid_info_raw):
        self.first_bid = self.get_first_bid(bid_info_raw)
        self.second_bid = self.get_second_bid(bid_info_raw)
        self.third_bid = self.get_third_bid(bid_info_raw)
        self.fourth_bid = self.get_fourth_bid(bid_info_raw)
        self.fifth_bid = self.get_fifth_bid(bid_info_raw)

    def get_first_bid(self,bid_info_raw):
        bid_price = self.hex_2_ascii(bid_info_raw[:10])
        bid_quantity = self.hex_2_ascii(bid_info_raw[10:24])
        return (bid_price,bid_quantity)

    def get_second_bid(self,bid_info_raw):
        bid_price = self.hex_2_ascii(bid_info_raw[24:34])
        bid_quantity = self.hex_2_ascii(bid_info_raw[34:48])
        return (bid_price,bid_quantity)

    def get_third_bid(self,bid_info_raw):
        bid_price = self.hex_2_ascii(bid_info_raw[48:58])
        bid_quantity = self.hex_2_ascii(bid_info_raw[58:72])
        return (bid_price,bid_quantity)

    def get_fourth_bid(self,bid_info_raw):
        bid_price = self.hex_2_ascii(bid_info_raw[72:82])
        bid_quantity = self.hex_2_ascii(bid_info_raw[82:96])
        return (bid_price,bid_quantity)

    def get_fifth_bid(self,bid_info_raw):
        bid_price = self.hex_2_ascii(bid_info_raw[96:106])
        bid_quantity = self.hex_2_ascii(bid_info_raw[106:120])
        return (bid_price,bid_quantity)

    def hex_2_ascii(self,hex_string):
        try:
            bytes_object = bytes.fromhex(hex_string)
            ascii_str = bytes_object.decode("ASCII")
            return ascii_str
        except:
            return (hex_string,'no bueno!')