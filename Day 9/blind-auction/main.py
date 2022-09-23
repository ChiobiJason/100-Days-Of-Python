from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

more_bidders = True

bidders = []

highest_bidder = ""

highest_bid = 0

def find_highest_bidder(bidders_list):
  global highest_bid
  global highest_bidder
  for item in bidders_list:
    bid = item['bid']
    bidder = item["name"]
    if bid > highest_bid:
      highest_bid = bid
      highest_bidder =  bidder

while more_bidders:
  name = input("What is your name?: ").capitalize()
  bid = int(input("What is your bid?: $"))

  def bidder(name, bid):
    new_bidder = {
    "name": name,
    "bid": bid
    }

    bidders.append(new_bidder)

  bidder(name=name, bid=bid)

  other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

  if other_bidders == "yes":
    clear()
  else:
    more_bidders = False

if more_bidders == False:
    find_highest_bidder(bidders_list=bidders)
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")