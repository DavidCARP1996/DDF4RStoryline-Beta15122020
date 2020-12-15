label camilla_exclusive_1:
    scene bg club_day
    with wipeleft_scene
    "Man..."
    "It looks like no one wants to be bothered today."
    "I want to read the book that Yuri gave me."
    "But at the same time, I want to take some breath outside."
    "... ... ..."
    "Suddently I look at my poem."
    "Honestly, I don't know if some of the girls would like it."
    "What if I dissapoint Yuri? What if Monika confirms that I am pathetic with my poem? What if Natsuki...?"
    "Hey!{w} I have an idea!"
    "I can go find {i}somebody{/i} who can rate my poem and see if it's good or bad for real."
    "I...I wonder if somebody will notice my ausence if I go out for a while..."
    "I grab my poem and save it inside the Yuri's book. I'll leave my bag here so nobody would think I want to leave the club."
    show yuri 2e at t11 zorder 2
    mc "!"
    "Yuri is peeking on me."
    show yuri 3n at h11
    "Oh-oh! She noticed I'm seeing her..."
    show yuri 3o at t11
    "I guess I need to tell her I'll read her book outside or something."
    mc "Yu...Yuri...?"
    show yuri 3n at h11
    y "Ah-!"
    y 4d "[player], I'm so sorry... I..."
    show yuri 4c at t11
    mc "No... I mean... D-Don't worry Yuri..."
    mc "I-I was about to tell you I'm going to read your book at the backyard."
    show yuri 4a
    mc "I-I hope it doesn't bother you..."
    y 1g "Well... um... In that case..."
    y 2f "It's not a bad idea, I think..."
    if persistent.clear[2] == True:
        "I would love to read it with you like in another timeline, but seriously I need to go out..."
    show yuri 1a
    mc "Thank you Yuri!"
    y "It's nothing..."
    y 1b "In fact, I'm so glad you got interested in the book..."
    y 3d "P-please, tell me later what are your thoughts about it no matter how long you reached~"
    mc "I will... Thanks again!"
    show yuri at thide zorder 1
    hide yuri
    "Well, it's time to go--"
    show natsuki 5b at t11 zorder 2
    n "Hey!"
    n "Where you think are you going?"
    menu:
        "Oh, shit..."

        "I want to buy something and I'll be back soon.":
            n 5c "Okay, but get hurry, okay?"
            mc "Sure..."
            pass
        "I'll go to the bathroom.":
            n "Then why are you carrying that book with you?!"
            show natsuki 5g
            mc "I want to read it while I'm..."
            mc "Uh... Why do you care anyway? Just let me go, please!"
            n 5w "Hush! Okay, but get hurry, okay?"
            pass
        "It doesn't bother you.":
            n 1o "Uuuuuuu-!"
            n 1p "I would punch you in your stupid face if weren't because Monika is here!"
            n 5x "Now, go anywhere you want to go before I change of mind..."
            pass
    show natsuki at thide zorder 1
    hide natsuki
    "It worked..."
    "Now let's----"
    show monika 5a at t11 zorder 2
    m "[player], where you think are you going?"
    menu:
        mc "Aahhh...!"

        "I want to buy something and I'll be back soon.":
            m "Can I go with you?"
            mc "No. Sorry but I want to go alone."
            m 1o "Um... Okay..."
            m 3b "Just get hurry because we'll share our poems soon, okay?"
            mc "Sure thing, Monika."
            pass
        "It's not of your business Monika...":
            m 5b "Hey! I'm trying to be nice with you and you treat me like that?"
            mc "Hehe, sorry. I got carried away..."
            m 1m "Um... Okay, no problem..."
            m 3b "Just get hurry because we'll share our poems soon, okay?"
            mc "Sure thing, Monika."
            pass
        #"Why the fuck do you care?!":
            #m 1s "What did you said to me?"
            #mc "Look, just leave me alone, okay?"
            #m 2i "And what if I don't?"
            #mc "Then..."
            #show monika 5c
            #show monika at lhide zorder 1
            #hide monika
            #"I push Monika away."
            #"My god! What a intrusive person!"
            #"I would NEVER be happy with a girl like that!"
            #"{b}NEVER--!!!{/b}"
            #pass
    stop music fadeout 1.0
    scene bg corridor
    with wipeleft_scene
    mc "Phew..."
    "It's curious that Sayori seems like she didn't care if I go out..."
    "???" "[player]-!"
    mc "Ah----!"
    play music t6 fadeout 1.0
    show sayori 1j at t11 zorder 2
    s "Where you think are you going?"
    s 4j "I brought you to the club so you can became friends with everyone but you're just leaving!"
    s 4i "You dummy-!!"
    mc "Sayori, first of all: it's not what you're thinking."
    mc "Second: I was just about to buy something and I'll be back soon."
    s 3c "You mean something to eat?"
    mc "Well...yes!"
    s 3x "Can I go? Please, please, please?!"
    mc "Sorry, but I want to go alone..."
    show sayori 5d at s11
    s "Uhhh..."
    mc "Don't worry, I'll buy a snack for you. I promise!"
    show sayori 1b at t11
    s "Hmm...okay!"
    s 1a "Just don't forget about your promise, alright?"
    mc "Sure..."
    show sayori at thide
    hide sayori
    "Anyway, let's go to the entrance."
    "At this hour I would meet her at the exit instead of her classroom."
    scene bg school_entrance
    with wipeleft_scene
    mc "Here I am."
    "The entrance is too crowded, it would be hard to find her..."
    "Girl" "[player]?!"
    mc "Ah-!"
    show camilla frontal uniform l1 r1 n1 mb e1a b1a hair_normal at t11 zorder 2
    c "What are you doing here? Aren't you supposed to be in the literature club now?"
    show camilla ma
    mc "Yeah but... I need your help."
    mc "I hope I'm not bothering you..."
    c r2 b1c "No! Of course you're not bothering me."
    c l3 e1d b1a "In fact, I would love to help you~!"
    c l1 r1 e1a mb "So... Tell me, what's the matter?"
    show camilla b1b ma
    mc "Well, the thing is..."
    mc "Monika gave to us an activity where we have to write a poem for today."
    mc "But I'm not sure if mine is okay..."
    c b1a md e1j "Wow! A poem?"
    c l5 r5 mb "Here, give it to me. I am delighted to read it~"
    mc "S-sure..."
    show camilla e1c n2
    "... ... ..."
    c l1 r1 me e1a b1b "Oh...!"
    c mb b1a "Nice!"
    c e1j "[player], your poem is great!"
    c ma "Are you sure it's your first time?"
    mc "Yes, it is..."
    mc "But please, be honest! This poem is the proof to everyone in the club that I worth."
    c r2 e1a b1c "Hehe~! Don't say such thing, sweety..."
    c "Of course you worth, a lot!"
    mc "..."
    c r1 me n1 b1a "Listen, if your poem where sooo bad, then I wouldn't have been so excited reading it."
    c l4 r4 b1c "I'm always honest with you [player]. Please, take me seriously..."
    mc "I will... I'm so sorry Camilla. I didn't pretended to make you feel bad..."
    c l1 r1 ma e1c "Don't worry, darling..."
    "She pats my head."
    c mb e1a b1b "Hey! Before I leave..."
    c e1d "Do you want to eat some ice cream with me?"
    mc "Of course! Let's go..."
    c ma n2 e1c "Thank you~!"
    scene bg school_backyard
    with wipeleft_scene
    "Camilla and I went to the school's closest ice cream shop."
    "We picked our flavors and then get back to the school before the prefects notice I was out."
    show camilla frontal uniform l1 r1 n1 ma e1c b1a hair_normal at t11 zorder 2
    #$ persistent.clear[x] = True
    #scene c_cg1_base with dissolve_cg
    c "Hmm~! Yummy!"
    c mb "Dude! I love those ice creams!"
    mc "Me too... It's awesome that we have such amazing ice cream shop so close to us..."
    c "Yeah!"
    "A few second passes, until..."
    #show c_cg1_exp1 at cgfade
    c e1a me b1b "Hey, I have an question about that book you've been holding all this time..."
    mc "Ah-! Well..."
    mc "Yuri, one of my clubmates gifted it to me as an welcome present."
    c l4 r4 ma n2 b1c "That sounds very lovely... Maybe she has some interests on you~ Hehehe!"
    show camilla e1c
    mc "C-C-Camilla...!"
    "I-I hope she's right... But that doesn't stop me from blushing coming from her..."
    c l5 r5 mb e1a b1a "May I read it a bit? Don't worry. I'll be careful~"
    mc "S-Sure..."
    c l1 r1 n1 ma "... ... ..."
    c mg b1b "... ... ..."
    mc "... ... ...?"
    mc "There's something wrong?"
    c ml b1c e1j n2 "Ah--!"
    c mb n4 "Umm...well..."
    c r2 ma e1a b1b n1 "The story seems a bit complex, even it has a sort of plot twist, if we can call it like that..."
    c b1c n3 "I mean, the story started nice. But after that everything start to become \"darker\"..."
    mc "With what little I saw of that book, I can confirm you're right."
    c b1a mb n1 "The plot looks interesting tho. But I guess if I read more further, then I'll think it won't be such of my interests. That's all what can I say."
    mc "I see..."
    mc "Anyway, thanks for the feedback."
    c r1 ma e1c b1a "Don't mention it~!"
    scene bg school_backyard
    show camilla frontal uniform l1 r1 n1 ma e1c b1a hair_normal at i11 zorder 2
    with dissolve_cg
    "..."
    "We finish our ice cream pots."
    c mb "Aaaah..."
    c mc "Delicious!"
    mc "Indeed."
    c ma e1a b1c "Well, I guess it's time to go."
    c "I'm so sorry..."
    mc "Don't worry Camilla."
    show camilla md e1j n2
    "I pat her shoulder"
    mc "Thank you for such fun time..."
    "I smile at her."
    c ma b1c "[player]..."
    show camilla e1b at face(y=600) with dissolve
    "Then she hugs me."
    c mf e1l b1a "..."
    show camilla l4 r4 mb e1c b1c at t11 zorder 2
    c "Oops! I guess I let myself drive by the emotion, hehe~"
    mc "Hehe... No problem, it was nice anyway."
    c ma e1a b1a "Well, good luck with the poem!"
    c l6 r1 mc e1d "I hope everyone loves it~!"
    mc "I hope that too..."
    c l1 ma e1a "Okay, see you later darling~"
    mc "See ya Camilla~!"
    show camilla at thide
    hide camilla
    pause 2.0
    show camilla frontal uniform l1 r1 n3 mf e1a b1c hair_normal at t11
    c "D'oh! I forgot something..."
    "Camilla reaches into her bag and pulls out some candies."
    c l4 r4 n2 ma b1b "I received some heart-shaped chocolates as a change when I bought the groceries this morning, and..."
    c "I want to give you one~"
    c e1c "Actually, I'll give you two. So you can share the other with anyone you think deserve it."
    c mc b1a "And don't worry about me, I already ate like 6 of them in class, ahaha..."
    "Right! I promised Sayori I'll bought something for her... Camilla saved my life!"
    mc "Camilla...{w} Thank you very much!"
    "I pull the candies to my chest just like an excited girl does, and suddently a smile is drawn in my face."
    c l1 r1 ma e1a b1c "Hehe... You're so cute~!"
    "That sounded nice... But I wonder if Camilla understands the real context of my reaction. *internal giggles*"
    c l3 r2 mb n1 e1d b1d "Alright tiger! Now it's time to show everyone in the club your poem and proof them of what are you done!"
    mc "I will! Thanks again Camilla..."
    c l4 r4 ma e1c b1a "If you want, tell me later how it went..."
    mc "Sure, no problem."
    c l1 r1 e1a "Good luck... And see you later~!"
    mc "See ya~!"
    show camilla at lhide zorder 1
    hide camilla
    "She starts to sprint straight to the entrance."
    stop music fadeout 1.0
    "... ... ..."
    "I grab my poem and look at it, getting some motivation from Camilla's feedback about it."
    mc "Alright!"
    "I stand and go forward to the literature club."
    scene bg corridor
    with wipeleft_scene
    "I save my poem into the page where Camilla stopped reading, so Yuri would think I really read her book."
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 2x at t11 zorder 2
    s "[player], finally you came back!!"
    mc "Yeah, and look, this is for you."
    show sayori 1n
    "I give one of the candies to Sayori."
    s 4s "Aww~!"
    s 2s "Thank you very much [player]~!"
    show sayori 2b at t21
    show natsuki 5e at f22 zorder 3
    n "You took longer than expected! Tell us the truth, what have you done all this time?!"
    show sayori at t31 zorder 2
    show natsuki at t32 zorder 2
    show yuri 2l at f44 zorder 3
    y "Natsuki, please, don't be so rude at him."
    show yuri 1v at t44 zorder 2
    show natsuki 4e at f43 zorder 3
    n "Oh, come on!"
    n 5y "I bet you're defending him because he took your book to read it outside!"
    n 1e "Unless you ve been doing {i}something different{/i} and didn't even read it..."
    show natsuki at t43 zorder 2
    show sayori at t41 zorder 2
    show monika 4d at f42 zorder 3
    m "Natsuki, let me solve this situation, please."
    m 2b "You girls go to grab your poems because it's almost time to share our poems."
    m "Let me handle [player]'s situation~"
    show monika 1a
    mc "Uhh... okay?"
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show monika at t21 zorder 2
    "Everyone returns to their respective stuffs, it's only Monika and me now."
    "I wonder what she wants..."
    m "Phew!"
    return

