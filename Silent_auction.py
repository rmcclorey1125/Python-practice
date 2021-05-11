# from replit import clear
from auction_art import logo

print(logo)

bids = {}
another_bidder = True
higgest_bid = 0
higgest_bidder = ""

while another_bidder:

  name = input("Please enter your name: ")
  bid = int(input("Please enter your bid: $"))

  bids[name] = bid

  new_bidder = input("Is there another bidder? please enter: Yes or No")

  if new_bidder == "No":
    another_bidder = False
#   elif new_bidder == "Yes":
#     clear()

for bid in bids:
  if bids[bid] > higgest_bid:
    higgest_bid = bids[bid]
    higgest_bidder = bid

print(f"The highest bidder was {higgest_bidder} with a bid of {higgest_bid}")