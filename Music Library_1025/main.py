from ai import call_gpt

def main():
    while True:
        answer = input("\nWelcome to Music Library! Ready to discover your next favourite melody? \nPress 0 to embark this music journey 🎼~ ")
        if answer == str(0):
            question()
            end()
            break
        else:
            print("Looking forward to see you next time!")
            break
    

def question():
    #Identify users' purpose of listening songs
    while True:
        song_purpose = input("\nWhat is the purpose of listening this song?(e.g. For studying, relaxing, crying, impressing someone?)\n")
        if song_purpose == "":
            print("Please enter a valid purpose.")
        else:
            print("\nWonderful!\n")
            break

    #Identify users preference on song's genre
    while True:
        song_genre = input("\nWhich genre would you like to choose?(e.g. Pop, rock, hip hop, classical)\n")
        if song_genre == "":
            print("Please enter a valid song genre.")
        else:
            print("\nGreat choice!\n")
            break

    #Identify users' preference on song's tempo
    while True:
        song_tempo = input("Do you enjoy fast, moderate, or slow songs?\n")
        if song_tempo == "fast":
            adjective = "vibrant"
            break
        elif song_tempo == "moderate":
            adjective = "pleasant"
            break
        elif song_tempo == "slow":
            adjective = "calming"
            break
        else:
            print("\nPlease type fast, moderate, or slow.")

    #Choose a mood for the targeted song
    while True:
        song_mood = input ("\nWhich adjective(s) best captures the vibe of the song you usually like?\n")
        if song_mood == "":
            print("Please enter a valid adjective for the song.\n")
        else:
            print("\nAwesome!\n")
            break

    #Choose a language for the targeted song
    while True:
        song_language = input ("Which language do you want this song to be in?\n")
        if song_language == "":
            print("Please enter a valid language for the song.")
        else:
            print("\nAmazing!\n")
            break
    
    #Choose a language for the targeted song
    while True:
        song_era = input ("Do you want a song that is newly released?\n")
        if song_era == "yes":
            era = "The song needs to be realeased within 5 years."
            break 
        elif song_era == "":
            print("Please enter a valid answer.")
        else:
            print("\nAmazing!")
            break

    #Customize special requests for the songs
    while True:
        special_request = input ("\nDo you have any further special requests for this song?\n")
        if special_request == "":
            print("Please enter a special request for the song.")
        else:
            print("\nMarvelous!\n")
            break

    print(f"Playing a {adjective} {song_genre} song 🎶🎵🎶~ ")
    print()

    #Recommendation
    print("Let me choose a song for you in our library...\n")
    chosen_song = call_gpt(f"You are a musician. Recommend one song that matches these inputs: tempo = {song_tempo}, genre = {song_genre}, mood = {song_mood}, language = {song_language}, purpose = {song_purpose}, era = {era}, special_request = {special_request}. Requirements: the song must have at least 100,000 views on YouTube and must be actually sung by the named singer. Verify the singer-song match before answering.")
    print(chosen_song)
    print()


    #About fun fact
    while True:
        answer = input("Do you want to know any fun facts about the chosen song?\n")
        if answer == "yes":
            fun_fact = call_gpt(f"Tell me a fun fact about {chosen_song}.")
            print(fun_fact)
            break
        elif answer == "no":
            break
        else:
            print("\nPlease type yes or no.")

def end():
    while True:
        decision = input("\nWould you like to search for another song?\n")
        if decision == "yes":
            question()
        elif decision == "no":
            print("\nThank you for this amazing music discovery! Looking forward to seeing you next time!")
            break
        else:
            print("\nPlease type yes or no.")




if __name__ == "__main__":
    main()