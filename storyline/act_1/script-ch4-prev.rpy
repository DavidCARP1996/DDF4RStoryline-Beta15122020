label ch4_prev:
    $ ch4_prev_activities = 0
    $ stamina = 10
    $ hr_hour = 16
    $ ch4_prev_sayori_visited = False
    $ ch4_sayoriknowsvisit = False
    $ bar_closed = False
    $ park_closed = False
    $ cafe_closed = False
    $ gamestore_closed = False
    $ library_closed = False
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full

    mc "Hmm..."
    "A bright sunshine hits my face."
    "I wonder what hour is..."
    mc "10:30 AM?!"
    mc "... ... ..."
    mc "Oh, fuck..."
    "Every weekend I oversleep until 10 AM or 11 AM... And in the worse of the cases; until 12 PM."
    "The good thing is today is Saturday, and [ch4_name] drops by at Sunday."
    "So I have time to clean up this house and something else..."
    mc "Hmm..."
    "A message from Ryoma?"
    "{i}Hey [player], what's up? Listen, if you wanna drink some beers with me, come at the bar at the evening. Just tell me if you're going. Greetings{/i}"
    mc "Of course I will come in."
    mc "I need to talk with him about..."
    "(...)"
    "I reply him asking if Camilla will come in too."
    pause 3.0
    play sound ringtone1
    "(!)"
    if ch4_scene == "camilla":
        "{i}Of course she will... And she seems to be very excited about it...{/i}"
        mc "Excellent!"
        mc "It's decided then, I'll go to drink some beers with them!"
    elif ch4_scene == "monika":
        "{i}I'm sorry but, seems like she's not in mood for it...{/i}"
        mc "I knew it..."
        mc "I need to talk with him about it... So I guess there's no option than go anyway..."
    else:
        "{i}Of course she will... As usual...{/i}"
        mc "Excellent!"
        mc "It's decided then, I'll go to drink some beers with them!"
    "But first I must clean up my house... It's a fucking mess."
    "I don't know what [ch4_name] would think if she see this."
    scene bg livingroom with dissolve_scene_full
    "16:12 PM"
    mc "It's about time to meet Ryoma at the bar."
    mc "So let's go!"

