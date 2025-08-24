from time import sleep

from POM.server_monitoring import server_monitor


def test_monitor_server1(server):
    monitor=server_monitor(server)
    monitor.server_mon1("Mule test server")
    # sleep(10)

def test_monitor_server2(server):
    monitor=server_monitor(server)
    monitor.server_mon2("test Kubenetes")

