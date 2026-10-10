print(f"[station] __name__ is {__name__}")

def announce():
    print(f"[station.announce] __name__ is {__name__}")

if __name__ == "__main__":
    print("[station] Running as main!")
    announce()
