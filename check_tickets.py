from google_mail_api import GoogleMailAPI
from selenium import webdriver
from time import sleep, time
from argparse import ArgumentParser


def check_tickets(args):

    # init gmail helper
    gmail = GoogleMailAPI()

    # init headless chrome driver
    op = webdriver.ChromeOptions()
    op.add_argument("headless")
    driver = webdriver.Chrome(options=op)

    while True:

        # load the web page in full and retrieve html
        driver.get(args.url)
        sleep(10)
        html = driver.page_source

        # check if strings occur in the html
        if any(s in html for s in args.strings):

            # send alert
            print("Tickets are out!")
            gmail.send_email(
                ", ".join(args.recipients),
                f"{args.url} has been updated!",
                f"Buy your tickets now at {args.url}",
            )

            break

        else:
            print(f"Tickets are not out as of {time()}")

        sleep(args.refresh - 10)


if __name__ == "__main__":

    parser = ArgumentParser(description="Ticket Checker")
    parser.add_argument("-u", dest="url", type=str, required=True)
    parser.add_argument("-s", dest="strings", nargs="+", type=str, required=True)
    parser.add_argument("-r", dest="recipients", nargs="+", type=str, required=True)
    parser.add_argument("-t", dest="refresh", type=int, default=60)

    check_tickets(parser.parse_args())

