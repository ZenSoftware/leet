# https://leetcode.com/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            split_ip = queryIP.split(".")
            if len(split_ip) != 4:
                return "Neither"
            for segment in split_ip:
                if (
                    not segment.isnumeric()
                    or (len(segment) > 1 and segment[0] == "0")
                    or not (0 <= int(segment) <= 255)
                ):
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            split_ip = queryIP.split(":")
            if len(split_ip) != 8:
                return "Neither"
            for segment in split_ip:
                if not self._is_hex(segment):
                    return "Neither"
            return "IPv6"

        return "Neither"

    def _is_hex(self, s: str) -> bool:
        if not (1 <= len(s) <= 4):
            return False
        for char in s:
            if char not in "0123456789abcdefABCDEF":
                return False
        return True
