label ch1_prev:
    stop music fadeout 2.0
    with dissolve_scene_full
    $ ch1_winner = poemwinner[0].capitalize()
    $ sayori_wait1 = False

    scene bg bedroom_night
    with dissolve_scene_full
    mc "Fuck."
    mc "Look at the hour."
    mc "I must go to sleep."
    scene black
    with dissolve_scene_full
    pause 3.0
    "After a few minutes trying to consilate the sleep, I'm success..."
    scene black
    with dissolve_scene_full
    if persistent.monika_help == True:
        pause 3.0
        show mask_2
        show mask_3
        with dissolve_scene_full
        play music m1
        "But sudently, I'm in a weird dream. Again."
        mc "Wait, again?!"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show monika sdwf1 at t11 zorder 2
        mc "You?!"
        if persistent.ytellyouherbookstore == True:
            "???" "... ... ..."
            mc "Hey! I must thank you for this Save/Load script..."
            mc "I just did something that made my day happy and..."
            "???" "..."
            mc "Ehm... Are you okay?"
            "???" "What in the world are you doing?"
            mc "What?"
            "???" "Don't play dumb."
            "???" "I know what have you done."
            "???" "Did you changed your course of the bookstore because you wanted to see that violet-haired girl?!"
            mc "And what's wrong with that?"
            mc "You gave me this power to make the right decisions, right?"
            "???" "You Idiot!"
            "???" "You already fucked up that timeline. When you regret for that there is no going back anymore..."
            mc "Well, maybe I will NEVER regret that!"
            "???" "Hush! I knew you would be a motherfucking asshole!"
            mc "..."
            "???" "Anyway..."
            pass
        else:
            "???" "Well..."
            pass
        "???" "Did you enjoy wasting your time writing a poem?"
        "???" "It's almost time to wake up."
        "???" "I feel bad for your misserable life."
        "???" "You weirdo freak."
        mc "Was that insult so neccesary?"
        "???" "Yes."
        "???" "But listen."
        if ch1_winner == "Monika":
            "???" "Hmmm...?"
            "???" "Wow!"
            "???" "Nice!"
            "???" "I didn't know you were very good with poems."
            "???" "Seems like I was right choosing you~!"
            mc "What are you talking about?"
            mc "That poem is not even for you!"
            mc "Give it back, please!"
            "???" "Okay~... Hehe~"
            "???" "You know? You're going in the right way..."
            "???" "This poem is the proof of that."
            mc "What?!"
            mc "It's just a fucking poem, it doesn't change anything."
            mc "Are you saying that the right way was entering in the Literature Club? Is that it?"
            "???" "..."
            "???" "Shut up!"
            "???" "Even if you're an good poet, looks like you're still an idiot."
            "???" "Look, just watch your back, ok?"
            "???" "I'll see you later..."
            pass
        else:
            "???" "Hmmm..."
            "???" "I see."
            "???" "You was just wasting your time."
            "???" "No."
            "???" "I'm wasting my time on YOU."
            mc "What are you talking about?"
            mc "That poem is not even for you, why are you acting so mad for this?"
            mc "And give it back, please!"
            "???" "Whatever, it doesn't worth anyway..."
            "???" "But I warn you that you are going the wrong way..."
            "???" "I can see it in this crappy poem."
            mc "What?!"
            mc "It's just a fucking poem, it doesn't change anything."
            mc "Are you saying that the wrong way was entering in the Literature Club? Is that it?"
            "???" "..."
            "???" "Shut up!"
            "???" "Look, just watch your back, ok?"
            "???" "I'm outta here..."
            pass
        $ gtext = glitchtext(20)
        "???" "{cps=60}[gtext]{/cps}{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        hide monika
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        call hideconsole
        mc "..."
        pause 2.0
        "Fuck."
        "She's really a strange woman."
        "Should I take that aware? Is something bad going to happen?"
        stop sound
        pause 3.0
        stop music fadeout 2.0
        pass
    else:
        pass

    scene bg bedroom_dark
    with dissolve_scene_full
    "..."
    "Wha-"
    mc "Hmm... 6 AM. It's very early."
    "*Grrrr~*"
    mc "Eh? I'm hungry..."
    "At this hour, the cafeteria must be open."
    menu:
        "Could I go?"

        "Yes":
            "Alright!"
            $ HKBShowButtons()
            $ ch1_prev_activities_m = 0
            $ stamina = 10
            $ hr_hour = 6
            $ park_closed = False
            $ cafe_closed = False
            $ library_closed = False
            $ gamestore_closed = False
            $ ch1_tell_sayori_meet_later = False
            $ ch1_battle_1_event = False
            $ accept_fightingclub_offer = None
            jump ch1_prev_loop
        "No":
            mc "Oh, come on!"
            mc "... ... ..."
            mc "Whatever, let's sleep a bit more then..."
            jump ch1_prev_go_sleep

