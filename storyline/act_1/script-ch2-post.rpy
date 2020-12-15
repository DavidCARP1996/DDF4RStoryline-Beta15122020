label ch2_post:
    $ ch2_post_activities = 0
    $ stamina = 10
    $ hr_hour = 17
    $ park_closed = False
    $ cafe_closed = False
    $ gamestore_closed = False
    $ library_closed = False
    $ ch2_mc_busted = None
    $ ch2_battle_2_won = False
    $ fightingclub_closed = False
    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    pause 3.0
    "..."
    jump ch2_post_loop

label ch2_post_loop:
    while (stamina > 0) and (hr_hour <= 20):
        if not renpy.music.get_playing(channel='music') == audio.t5:
            play music t5 fadeout 1.0
        $ HKBShowButtons()
        show screen freeroam_hud
        with Dissolve(.5)
        if ch2_post_activities == 0:
            $ menutext = "Where should I go first?"
        else:
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                if ch1_battle_2_won == True:
                    mc "I don't want to come back to the park for now..."
                else:
                    mc "I have a bad feeling about going there."
                    mc "I'd better go somewhere else."
                $ park_closed = True
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_gaming_store
                pass
            "Go to the library" if not library_closed:
                mc "Wtf?!"
                mc "The library is closed today because of bugs?"
                mc "Well, I will come there another day..."
                $ library_closed = True
                pass
            "Go to the Mixed Martial Arts Club" if not fightingclub_closed:
                $ ch2_post_activities += 1
                call ch2_post_go_to_fightingclub
                pass
            "Go home":
                jump ch2_post_go_home
                pass

        pass
    jump ch2_post_go_home

    label ch2_post_go_to_fightingclub:
        mc "The Mixed Martial Arts Club..."
        if fightingclub_activities > 1:
            if accept_fightingclub_offer == "Yes":
                "I said I will go. I will not break that promise to Ryoma."
                pass
            elif accept_fightingclub_offer == "Maybe":
                "I guess I can enter in... But I didn't confirmed that."
                menu:
                    mc "Hmm..."
                    "Yes":
                        pass
                    "No":
                        mc "Naaaah, honestly I'm not in mood..."
                        mc "Maybe the next time."
                        $ fightingclub_closed = True
                        jump ch2_post_loop
                        pass
                pass
            elif accept_fightingclub_offer == "No":
                "I told Ryoma that I don't have enough time for his club, but honestly, it was a silly lie to not hurt him."
                "But {i}maybeee{/i} I can change of mind and join in anyways..."
                menu:
                    mc "Hmm..."
                    "Yes":
                        pass
                    "No":
                        mc "Naaaah, honestly I'm not in mood..."
                        mc "Maybe the next time."
                        $ fightingclub_closed = True
                        jump ch2_post_loop
                        pass
                pass
            else:
                "I saw a pamphlet about a Mixed Martial Arts Club founded by Ryoma, which announces a new schedule for activities, post-school to be exact."
                "I wasn't interested before, but now I'm thinking that I need to do some exercises anyway."
                "And yeah, it has something to do with [ch2_winner]..."
                menu:
                    mc "Hmm..."
                    "Yes":
                        pass
                    "No":
                        mc "Naaaah, honestly I'm not in mood..."
                        mc "Maybe the next time."
                        $ fightingclub_closed = True
                        jump ch2_post_loop
                        pass
                pass
        "Alright. Let's go then."
        call fightingclub
        mc "Well, see you tomorrow then."
        "Ryoma & Camilla" "See ya~"

        $ fightingclub_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 5

        return

    label ch2_post_go_to_cafe:
        mc "Hmm..."

        menu:
            "..."

            "Invite Camilla" if backyard_check == True: # Cita con Camilla
                mc "That's right! I must thank her for her will helping me."
                mc "I'm gonna call her so we can meet in the cafe."
                scene bg cafe
                with wipeleft_scene
                show camilla at t11 zorder 1
                c "Hey~! [player]~! It's good to see you!"
                "She hugs me strongly..."
                mc "Me too Camilla."
                "I hug her back."
                c "Look, I saw that portion of chocolate cake and that give me hungry.. a lot to be exactly."
                c "Oh! And I want this banana smoothie too..."
                mc "No problem Camilla, for you, I could buy the entire cafeteria!"
                c "Hmm... Don't worry about the money. I will pay it."
                mc "C-Camilla, it's supposed it was me who invited you. It's my duty paying for anything we eat!"
                c "And what's the problem? I want to contribute with something too."
                "Geez... She wants to be nice to me at all costs."
                "I mean, since when the guest must pay for what the host invited her?"
                c "Ehm... Did you said something?"
                mc "What? Oh... It's nothing, I was rambling around because the Literature Club, that's all..."
                c "Oh! Sorry, I thought I said something bad."
                mc "Hehe... You didn't said anything bad Camilla."
                mc "In fact, I want to thank you again for the mission of searching Sayori."
                c "Hehe~! It was nothing darling, you know I will do anything for you."
                "She grabs my hands."
                c "Anything you ask, I will be there to help you."
                mc "Thanks Camilla... It's very nice from your part."
                mc "And remember that I can help you too if you need help in something."
                c "I know. After all, that's what friends do. Right?"
                "She's giving me a sweet and irresistible smile."
                "I imitate her..."
                mc "Right!"
                scene black
                with dissolve_scene_full
                scene bg cafe
                with dissolve_scene_full
                show camilla at t11 zorder 1
                c "This is awesome! The best chocolate cake and banana smoothie I've tasted ever!"
                mc "Indeed, the food here is delicious. That's why every time I have to get up early, I come here for breakfast."
                c "You know, you must invite to one of your friends from the Literature Club to eat here too."
                mc "Well, I already invited Sayori here many times... But I will take your offer about the others too."
                mc "Thanks Camilla."
                c "Uhuhu~! Don't mention it [player]."
                c "Thanks to you for inviting me to eat this delicious food."
                mc "You're welcome."
                mc "And if you want, we can go to a bar and drink some beers someday. What do you think?"
                c "Good idea!"
                c "Alright, call me if you want to hang with me again."
                mc "I'll do."
                c "Goodbye [player]! Best wishes..."
                mc "Best wishes for you too Camilla. Good bye!"
                pass

            "Go alone": # No invitas a nadie, tacaño '¬.¬
                mc "Ahh, fuck it!"
                scene bg cafe
                with wipeleft_scene
                mc "Hmm..."
                menu:
                    "What should I have for snack?"

                    "Coffee with milk & croissants - $250":
                        mc "..."
                        pause 5.0
                        $ mc_hp = mc_hp_max
                        $ mc_mp = mc_mp_max
                        "Oh man..."
                        "This was delicious!"
                        $ money -= 250
                        pass
                    "Orange juice & ham and cheese toast - $280":
                        mc "..."
                        pause 5.0
                        $ mc_hp = mc_hp_max
                        $ mc_mp = mc_mp_max
                        "Oh man..."
                        "This was delicious!"
                        $ money -= 280
                        pass
                    "Strawberry smoothie & portion of cake - $320":
                        mc "..."
                        pause 5.0
                        $ mc_hp = mc_hp_max
                        $ mc_mp = mc_mp_max
                        "Oh man..."
                        "This was delicious!"
                        $ money -= 320
                        pass
                "Alright, let's pay the bill and let's go somewhere else..."
                pass

        $ cafe_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1

        return

    label ch2_post_go_to_gaming_store:
        mc "I want to see that game I've looking for so long."
        mc "Let's check the gaming store if it's available to buy..."
        scene bg gamingstore
        with wipeleft_scene
        mc "Hmm..."
        "Here it is!"
        "That new 'Car Thief' game for PC it's here. But..."
        mc "That shit costs $3000???"
        mc "Fuck!"
        mc "I don't even know if this can run in my computer..."
        mc "Eh???"
        mc "Wow! Symbol of Blaze: Destiny is finally here!"
        menu:
            mc "..."

            "Buy\n Car Thief 5 ($3000)":
                if money >= 3000:
                    mc "Ok, I hope it's worth..."
                    $ bag_inventory.add_item("mcvideogame", score=1)
                    $ money -= 3000
                    "[player] bought Car Thiefs 5."
                    pass
                else:
                    mc "No! I don't have such money by the way..."
                    pass
            "Buy\n Symbol of Blaze: Destiny ($4000)":
                if money >= 4000:
                    mc "Ok, I hope it's worth..."
                    $ bag_inventory.add_item("yvideogame", score=1)
                    $ money -= 4000
                    "[player] bought Symbol of Blaze: Destiny."
                    pass
                else:
                    mc "No! I don't have such money by the way..."
                    pass
            "Don't buy anything":
                mc "I pass, for now."
                pass
        "Alright, let's go somewhere else..."
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1
        $ gamestore_closed = True

        return

    label ch2_post_go_to_library:
        mc "Let's go to a library."

        if persistent.ytellyouherbookstore == True:
            "Let's go to the bookstore Yuri mentioned."
            scene bg library_old
            with wipeleft_scene
            mc "..."
            "Fuck! No Yuri signals..."
            "Anyway, let's buy a book or let's get out of here."
            pass
        else:
            scene bg library
            with wipeleft_scene
            "Alright, let's choose a book."
            pass

        $ books_bought = 0
        $ exit_library = False
        #while exit_library == False or "(Book) Happy Thoughts", "(Book) Dark in the blossoms", "(Book) How to understand a tsundere", "(Book) Shadows of epiphany" not in keyitems or money < 1000:
        while (money > 1000) and (not exit_library):

            menu:
                "Alright, let's see..."
                "Happy Thoughts \n $1200" if not bag_inventory.has_item("sbook1"):
                    mc "..."
                    mc "Sayori may like this one..."
                    menu:
                        "Buy Happy Thoughts ($1200)?"
                        "Yes":
                            $ money -= 1200
                            $ bag_inventory.add_item("sbook1", score=1)
                            "You bought the book \"Happy Thoughts\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Dark in the blossoms \n $1300" if not bag_inventory.has_item("ybook1"):
                    mc "..."
                    mc "Could Yuri love this?"
                    menu:
                        "Buy Dark in the blossoms ($1300)?"
                        "Yes":
                            $ money -= 1300
                            $ bag_inventory.add_item("ybook1", score=1)
                            "You bought the book \"Dark in the blossoms\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Anime & Stuff \n $1250" if not bag_inventory.has_item("nbook1"):
                    mc "..."
                    mc "Maybe this can help me with Natsuki..."
                    menu:
                        "Anime & Stuff ($1250)?"
                        "Yes":
                            $ money -= 1250
                            $ bag_inventory.add_item("nbook1", score=1)
                            "You bought the book \"Anime & Stuff\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Shadows of epiphany \n $1000" if not bag_inventory.has_item("mbook1"):
                    mc "..."
                    mc "So, this is the book that Monika talked about..."
                    menu:
                        "Buy Shadows of epiphany ($1000)?"
                        "Yes":
                            $ money -= 1000
                            $ bag_inventory.add_item("mbook1", score=1)
                            "You bought the book \"Shadows of epiphany\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Car Thief 5 - The Guide \n $300" if not bag_inventory.has_item("mcbook1"):
                    mc "Oh my God!"
                    mc "The Official guide of Car Thief 5!"
                    menu:
                        "Buy Car Thief 5 - The Guide ($300)?"
                        "Yes":
                            $ money -= 300
                            $ bag_inventory.add_item("mcbook1", score=1)
                            "You bought the book \"Car Thief 5 - The Guide\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Symbol of Blaze: Destiny - The Guide \n $400" if not bag_inventory.has_item("mcbook1"):
                    mc "Oh my God!"
                    mc "The Official guide of Car Thief 5!"
                    menu:
                        "Buy Car Thief 5 - The Guide ($300)?"
                        "Yes":
                            $ money -= 300
                            $ bag_inventory.add_item("mcbook1", score=1)
                            "You bought the book \"Car Thief 5 - The Guide\"."
                            $ books_bought += 1
                        "No":
                            pass
                "Exit" if books_bought >= 1:
                    $ exit_library = True
                    pass

        "I think I'm done. Let's go somewhere else..."
        $ library_closed = True
        scene bg residential_day
        with wipeleft_scene
        $ stamina -= 1

        return

label ch2_post_go_home:
    stop music fadeout 2.0
    hide screen freeroam_hud
    $ HKBShowButtons()
    $ HKBHideButtons()
    with Dissolve(.5)
    pass
    if menutext == "Where should I go next?" or stamina <= 0:
        scene bg house
        with wipeleft_scene
        mc "Finally! Home sweet home..."
        mc "I'm tired, you know?"
        "..."
        mc "Let's write the poem."
    else:
        "..."
        mc "You know what?"
        mc "Let's write the poem."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    mc "Okay? Let's go!"

return
