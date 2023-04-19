# Introduction
This project was part of the [Tsuru-Capital](https://www.tsurucapital.com/en/) [challenge](https://www.tsurucapital.com/en/code-sample.html) (put the link here). <br>

The task of the challenge was to create a programme that will parse and print quote messages from a market data feed - which is coming from the Tokyo Stock Exchange. The programme should also allow for ordering of the messages according to the *quote accepting time* at the exchange. <br>

The main goal of this task for me was to learn the basics about networks and packets, how to handle large sums of data, and write a system that can handle .pcap files.
For that reason I tried to limit the usage of any sort of libraries that are available for Python and try to implement the majority of algorithms on my own. This turned out to be a very interesting self-learning experience and I have gained a lot of valuable knowledge. It has also introduced me to various fields I previously did know exist or had very limited knowledge about. While it was very exciting trying to play with these packets, I have to admit, I am beyond curious what exactly you do after these packets are intercepted and analysed?

# Parsing the Market Data Feed
The communication between the market and the clients is happening via the UDP broadcast to ports 15515/15516. But for the purpouse of this project a PCAP file is supplied, which already includes the UDP packets and hence we do not require to listen to that port constantly and intersect the incoming packets.<br>
We are only interested in the UDP packets that contain the quote information and begin with the ASCII bytes "B6034". We are only interested in the information of the five best bids and asks. Everything else can be ignored.

# What are PCAP files?
In the field of computer network administration, pcap is an application programming interface (API) for capturing network traffic. The PCAP files follow a specific order and can hence be analysed easily if we know the frame.

# The Data
The PCAP file contains captured trafic of UDP packets of the first 30s of trading the KOSPI 200 on 2011-02-16. KOSPI 200 - The Korean Composite Stock Price Index, which consists of 200 big companies of the Stock Market Division. <br>
Each quote packet contains information of bid and ask quotes at the given time from the stock exchange. 

# Structure of the Programme
The architecture idea of the project can be seen in the picture below:

![Architecture](https://user-images.githubusercontent.com/48606569/233208419-d2fe1d48-1834-48d1-a90d-6a2d1de04a34.png)

At the heart of the system is the *Controllet*, which controls the communication across the entire system. It firstly reads the data from the incoming PCAP file. It divided the information into a PCAP Header and the packet information. It then passes the header information to *file_header* and the packet information to the *packet*. *Packet* then analyses the data and breaks it into the *Bid* and *Ask* components, which are handled seperately. Once every component has analysed the necessery data, the *Controller* then arranges results in a desireable output.

# How Can I Run the Code?
The setup for running the code is fairly simple. Avoiding the unnecessary usage of off-the-shelf solutions in a form of various libraries allows for using the programme without any special environments. <br>
Code runs on Python version 3.7.10 and the only libraries that I have used were the sys library, which allows for the arguments to be read from the command line, and the datetime library, which allowed me to time my code as well as to translate UNIX (or Epoch) time to Date Time format that we are used to. <br>
To run the code please navigate to the folder. Once in the folder, run the following command: python3 Controller.py -r where the last argument is optional - it allows for the packets in the .pcap file to be arranged based on the quote accepted time. <br>
