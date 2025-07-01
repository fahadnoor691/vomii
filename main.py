from vomi import Vomi

def main():
    try:
        vomi = Vomi()
        vomi.start()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
