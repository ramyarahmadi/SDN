# Network Performance Testing (iPerf)

'''
def test_iperf(net):
    
    h1, h3=net.getNodeByName('h1', 'h3')
    h3.popen('iperf -s -p 5001 -w 16m > iperf_server_%s ' %(h3.name), shell=True)   
    h1.popen('iperf -c %s -t 10 -i 1 -y -Z cong > tcp_thr_%s' %(h3.IP(), h1.name), shell=True)
'''

The script utilizes iperf to measure TCP throughput and network performance between nodes:

    Server Setup (h3): An iperf server instance is initialized on h3 listening on port 5001. A large TCP window size (-w 16m) is configured to optimize throughput, with logs saved to iperf_server_h3.
    Client Execution (h1): The h1 host acts as the client, initiating a 10-second traffic stream (-t 10) toward the server’s IP address.
    Testing Parameters:
    Reporting: Performance metrics are reported at 1-second intervals (-i 1).
    Output Format: Data is exported in CSV format (-y) and stored in the file tcp_thr_h1 for post-test analysis.
    Congestion Control: The -Z cong flag is used to apply a specific TCP congestion control algorithm to the data stream.