label ch1_prev_loop:
    while (stamina > 0) and (hr_hour <= 7):
        if not renpy.music.get_playing(channel='music') == audio.t5:
            play music t5 fadeout 1.0
        show screen freeroam_hud
        with Dissolve(.5)
        if ch1_prev_activities_m == 0:
            scene bg house_morning
            with wipeleft_scene
            $ menutext = "Where should I go first?"
        else:
            scene bg residential_morning
            with wipeleft_scene
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the park" if not park_closed:
                mc "I don't want to go to the park for now..."
                $ park_closed = True
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch1_prev_activities_m += 1
                jump ch1_prev_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                mc "The game store is closed right now."
                $ gamestore_closed = True
                pass
            "Go to the library" if not library_closed:
                mc "The library is closed right now."
                $ library_closed = True
                pass
            "Go home":
                jump ch1_prev_go_home
                pass
            "Go to school":
                jump ch1_prev_go_play
                pass
        pass
    jump ch1_prev_go_home

label ch1_prev_go_to_cafe:
    scene bg cafe_dark
    with wipeleft_scene
    mc "..."
    mc "Eh?"
    "Guy" "Hey [player]! What's up man?"
    stop music fadeout 3.0
    "He is...?"
    show ryoma 1 at t11 zorder 1
    play music ryomatheme fadeout 3.0
    mc "Ryoma?!"
    "That guy is Ryoma. Fortunately my best friend between the most important boys in the entire school."
    "We becamed friends since we teamed up in the soccer club, I was the defender and he was the scorer, I've used to give him assistences too."
    "When I'm having problems with anybody from his circle, he always shows up to stop us and save my ass."
    "He always does his best to make the convivence peacefully as possible. He doesn't a troublemaker like the other popular boys because he knows bullying people to feel important is a waste of time."
    mcf1 2 "What are you doing here? I thought you'be still sleeping..."
    mcf1 "And how is Sayori?"
    mc "Nah, I slept sooner and woke up sooner too..."
    mc "And Sayori is fine thank goodness."
    mcf1 1 "It's nice to hear that. She's a pretty girl, you're lucky having her always at your side."
    mc "Hehe, you got a point."
    mcf1 2 "And what a coincidence, I was about to go to my new club's spot earlier to make preparatives. So I decided to have breakfast here."
    mc "Nice."
    mcf1 "Come on, choose anything you want, I'll pay."
    mc "No, it's not neccesary, I will pay my food."
    mcf1 1 "Don't worry about it, I have enough money to invite an entire group."
    mc "If you say so..."
    mcf1 "Now that we are here, tell me: How is that Literature Club that Monika founded?"
    mc "Well..."
    scene black
    with dissolve_scene_full
    scene bg cafe
    with dissolve_scene_full
    show ryoma 2 at t11 zorder 1
    mcf1 "There's nothing better than a coffee and a ham & cheese toast..."
    mc "Indeed."
    mc "Thanks Ryoma."
    mcf1 1 "Don't mention it."
    mcf1 "Oh! I almost forgot..."
    mcf1 "Before you entered to the Literature Club I was about to inviting you to my club, but..."
    mc "Sorry about that."
    mcf1 4 "Wait, I guess you can be a 'member' there at the same time..."
    mcf1 "But there's a problem:"
    mc "What?"
    mcf1 "How your leg is?"
    mc "This? I guess it's fixed."
    mc "The accident was about 2 years ago, at the first year of rehabilitation I was able to run again, so I can do anything."
    mc "Why are you asking?"
    mcf1 1 "Well... the fact it's my club is..."
    mcf1 "A Mixed Martial Arts Club."
    mc "Oh, I see..."
    mc "Well, I guess my leg is in conditions to beat people. But why should I join in?"
    mcf1 2 "It's easy... First: We need some promotion, if people see someone has interests in the club activities they could be interested too."
    mcf1 "And for some reason, the Literature Club got more attention when you joined in. But everybody is waiting for the Festival to see what the club 'really' offers."
    mcf1 "Second: If you reach the Top of the \"Mini Tournament\" on the 3rd day, you will get some cash as reward."
    mcf1 "And Third: We don't have the same schedule like the Literature Club, you can go there after school if you want, we have two schedules."
    mc "Aha!"
    show ryoma 1
    mc "Well, it sounds good."
    menu:
        "Should I join the Mixed Martial Arts Club? (I won't quit the Literature Club for this, it's just more activities and EXP farming included)"

        "Yes.":
            mc "I'm in!"
            mc "Also, I need to do some exercises."
            mcf1 "Thank you very much [player]!"
            mc "It's nothing."
            mc "If the school has no problems about participating in two clubs at the same time, you can count on me."
            mcf1 "Alright! It's official then."
            mcf1 "Welcome to the Mixed Martial Arts Club!"
            mc "Thanks Ryoma..."
            mcf1 "You're welcome bro."
            $ accept_fightingclub_offer = "Yes"
            pass
        "I'm gonna think about it...":
            mc "I need to check my agenda, but don't worry, I will consider your offer..."
            mcf1 "Okay, I will wait for your answer then. The doors will be open for you if you decide to join in."
            mc "Alright, thanks Ryoma."
            mcf1 "Don't mention it."
            $ accept_fightingclub_offer = "Maybe"
            pass
        "No.":
            mc "Sorry, but I'm affraid I don't have enough time."
            mcf1 "Too bad..."
            mcf1 "Well, if for some reason you change of mind, just tell me okay?"
            mc "Okay, thanks fot the offer anyway Ryoma."
            mcf1 "Don't mention it."
            $ accept_fightingclub_offer = "No"
            pass
    mcf1 "Alright then... See you later?"
    if accept_fightingclub_offer == "Yes":
        mc "Yeah Ryoma, I'll see you in the Mixed Martial Arts club."
        pass
    else:
        mc "Yeah Ryoma, I'll see you later."
    mc "Oh, wait!"
    mc "Why are you going to your club so sooner?"
    mcf1 "You see, we have our club in an abandoned dojo in addition to the school gym."
    mcf1 "That is you must go to that dojo if you're in the Literature Club in our school hour."
    mcf1 "I'm going sooner because I need to clean some mess up, that's all."
    mc "Oh, I see..."
    if accept_fightingclub_offer != "No":
        mcf1 "Come with me if you want, and then I can teach you some tips about our club. And in the way you can go to school sooner."
        mcf1 "Unless you want to know all of this later..."
        menu:
            mc "Well..."

            "Go with Ryoma.":
                mcf1 "Nice! Then let's go..."
                mc "Yeah!"
                jump ch1_prev_go_fightingclub
                pass
            "Pass.":
                mc "Sorry..."
                mcf1 "Don't worry, we can do this afterschool if you want."
                pass
            "I don't know, I need to pick up Sayori in time to go to school.":
                mcf1 "Shit dude, that's true!"
                mcf1 "She's been overslepting more frequently, isn't? You should do something at the respect."
                "Fuck, he's true... But, it's not like I don't want to help her, she's just retracts and says \"I'm okay\" everytime I asking her and deflects the subject..."
                mc "I'm doing my best, but she says everytime that she's fine..."
                mcf1 "I see..."
                mcf1 "Well, take good care of her, and come to my club afterschool if you want."
                mc "Alright!"
                pass
    else:
        pass
    mc "Thanks again..."
    mcf1 "Don't mention it."
    mcf1 "See you later!"
    stop music fadeout 3.0
    $ stamina -= 1
    $ cafe_closed = True
    jump ch1_prev_loop

    return

