### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#ERRORS
#else is missing ':'
#value is not defined anywhere
#if statement needs '==' for boolean to work

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   


#ERRORS
#typo 'dif' should be 'def'
#comma separator missing between card1 and card2
#indentation error for 'if' line, and subsequent code after
#'return card' will not return anything as 'card' is not defined
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  



#ERRORS
#'total' is not defined or defining anything
# total += card.value will not accumulate anything or return
# anything as total is not defined
# total in the return could be refactored into a f sting.
#returning string can't relate to any callable item.
#indentations of 'def' could be an issue if in a class.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

#END
```

