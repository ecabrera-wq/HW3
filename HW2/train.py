import station

print(f"[train] __name__ is {__name__}")

def depart():
    print(f"[train.depart] __name__ is {__name__}")
    station.announce()

if __name__ == "__main__":
    print("[train] Running as main!")
    depart()
