label ch3_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    $ ch3_winner = poemwinner[2].capitalize()
    $ sayori_wait3 = False

    scene bg bedroom
    with dissolve_scene_full
    mc "Aaaand it's done!"
    "12:07 PM"
    mc "Umm... Today I don't want to do anything fun."
    mc "I'd better go to sleep."
    pause 0.5
    play sound click
    scene bg bedroom_night
    pause 0.5
    scene black
    with dissolve_scene_full
    pause 3.0
    scene bg bedroom
    with wipeleft_scene
    pause 1.0

    mc "..."
    "8:02 AM"
    mc "It's a good time for go to school."
    mc "However, I don't know if I should check for Sayori now or later..."
    menu:
        mc "What do you say?"

        "Go now.":
            mc "I guess you're right."
            mc "Otherwise we could be late."
            jump ch3_prev_go_school_A
            pass
        "Go later.":
            mc "Okay then..."
            mc "I will pick up her at 8:25 AM."
            jump ch3_prev_go_school_A
            pass
        "Why do you need to go always with her?":
            mc "There's something wrong with that?"
            mc "No!{w} So shut up!"
            "... ... ..."
            jump ch3_prev_go_school_B
            pass

label ch3_prev_go_school_A:
    play music t2
    scene bg house
    with wipeleft_scene
    "I can't believe this..."
    "Sayori once again has her phone out of battery!"
    mc "Sayoriii!!!"
    "..."
    mc "SAAAYOOOORIIIII----!!!"
    "..."
    "What's wrong with her?"
    "I could enter to her house in case she's still sleeping but..."
    menu:
        "Do it.":
            mc "Alright then, let's go!"
            scene bg sayori_bedroom
            with wipeleft_scene
            stop music fadeout 3.0
            mc "What the..."
            mc "She's not here?!"
            mc "Did she really went to the school without me?"
            mc "Or..."
            "..."
            mc "Ah, fuck this shit, let's go to the school then. Maybe she's waiting for me..."
            pass
        "Don't do that.":
            mc "Naaah!"
            mc "She may went sooner and she didn't advised me..."
            mc "Let's fucking go."
            pass
    $ sayori_wait3 = True
    jump ch3_prev_go_school_B
    return

label ch3_prev_go_school_B:
    if not renpy.music.get_playing(channel='music') == audio.t2:
        play music t2 fadeout 1.0
    scene bg school_entrance
    with wipeleft_scene
    #$ HKBShowButtons()
    "8:55 AM"
    "It's almost time to enter school..."
    "I'm worried about Sayori."
    show ryoma frontal uniform l1 r1 e1a b1a ma at t11 zorder 1
    mcf1 "Hey, [player]!"
    mc "Ryoma! What's up dude?"
    mcf1 "Not much..."
    if sayori_wait1 == False and sayori_wait2 == False:
        mcf1 "Hey, what's going on between you and Sayori?"
        mcf1 "It's been three days in a row since you're walking to the school without her..."
    elif sayori_wait1 == True and sayori_wait2 == False:
        mcf1 "Hey, what's going on between you and Sayori?"
        mcf1 "It's been two days in a row since you're walking to the school without her..."
    else:
        mcf1 "I'm just wondering why Sayori didn't come with you today..."
    mc "Oh, that's..."
    mc "I don't even know. I tried call to her phone but she doesn't answers neither."
    mc "I thought she went here before me but..."
    mc "Didn't you saw her?"
    mcf1 "No, sorry."
    mc "Damn it!"
    mc "She's acting weird ultimately..."
    mcf1 "I see..."
    mcf1 "Please, take good care of her [player], I have a bad feeling about this."
    mc "Don't worry Ryoma, once I met her no matter if is on the club or at lunch time, I will ask her what's happening."
    mc "I'm also worried about her..."
    mcf1 "Okay bro."
    show ryoma at t21 zorder 2
    show camilla frontal uniform l1 r2 e1a b1a ma n1 hair_normal at f22 zorder 2
    c "Guys, it's almost time to enter to our classes!"
    c "[player], where is Sayori?"
    show camilla at t22
    mc "I don't know. Didn't you saw her inside the school during school time?"
    c "No..."
    "Fucking shit, she's not even in the school."
    "Now I am very nervous... So much that I start to breath heavily..."
    c "Don't worry [player], I believe she's okay and may coming soon."
    mc "Thank you Camilla, but I can't stop thinking about her..."
    c "Here..."
    "What the...?!"
    "Camilla can't help but hug me to make me feel better."
    "It's nice I know, but...{w} It's also a bit awkward in view of everyone..."
    "Anyway, it seems to be working, my tension are gradually decreasing. So I hug her back."
    "Hehe ~ I can't help but see Ryoma's shocked face for this moment..."
    play sound school_bell
    "Oh-oh! It's time to enter in!"
    "Once Camilla release me, I turn back to see if Sayori is coming..."
    "Nothing."
    "Both Camilla and Ryoma look at the horizon too."
    "Since Sayori's not coming, they pat me at my back and takes me to the school building."
    "I wonder what happened to her..."
    scene black
    with wipeleft_scene
    stop sound fadeout 2.0
    pause 2.0
    scene bg class_day
    with wipeleft_scene
    "Dude."
    "I haven't seen Sayori in the entire day!"
    "What kind of excuse can I use in the club to justify her ausence???"
    mc "Hmm..."
    "There's something else that I noticed at lunchtime..."
    "That girl who's kneeling in front of the vending machine...{w} won't she be Natsuki?"
    play sound school_bell
    pause 1.0
    mc "Shit!"
    "Just let's hope she's in the club right now."
    scene bg corridor
    with wipeleft_scene
    stop sound fadeout 2.0
    "Before arriving at the club's door, I meet a familiar face..."
    show yuri 2b at t11 zorder 2
    y "Hi [player]...!"
    mc "Oh, hi Yuri...! What's up?"
    y 1c "I just went to fill my teapot, since Monika didn't arrive yet I take the opportunity to make some tea before club activities."
    mc "Oh, I see..."
    y 3f "Ummm... Is anything okay?"
    mc "Eh... yeah... I'm very glad you're asking..."
    y 2g "I'm asking because..."
    y 1f "One, I see your face very pale."
    y "And second, Sayori entered even before clubs hour... And seems very sad."
    mc "Ah-"
    "Why did Sayori entered earlier than the others? And why she's sad?"
    y 3t "Did something bad happened between both of you?"
    mc "No..."
    mc "At least not that I know of."
    mc "She didn't answered my phone calls, I was very worried about her."
    if sayori_wait3 == True:
        mc "In fact, I went to her house but she wasn't there neither."
    mc "Did-Did you saw her during school time?"
    y 2w "No..."
    y "I thought she was with you..."
    mc "How strange..."
    y 1a "Well, you can talk inside with her if you want."
    y "Come on, let's get in..."
    mc "S-Sure..."

    return
