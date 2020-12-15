label fightingclub:
    scene bg fightingclub_clean
    with wipeleft_scene
    play ambient fightingclub1
    hide screen freeroam_hud with Dissolve(.5)
    $ HKBShowButtons()
    $ HKBHideButtons()
    $ mc_current_weapon = None
    $ mc_current_weapon_type = None
    $ fightingclub_battle = True
    $ fightingclub_activities += 1
    if fightingclub_activities == 1:
        $ fightingclub_activities_day = "one"
    elif fightingclub_activities == 2:
        $ fightingclub_activities_day = "two"
    elif fightingclub_activities == 3:
        $ fightingclub_activities_day = "three"
    $ renpy.notify("Notice: inventory will be temporarily disabled.")
    if fightingclub_activities == 1:
        jump fightingclub_introduction
    else:
        jump fightingclub_introskip
    return

label fightingclub_introduction:
    show ryoma frontal sports l1 r1 b1a e1a mb at t11 zorder 2
    mcf1 "Yo, [player]!"
    if accept_fightingclub_offer == "Yes":
        pass
    elif accept_fightingclub_offer == "No":
        mcf1 "What a surprise. I thought you are not interested..."
        mc "Yeah, well... I changed of mind."
        mcf1 "Cool then."
        pass
    elif accept_fightingclub_offer == "Maybe":
        mcf1 "So you finally decided to join in?"
        mc "Yes."
        mcf1 "Cool then."
        pass
    elif accept_fightingclub_offer == "Camilla":
        mcf1 "What a surprise seeing you here..."
        mc "Yeah, well... Camilla invited me and I cannot reject her."
        mcf1 "Really? Cool then."
        pass
    else:
        mcf1 "What a surprise seeing you here..."
        mc "Yeah, well... I just saw a pamphlet if your club and I said \"Why not?\"."
        mcf1 "Cool then."
        pass
    mcf1 ma "Welcome to the Mixed Martial Arts club!"
    mc "Thanks!"
    "..."
    mc "Wow, Ryoma, this place is nicely crowed..."
    mcf1 mb "Yeah, but most of them are new people which comes from another clubs, like you."
    mc "Oh, I see..."
    show ryoma ma
    if camilla_presentation == True:
        c "[player]~!"
        show ryoma at t21 zorder 2
        show camilla frontal sports l2 r1 b1a e1a mb n1 hair_normal at t22 zorder 3
        mc "Hey, Camilla!"
    else:
        $ c_name = "Girl"
        c "[player]~!"
        show ryoma at t21 zorder 2
        show camilla frontal sports l1 r2 b1a e1a mb n1 hair_normal at t22 zorder 3
        mc "Hey, Camilla!"
        "She is Camilla. Maybe the second most popular girl in the school..."
        "She has everything to be even better than Monika, but... just like me, she's a bit lazy to do what Monika does to deserve the school's throne."
        "Also, we are friends since I was in the soccer club. For some reason she always cheered for me, all what I know is we love the same soccer team."
        "So it's a bit curious how a girl like her is very interested on my life and wants to help if she can."
        $ camilla_presentation = True
    mc "It's good to see that we'll be sharing activities together guys."
    show camilla l4 r4 e1c ma n2 at f22
    c "Yeah~!"
    show camilla at t22 zorder 2
    jump fightingclub_activities
    return

label fightingclub_introskip:
    show ryoma frontal sports l1 r1 b1a e1a mb at f21 zorder 2
    show camilla frontal sports l2 r1 b1a e1a mb n1 hair_normal at t22 zorder 2
    mcf1 "[player]! Welcome again!"
    show ryoma at t21 zorder 2
    show camilla at f22 zorder 3
    c "It's good to see you again darling~"
    show camilla at t22 zorder 2
    mc "Thanks guys..."
    jump fightingclub_activities
    return

