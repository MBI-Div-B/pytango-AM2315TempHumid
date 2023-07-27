from .AM2315TempHumid import AM2315TempHumid


def main():
    import sys
    import tango.server

    args = ["AM2315TempHumid"] + sys.argv[1:]
    tango.server.run((AM2315TempHumid,), args=args)
