print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0
answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    score += 1
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer == "graphics processing unit":
    score += 1
    print('Correct!')
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")

if answer == "random access memory":
    score += 1
    print('Correct!')
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")

if answer == "power supply":
    score += 1
    print('Correct!')
else:
    print("Incorrect!")

print('Your score: ' + str(score))