label fightingclub_activities:
    if chapter == 1:
        show camilla e1a b1b mc n1 at f22 zorder 3
        c "So, [player]... How are you doing at the literature club?"
        show camilla at t22 zorder 2
        mc "Well... I guess we had some problems around and..."
        show ryoma md
        show camilla mf
        mc "... ... ..."
        mc "I don't know if I should say it. It was a sort of embarrasing for everyone there."
        show camilla l2 r2 b1f me at f22 zorder 2
        c "It has something to do with Monika?"
        show ryoma e1b b1e at f21 zorder 2
        show camilla at t22 zorder 3
        mcf1 "Camilla, please..."
        show ryoma at t21
        mc "Not exactly..."
        show ryoma e1a b1a mc
        show camilla l1 r1 b1a me
        mc "But some members had a dispute about their poems style and..."
        if ch1_choice == "sayori":
            mc "...Let's say that Sayori saved the day. That's all."
            show ryoma ma at f21 zorder 3
            mcf1 l3 r2 mb "Sayori? Wow, she seems to have the guts of a club president."
            show ryoma mb at t21 zorder 2
            c "Yeah! That's amazing!"
            show camilla e1b ma at t22 zorder 2
            mc "Yes."
            pass
        elif ch1_choice == "mc":
            mc "...It didn't ended well at all..."
            mc "And please, don't ask what happened. Let's just say that everything was solved after all."
            "Ryoma & Camilla" "Hmm...{w} Okay."
            pass
        else:
            mc "...Well, at least everything was solved after all."
            show ryoma ma at f21 zorder 3
            mcf1 "I see..."
            show ryoma at t21 zorder 2
            show camilla ma b1b at f22 zorder 3
            c "Good..."
            show camilla at t22 zorder 2
            mc "Yeah..."
            pass
        pass
    elif chapter == 2:
        c "Hey, [player]. Do you have some gossip about the Literature Club?"
        mcf1 "Camilla, I guess you shouldn't..."
        mc "Don't worry Ryoma, it's okay what is she doing."
        mc "Well, back to the topic.{w} Not much..."
        mc "We just recited our poems in order to be ready for the festival."
        if ch2_winner == "Sayori":
            mc "And Sayori loved mine."
            mcf1 "Well, I guess everybody here knows she loves anything coming from you... Right Camilla?"
            c "Hehehe, yes. Indeed."
            mc "Hehe... You're right."
            pass
        elif ch2_winner == "Monika":
            mc "And Monika loved mine."
            c "For real?"
            c "Jeez, seems like {i}finally{/i} Monika \"loves\" something coming from you..."
            mcf1 "Camilla..."
            c "What?"
            mc "No Ryoma, she's right."
            mc "I don't even understand why suddently Monika have some \"interests\" on me..."
            mcf1 "Really?"
            c "Just be careful [player], I wouldn't trust her so much if I were you."
            mc "I will... Don't worry about me Camilla."
            mcf1 "Ehm... What if we change of topic?"
            "[player] & Camilla" "Sure, why not?"
            pass
        elif ch2_winner == "Yuri":
            mc "And Yuri loved mine."
            c "Isn't she the purple-haired girl with a sexy body?"
            c "Wow! You must feel very lucky [player]~"
            mc "Indeed... Hehe~"
            mcf1 "Amazing..."
            pass
        elif ch2_winner == "Natsuki":
            mc "And Natsuki loved mine."
            c "Isn't she the pink-haired girl who looks cute?"
            mc "Yep."
            c "Hehehe..."
            mcf1 "Wow... I've heard that she's very hard to deal with."
            mc "You're right Ryoma. Hahahaha!"
            pass
        else:
            mc "But nobody liked it..."
            "Ryoma & Camilla" "Eeehh--??"
            c "Here, hand me that poem."
            mc "Why? If nobody liked it it's because it sucks..."
            mcf1 "Camilla, don't pressure [player]. If he doesn't want to share it, then you can't compel him."
            c "But I just wanted to read it... Please [player]~"
            menu:
                "Alright...":
                    pass
            c "Yay! Let's see..."
            "... ... ..."
            mcf1 "Hey! Not bad [player]."
            c "This...{w} is...{w} Beautiful--!"
            c "I loved it [player]! Good job!"
            mc "Are you serious?"
            mc "Are you sure that you're don't trying to comfort me? Because..."
            c "No. Absolutely no."
            c "I'm serious [player], this poem is very good. Even Ryoma liked it."
            mcf1 "Yes [player]. It's good."
            mc "Well...{w} Thanks then guys~!"
            c "Hehe~"
            pass
        pass
    elif chapter == 3:
        if ch3_battle_1_victory == True:
            mcf1 "Guys... Is that true that both of you beated up Akuma during club activities?"
            menu:
                "Yes.":
                    pass
                "It was me, don't blame Camilla please.":
                    pass
                "Eehhh...":
                    pass
            mcf1 "Because everybody were talking about that at the exit of the school."
            mcf1 "Also, Akuma was very upset about that. So much that he was waiting for [player] to beat him at the exit!"
            mcf1 "I didn't knew what to do... It was a good thing that you dissapeared before exit [player]."
            menu:
                "Well, I could kick his ass once again.":
                    c "I agree with you~!"
                    mcf1 "You guys can't be talking seriously..."
                    pass
                "Yeah, it was a very good thing...":
                    c "Hehehe..."
                    mcf1 "... ... ..."
                    pass
            mcf1 "Well [player], the next time you must be very careful..."
            mcf1 "You can't pass the rest of your life fighting against Akuma."
            mc "Aaaaahh..."
            c "Ryoma, if Akuma doesn't stop beign a jerk, we have no other option than show him some respect."
            c "I'm also tired of his attitude. But I won't let him hurt [player], no matter the reasons he have."
            mcf1 "I understand Camilla, but..."
            mcf1 "Uh...{w} Nevermind."
            mcf1 "Let's change of topic and forget about this. Okay?"
            "[player] & Camilla" "Sure."
            pass
        elif not ch3_battle_1_victory:
            mcf1 "Guys... Is that true that Akuma beated up [player] during club activities?"
            menu:
                "...":
                    pass
                "It was my fault, don't blame Camilla please.":
                    pass
                "Yes...":
                    pass
            mcf1 "Because everybody were talking about that at the exit of the school."
            mcf1 "Also, Akuma was very upset because Camilla hit him very strong. So much that he was waiting for [player] to beat him at the exit."
            mcf1 "I didn't knew what to do... It was a good thing that you dissapeared before exit [player]."
            menu:
                "Well, I could kick his ass the next time.":
                    c "I agree with you~!"
                    mcf1 "You guys can't be talking seriously..."
                    pass
                "Yeah, it was a very good thing...":
                    c "... ... ..."
                    pass
            mcf1 "Well [player], the next time you must be very careful..."
            mcf1 "You can't pass the rest of your life fighting against Akuma."
            mc "Aaaaahh..."
            c "Ryoma, if Akuma doesn't stop beign a jerk, we have no other option than show him some respect."
            c "I'm also tired of his attitude. But I won't let him hurt [player], no matter the reasons he have."
            mcf1 "I understand Camilla, but..."
            mcf1 "Uh...{w} Nevermind."
            mcf1 "Let's change of topic and forget about this. Okay?"
            "[player] & Camilla" "Whatever..."
            pass
        else:
            pass
        c "So, [player]... Tell me what happened with Sayori?"
        c "I've saw her leaving the school and..."
        mcf1 "Sayori?!"
        mcf1 "What's wrong with her?"
        mc "You see..."
        mc "She is still evasive. She even left the club without saying anything except that she wasn't feeling good."
        mc "And...{w} I'm so idiot that I let her go..."
        c "Aaahh... Don't say such thing [player]. You're not an idiot!"
        mcf1 "I knew something was wrong about Sayori..."
        mcf1 "I wish I could do something for her, [player]."
        mcf1 "Just keep me aware of everything about her... I may do something big to make her happy again."
        mc "I will..."
        mc "Thank you guys for all your support."
        c "No problem, that's why we are with you~"
        mcf1 "She's right [player]..."
        mc "Hehe~"
        pass

    $ fightingclub_activities_day = "fightingclub_activities_" + fightingclub_activities_day
    call expression fightingclub_activities_day
    return

