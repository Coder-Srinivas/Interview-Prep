from logger import Logger

logger = Logger()

while True:

    print("1. Log info")
    print("2. Log debug info")
    print("3. Log error")
    print("4. Log History")

    try:
        inp = int(input("Make a choice "))
    except TypeError as error:
        print(error)
    
    if inp == 4:
        logger.log_history()
        continue
    message = input("Enter your message ")
    logger.log(message, inp)