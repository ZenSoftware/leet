# https://leetcode.com/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        neither = "Neither"

        if "." in queryIP:
            split_ip = queryIP.split(".")
            if len(split_ip) != 4:
                return neither
            for segment in split_ip:
                if not segment.isnumeric():
                    return neither
                if len(segment) > 1 and segment[0] == "0":
                    return neither
                if not (0 <= int(segment) <= 255):
                    return neither
            return "IPv4"
        elif ":" in queryIP:
            split_ip = queryIP.split(":")
            if len(split_ip) != 8:
                return neither
            for segment in split_ip:
                if not self._is_hex(segment):
                    return neither
            return "IPv6"

        return neither

    def _is_hex(self, s: str) -> bool:
        if not (1 <= len(s) <= 4):
            return False
        for char in s:
            if char not in "0123456789abcdefABCDEF":
                return False
        return True