label fightingclub_activities_one:
    mc "So... How shall I start?"
    show ryoma b1a mb at f21 zorder 3
    mcf1 "I'm glad you ask."
    mcf1 "Well, today we can start with a Trio Tag Team match with switching rules."
    show camilla l4 r4
    mcf1 "We three will battle against another Team conformed by three opponents at the same time, but in a divided 1 vs 1."
    mcf1 "After all the three finish our respective battles, another round starts but switching opponents."
    mcf1 "That switching repeats again in round 3. However, that's the final round, so after we finish our battles the winner Team will be defined by how many victories had each Team."
    mcf1 "Did everybody understood?"
    show ryoma b1b ma at t21 zorder 2
    show camilla l3 r1 e1d b1d mb at f22 zorder 3
    c "Yes."
    show camilla at t22 zorder 2
    mc "Yes."
    menu:
        "Did you understood everything?"

        "Yes.":
            "Good then."
            "In any case, check the History list on the Menu to read everything again, I don't want to disturb Ryoma because of you."
            pass
        "No.":
            "Then check the History list on the Menu to read everything again, I don't want to disturb Ryoma because of you."
            pass
    show ryoma mb at f21 zorder 3
    mcf1 "Fine then."
    show ryoma b1a ma at t11 zorder 2
    show camilla l1 r1 ma e1a b1b at t44 zorder 3
    "After Ryoma finish his explanation, he does a loud clap to call attention."
    show ryoma mb at f11
    mcf1 "Okay, everyone!"
    mcf1 "We need 3 volunteers for a activity."
    mcf1 "Today I want to do a Trio Tag Team match which consists on 3 rounds where both teams switches opponents on each round."
    show camilla l4 r4 b1a e1c n2
    mcf1 "I already have my own Team conformed by the beautiful Camilla and my pal [player]."
    mcf1 "Who wants to challenge us?"
    scene bg fightingclub_clean
    with wipeleft_scene
    "Round 1"
    call fightingclub_day1_battle1
    "Finish!"
    if fightingclub_day1_battle1_victory:
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        show camilla frontal sports l3 r3 mb e1c b1a n1 hair_normal at t22 zorder 2
        c "Yaay~!"
        show camilla at thide
        hide camilla
        pass
    else:
        mc "Fuck!"
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        show camilla frontal sports l4 r4 ma e1c b1c n1 hair_normal at t22 zorder 2
        c "Don't worry [player], we won anyway."
        mc "But..."
        show camilla at thide
        hide camilla
        pass
    pause 3.0
    $ mc_hp = mc_hp_max
    "Round 2"
    call fightingclub_day1_battle2
    "Finish!"
    if fightingclub_day1_battle2_victory:
        mc "Takeshi, please do yourself a favor... Just quit and go home."
        show takeshi at t11 zorder 2
        nbf "Hnng! You win this time!"
        show takeshi at lhide
        hide takeshi
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        "Opponent" "It can't be, they're winning..."
        show ryoma frontal sports l1 r1 b1b e1a mc at t11 zorder 2
        mcf1 "Oh come on guys! What happened to your fighting spirit?"
        mcf1 b1c md "Will you throw your towel in a simple training challenge?"
        mcf1 "Remember: we aren't doing this in a competitive way, we are just training."
        mcf1 b1b mb "Come on! The last round."
        show ryoma at lhide
        hide ryoma
        if fightingclub_day1_battle1_victory:
            show camilla frontal sports l2 r2 ma e1a b1b n3 hair_normal at t22 zorder 2
            mc "Seems like a miracle my 2 wins streak."
            c r3 b1a e1c mb n4 "Nah, you're awesome. That's all..."
            show camilla at thide
            hide camilla
            pass
        else:
            show camilla frontal sports l2 r2 ma e1a b1b n3 hair_normal at t22 zorder 2
            mc "At least I beat that loser of Takeshi..."
            c l3 r3 mb b1a n4 "You're lifting up, that's good [player]..."
            show camilla at thide
            hide camilla
            pass
        pass
    else:
        show takeshi at t11 zorder 2
        nbf "Ahahahaha-! I won!"
        nbf "Bro, you're pathetic... I beated you!"
        mc "Fuck you! You just had luck!"
        show takeshi at lhide
        hide takeshi
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        "Opponent" "It can't be, they're winning..."
        show ryoma frontal sports l1 r1 b1b e1a mc at t11 zorder 2
        mcf1 "Oh come on guys! What happened to your fighting spirit?"
        mcf1 "Will you throw your towel in a simple training challenge?"
        mcf1 "Remember: we aren't doing this in a competitive way, we are just training."
        mcf1 "Come on! The last round."
        show ryoma at lhide
        hide ryoma
        if fightingclub_day1_battle1_victory:
            mc "What the fuck did just happened? I beat that thin guy but I lost against that loser of Takeshi! It's ridiculous!!!"
            pass
        else:
            mc "Once again I'm so fucking useless..."
            pass
        show camilla frontal sports l2 r2 mf e1a b1c n3 hair_normal at t22 zorder 2
        c "Relax [player], everybody has a bad day."
        c l4 r4 ma e1c b1a n4 "And remember, I will never get mad if you're losing, never."
        mc "Thanks Camilla..."
        show camilla at thide
        hide camilla
        pass
    pause 3.0
    $ mc_hp = mc_hp_max
    "Round 3"
    call fightingclub_day1_battle3
    "Finish!"
    if fightingclub_day1_battle3_victory:
        "Flawless victory for Ryoma's Team. Point for Ryoma's Team."
        show ryoma frontal sports l1 r1 ma e1a b1b at t21 zorder 2
        show camilla frontal sports l3 r3 mb e1c b1a n3 hair_normal at t22 zorder 3
        c "Yes~!"
        show camilla at h22
        show ryoma e1c b1e mb sp_sweat
        c "We{w=0.5} are{w=0.5} the winners!{w=0.5} We{w=0.5} are{w=0.5} the winners!"
        show camilla mc at t22 zorder 2
        "Camilla is acting euphorically, just like Sayori would do in this kind of situation..."
        "But it's because she's teaming up with me and Ryoma, otherwise she could be acting normal."
        show ryoma mb e1a b1a sp_none at f21 zorder 3
        mcf1 "Well done! Everybody did a good job today."
        show ryoma at t21 zorder 2
        show camilla l1 r1 ma e1a b1b
        "Opponent" "Whatever. All of you kicked our asses so easy."
        if fightingclub_day1_battle1_victory and fightingclub_day1_battle2_victory:
            mc "I did it very well to be my first day. It's a good sign..."
            show camilla n2 b1a e1c at f22 zorder 2
            c "Of course it is..."
            show ryoma md b1a sp_sweat at t41 zorder 1
            show camilla e1c at face(y=600) with dissolve
            "She suddently hugs me."
            c "I knew you will do it amazing~!"
            mc "Hehehe, thanks Camilla..."
            show camilla at t11
            pass
        elif fightingclub_day1_battle1_victory and not fightingclub_day1_battle2_victory:
            mc "I can't believe I've lost against Takeshi... Fucking bullshit!"
            show camilla at f22 zorder 3
            c "Calm down [player], it's not the end of the world."
            "She pats my head."
            show camilla at t22
            pass
        elif not fightingclub_day1_battle1_victory and fightingclub_day1_battle2_victory:
            mc "I started with the wrong foot. At least I did it better in the last two matches."
            show camilla at f22 zorder 3
            c "Yeah, but it's normal... Nobody is so perfect to do everything good."
            mc "Yeah, you're right..."
            "She pats my head."
            show camilla at t22
            pass
        else:
            mc "Finally! My first fucking victory!"
            mc "But it's still a bit shameful from my part."
            show camilla at f22 zorder 3
            c "Don't worry [player], at least you beated the strongest one... I think you was mercyful to the others."
            show camilla at t22
            mc "No... That's not."
            pass
        pass
    else:
        "Ryoma's Team 2 - Opponents Team 1. Point for Ryoma's Team."
        show ryoma at t21 zorder 2
        show camilla at f22 zorder 3
        c "Yes~!"
        show camilla at h22
        c "We{w=0.5} are{w=0.5} invictus!{w=0.5} We{w=0.5} are{w=0.5} invictus!"
        show camilla at t22 zorder 2
        "Camilla is acting euphorically, just like Sayori would do in this kind of situation..."
        "But it's because she's teaming up with me and Ryoma, otherwise she could be acting normal."
        show ryoma at f21 zorder 3
        mcf1 "Well done! Everybody did a good job today."
        show ryoma at t21 zorder 2
        "Opponent" "Whatever. All of you kicked our asses so easy."
        if fightingclub_day1_battle1_victory and fightingclub_day1_battle2_victory:
            mc "I guess that big guy was enough for me..."
            mc "Sorry guys, I ruined a nice invict."
            show camilla at f22 zorder 3
            c "Don't worry about that [player], you did it good anyway."
            mc "Hehe, thank you Camilla..."
            show camilla at t22
            pass
        elif fightingclub_day1_battle1_victory and not fightingclub_day1_battle2_victory:
            mc "What happened? I beated the first one but I wasn't able to beat the others?"
            mc "I feel ridiculous!"
            show camilla at f22 zorder 3
            c "Come on [player], it's not the end of the world..."
            show camilla at t22
            pass
        elif not fightingclub_day1_battle1_victory and fightingclub_day1_battle2_victory:
            mc "Incredible, the only one I manage to beat was that loser of Takeshi..."
            show camilla at f22 zorder 3
            c "Hehe~"
            show camilla at t22
            pass
        else:
            mc "I'm a fucking idiot..."
            mc "I wasn't able to beat anyone of them! Shame on me!"
            c "[player]..."
            show camilla at t22
            mcf1 "I'm so sorry [player]."
            mcf1 "But don't worry, you can have a rematch tomorrow."
            show camilla at t22
            mc "... ... ..."
            pass
        pass
    scene bg fightingclub_clean with wipeleft_scene
    stop ambient
    play music t5 fadeout 1.0
    show ryoma frontal sports l1 r1 mb e1a b1a at f21 zorder 2
    show camilla frontal sports l2 r2 ma e1a b1b n1 hair_normal at t22 zorder 3
    mcf1 "Okay, everyone!"
    mcf1 "We're done for our activities today."
    mcf1 e1c ma "I hope all of you enjoyed this moment."
    if not fightingclub_day1_battle1_victory and not fightingclub_day1_battle2_victory and not fightingclub_day1_battle3_victory:
        show ryoma e1a b1b mc at t21 zorder 2
        show camilla l1 r1 mh n3 e1c
        mc "... ... ..."
        show camilla me at f22 zorder 3
        c "[player]..."
        show camilla mf at t22 zorder 2
        mcf1 "..."
        show ryoma at f21 zorder 3
        mcf1 "Anyway."
    mcf1 "If everyone are interested on keep going at this hour, you're all welcome."
    if chapter == 3:
        mcf1 "But before we leave, I have an announcement to do:"
        mcf1 "At the festival we will organize a big Tournament."
        "Heh! What a shame I can't participate due to the Literature Club..."
        mcf1 "We'll bring the Champion a nice prize."
        mcf1 "I'm talking about $5000."
        "Wow! With that money I could buy the Car Thief 5 game!!!"
    mcf1 "Well, that's all for today."
    if chapter != 3:
        mcf1 e1a b1a mb "Alright. See you tomorrow then."
    else:
        mcf1 e1a b1a mb "Thank you for come in, and I'll see you in Monday!"
    "Everyone" "Yes sensei!"
    "..."
    if fightingclub_day1_battle1_victory and fightingclub_day1_battle2_victory and fightingclub_day1_battle3_victory:
        show ryoma ma e1c
        mcf1 "[player], you did it excellent! I knew it was a good idea inviting you."
        show ryoma at t21 zorder 2
        show camilla l3 mb e1c b1a at f22 zorder 3
        c "He's right. You're great [player]!"
        mc "Thanks guys...!"
        c r2 mc e1d b1d "Together, nobody will dare to stop us!"
        show camilla at t22 zorder 2
        show ryoma e1a b1b mb at f21 zorder 3
        mcf1 "Well said Camilla."
        show ryoma ma at t21 zorder 2
        "I'm so lucky having them has friends..."
        pass
    elif not fightingclub_day1_battle1_victory and not fightingclub_day1_battle2_victory and not fightingclub_day1_battle3_victory:
        mc "I'm a disaster Ryoma. I don't know why you bothered to invite me..."
        show ryoma at f21 zorder 3
        mcf1 "Oh, come on [player]! Nobody starts winning everything at the first day."
        show ryoma at t21 zorder 2
        show camilla at f22 zorder 3
        c "Ryoma is right, I have the sense you will do it better for tomorrow."
        c "Please, don't quit..."
        mc "What if I..."
        show camilla at t22 zorder 2
        c "Then I will be sad."
        "How can I say No to that face???"
        mc "Okayyy... Tomorrow I will have my rematch."
        show camilla at f22 zorder 3
        c "Yaay~!"
        show camilla at t22 zorder 2
        pass
    else:
        show ryoma at f21 zorder 3
        mcf1 "Not bad [player], not bad."
        show ryoma at t21 zorder 2
        mc "Are you kidding me? Both of you were invictus and I don't..."
        show camilla at f22 zorder 3
        c "Don't complain about it [player], at least you putted your part there. Something is something, isn't?"
        show camilla at t22 zorder 2
        mc "Well... maybe..."
        show ryoma at f21 zorder 3
        mcf1 "Don't worry, the next time you will do it better, that's for sure."
        show ryoma at t21 zorder 2
        show camilla at f22 zorder 3
        c "Ryoma is right, we trust on you [player]~!"
        show camilla at t22 zorder 2
        mc "Alright... Thanks guys."
        pause 1.0
        pass
    $ mc_hp = mc_hp_max
    $ fightingclub_battle = False
    if chapter != 3:
        mc "Well, see you tomorrow then."
    else:
        mc "Well, see you at Monday then."
    show camilla l1 r1 ma e1c b1a
    show ryoma ma e1c b1a
    "Ryoma & Camilla" "See ya~"
    return