label camilla_exclusive_2:
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "Well, today I feel more confident about my poem..."
    "But I need to go outside anyway."
    "Camilla told me that if I want to spend some free time afterschool, we can encounter in the entrance again."
    "This time, I told Sayori about that during lunch. Fortunatelly, she agreed."
    "However, Monika and the others doesn't know about that yet. I don't know what would they think if I'll always go outside before poem sharing time."
    mc "Sayori..."
    show sayori 1a at t11 zorder 2
    s "What's happening [player]?"
    mc "Listen, do me a favor and invent an excuse about my ausence to the girls."
    mc "I will meet Camilla now."
    s 2x "S-Sure! Don't worry, I will tell them a good excuse."
    mc "Thanks Sayori... I promise I will give you an cookies pack now."
    show sayori 4s at h11
    s "Yaay~!"
    show sayori at thide zorder 1
    hide sayori
    "Alright, everyone is distracted, so now I can go free and trust Sayori."
    scene bg school_entrance
    with wipeleft_scene
    show camilla frontal uniform l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
    c "[player]~!"
    show camilla e1c
    mc "Camilla~!"
    "We greetly saludate each other."
    mc "Soo... What's your plans for today's date?"
    c "Umm..."
    c "Ah-! I don't know..."
    c "All what I know is that you can't go too far because you have to come back to your club in a few minutes."
    mc "Oh.....That's right..."
    menu:
        mc "Well, I guess we can..."

        #"...go to the roof.":
            #c "Do you want to see the city's landscape?"
            #mc "Yeah, why not?"
            #c "Good then, let's go~!"
            #scene bg school_roof
            #with wipeleft_scene
            #"And then, Camilla and I went to the school's roof."
            #"It's a nice view here, and the wind is so refreshing..."
            #"It was a good idea after all, it's hot today so a fresh wind is perfect."
            #show camilla frontal uniform l1 r1 n1 mb e1a b1a hair_normal at t11 zorder 2
            #c "Aaaahh...! Fresh air..."
            #mc "Indeed. It's a nice place I gotta say."
            #c "You're right..."
            #"..."
            #mc "And... such a nice view."
            #c "Yeah, right?"
            #$ persistent.clear[x] = True
            #scene c_cg2a_base with dissolve_cg
            #pass
        "...go to Downtown.":
            c "Are you sure?"
            mc "Why not? It's just a little walk and it's not so far..."
            c "Well..."
            c "Good then, let's go~!"
            scene bg downtown_day
            with wipeleft_scene
            "And then, Camilla and I went to take a walk in Downtown."
            "Today it's a beautiful day to do such thing..."
            "Camilla and I already passed above some stores, but now we are in front of an cafeteria."
            show camilla frontal uniform l1 r1 n1 ma e1a b1a hair_normal at t11 zorder 2
            mc "What's up Camilla? Are you hungry?"
            c "Eh--"
            c "No... I mean, umm..."
            mc "Listen, don't worry about my time, if you want to eat something let's get in then."
            c "But your club..."
            mc "Ehehe... I said {i}don't worry{/i} Camilla."
            mc "In fact, we can order something quick, we don't need to wait for something big to enjoy some delicious food there..."
            c "Ehm..."
            c "Okay then. Let's go~!"
            mc "Hehe~ You're welcome."
            scene bg cafe
            with wipeleft_scene
            "Fortunately for us, this place is not crowded at this hour. So Camilla and I asked just an orange juice with three croissants each other."
            "We've been doing this a lot of times, but this time seems to be more \"special\"."
            #$ persistent.clear[x] = True
            scene c_cg2b_base
            show camilla frontal uniform l1 r1 n1 ma e1a b1a hair_normal at sitfront zorder 2
            show c_cg_2b_table1 zorder 3
            with dissolve_cg
            "For some reason, she seems to be more {i}cutier{/i} than before."
            "I wonder if she..."
            c "Hey, [player]."
            c "Can I read your today's poem?"
            mc "Sure, here-"
            mc "Oh, fuck."
            c "What's the matter?"
            mc "I left it in my bag at the club."
            mc "I'm so sorry."
            c "Don't worry darling, I can read it afterschool, you know."
            c "You can encounter me at the Ryoma's mixed martial arts club once you exit the school."
            if fightingclub_activities >= 1:
                "That's right, I almost forgot that she's in Ryoma's mixed martial arts club too."
                mc "That's right. Then I will show you the poem there."
            else:
                "So, she's in the mixed martial arts club as well?"
                "Wow! I guess I have a real purposal to sign in now."
                mc "Well, I wasn't interested in another club but..."
                mc "I think I'm about to sign in there, not only to show you my poem, but I'm pretty interested on practice some fighting skills with you at my side."
                c "Aww~~!!"
                c "You're such a sweetheart, you know that?"
                mc "Ehehe... Yes, I guess..."
            c "I will be very glad to read your new poem~!"
            mc "Me too Camilla."
            show c_cg_2b_table2 zorder 3
            with dissolve_cg
            "The food arrived pretty quick."
            mc "Okay then, let's eat~!"
            c "Yeah~!"
            scene black
            with dissolve_scene_full
            pause 1.0
            scene bg cafe
            with dissolve_scene_full
            show camilla frontal uniform l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
            "Camilla and I finished our food, payed the bill and we are ready to go."
            c "Alright then, let's go back to the school."
            mc "Yeah."
            scene bg downtown_day
            with wipeleft_scene
            show camilla frontal uniform l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
            "Camilla and I are now walking back to the school."
            "But there's something that I always wanted to ask her..."
            "I guess it's the best chance, so let's go."
            stop music fadeout 3.0
            mc "Camilla..."
            c "Yes?"
            mc "Listen, I have question I wanted to ask you..."
            play music t9
            mc "Why are you always so gentile with me?"
            c "E-Eh??"
            pass
        "...go to the soccer field.":
            c "Do you want to play some soccer again?"
            mc "I feel like I need to do it..."
            c "Good then, let's go~!"
            scene bg school_football_field
            with wipeleft_scene
            "And then, Camilla and I went to the school's soccer field."
            "This place give me such memories... Good and bad memories..."
            "But it's not time to think about it. Let's have some fun with Camilla."
            "I just hope that incident doesn't repeat just like with S{nw}"
            show camilla frontal sports l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
            c "I'm baaack~!!"
            c "Eh?"
            c "Are you rambling [player]?"
            mc "Wha-"
            mc "Oh... sorry... I didn't..."
            c "It's okay, just try to forget that."
            mc "Did you know that I was thinking about..."
            c "Of course!"
            c "It's writen in your whole face:{w} You're still remembering that accident of yours."
            c "Listen, if you're not okay to play, then let's do it another time and relax a little with anything else."
            mc "No...no...! It's okay Camilla, I'm fine, really."
            c "Are you sure?"
            mc "Yeah!"
            mc "I brought this ball while I was changing to my gym outfit."
            mc "Let's do some warming up. After that we can play some passes, it's okay?"
            c "Sure~"
            #$ persistent.clear[x] = True
            #scene c_cg2c_base with dissolve_cg
            "And so, Camilla and I are doing warming up exercises like we're doing Gym class."
            "She flexes her body so naturally."
            "It's like she dedicates her life training."
            "That explains why she's so tough, agile, skilled... and healthy."
            c "Well, I'm ready~!"
            mc "Ah..."
            c "Hey! Were you distracted?"
            mc "Me...? Well..."
            mc "Sorry I guess I was...."
            c "Ehehehe~!"
            c "Are you saying that you got distracted looking at me?"
            mc "Well... Yes."
            c "Uhuhu~"
            c "That's okay."
            c "But once we start to play, pay attention to the ball and not to me~"
            "She winks when said that."
            mc "Okay! I will consider that then."
            mc "So, are you ready to play some passes?"
            c "Sure! Go on [player]!"
            scene bg school_football_field
            with dissolve_cg
            "Camilla goes a few meters apart to receive my pass."
            mc "Here we go~!"
            show camilla frontal sports l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
            "I kick the ball."
            c "Here-!"
            "Then she give me a quick pass."
            mc "Go-!"
            "And then we are doing various 1-2 passes until..."
            c "Hah-!"
            stop music fadeout 3.0
            mc "Ouch!"
            "The ball hits directly to my face... it hurted."
            c "Ohmygod!"
            c "[player]...!!!"
            mc "Don't worry... I'm... fine..."
            mc "It was... nothing..."
            mc "See?"
            c "Jesus Christ, I'm so sorry!"
            mc "Hehehe... It's okay Camilla, these things happens."
            "Camila caresses my face."
            play music t9
            c "I'm so sorry. Really."
            mc "That's okay Camilla."
            c "(...)"
            mc "Listen, you don't need to be very gentile to me."
            c "Why??"
            pass

    c "There's... something wrong with that?"
    menu:
        mc "Well, there's nothing wrong, but..."

        "...That's not so neccesary.":
            c "But..."
            mc "I'm not saying that's a bad thing, but sometimes..."
            mc "I mean... aah...{w} sometimes it's a bit awkward, you know...?"
            c "I understand what do you mean..."
            c "But I'm not doing this on purpose."
            c "The main reason why I'm treating you like that is..."
            pass
        "...What would people think about it?":
            c "It doesn't matter."
            c "I don't care what people say about our friendship."
            mc "I see..."
            mc "It's a good point tho."
            c "Of course."
            c "..."
            c "But you know..."
            c "The main reason why I'm treating you like that is..."
            pass
        "...I don't deserve it.":
            c "[player]--!"
            c "Don't say such thing never again!"
            mc "But..."
            c "But nothing."
            c "I want to give you the love that..."
            c "That..."
            pass
        "...Nevermind.":
            mc "It's very nice tho."
            c "Of course it is..."
            "I remain silent for a while."
            c "..."
            c "By the way..."
            c "The main reason why I'm treating you like that is..."
            pass
    c "..."
    mc "Camilla... Are you okay?"
    c "I'm fine, thanks."
    "She wipes her tears."
    c "N-Nevermind."
    "Is she hiding me something?"
    "I will keep silent for a while."
    c "Hey!"
    c "Don't forget about your club honey~"
    mc "Ah--!"
    mc "That's true..."
    c "Come on, I will accompany you to the school."
    mc "Sure..."
    scene bg school_backyard
    with wipeleft_scene
    show camilla frontal uniform l1 r1 n1 mb e1j b1a hair_normal at t11 zorder 2
    mc "I... I'm so sorry for asking you such awkward question."
    mc "I never thought that..."
    c "It's okay [player]."
    c "I know it was just for curiosity."
    c "But I shall sorry about my response to that..."
    mc "It's okay Camilla, it was my fault after all."
    mc "But it's okay if you can't say the answer right now, I won't dare to force you..."
    "I pat Camilla's shoulders."
    mc "Let's talk about that once you feel when the time is right. Okay?"
    c "S-Sure..."
    c "Thank you [player]!"
    mc "Ehehe, you're welcome."
    if fightingclub_activities >= 1:
        c "Alright, I'll be waiting for you at the mixed martial arts club."
        mc "Yeah, I'll be there!"
    else:
        c "Alright, I'll see you tomorrow then."
        mc "Yeah."
    c "Good luck with your today's poem~"
    c "Please, tell me later how it went."
    mc "Sure..."
    c "See ya [player]~~!"
    mc "See ya Camilla~~!"
    show camilla at lhide zorder 1
    hide camilla
    "Alright then, that was so much fun for today."
    "Now it's time to face the reality and show everyone in the literature club my poem."
    "Let's go!"
    stop music fadeout 1.0
    scene bg corridor
    with wipeleft_scene
    "Shit, I almost forgot Sayori's cookies!"
    "I went to the closest vending machine to buy the biggest one."
    "Now I'm fucking ready...!"
    play music t6 fadeout 1.0
    show yuri 1a at t11 zorder 2
    y "[player]!"
    y "There you are..."
    mc "Yu-Yuri...?"
    y "The girls where asking about you."
    y "Where did you go this time?"
    mc "What did Sayori told you all?"
    y "Well, umm..."
    y "She said you went to buy some snacks to eat, considering that Natsuki brought two cookies only when we are five people in the club."
    "I knew it."
    "Sayori only thinks about food."
    mc "I see..."
    mc "Well, I'm gonna tell you the truth."
    mc "I wanted to buy some cookies packs out of the school,{w} but in the way I encounter a friend of mine and I..."
    mc "...I forgot to buy the cookies!"
    mc "So now I'm paying for the cookies at this vending machine to waste no more time, the worst of all is these cookies are more expensive than the ones you buy at the market."
    y "I believe in you..."
    mc "Thanks!"
    y "Well, I was worried about your prolongued absence, so I wanted to check if you were at least closer to the club."
    mc "Hehehe... Don't worry about that Yuri."
    mc "Shall we get in then?"
    y "Y-Yeah."
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 2x at t41 zorder 2
    show monika 1a at t42 zorder 2
    show natsuki 1a at t43 zorder 2
    show yuri 1a at t44 zorder 2
    with wipeleft
    n "Well, well, well..."
    n "It seems that we must have you in chains so that you stay here!"
    s "Girls, please no..."
    s "At least he brought the cookies here~!"
    s "Give him another chance, okay?"
    m "I hate to say that Natsuki but... Sayori is right."
    n "What?!"
    m "Despite the fact he's always out of the club at this hour, he didn't did anything bad to deserve such punishment."
    m "I mean, he just wanted to brought some cookies, right?"
    mc "Yeah..."
    n "Uuuuuu-!"
    n "Okay! But [player] must forget about hanging around out of the club the next time."
    mc "I will try... Don't worry about that."
    "I don't want to say I get bored waiting until poems sharing hour, otherwise I would offend them."
    $ camilla_route_complete = True
    return
