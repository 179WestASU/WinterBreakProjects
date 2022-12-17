import pandas as pd
import fundamentalanalysis as fa
import numpy
import smtplib

api_key = 'd225c7f3f21c31c3f856da93b4c64a2d'

def stockData():
  # Download general stock data
  stock_data = fa.stock_data(ticker, period="ytd", interval="1d")

  # Printing stock data for the current date

  print("History for " + ticker + " downloaded!\n")

  count = 0
  msg = "\nTicker data for " + ticker + ":\n\n"
  for col in stock_data.columns:
    if (col == "close"):
      msg += "Closing price:\n"
    elif (col == "low"):
      msg += "Lowest price:\n"
    elif (col == "open"):
      msg += "Opening price:\n"
    elif (col == "high"):
      msg += "Highest price:\n"
    elif (col == "volume"):
      msg += "Stock volume:\n"
    elif (col == "adjclose"):
      msg += "Adjusted closing price:\n"
    msg += (numpy.around(stock_data.iloc[-1, count], 2).astype('str'))
    msg += "\n"
    count += 1
  return msg


def sendEmail(msg):
  # send to email
  answer = input("\nWould you like to have an email sent to you detailing this stock? (Y/N): ")
  if (answer == "Y" or answer == "y"):
    email = "bchirr@gmail.com"
    password = "bnkewckegjetewfq"
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)
    subject = "Stock Alert for " + email
    message = f'subject: {subject} \n {msg}'
    server.sendmail(email, email, message)
    print('Email has been sent to bchirr@gmail.com.\n')
    server.quit()
  else:
    print()

if __name__ == "__main__":
  massMsg = ""
  while True:
    ticker = input("Enter name of ticker (in all caps) to display data for: ")
    message = stockData()
    massMsg += message
    cont = input("Would you like to enter another ticker? (Y/N): ")
    if (cont == "n" or cont == "N"):
      break
  sendEmail(massMsg)