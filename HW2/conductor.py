import train

print(f"[conductor] __name__ is {__name__}")

if __name__ == "__main__":
    print("[conductor] Running as main!")
    train.depart()