label ch1_prev_go_sleep:
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school_A

return

label ch1_prev_go_home:
    stop music fadeout 2.0
    hide screen freeroam_hud
    with Dissolve(.5)
    mc "..."
    mc "You know what?"
    mc "Damn..."
    mc "Should I try to sleep a bit more? There's still more free time before go to school..."
    scene bg bedroom
    with wipeleft_scene
    pause 1.0
    $ HKBShowButtons()
    $ HKBHideButtons()
    play sound click
    scene bg bedroom_dark
    mc "Zzzzzzzzzzz..."
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school_A

return

label ch1_prev_go_play:
    stop music fadeout 2.0
    hide screen freeroam_hud
    with Dissolve(.5)

    mc "I still have some free time before going to school."
    mc "Maybe I should play some videogames, right?"
    mc "Yeah, good idea..."
    mc "Let's get back home!"
    scene bg bedroom
    with wipeleft_scene
    pause 0.5
    $ HKBShowButtons()
    $ HKBHideButtons()
    mc "Now let's turn on the console and..."
    scene black
    with dissolve_scene_full
    jump ch1_prev_go_school_A

return

label ch1_prev_go_fightingclub:
    hide screen freeroam_hud
    with Dissolve(.5)
    $ HKBShowButtons()
    $ HKBHideButtons()
    scene bg fightingclub_dirty
    with wipeleft_scene
    $ renpy.notify("Notice: inventory will be temporarily disabled.")
    show ryoma 1 at t11 zorder 1
    mcf1 "Here we are!"
    menu:
        "My god, what a mess...":
            mcf1 "Yeah, sorry for that."
            pass
        "Thank God I came to help you...":
            mcf1 "Yeah, sorry for that."
            pass
        "(Don't say anything...)":
            mcf1 "I know, this place is a mess."
            pass
    mcf1 "But in order to open the new schedule, I need a new space apart of the school gym."
    mc "I see..."
    mc "Well, we have time enought before the school gates open up."
    mc "So count on me! Let's make this place an nice training dojo."
    mcf1 "Well said, let's go!"
    scene black
    with dissolve_scene_full
    pause 3.0
    scene bg fightingclub_clean
    with dissolve_scene_full
    show ryoma 1 at t11 zorder 1
    mc "Phew! I guess it's done..."
    mcf1 "Yeah, that was the last thing to do."
    mcf1 "Look at this place bro, it isn't awesome?"
    mc "Yes, indeed!"
    mcf1 "[player], I owe you a big thanks for this!"
    mc "It was nothing Ryoma, you'be been doing for me things heavier than this."
    mc "Trust me, this is just a part of my pay to all of your favors done for me."
    mc "I still owe you more..."
    mcf1 "Don't say such thing, without your help I could cleaned this place after the school hour, I could entered very late..."
    mcf1 "You did for me a giant favor, remember that. You don't owe me nothing!"
    mc "Alright... Thanks Ryoma."
    mcf1 "It's nothing bro."
    show ryoma at thide zorder 1
    hide ryoma
    "..."
    "Ryoma and I lie down to rest watching at the dojo's roof."
    "Suddently I look at the phone's hour."
    mc "HOLY SHIT!!!"
    show ryoma 1 at t11 zorder 1
    mcf1 "What's wrong [player]?!"
    mc "It's 8 AM already!!!"
    mc "We'll be late-!!!"
    mcf1 "Hey, hey! Relax!"
    mcf1 "We take only 4 minutes walking directly to the school, don't worry!"
    mc "Oh, I forgot that... Sorry..."
    "..."
    mcf1 "Hey! I have an idea..."
    mc "?"
    mcf1 "What if we practice some fighting before school?"
    mc "Are you serious?"
    mcf1 "Well, you're a member of the Mixed Martial Arts Club now, so you must do it to proof you're done for this place."
    mcf1 "It's like when you write poems for the Literature Club..."
    mc "Well..."
    menu:
        "Okay, but first let me call Sayori to make sure she will go to school sooner.":
            mcf1 "Sure!"
            mc "Thank you..."
            "*calling Sayori*"
            s "Uh?! [player]...?"
            mc "Sayori, I'm warning you I can't go to school with you this time."
            mc "I'm helping a friend of mine with something and we'll come to school in the way, so I can't go to your house in time."
            mc "Sorry about that..."
            s "S-sure, no problem."
            mc "At least promise me we'll meet at the entrance in hour. Or you will be in school right on time."
            s "Yeah [player], don't worry about that."
            s "Thanks for calling me."
            mc "Don't mention it."
            mc "See you later Sayori..."
            s "Hehe~ See you later [player]..."
            "*click*"
            $ ch1_tell_sayori_meet_later = True
            mc "Aaand it's done!"
            call ch1_prev_fightingclub_battle
            $ ch1_battle_1_event = True
            "He watch his phone."
            mcf1 "Oh-oh! We must go to school!"
            "I watch the mine..."
            "8:50 AM"
            mc "Shit, you're right!"
            mcf1 "Let's go dude!"
            mc "Yes!"
            jump ch1_prev_go_school_B
            pass
        "Let's go!":
            call ch1_prev_fightingclub_battle
            $ ch1_battle_1_event = True
            "He watch his phone."
            mcf1 "Oh-oh! We must go to school!"
            "I watch the mine..."
            "8:50 AM"
            mc "Shit, you're right!"
            mcf1 "Let's go dude!"
            mc "Yes!"
            jump ch1_prev_go_school_B
            pass
        "Pass.":
            mcf1 "Alright then, no problem..."
            mc "Well... Shall we go to school?"
            mcf1 "If you want..."
            stop music fadeout 2.0
            jump ch1_prev_go_school_B
            pass
        "I remember I need to pick up Sayori, sorry.":
            mcf1 "Really? Then let's do this later, okay?"
            mc "Sure... See you later Ryoma!"
            mc "And thanks for the invitation..."
            mcf1 "Thanks to you for accepting it!"
            stop music fadeout 2.0
            jump ch1_prev_go_school_A
            pass

    label ch1_prev_fightingclub_battle:
        mcf1 "Alright [player]! Are you ready?"
        $ mc_current_weapon = None
        $ mc_current_weapon_type = None
        mc "Yes! I am!"
        mcf1 "Let's go then..."
        call ch1_battle_1
        $ mc_hp = 1
        if ch1_battle_1_victory == True:
            mc "Aaaaand K.O.!"
            "I lift Ryoma from the ground."
            show ryoma 1 at t11 zorder 1
            mcf1 "Dude, you're very good!"
            mcf1 "Have you been training in your house or something?"
            mc "Something like that, in fact."
            mcf1 "What?"
            mc "Well, I like to punch the walls, kick everything around me, run even if it's unnecessary, and sometimes I practice some basic karate."
            mc "Even I've using Sayori to practice evasion and resistance to the hits making her hit me."
            mcf1 "Incredible..."
            pass
        elif ch1_battle_1_victory == False:
            mcf1 "Knock Out! I won..."
            "Ryoma lift me from the ground."
            show ryoma 1 at t11 zorder 1
            mc "Ouch!"
            mcf1 "Sorry..."
            mcf1 "Too bad bro, I was expecting something better from you."
            mc "Well, I guess I'm not so ready for this..."
            mcf1 "Don't say that. You can be even better, just come here after school everytime and try to gain some fighting skills (EXP)."
            mcf1 "Me and the boys will try to train you harder in order to make you stronger!"
            menu:
                "Next time I will do my best, you can count on that!":
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
                "Okay...":
                    mcf1 "Not so enthusiastic, isn't?"
                    mc "Well..."
                    "Who am I kidding? I need this kind of training to become stronger..."
                    "Alright! I will train with him!"
                    mc "You're right! And that's why I'm joining your club!"
                    mc "I will train harder as possible to become stronger!"
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
                "And why should I enhance my fighting skills? What's the point?":
                    mcf1 "I already kicked your butt, and we only had a training battle..."
                    mcf1 "What do you think could happen if you were in a different situation?"
                    mc "Eeeeh..."
                    "He's fucking right! I can't do anything if I'm still weak as fuck! They can kill me!"
                    "Alright! I will train with him!"
                    mc "You're right! And that's why I'm joining your club!"
                    mc "I will train harder as possible to become stronger!"
                    mcf1 "Perfect! That's the [player] I know..."
                    pass
            pass
        else:
            "*pant* *pant*"
            show ryoma 1 at t11 zorder 1
            mcf1 "Draw!"
            mcf1 "Incredible, are we so similar in strenght?"
            mc "I guess so..."
            pass
        mcf1 "You have been doing cool, but honestly, I was expecting a little more..."
        mc "Why? You are the athletic boy in the school, and I am an loser who waste his time playing videogames and/or watching anime."
        mcf1 "Oh come on! Don't say such thing!"
        mcf1 "Don't you remember when we were in the Soccer Club? You had a lot of potential in strenght and speed."
        mcf1 "Even in the Computing classes you had a lot of potential to be programmer, I remember how Monika was asking you for the right notes when she had absolutely zero interest on you."
        mcf1 "That's why I respect you a lot, you are a guy with potential in anything what you do."
        mcf1 "And I trust that you will become stronger if you train here everyday!"
        mcf1 "Come on! Just give me the opportunity..."
        mc "I haven't said I won't do it, it's just... I guess you've been overrating that \"potential\"."
        play music tmod2
        mc "Since that accident I'm not the same. Every problems I have I tried to fix them with violence instead of talking like normal people does."
        mc "The only reason I haven't committed suicide yet is because of Sayori. She's like a sunshine in my life of darkness."
        mc "And now I met more fantastic persons in the Literature Club..."
        mc "Yuri for example, she's my new crush now."
        mc "Natsuki seems to be an interesting person despite her bipolar personality."
        mc "And Monika has become friendlier to me since I joined. Putting aside some hypocrisy, I have seen a good side of her."
        mc "I have 4 reasons why to live, I don't know what can I do without them."
        mc "Oh, and I will never forget about you and Camilla... I guess there are 6 reasons."
        mcf1 "... ... ..."
        mcf1 "I... I don't know what to say."
        mcf1 "I didn't know you have such thoughts..."
        mcf1 "N-Now I understand why you are so withdrawn since that damned accident."
        mcf1 "Sorry bro, I..."
        mc "Don't worry Ryoma, you have nothing to sorry for."
        mc "On the contrary, I should apology to throw all my shit on you like if you were an psychologist or something like that..."
        mcf1 "No bro, it's okay if you do that."
        mcf1 "That 'shit' what you mean it's all the negative thoughts you've been retaining in your mind all this time."
        mcf1 "Don't you feel like some kind of \"freedom\"?"
        stop music fadeout 2.0
        mc "... ... ..."
        mc "Maybe..."
        play music t8
        mc "Maybe you're right!"
        mc "So was that then, all my thoughts was driving me into an negative status which asks for such thing like suicide!"
        mc "Ryoma... I owe you a big one!"
        "We do Hi-Five."
        mcf1 "No problem [player], that's what friends are for."
        $ mc_hp = mc_hp_max
        pass
    return

