emoticon = ("🙁")

def main():
    global emoticon 
    say("Is there anyone?")
    emoticon = "🙂"
    say("Hi, I'm.")
    say("InshaALLAH, Future's CEO")
    say("Yes, I'll be Future's CEO!")

def say(phrase):
    print(phrase + " " + emoticon)

main()