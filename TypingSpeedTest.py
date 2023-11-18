import time

#2.1. Define the text that the user will need to type.

words = "The quick brown fox jumps over the lazy dog. "

#2.2. Print instructions to the user.

print("Type the following text as fast as you can:\n", words * 3)

#2.3. Wait for the user to press enter before starting the timer.

input("Press enter to start the test. The quick brown fox jumps over the lazy dog")

#2.4. Start and Stop the timer.

startTimer = time.time()

type = str(input()) #2.5. Get user input
type = type.strip() #2.5 remove trailing and preceding white spaces

stopTimer = time.time()

#2.6. Calculate the time it took the user to type the text.

timeElapsed = stopTimer - startTimer

#2.7. Calculate the user's typing speed in words per minute.

wordcount = len(type.split())
wpm = wordcount/ (timeElapsed /60) #60 seconds in a minute, divider by 60 to get time 
                                    #in minutes

#2.8. Calculate the accuracy of the user's typing.

accuracy = set(words.split()) and len(type.split())
finalAccuracy = wordcount/accuracy

#2.9. Print the user's typing speed and accuracy.

timeTaken = round(timeElapsed, 2)
wpm = int(wpm)

print("Time taken: ", timeTaken, " seconds\nNumber of words typed: ", wordcount, \
      "\nTyping speed: ", wpm, "wpm")
if accuracy < 100:
    print("There was an error while typing")