label fightingclub_activities_two:
    mc "So... How shall we start today?"
    mcf1 "Hmm... Let's see..."
    mcf1 "Well, first we can start with warming up excercises."
    mcf1 "And then I can make an activity where you should pick a group of 3 opponents to battle."
    mcf1 "Do you like it?"
    c "I like it!"
    mc "Me too!"
    mcf1 "Alright then."
    mcf1 "Let's get moving!"
    scene bg fightingclub_clean with wipeleft_scene
    "1 hour later..."
    show ryoma frontal sports l1 r1 mb e1a b1a at t11 zorder 2
    mcf1 "Okay, everyone!"
    "*clap!* *clap!*"
    show ryoma at t21
    show camilla frontal sports l2 r2 ma e1a b1b n3 hair_normal at t22 zorder 3
    "Jeez! I'm exhausted!"
    "But unlike me and the others, Camilla seems to be fine."
    "How does she have such resistance?"
    mcf1 "Alright!"
    mcf1 "Now it's time of a new activity."
    mcf1 "[player], you should pick one of the 3 groups I'm about to show you."
    mcf1 "One of them is easier than the other."
    mcf1 "Remember that the harder group you pick, the best EXP you will earn."
    mc "Okay!"
    menu:
        mc "Let's see..."

        "Easy":
            mcf1 "As you wish..."
            $ fightingclub_act2 = "easy"
            pass
        "Medium":
            mcf1 "Good!"
            $ fightingclub_act2 = "normal"
            pass
        "Hard":
            mcf1 "Daring today, aren't we?"
            $ fightingclub_act2 = "hard"
            pass
    c "Good luck, [player]!"
    c "I'll be cheering for you~!"
    mc "Thanks Camilla, I appreciate that!"
    c "Ehehe~"
    show ryoma at thide
    hide ryoma
    show camilla at thide
    hide camilla
    pause 2.0
    $ nextbattle = "fightingclub_day2_" + fightingclub_act2 + "_battle1"
    call expression nextbattle
    "Finish!"
    if fightingclub_day2_battle1_victory:
        "[player] WINS!"
        mc "Great!"
    if not fightingclub_day2_battle1_victory:
        "Opponent WINS!"
        mc "Shit..."
    $ nextbattle = "fightingclub_day2_" + fightingclub_act2 + "_battle2"
    call expression nextbattle
    if fightingclub_day2_battle2_victory:
        "[player] WINS!"
        mc "Nice!"
    if not fightingclub_day2_battle2_victory:
        "Opponent WINS!"
        mc "Oh, come on!"
    $ nextbattle = "fightingclub_day2_" + fightingclub_act2 + "_battle3"
    call expression nextbattle
    if fightingclub_day2_battle3_victory:
        "[player] WINS!"
        mc "Fuck yeah!"
    if not fightingclub_day2_battle3_victory:
        "Opponent WINS!"
        mc "Fucking damn it!!"
    stop ambient
    mcf1 "Alright! That's enough for today!"
    mcf1 "But before we leave, I have an announcement to do:"
    if chapter != 3:
        mcf1 "Tomorrow we'll start a pre-festival Tournament."
        mc "What?!"
        c "Yaaay~!"
        mcf1 "With that we hope more people gets interested on our club, because this Monday we'll start the Real Tournament."
        "Heh! What a shame I can't participate due to the Literature Club..."
        mcf1 "Just like at Monday, tomorrow we'll bring the Champion a nice prize."
    else:
        mcf1 "At the festival we will organize a big Tournament."
        "Heh! What a shame I can't participate due to the Literature Club..."
        mcf1 "We'll bring the Champion a nice prize."
    mcf1 "I'm talking about $5000."
    "Wow! With that money I could buy the Car Thief 5 game!!!"
    mcf1 "Well, that's all for today."
    if chapter != 3:
        mcf1 "Thank you for coming back, and I'll see you tomorrow!"
    else:
        mcf1 "Thank you for coming back, and I'll see you in Monday!"
    "Everyone" "Yes sensei!"
    mc "$5000..."
    c "Yeah, right?"
    c "It's a good amount of money."
    mc "Yeah..."
    $ mc_hp = mc_hp_max
    $ fightingclub_battle = False
    if chapter != 3:
        mc "Well, see you tomorrow then."
    else:
        mc "Well, see you at Monday then."
    show camilla l1 r1 ma e1c b1a
    show ryoma ma e1c b1a
    "Ryoma & Camilla" "See ya~"
    return

