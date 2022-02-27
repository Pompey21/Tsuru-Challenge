class Ask:
    def __init__(self,ask_info_raw):
        self.first_ask = self.get_first_ask(ask_info_raw)
        self.second_ask = self.get_second_ask(ask_info_raw)
        self.third_ask = self.get_third_ask(ask_info_raw)
        self.fourth_ask = self.get_fourth_ask(ask_info_raw)
        self.fifth_ask = self.get_fifth_ask(ask_info_raw)

    def get_first_ask(self,ask_info_raw):
        ask_price = self.hex_2_ascii(ask_info_raw[:10])
        ask_quantity = self.hex_2_ascii(ask_info_raw[10:24])
        return (ask_price,ask_quantity)

    def get_second_ask(self,ask_info_raw):
        ask_price = self.hex_2_ascii(ask_info_raw[24:34])
        ask_quantity = self.hex_2_ascii(ask_info_raw[34:48])
        return (ask_price,ask_quantity)

    def get_third_ask(self,ask_info_raw):
        ask_price = self.hex_2_ascii(ask_info_raw[48:58])
        ask_quantity = self.hex_2_ascii(ask_info_raw[58:72])
        return (ask_price,ask_quantity)

    def get_fourth_ask(self,ask_info_raw):
        ask_price = self.hex_2_ascii(ask_info_raw[72:82])
        ask_quantity = self.hex_2_ascii(ask_info_raw[82:96])
        return (ask_price,ask_quantity)

    def get_fifth_ask(self,ask_info_raw):
        ask_price = self.hex_2_ascii(ask_info_raw[96:106])
        ask_quantity = self.hex_2_ascii(ask_info_raw[106:120])
        # print('******************')
        # print(bid_info_raw[96:106])
        # print('******************')
        return (ask_price,ask_quantity)

    def hex_2_ascii(self,hex_string):
        try:
            bytes_object = bytes.fromhex(hex_string)
            ascii_str = bytes_object.decode("ASCII")
            return ascii_str
        except:
            return (hex_string,'no bueno!')