from validate_ip_address import Solution


def test1():
    assert Solution().validIPAddress("172.16.254.1") == "IPv4"


def test2():
    assert Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"


def test3():
    assert Solution().validIPAddress("256.256.256.256") == "Neither"


def test4():
    assert Solution().validIPAddress("2001:0db8:85a3:0000:0:8A2E:0370:733a") == "IPv6"
