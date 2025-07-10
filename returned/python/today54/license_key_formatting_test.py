from license_key_formatting import Solution


def test1():
    assert Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"


def test2():
    assert Solution().licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"