label ch4_prev_loop:
    while (stamina > 0):
        if not renpy.music.get_playing(channel='music') == audio.t5:
            play music t5 fadeout 1.0
        show screen freeroam_hud
        with Dissolve(.5)
        if ch4_prev_activities == 0:
            scene bg house
            with wipeleft_scene
            $ menutext = "Where should I go first?"
        else:
            scene bg residential_day
            with wipeleft_scene
            $ menutext = "Where should I go next?"
        menu:
            "[menutext]"

            "Go to the bar" if not bar_closed:
                $ ch4_prev_activities += 1
                call ch4_prev_go_to_bar
                $ bar_closed = True
                pass
            "Go to the park" if not park_closed:
                $ ch4_prev_activities += 1
                mc "I don't want to go to the park for now..."
                $ park_closed = True
                pass
            "Go to the cafe" if not cafe_closed:
                $ ch4_prev_activities += 1
                call ch4_prev_go_to_cafe
                pass
            "Go to the gaming store" if not gamestore_closed:
                $ ch4_prev_activities += 1
                mc "The game store is closed right now."
                $ gamestore_closed = True
                pass
            "Go to the library" if not library_closed:
                $ ch4_prev_activities += 1
                mc "The library is closed right now."
                $ library_closed = True
                pass
            "Go to Sayori's house" if not ch4_prev_sayori_visited:
                $ ch4_prev_activities += 1
                mc "Sayori..."
                call ch4_prev_visit_sayori
                $ ch4_prev_sayori_visited = True
                pass
            "Go home" if bar_closed and ch4_prev_sayori_visited:
                jump ch4_prev_go_home
                pass
                pass
        pass
    jump ch4_prev_go_home

    label ch4_prev_go_to_bar:
        mc "Okay then, let's go..."
        scene bg tavern with wipeleft_scene
        "(...)"
        if ch4_scene == "monika":
            show ryoma 1 at t11 zorder 2
            mcf1 "Hey, [player]! Over here!"
            mc "Hey, Ryoma!"
            mcf1 "Waiter!"
            mcf1 "Give us 2 beer bottles and a big plate of salad snacks please."
            "Waiter" "Sure."
            "(...)"
            mcf1 "[player], what's the matter?"
            mcf1 "You don't seems to be in good mood."
            mc "I've been wondering..."
            mc "What happened to Camilla?"
            mc "Why she's not in mood to drink a beer with us?"
            mc "Do you know something?"
            mcf1 "I thought you already know it but..."
            mcf1 "She found out that you'll spend the Sunday with Monika. And that made her sad..."
            mc "No way..."
            mc "But I didn't told anything to anyone!"
            mc "How did she...??"
            mcf1 "I don't know, but seems like she found out in the worst way."
            mcf1 "She didn't even told me how, but judging her expression..."
            mc "Jesus Christ..."
            mc "I guess I know who told Camilla about that."
            mc "Monika."
            mcf1 "What?"
            mc "The only people who knew about it was me, Monika, Yuri and Natsuki."
            if ch4_sayoriknowsvisit:
                mc "And Sayori also knews it thanks to Monika."
            mc "So the only one who dares to spread that gossip is nothing more and nothing less than Monika."
            mc "I know Camilla and Monika doesn't like each other... But there's no reason to beign sad about it."
            mc "And I'm wondering in which way Monika told Camilla about it..."
            mcf1 "[player]..."
            "Waiter" "Here's your order: 2 beers with a big plate of salad snacks."
            "Waiter" "Enjoy."
            mcf1 "Thank you!"
            "After the waiter served our order, Ryoma starts to focus on the food than the topic."
            mcf1 "Cheers!"
            "(...)"
            mc "Waiter, give me more beer please."
            "Ryoma & Waiter" "Wait, what?!"
            mc "I'm gonna give you $100 of tips."
            "Waiter" "S-sure!"
            mcf1 "[player], you can't be serious!"
            mc "Shut up... I need it."
            scene black with dissolve_scene_full
            hide screen freeroam_hud with Dissolve(.5)
            $ money -= 100
            show vignette zorder 3:
                alpha 0.0
                linear 3.0 alpha 0.75
            show layer master at dizzy(0.5, 1.0)
            show layer screens at dizzy(0.5, 1.0)
            $ currentpos = get_pos()
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>mod_assets/sounds/mod_bgm/5_drunk.ogg"
            stop music fadeout 2.0
            $ renpy.music.play(audio.t5b, fadein=2.0, tight=True)
            scene bg tavern with dissolve_scene_full:
                dizzy(1, 1.0)
            show ryoma 1 at t11 zorder 2:
                dizzy(1, 1.0)
            mcf1 "[player], stop drinking please!"
            mc "Shut the fuck up... I deserve beign drowned in alcohol..."
            mcf1 "Jesus... He's drunk..."
            mc "Who the fuck is drunk?? Eh??"
            "*glup* *glup* *glup*"
            "Ryoma grabs my beer bottle."
            mcf1 "Stop it!"
            mcf1 "I didn't wanted to say it, but you're acting like a stupid!"
            mc "Grrr--!"
            mc "F u c k  y o u !"
            mcf1 "[player]..."
            mcf1 "... ... ..."
            mcf1 "I'm sorry but you let me no choice..."
            pause 1.0
            stop music
            show ryoma at face(y=500)
            scene black
            play sound "mod_assets/sounds/mod_sfx/singlepound.ogg"
            show layer master:
                truecenter
                parallel:
                    zoom 1.5
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 0
                    easein_elastic 0.35 xpos 640
            show layer screens:
                truecenter
                parallel:
                    zoom 1.5
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 0
                    easein_elastic 0.35 xpos 640
            show noise onlayer front:
                alpha 0.3
                easeout 0.35 alpha 0
                alpha 0.3
                1.35
                linear 1.0 alpha 0.0
            pause 5.0
            show vignette zorder 3:
                alpha 0.0
                linear 3.0 alpha 0.75
            show layer master at dizzy(0.5, 1.0)
            show layer screens at dizzy(0.5, 1.0)
            "Uuuuhh..."
            mc "Where...am...I...?"
            scene bg bedroom_afternoon with dissolve_cg:
                dizzy(1, 1.0)
            mc "Is this... my bedroom...?"
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            show layer master
            show layer screens
            hide vignette
            scene bg bedroom_afternoon
            mc "AAAaaaAAaahhHhh--!!!"
            "My head... It hurts a lot..."
            "... ... ..."
            "I don't remember anything what happened before."
            "What the fuck is wrong with me?"
            "And why I'm smelling like a skunk?"
            mc "Ugh--!"
            "I gotta take a bath!"
            "I'm not gonna give Monika a good impression tomorrow if I'm in this deplorable state!"
            scene black with dissolve_scene_full
            pause 3.0
            scene bg bedroom_night with dissolve_scene_full
            "Okay then, I feel a little better now."
            "Let's go to sleep."
            jump ch4_main
        else:
            show camilla frontal casual l1 r1 e1a b1a mb n1 hair_normal at t22 zorder 3
            c "Hey, [player]! Over here~!"
            mc "Hey, Camilla~!"
            show ryoma 1 at t21 zorder 2
            mcf1 "Hey, [player]!"
            mc "Hey, Ryoma!"
            mc "It's good to see you guys once again!"
            c "Yeah~!"
            mcf1 "Yeah!"
            mcf1 "Hey, waiter!"
            mcf1 "Give us 3 beer bottles and a big plate of salad snacks please."
            "Waiter" "Sure."
            c "So... While we're waiting our food..."
            c "Tell me, [player]..."
            if ch4_scene == "camilla":
                c "Are you excited about our {i}date{/i} tomorrow?"
                mcf1 "A date?"
                mc "Ahahaha, sort of Ryoma..."
                mc "We'll do a huge task for the literature club, that's all."
                mc "And yes Camilla, I'm very excited."
            else:
                c "Are you excited about your adventure with [ch4_name]?"
                c "Because I am with [ch4_nameB]..."
                mcf1 "Adventure?"
                mc "Ahahaha, not exactly like that Ryoma..."
                mc "We'll do a huge task for the literature club, that's all."
                mc "And yes Camilla, I'm very excited."
                mc "And I'm glad that you're excited to help [ch4_nameB] for me."
            mc "Honestly, in that moment where Monika made me choice between one of the girls to help them, I though I was screwed up."
            mc "But then I realised that I could ask you for help and avoid the fact of making one of them work alone."
            mc "However..."
            "[c] & [mcf1]" "Eh?"
            mc "Despite that Yuri and Natsuki liked the idea, seems like Monika didn't liked it at all."
            mc "I don't know why, but she seemed a bit pissed off about my idea."
            c "She may be a little jealous that I am contributing something to her club."
            c "I mean, there's something wrong if [player] asks for help to someone or if I help one of her club members?"
            c "What do you think Ryoma?"
            mcf1 "Me? Eeh..."
            mcf1 "I disagree with Monika attitude, that's for sure."
            mcf1 "But it's pretty strange coming from her..."
            mc "What do you mean?"
            mcf1 "She's supposed to agree to a proposition like that."
            mcf1 "Even if Camilla is her arch-rival, if she offers to help with her club, then she must gladly accept it."
            mcf1 "I never thought that Monika would be such a proud person."
            mcf1 "Or at least that's my response to why Monika disliked Camilla's help."
            c "To be honest, I expected it."
            c "She may think that if I help to her club's tasks it could affect her reputation or something like that."
            mc "I don't know..."
            mc "Consider this:{w} {b}I am{/b} one of {i}her{/i} club members."
            mc "If Monika really cares about her reputation, then she must rejected me in first place when Sayori dragged me to the club."
            mc "However, she seemed to me happy with my presence. Something very strange by the way."
            mcf1 "Really? Wow, that's new..."
            c "And how did she treated you all this time?"
            mc "Well... At first she seems to be nice, a \"new\" Monika. Here's everything normal."
            mc "But with the passing of the days, she start to beign a bit annoying."
            mc "It's like if she's hinting on me."
            mc "Obviously I'm trying to stay away from her when she does that."
            mc "And that open this question:{w} What is she up to?"
            "[c] & [mcf1]" "Hmm..."
            "Waiter" "Here's your order: 3 beers with a big plate of salad snacks."
            "Waiter" "Enjoy."
            "Everyone" "Thank you!"
            "After the waiter served our order, Camilla and Ryoma starts to focus on the food than the topic."
            "It's good tho, I think Monika has topic ruined our first-step happy moment."
            mcf1 "Cheers!"
            "[player] & [c]" "Cheers!"
            scene bg tavern with dissolve_scene_full
            $ hr_hour = 18
            show ryoma 1 at t21 zorder 2
            show camilla frontal casual l1 r1 e1c b1a ma n1 hair_normal at t22 zorder 3
            c "Delicious!"
            mcf1 "Indeed!"
            mc "Yeah!"
            "It's like 18:15 PM"
            c "Well, sorry but I gotta go."
            if ch4_scene == "camilla":
                c "I need to get prepared for tomorrow meeting with [player]~!"
                mc "Me too."
                mc "I can't wait to spend the day with you Camilla."
                c "Ehehe~"
                c "You're so cute..."
                mcf1 "If I earn 1 dollar every time Camilla says that to [player]..."
                c "If what you say were real, then I'll not doubt on making you a billionarie~"
                "Everyone" "Ahahahahaha..."
            else:
                c "I need to get prepared for tomorrow meeting with [ch4_nameB]..."
                mc "And me with [ch4_name]..."
            mcf1 "Okay then, you two can go. I'll pay the bill."
            c "But Ryoma..."
            mcf1 "I insist!"
            c "Uuuu..."
            c "Okay then."
            c "Thanks for everything~!"
            mc "Yes, thanks Ryoma."
            mcf1 "I see you guys at the festival."
            mcf1 "Good luck!"
            "[player] & [c]" "Thank you! Good luck for you too!"
            scene bg downtown_evening
            show camilla frontal casual l1 r1 e1a b1a ma n1 hair_normal at t11
            if ch4_scene == "camilla":
                c "So... [player]...?"
                mc "Yeah?"
                c "You know... We haven't decided where we should start working in your club's task."
                mc "Oh, that's true!"
                mc "Well, today at the morning I did an entire cleaning up of my house, so..."
                c "Ehehe~! It's nice, but I've been thinking..."
                c "We shall do it at my house instead~"
                mc "Wha- Really?"
                c "Of course!"
                c "My dad will be very glad to receive you with food and every fun things we can do there."
                mc "Oh, that's right..."
                mc "In my house I have nothing of that unfortunatelly..."
                mc "Alright then, tomorrow I'm gonna coming to your house."
                show camilla l5 r5 e1c b1a mb n2 at h11
                c "Yaaaay~!!"
                c e1d "Trust me, you will not regret~"
                mc "That's for sure..."
                mc "So... I'll see you tomorrow at your house then."
                c "Yes."
                c "We'll be waiting for you..."
                c "I can't wait~!"
                mc "Ehehe... Me too Camilla."
                c "Well, I'm going to reserve all the materials for tomorrow before it's late."
                mc "And I'm gonna sleep sooner so I'll be not sleepy for tomorrow."
                c "Nice!"
            else:
                c "Well [player]..."
                c "Good luck with [ch4_name]~!"
                mc "Thanks Camilla."
                mc "And good luck with [ch4_nameB] too."
                "We bump our fists."
            mc "See ya~!"
            c "See ya~!"
            pass

        return

    label ch4_prev_visit_sayori:
        "I haven't known about Sayori since she left the school earlier."
        "I shall visit her..."
        if not bar_closed:
            "At least to see if she wants to come with me."
        scene bg house with wipeleft_scene
        mc "Sayoriii--!!"
        "... ... ..."
        mc "Sayoooriiii--!!!"
        "... ... ..."
        "Suddently, the door is opening."
        mc "Oh, there you are..."
        show sayori 1ba at t11 zorder 2
        s "Hi [player]! What's up?"
        mc "Not much, I've been worried about yesterday situation and..."
        mc "...I wanted to know how are you going."
        s "Oh."
        s "Well, I'm fine of course."
        s "I just needed to take a breath outside. But now I'm fine."
        mc "I see..."
        if not bar_closed:
            if ch4_scene == "monika":
                mc "Well, Ryoma invited me to drink something today."
            else:
                mc "Well, Ryoma invited me to drink something today. Camilla will also be there..."
            mc "Do you wanna join us?"
            s "Aah..."
            s "I would love to come with you but... I want to clean my house today."
            mc "Really? That's too bad."
            "I did the same thing today at the morning..."
            "Don't tell me that she will start right now or she woke up very late."
            "Or it's just an excuse to not come with me?"
            mc "{i}*sigh*{/i}"
            mc "Anyway, I gotta go. Sorry but I can't stay."
            s "Don't worry."
            s "Send my greetings, okay?"
            mc "I will."
            s "Enjoy!"
            mc "Thanks! See you later..."
            $ ch4_sayoriknowsvisit = False
        if bar_closed:
            mc "Well, do you wanna do something fun today?"
            s "Aah..."
            s "I would love to...But I want to clean my house today."
            mc "Really? That's too bad."
            "I did the same thing today at the morning..."
            "Don't tell me that she will start right now or she woke up very late."
            "Or it's just an excuse to keep me away?"
            mc "I can help you."
            s "Sorry but you can't."
            mc "Eh?!"
            s "You got business to do with [ch4_name] tomorrow, I don't want to spend your energy for tomorrow on my things."
            mc "...Wait, how did you know that?"
            "Sayori had already left by the time we decided that last meeting."
            s 1ba "Monika told me."
            s "It's only natural for her to keep me informed about the festival preparations, right?"
            mc "Ah, that's true..."
            mc "{i}*sigh*{/i}"
            mc "So, you want to be alone then?"
            s "Yes."
            mc "Hmm...{w} Okay then, I will not bother you."
            mc "See you tomorrow Sayori."
            s "Thanks, see ya~."
            $ ch4_sayoriknowsvisit = True
        show sayori at thide
        hide sayori
        "It's not use, she's acting very weird..."
        "Anyway, we have things to do. So let's go!"
        return

    label ch4_prev_go_home:
        stop music fadeout 2.0
        hide screen freeroam_hud
        with Dissolve(.5)
        mc "..."
        "Well, I finished all my tasks, so I guess I'm going to sleep sooner."
        return