label fightingclub_activities_three:
    mcf1 "Alright! I hope you guys are ready...!"
    "Oh shit, I almost forgot today is the day..."
    mcf1 "Everyone!"
    "*clap!* *clap!*"
    mcf1 "Is everybody ready for the pre-festival Tournament?"
    "Everyone" "Yes sensei!"
    mcf1 "Alright!{w} I stuck a poster on the wall with the fixture. You must check it to see who'll be your rivals..."
    mc "Uh, let's see..."
    $ quick_menu = False
    play sound page_turn
    show fightingclub_fixture_1 with Dissolve(1)
    pause 5.0
    hide fightingclub_fixture_1 with Dissolve(1)
    $ quick_menu = True
    "Wow! Will I really fight against Takeshi at first round? LOL"
    mcf1 "Impressed?"
    mc "Ah-!"
    mcf1 "I made it on purpose, I know Takeshi is a weak dude, that's why I make you fight him first."
    menu:
        mc "I can't believe this Ryoma..."

        "You shouldn't had do that!":
            pass
        "Do you think I'm so fucking weak?":
            pass
    mcf1 "Eh?"
    mcf1 "Come on [player]..."
    mcf1 "Do you really wanted a tough opponent on first round? Because those guys aren't easy than you though..."
    mc "Aahhh......."
    c "Ryoma is right [player]."
    c "In fact, if they're a sort of difficult, then you can have some advantage with the stamina. You will not spend to much with that Takeshi dude, isn't?"
    mc "Of course not. But..."
    mc "... ... ..."
    mc "Nevermind. I'll accept the challenge!"
    mcf1 "Well said!"
    c "Yaay~!"
    mc "Hmm... Hold on a second..."
    mc "I'm surprised that Camilla isn't participating here..."
    mcf1 "Yeah, well... This club is already full of tough mens, so I think it was unfair that a girl like Camilla participate."
    c "And... I'll confess that I was upset about Ryoma's decision of discard me."
    c "But then I said myself: I can cheer for [player] during the Tournament since he's participating, so I took it easy."
    mc "Nice then, Camilla."
    mc "I would love to have a cheerleader."
    mc "It's a shame that Sayori is currently... you know..."
    "... ... ..."
    "From smiles and cheering, everything became deep silence when I mentioned Sayori... Seriously, what the fuck is happening in this world?"
    hide ryoma
    hide camilla
    with wipeleft
    stop ambient
    "Ryoma organizes the correspondent groups fighters to start the round of 16."
    mcf1 "Alright!"
    mcf1 "Our first battle is between [player] and this guy..."
    call fightingclub_day3_battle1
    if fightingclub_day3_battle1_victory:
        "Finish!"
        "[player] WINS!"
        mc "Piece of cake!"
        c "Good job~!"
    if not fightingclub_day3_battle1_victory:
        jump fightingclub_day3_loser
    "Now it's turn of the quarter finals."
    call fightingclub_day3_battle2
    if fightingclub_day3_battle2_victory:
        "Finish!"
        "[player] WINS!"
        mc "Cool!"
        c "Well done~!!"
    if not fightingclub_day3_battle2_victory:
        jump fightingclub_day3_loser
    "Now the semifinals."
    call fightingclub_day3_battle3
    if fightingclub_day3_battle3_victory:
        "Finish!"
        "[player] WINS!"
        mc "Yes!!!"
        c "That's my [player]~!!"
    if not fightingclub_day3_battle3_victory:
        jump fightingclub_day3_loser
    "It's the time for the Finals."
    "Funnily enough, my opponent is Ryoma..."
    call fightingclub_day3_battle4
    if fightingclub_day3_battle4_victory:
        "Finish!"
        "[player] WINS!"
        mc "Oh my god..."
        c "Woohoo~~!!!"
        mcf1 "Heh! Congratulations [player]."
        mcf1 "You are our new Champion!"
        mc "Thanks Ryoma."
    if not fightingclub_day3_battle4_victory:
        "Finish!"
        "Ryoma WINS!"
        mc "gg"
        mcf1 "What?"
        mc "I mean, \"Good Game\"."
    "Today was the last Mixed Martial Arts Club activity."
    "Being honest, it was pretty fun."
    $ mc_hp = mc_hp_max
    $ fightingclub_battle = False
    mc "Well, see you at Monday then."
    show camilla l1 r1 ma e1c b1a
    show ryoma ma e1c b1a
    "Ryoma & Camilla" "See ya~"
    return

    label fightingclub_day3_loser:
        "Finish!"
        "[enemy] WINS!"
        mc "WHAT THE--??!!"
        c "[player]..."
        mcf1 "Camilla, please, take him away before he loses his mind..."
        c "S-sure."
        mc "I can't..."
        mc "I can't believe it!!!!"
        c "[player], chill..."
        c "It's okay."
        c "It's not the apocalypse because you was defeated."
        mc "(...)"
        c "Listen, if you don't feel good, I can take you to your home."
        c "Or, we can go eat something, as you wish..."
        mc "Camilla..."
        c "Come here~"
    return