label ch1_prev_go_school_A:
    scene bg house
    with wipeleft_scene
    play music t2
    $ HKBShowButtons()
    "8:15 AM"
    "Time enough to wait for Sayori and go to the school together..."
    mc "Sayori!"
    "If she's not showing up until 8:30, I will go alone."
    mc "SAYOOORIIIIIIIIIIIIIIIIIII-!!!{nw}"
    s "I'M COMING~!"
    mc "What the..."
    "It's me or Sayori sounded a bit upset? Geez, does she know what hour it is now?"
    "The door is opening gently."
    show sayori 4a at t11 zorder 2
    s "Hi [player]! I'm so glad you waited for me again~!"
    mc "It's a pleasure."
    "She doesn't look so good, look at her: her hair is messy, one of the buttons is opened..."
    show sayori 1b
    "But no matter what defects she's having, she's still perfect for me."
    "(...or for someone else. Honestly, She doesn't deserves an asshole like me.){nw}"
    s 1c "Hey!"
    s 3c "It's me or are you rambling?"
    mc "Wha-"
    "Fuck!"
    "Well, let's stop fucking around and let's take her to the school..."
    show sayori 1b
    mc "Ehm... It's nothing Sayori, I just... didn't take a good sleep... that's all..."
    s 4r "Me either, hahaha~!"
    mc "Hahaha!"
    mc "Are you ready?"
    show sayori at h11
    s "Yeah! Let's gooo-!"
    $ sayori_wait1 = True
    scene black
    with dissolve_scene_full
