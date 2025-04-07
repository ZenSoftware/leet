# https://leetcode.com/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            split_ip = queryIP.split(".")
            if len(split_ip) != 4:
                return "Neither"
            for segment in split_ip:
                if not self._is_ipv4_part(segment):
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            split_ip = queryIP.split(":")
            if len(split_ip) != 8:
                return "Neither"
            for segment in split_ip:
                if not self._is_ipv6_part(segment):
                    return "Neither"
            return "IPv6"

        return "Neither"

    def _is_ipv4_part(self, s: str) -> bool:
        return (
            s.isnumeric() and not (len(s) > 1 and s[0] == "0") and (0 <= int(s) <= 255)
        )

    def _is_ipv6_part(self, s: str) -> bool:
        if not (1 <= len(s) <= 4):
            return False
        for char in s:
            if char not in "0123456789abcdefABCDEF":
                return False
        return True