return

label ch1_prev_go_school_B:
    if not renpy.music.get_playing(channel='music') == audio.t8:
        play music t8 fadeout 1.0
    scene bg school_entrance
    with wipeleft_scene
    pause 1.0
    show ryoma 2 at t11 zorder 1
    mc "Here we are..."
    show ryoma 1 at t21 zorder 2
    show camilla frontal uniform l1 r2 n1 mb e1a b1a hair_normal at f22
    $ c_name = "Girl"
    c "What's up guys?!"
    show camilla ma at t22
    "[player] & Ryoma" "Camilla!"
    $ c_name = "Camilla"
    "She's Camilla. Maybe the second most popular girl in the school..."
    "She has everything to be even better than Monika, but she's a bit lazy to do what Monika does to deserve the school's throne."
    "Also, we are friends since I was in the soccer club. For some reason she always cheered for me, all what I know is we like the same things."
    "So it's a bit curious how a girl like her is very interested on my life and wants to help if she can. She's not like other people too."
    $ camilla_presentation = True
    show camilla r1 e1c at h22 zorder 2
    "She hugs us at the same time very enthusiastic."
    show camilla e1a mb at f22 zorder 2
    c "Sooo... Where did you come from?"
    if ch1_battle_1_event == True:
        c me "Both are sweating!"
        show camilla at t22 zorder 2
        mcf1 "Yeah..."
    else:
        show camilla at t22 zorder 2
        pass
    mc "We came from Ryoma's dojo."
    c l2 r2 md "A dojo?"
    show ryoma 2 at f21 zorder 2
    mcf1 "I invited [player] to join my Mixed Martial Arts Club, and he helped me with the refactions."
    if ch1_battle_1_event == True:
        mcf1 "We also had a training fight to test his skills..."
    show camilla l1 r1 mb at f22
    show ryoma 1 at t21
    c "Oh, I see..."
    c l3 r3 e1c ma "May I join in too?"
    show camilla at t22
    show ryoma 2 at f21
    mcf1 "If you want..."
    show camilla e1a mb
    mcf1 "At least everybody knows you have a strong physique, even if you don't appear to."
    mcf1 "So there's no problem on participating in the competitions."
    show camilla e1c at f22
    show ryoma 1 at t21
    c "Hehe! Thanks Ryoma~"
    show camilla l4 r4 at t22
    mc "That's great!"
    menu:
        "I wish you both join my Literature Club too...":
            show camilla ma at f22
            c "I hope so..."
            show camilla at t22
            show ryoma 4 at f21
            mcf1 "Sounds good, but Camilla, you got a \"serious problem\" in that club about, you know..."
            show ryoma at t21
            show camilla l1 r1 b1b e1a md at f22
            c "What it is?"
            c r2 mf e1b "Oh true, that green eyed girl is the President."
            c me e1a b1c "[player], how do you spend time in the same room with her? You're very psychologically strong to stand her..."
            show camilla at t22
            mc "Yeah... well..."
            if ch1_winner != "Monika":
                mc "I'm trying to ignore her."
            else:
                mc "I'm trying to give her an opportunity, she's beign so nice to me since I joined in..."
            show camilla mg b1a
            mc "In fact, seems like she's not so dumbass to me like before."
            mc "I don't know why she's beign so nice to me suddently... Even I don't understand it."
            mc "Sayori says Monika is a great person. Also Yuri and Natsuki seems to be agree."
            show camilla r2 mf b1b at f22
            c "I see..."
            show camilla at t22
            mc "Anyway, I guess Monika is changing progressively, I hope she treats the others so nice too."
            show camilla l4 r4 mg e1b b1b at f22
            c "I don't know... You must be careful darling. I have a bad feeling about this."
            show camilla at t22
            mc "I'll keep it in mind. Thanks Camilla."
            show camilla ma e1c b1a at f22
            c "Hehe~! Don't mention it."
            "She pats my head."
            show camilla at t22
            pass
        "We'll be a great team!":
            show camilla l3 r2 mc e1d b1a at f22
            c "I agree..."
            show camilla at t22
            show ryoma 1 at f21
            mcf1 "Me too..."
            show ryoma at t21
            pass
    "The school bells sounds."
    show camilla l1 r1 mf e1a b1b
    show ryoma 4 at f21
    mcf1 "Oh oh! It's time to enter in..."
    show ryoma 3 at t21
    show camilla me
    mc "Wait a minute!"
    mc "Have you seen Sayori enter in while we been talking?"
    show ryoma 4 at f21
    mcf1 "No."
    show ryoma at t21
    show camilla r2 mh b1c at f22
    c "No."
    show camilla at t22
    mc "Fuck!"
    show ryoma 3
    "I dial to Sayori's phone..."
    s "Hello?"
    mc "Sayori, where are you?"
    s "I'm at one square from the school..."
    s "Hey! I see you!"
    "I spot a Sayori-shaped girl in the horizon..."
    show camilla r1 mb b1a at f22
    c "Look, here comes Sayori!"
    show camilla at t22
    show ryoma 1
    mc "Thank Goodness!"
    show ryoma 2 at f21
    mcf1 "Yeah!"
    show sayori 1a at f31 zorder 3
    show ryoma at t32 zorder 2
    show camilla at t33 zorder 2
    s "Hello everyone~!"
    show sayori at t31 zorder 2
    show camilla e1c at f33 zorder 3
    show ryoma at f32 zorder 3
    "Everyone" "Hi Sayori!"
    show sayori at f31 zorder 3
    show camilla at t33 zorder 2
    show ryoma 1 at t32 zorder 2
    s "Ready for a new class day?"
    show sayori at t31 zorder 2
    mc "Sure! Let's go everyone..."
    stop music fadeout 3.0
    scene black
    with dissolve_scene_full

    return
