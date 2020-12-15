label ch3_main:
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    #with dissolve_scene_half
    play music t3
    show yuri 2v at t21 zorder 2
    show natsuki 2b at f22 zorder 3
    n "Oh, there you are..."
    n "You must pay more attention to Sayori, you know?"
    n "Here, talk to her to make her feel better..."
    show yuri 1f at t32
    show natsuki 1c at t33 zorder 2
    show monika 1g at l31
    m "Aw, man..."
    m "I'm the last one here again!"
    menu:
        "Don't worry, I just walked in too.":
            pass
        "...":
            pass
    show yuri at f32 zorder 3
    y "Were you practicing piano again?"
    show yuri at t32 zorder 2
    show monika at f31 zorder 3
    m 1l "Yeah..."
    m "Ahaha..."
    show monika at t31 zorder 2
    show yuri at f32 zorder 3
    y 1m "You must have a lot of determination."
    y "Starting this club, and now picking up piano..."
    show yuri 1a at t32 zorder 2
    show monika at f31 zorder 3
    m 1a "Well, maybe not determination..."
    m "But I guess passion."
    m "Remember that the club wouldn't be here if it wasn't for all of you."
    m 1b "And I'm super happy that you're all willing to help out for the festival, too!"
    show monika at t31 zorder 2
    menu:
        "Of course!":
            pass
        "Yeah, whatever...":
            pass
        "...":
            pass
    show natsuki 1z at f33 zorder 3
    n "Aaah, I can't wait for the festival!"
    n "It's gonna be great!"
    show natsuki at t33 zorder 2
    show monika at f31 zorder 3
    m 1d "Eh?"
    m "Weren't you complaining about it just yesterday, Natsuki?"
    show monika at t31 zorder 2
    show natsuki 2a at f33 zorder 3
    n "Well, yeah."
    n "I'm not talking about {i}our{/i} part of the festival."
    n 4l "But it's a whole day of school where we get to play and eat all kinds of delicious food!"
    show natsuki at t33 zorder 2
    menu:
        "You sound a bit like Sayori all of a sudden...":
            pass
        "I agree with you, Natsuki...":
            pass
        "...":
            pass
    show natsuki at f33 zorder 3
    n 4a "Monika! Do they usually have fried squid?"
    show natsuki at t33 zorder 2
    show monika 2a at f31 zorder 3
    m "Squid...?"
    m "That's a pretty specific thing to look forward to..."
    show monika at t31 zorder 2
    show natsuki 2k at f33 zorder 3
    n "Oh, come on."
    n "Are you saying you don't like squid?"
    n "You, of all people?"
    show natsuki at t33 zorder 2
    show monika 1d at f31 zorder 3
    m "Eh? I didn't say I don't like it."
    m "Besides, what do you mean by 'you of all people'?"
    show monika at t31 zorder 2
    show natsuki 1d at f33 zorder 3
    n "Because!"
    n "It's right in your name!"
    n 4z "Mon-ika!"
    show yuri 1d
    show natsuki at t33 zorder 2
    mc "*internal gigglings*"
    "It may sound better in japanese but, OMFG this is hilarious!! HAHAHAHAHAHAHAHAHAHA----!!"
    show monika 5b at f31 zorder 3
    m "Eh?!"
    m "That's not how you say my name at all!"
    mc "Oh come on Monika, what a lack of humor sense!"
    m "Also, that joke makes no sense in translation!"
    show monika at t31 zorder 2
    show yuri 1v
    show natsuki at f33 zorder 3
    n 4m "...?"
    show natsuki at t33 zorder 2
    mc "What the fuck..."
    show monika 4l at f31 zorder 3
    m "Ah...never mind!"
    m "Let's just focus on our own event for now, okay?"
    show monika at t31 zorder 2
    show natsuki 2a at f33 zorder 3
    n "Ehehe."
    n "Fine, fine."
    n "Your reactions aren't as fun as [player]'s, Yuri's or Sayori's, anyway."
    show natsuki at t33 zorder 2
    mc "What?!"
    show yuri 2h at f32 zorder 3
    y "Excuse me..."
    show yuri at t32 zorder 2
    mc "Eh... Where is Sayori, anyway...?"
    mc "Oh, there you are."
    hide monika
    hide yuri
    hide natsuki
    with wipeleft
    "Sayori is sitting at a desk in the corner of the room, looking down at nothing."
    "I walk over to her."
    mc "Hey, Sayori."
    show sayori 1k at t11 zorder 2
    "I wave my hand in front of her face."
    s 1n "Eh--?"
    #mc "You're spacing out again."
    mc "Sayori, what in the holy world happened to you this morning?"
    if sayori_wait3 == True:
        mc "I went to your house to pick up you, but nobody was there."
    mc "I tried to contact you by any ways but seems like your phone is off again."
    mc "Also, I didn't saw you in the school everyday. Where did you go?"
    mc "Please, answer me!"
    s "A-Ah..."
    s 4l "Ehehe, sorry..."
    s "Don't mind me."
    s 4y "You can go talk to everyone else."
    mc "Huh...???"
    mc "Is everything alright?"
    s 1h "O-Of course!"
    s "Why wouldn't it be?"
    mc "It just feels like you're a little off..."
    mc "But please, answer my previous question: What happened to you this morning?"
    s "Jeez, you worry too much about me."
    s 4r "I'm fine, see?"
    show sayori at h11
    "Sayori shows me a big smile."
    s 1a "Don't let me distract you from having fun with everyone."
    menu:
        mc "*Sigh*"

        "Are you hiding me something?":
            "..."
            "She keeps ignoring me."
            pass
        "Well...alright.":
            mc "If you say so."
            pass

    "I give up, I won't push her anymore..."
    show sayori at thide zorder 1
    hide sayori
    "I worriedly glance at Sayori before turning back toward everyone else."
    "But the conversation has already dispersed, with everyone back at their usual activities."
    "Maybe I should ask Monika if she's noticed anything about Sayori recently..."
    "Since they've been preparing for the festival, they must be spending a lot of time together."
    "I nerviously approach Monika, who is shuffling through some papers at her desk."
    show monika 2b at t11 zorder 2
    m "[player]! What's up?"
    mc "Hey, this might sound a little strange, but..."
    mc "Have you noticed anything up with Sayori recently?"
    m 1d "Anything up with her...?"
    m "In what way do you mean?"
    mc "Maybe I'm reading into it a little too much, but she seems a bit downcast today..."
    m "Oh? You think so?"
    m "I can't say I've noticed anything about her..."
    "Monika peers across the room at Sayori, who is idly dragging a rubber eraser up and down her desk."
    m "Maybe there is something on her mind..."
    m 2a "But I'm surprised I'm not the one asking you, [player]."
    m "You certainly know her a lot better than I do."
    mc "Yeah, but she's never really like this..."
    mc "She's always talked to me about things that bothered her."
    mc "But this time, when I asked her, she was really dismissive."
    mc "...Sorry, I know it's not your problem!"
    mc "I just wanted to ask if you knew anything, so I'll drop it now..."
    m 1g "No, no..."
    m "It's important to me, too."
    m 1e "I mean, I'm also friends with her..."
    m "And I also care about the well-being of my club members, you know?"
    m 1i "Maybe I'll try talking to her myself..."
    mc "Eh? Are you sure about that...?"
    mc "She seemed like she wanted to be left alone..."
    m "Are you sure?"
    m "Maybe she just has a hard time bringing it up with the person of interest..."
    mc "Person of interest...?"
    mc "What do you mean by that?"
    m 2e "I'm saying that maybe the thing on her mind is you, [player]."
    menu:
        mc "M-M-Me...?"

        "How on Earth would you come to that conclusion?":
            pass
        "...":
            pass
    m 1j "Well..."
    m "I probably shouldn't say too much, but..."
    m 1a "Sayori talks about you more than anything else, you know?"
    mc "I know."
    m "She's been so much happier ever since you've joined the club."
    m "It's like an extra light was turned on inside of her."
    mc "What?!"
    mc "Monika, it makes no fucking sense!"
    mc "Sayori is always like that."
    mc "She's always been full of sunshine."
    mc "But now she is... Well, a bit \"off\"? Honestly, I don't know what's going on with her."
    #mc "It's not any different now than it always has been."
    m 5 "Ehehe."
    m "You're so funny, [player]."
    mc "Funny?!"
    m "Have you thought that maybe you've always seen her as so cheerful..."
    m "...because that's just how she is when she's around you?"
    mc "Ah--"
    m 1n "Ah...I said too much."
    m "I'm sorry...what do I know, anyway?"
    m 1a "I didn't mean to jump to conclusions, so you should just forget about what I said."
    m "I'll try to talk to her, so try not to think about it for now."
    mc "Ah..."
    mc "Alright..."
    "Monika smiles meaningfully."
    "I know she said to forget about it..."
    "But I already know that I won't be able to get her words out of my head."
    "I'm in a deep shock state now."
    show monika at thide zorder 1
    hide monika
    "Monika stands up from her desk and walks across the room to where Sayori is sitting."
    "I watch her kneel down next to Sayori and gently talk to her."
    "But she's keeping her voice so quiet that I can't hear her from here."
    "I sigh and sit myself down."
    "I know Sayori told me not to worry about her, and to have fun with everyone else..."
    "But that's impossible to do when she's behaving like this."
    "Exactly how much do I care about her, that I'm letting this weigh me down so much?"
    "Now it feels like I'm the one behaving out of the ordinary..."
    "But there's nothing I can do besides wait for Monika."

    # Natsuki or Yuri will come up to you depending on whose appeal is higher
    # If tied, the winner of chapter 2 comes up to you
    # If neither won chapter 2, the winner of chapter 1 comes up to you
    # If neither have any appeal, then neither come up to you
    if n_appeal == 0 and y_appeal == 0:
        jump ch3_start_none
    elif n_appeal > 1:
        jump ch3_start_natsuki
    elif y_appeal > 1:
        jump ch3_start_yuri
    elif poemwinner[1] == "natsuki":
        jump ch3_start_natsuki
    elif poemwinner[1] == "yuri":
        jump ch3_start_yuri
    elif poemwinner[0] == "natsuki":
        jump ch3_start_natsuki
    elif poemwinner[0] == "yuri":
        jump ch3_start_yuri
    else:
        jump ch3_start_none

label ch3_start_natsuki:
    play music t6 fadeout 1
    show natsuki 3c at t11 zorder 2
    n "Hey, you."
    mc "Eh?"
    "I look up to see Natsuki next to me."
    n "Are you just gonna sit there and keep staring at nothing?"
    n "There isn't that much time, so..."
    mc "Ah, sorry."
    mc "I didn't mean to make you worry or anything."
    n 1q "I-It's not like I'm worried!"
    n "I was just..."
    "Natsuki glances down at her side."
    "She's holding a volume of manga in her hand."
    mc "That's right..."
    mc "Something just came up for a minute, but we can get started now."
    mc "I won't make you wait any longer."
    n 5n "Jeez..."
    n "Now you're making me feel like a jerk."
    n "If something's bothering you, then you can just tell me to leave you alone, and I will."
    n 5u "I mean..."
    n "Assuming you didn't feel like talking about it or anything..."
    "She practically mumbles that last part."
    mc "Nah...I'm probably making it seem like a bigger deal than it is."
    mc "I've just been thinking about Sayori, that's all."
    n 1p "S-Sayori...?"
    n "Thinking about her...?"
    mc "Yeah, she seems pretty down today."
    mc "But she didn't want to admit it to me."
    mc "So I can't help but wonder if something happened to her."
    n 1q "Oh..."
    "Natsuki exhales."
    n 4w "Well, first of all..."
    n "You should really work on your phrasing!"
    n 4c "But anyway..."
    n "You're her best friend, right?"
    mc "Yeah, I guess so..."
    n "Yeah."
    n 3k "Then in that case, I think you should trust her a little more."
    n "If she needed you, then you would be the first person she would go to, right?"
    mc "Well... I guess that's true."
    n 3c "I mean, some people just have those days."
    n "You can't always avoid it."
    n "If anything, she probably doesn't want you to worry about her because it's not important."
    mc "Yeah, that's kind of what she said to me..."
    mc "Maybe it's not right for me to go against her wishes."
    n 3a "Exactly."
    n "If she needs you to worry about her, then it'll be a lot more obvious."
    mc "Yeah..."
    mc "I should have thought of it that way from the start."
    show natsuki 3q
    "Natsuki fiddles with the book she's holding in her hands."
    n 1q "She..."
    n "She really means a lot to you, doesn't she...?"
    mc "Ah--"
    mc "Don't get the wrong idea or anything...!"
    mc "We've just been friends for a long time."
    mc "It's normal to be worried about your friends."
    mc "I mean, you were worried about me, so--"
    n 4w "I was not!!"
    n "Jeez...if you're fine, then let's hurry and get started already!"
    mc "Yeah, yeah..."

    # If we haven't seen her exclusive yet, play it now
    if not n_exclusivewatched and poemwinner[2] == "natsuki":
        call natsuki_exclusive_2_ch3
    else:
        jump ch3_start_end
    return

label ch3_start_yuri:
    "Why does it feel like I'm being watched...?"
    "I glance around the room."
    show yuri 2t at t11 zorder 2
    "Suddenly, I notice Yuri peering at me from over her book."
    show yuri 4b
    "But she looks away just as quickly with a flustered look on her face."
    "I realize that she won't get anywhere like this."
    "I've never really seen Yuri approach anyone or start a conversation on her own accord."
    "So, I have no choice but to approach her myself."
    "By now, it's a little easier for me to do that."
    "I stand up from my desk and sit in one next to her own."
    play music t6 fadeout 1
    y 2v "..."
    y "I...didn't mean to bother you or anything..."
    mc "Relax, you didn't even do anything."
    y "But..."
    y "I could tell that you wanted to be alone with your thoughts..."
    mc "Alone with my thoughts...?"
    mc "How were you even able to tell that I was thinking like that?"
    y 1t "Well..."
    y "It's something that I do a lot..."
    y "So it wasn't hard for me to spot based on your posture and expression."
    y 3o "N-Not that I was staring or anything...!"
    y "I didn't do anything creepy like that...!"
    mc "In any case, I guess you were right."
    mc "I'm sorry if I caused you any concern."
    y 1s "Don't apologize..."
    y "Your troubles are only the concern of those who willingly share in that concern."
    y "Of course, there are certainly those who find the most comfort in keeping to themselves..."
    y "But if you would prefer to share what's on your mind, then I would be glad to listen."
    mc "Ah, it's really not that big of a deal..."
    mc "I was just feeling a bit uneasy about Sayori."
    y 2t "Sayori...?"
    mc "Yeah...she seems a little off today, but when I asked her about it, she didn't want to admit it to me."
    mc "So I can't help but wonder if something happened to her."
    y 3u "Oh?"
    y "That's quite romantic..."
    mc "Eh...?"
    y 4c "S-Sorry!"
    y "I didn't mean to say something stupid...!"
    mc "It's not that, I just didn't want you to misunderstand."
    mc "Sayori and I have just been friends for a long time, that's all."
    y 2l "Ah...I see..."
    y 2f "Then perhaps it is unusual for her to be dismissive to you about her feelings..."
    mc "Or maybe I'm just reading into it a little too much..."
    y 1u "[player]..."
    y "The world is full of meaning, often hidden deep beneath plain sight."
    y 1s "And there are many untold mysteries behind every person, no matter how well you may know them."
    mc "Ah..."
    mc "So you think that there might be something behind it after all?"
    y 1l "Mm..."
    y "I think that Sayori is a very complex person."
    y 1h "Her mannerisms on the outside don't always match what may be going on inside her head..."
    y "And she may not always know what she wants."
    y "I noticed her strange behavior today, too..."
    y "And I also feel some concern for her."
    y 1f "But in your case, it looked like she was fully occupying your thoughts, wasn't she?"
    mc "Well..."
    mc "I guess that was the case."
    y 3u "Sayori..."
    y "She really...means a lot to you, doesn't she?"
    mc "Ah--I...I guess..."
    mc "But you don't need to put it that way!"
    mc "We're just good friends, that's all..."
    y 2t "..."
    "Yuri suddenly looks deeply into my eyes."
    "Her expression is gentle and curious, as if she was searching for something."
    "Embarrassed, I avert my gaze."
    y 2m "Sometimes..."
    y "A person's mysteries are untold even to themselves."
    y 2a "And you, as someone honest and caring..."
    y "May uncover feelings you weren't aware were in you."
    y 4b "T-That is..."
    y "I think that..."
    y "She would be a very fortunate person..."
    y "To have you...feel that way about her."
    mc "Yuri..."
    mc "You're giving me too much credit."
    mc "I'm a pretty simple guy."
    mc "So I think I'm pretty good at understanding my own feelings."
    mc "I'm not nearly as sophisticated as you."
    y 2t "A-Ah..."
    y "That's not...a compliment, is it?"
    mc "It is what it is."
    mc "Anyway, as long as we're here, why don't we do some reading?"
    y 2s "Well..."
    y "As long as you're okay with it."
    mc "Yeah."
    mc "I should be taking my mind off this whole thing anyway."

    # If we haven't seen her exclusive yet, play it now
    if not y_exclusivewatched and poemwinner[2] == "yuri":
        call yuri_exclusive_2_ch3
    else:
        jump ch3_start_end
    return

label ch3_start_none:
    "I'm still trying to focus on Monika's and Sayori's conversation."
    "But I still can't heard a fucking word about what they're talking about!"
    menu:
        "I don't know what to do right now..."

        "Walk around the school":
            jump ch3_start_alone
            pass
        "Talk with Yuri":
            jump ch3_start_yuri
            pass
        "Talk with Natsuki":
            jump ch3_start_natsuki
            pass
        "Go straight at them":
            jump ch3_start_sayori
            pass

label ch3_start_sayori:
    "... ... ..."
    mc "I can't stand it anymore! I need to know what they're talking about!"
    "I lift from my sit and walk directly to them."
    show sayori 1g at t21 zorder 2
    show monika 1a at t22 zorder 2
    "I'm nearly closer to them."
    "I can almost hear some words..."
    show monika at f22
    m "...you should consider to do that, okay?"
    show monika at t22
    show sayori 1g at f21
    s "..."
    show monika 1c
    s 4b "[player]?!"
    show sayori at t21
    show monika 2d at f22
    m "[player], I told you I will talk with Sayori."
    show monika at t22
    show sayori 3c at f21
    s "Yeah, it's woman business."
    show sayori at t21
    mc "Sayori?! Since when you-"
    show monika 5 at f11
    m "Why don't you better go somewhere else?"
    mc "Hey! She's MY BEST FRIEND, YOU shouldn't..."
    show monika at t22
    show sayori 4j at f21
    s "[player], please! Leave us alone!"
    mc "Sayori..."
    show sayori at t21
    show monika 1a
    "What's wrong with her...?"
    "... ... ..."
    mc "Grrr----!"
    mc "Fine... Fine!"
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    "Without saying another fucking word, I leave them alone."
    jump ch3_start_alone
    return

label ch3_start_alone:
    mc "Alright then!"
    mc "Let's do something else around to waste no time."
    stop music fadeout 6.0
    scene bg corridor
    with wipeleft_scene
    "I still cannot figure out what's the matter..."
    "I never saw Sayori like this before."
    "I'm going to drink some water."
    scene bg school_dining_room
    with wipeleft_scene
    $ HKBShowButtons()
    pause 2.0
    mc "It's weird to see this place so empty..."
    "Hmm..."
    "Monika may start the poem sharing activity in a few minutes."
    menu:
        mc "Where shall I go?"

        "The backyard":
            mc "Good idea!"
            scene bg school_backyard
            with wipeleft_scene
            mc "Aaahh... The Backyard."
            mc "So full of green..."
            pass
        "The roof":
            mc "Good idea!"
            scene bg school_roof
            with wipeleft_scene
            mc "Aaahh... The Roof."
            mc "The wind hitting my face feels so relaxing..."
            pass
        "The entrance":
            mc "Good idea!"
            scene bg school_entrance
            with wipeleft_scene
            mc "Aaahh... The Entrance."
            mc "I wonder if I can go out..."
            pass
    c "[player]?"
    mc "Eh?"
    play music t6
    show camilla frontal uniform l1 r2 e1a b1b ma n1 hair_normal at t11 zorder 2
    mc "C-Camilla... What are you doing here?"
    c mb "I followed you honey."
    c mb b1a "But hey, why aren't you in the Literature Club? What's wrong?"
    c mf "Is Monika giving you problems or something?"
    mc "Well, sort of."
    mc "But the real problem here is Sayori."
    show camilla r1 me
    mc "She is...{w} Well, I don't know what's going on with her."
    c mb "Did you found her?"
    mc "Yeah, but..."
    c l2 r2 b1b "It's good then. Why are you bothering?"
    mc "The thing is, she's not the same Sayori I always knew."
    show camilla l1 r1 me
    mc "She seems to be very sad."
    mc "I tried to ask her what's going on but... She just ignored my questions."
    c mh b1c "Ummm..."
    c r2 me "It's weird."
    c "She is always happy, and she never hides anything to you."
    c mh "Are you sure you didn't said anything bad to her?"
    mc "No. Of course not!"
    c l4 r4 ma e1c "I believe in you, don't worry."
    c e1a me b1b "Do you know something else what can bother her?"
    mc "Let's see..."
    if ch1_winner == "Sayori" and ch2_winner == "Sayori" and ch3_winner == "Sayori":
        mc "I guess I have the answer:{w} She dragged me to the club because she wanted me to spend some time with other girls apart of her. But instead I rathed to keep spending time with Sayori."
    elif ch1_winner != "Sayori" and ch2_winner != "Sayori" and ch3_winner != "Sayori":
        mc "I guess I have the answer:{w} She dragged me to the club because she wanted me to spend some time with other girls apart of her. Since then, we've been very distanced each other."
    else:
        mc "I don't know exactly...{w} I know she dragged me to the club because she wanted me to spend some time with other girls apart of her. But I also spent time with her too."
    c b1a "I see..."
    c l1 r2 mg "Yeah, it's complex to understand such attitude."
    c ma "But don't worry, I will try to help you in any way."
    c l3 mc e1d b1d "Count on me [player], anything what you need, I'll be there for you..."
    mc "Thank you Camilla."
    c l1 r1 ma e1c b1a n2 "Hehe~!"
    pause 1.0
    stop music fadeout 3.0
    show camilla e1j mf n1
    "???" "But look what we've got here?"
    c l2 r2 b1d mi "No way..."
    mc "What the fuck..."
    play music tyrant
    show camilla at t22 zorder 2
    show akuma at t21 zorder 3
    c n3 "akuma, what the hell are you doing here?"
    mbf "Nothing. Why do you care?"
    #if mbf_presentation == False:
    "That asshole is akuma, the most popular boy in the school."
    "He's strong, handsome, but he's also an idiot who skips his classes and a arrogant motherfucker who likes to tease on everybody who doesn't from his circle."
    "He also likes to presume a relationship with Monika, without caring if she's really interested on him or not. But mostly she uses that to kick some butts."
    "Ryoma is his archirival, they're from the same circle, but they aren't compatible each other to become friends."
    "As for myself, we hate each other. We cannot be closer together because one of us will dare to kick the other's ass."
    "And why we hate each other? First, I won his position on the soccer team like 3 years ago... And second, I hate bullies."
    "Camilla hates him too, but it has something to do with me of course..."
        #pass
    #else:
        #pass
    c l1 r1 mj b1e "Scram! You're not welcome!"
    mbf "Hahahahahahaha!"
    mbf "You got guts to say such thing to me, girl."
    mc "You heard her, punk, get out!"
    mbf "Oooooh... The loser has spoken."
    c l3 r3 mi "What's wrong with you? You idiot, leave us alone!"
    mbf "Or what?"
    mbf "Will he dare to punch me in the face?"
    mbf "Hahahahaha! I want to see that..."
    menu:
        "Grrrrr----! I can't stand him anymore!!!"

        "Punch him":
            mc "As you wish..."
            show akuma at t11 zorder 2
            show camilla l1 r1 me b1a at t44
            play sound punch1
            "..."
            mbf "Now you are dead, motherfucker!"
            mc "If you say so..."
            mc "Camilla, get back! I can handle it myself!"
            c b1c "O-okay..."
            pass
        "Kick his balls":
            mc "As you wish..."
            show akuma at t11 zorder 2
            show camilla me b1a at t44
            play sound punch2
            "..."
            c l4 r4 b1a e1c mc n1 "Ouch! Hehehe~"
            mbf "A-A-A....................."
            show camilla l1 r1 me b1e e1j n3
            mbf "YOU WILL PAY FOR THIS!! CONSIDER YOURSELF DEAD!!!"
            mc "Fuck you!"
            mc "Camilla, get back! I can handle it myself!"
            c b1c "O-okay..."
            pass
        "Do nothing":
            mbf "Come on! Come on!"
            c l5 r1 me b1c n3 "[player]..."
            mbf "Alright then..."
            show akuma at t11 zorder 2
            show camilla l1 mj e1l b1a n1 at t44
            call mc_pain2
            mc "AAAaaaaahh--!!!"
            mc "You fucking piece of..."
            c "[player]!!!"
            c l3 r3 mi e1j b1e "DON'T TOUCH HIM YOU BASTARD!!!"
            show camilla at t22 zorder 3
            show akuma at t32
            play sound slap
            mbf "Aah-!"
            show akuma at t11
            show camilla n3 at t33 zorder 2
            mbf "I see... You want some too?"
            stop music
            show camilla e1l b1c mi at t44
            play sound slap
            show white zorder 4:
                alpha 0.6
                linear 0.25 alpha 0.0
            mbf "Eh?"
            mc "DON'T...{w=1.0} TOUCH...{w=1.0} HER...!!!"
            show akuma:
                0.1
                easeout_cubic 0.5 yoffset 1500
            play sound fall
            "I push him strongly in order to protect Camilla."
            c l1 r1 e1j mf "[player]...!"
            mc "Camilla, get back! I can handle it myself!"
            c "O-okay..."
            show akuma at t11 zorder 2
            pass
    show camilla at rhide zorder 1
    hide camilla
    call ch3_battle_1
    if ch3_battle_1_victory == True:
        "*pant* *pant*"
        show camilla frontal uniform l1 r2 e1a b1d mf n3 hair_normal at t33 zorder 2
        c "You deserved this!"
        show camilla r1 at t22
        play sound punch2
        "Camilla kicks akuma who is on the floor."
        "...and spit in his face."
        show camilla at t11
        c l2 r2 mg n1 "Come on [player], let's get out of here..."
        mc "Sure."
        scene bg corridor
        with wipeleft_scene
        pass
    else:
        show camilla frontal uniform l1 r1 e1l b1d mj n3 hair_normal at t44 zorder 2
        c "[player!u]----!!!!!"
        c e1m b1e "YOU SON OF A BITCH!!! HOW DARE YOU--!!!"
        show camilla l3 r3 mi at t11
        play sound punch1
        show akuma:
            0.1
            easeout_cubic 0.5 yoffset 1500
        pause 0.25
        play sound fall
        "Camilla knocks out akuma."
        play sound punch2
        "She also gives him several punches and kicks."
        c l1 r1 e1b b1d mh "... ... ..."
        c b1c e1a mf "[player]..."
        "Camilla helps me to get up."
        c "Come on, let me take you to the infirmary."
        scene bg health_room_day
        with wipeleft_scene
        pass
    show camilla frontal uniform l1 r1 e1a b1c me n2 hair_normal at t11 zorder 2
    c "Are you okay?"
    mc "I'm fine, thanks."
    c ma "I'm glad..."
    show camilla e1b mh
    "... ... ..."
    pause 1.0
    c r2 b1d mf n1 "That irritating jerk..."
    c l3 "At least we give him from his own medicine."
    c l1 e1a mi n4 "But I can't stand him! He thinks he's so important..."
    c r1 "I don't understand why he's so respected here, also I don't know why Ryoma still hanging around with his group..."
    mc "Yeah, akuma is an asshole. Everybody knows that."
    mc "But don't worry Camilla, it's not of our business."
    show camilla b1a me
    mc "Also, remember that Ryoma is part of the Elite group, the same where Monika belongs."
    mc "In fact, I'm very surprised that you don't belong there. You were quite popular..."
    c e1b b1d mg n2 "Because I don't care about my schoollar status, I rather be myself, and if people here don't like it then so be it."
    mc "I see..."
    mc "Well, you got a point."
    mc "I would do the same thing if I were popular too."
    c e1a b1b ma "Indeed."
    pause 2.0
    play music t9
    c b1c "You know [player]..."
    c "That's why I like you."
    c "You're so different compared to other guys I know..."
    c r2 mb "Jeez... Sayori is a lucky girl for having you at her side..."
    if ch1_winner == "Sayori" and ch2_winner == "Sayori" and ch3_winner == "Sayori":
        mc "Well, if you say so..."
        mc "But I guess I'm the lucky here for having friends like you, Sayori and Ryoma."
    elif ch1_winner == "Yuri" and ch2_winner == "Yuri" and ch3_winner == "Yuri":
        c "...Or, I guess you're hanging more with the beautiful purple girl now, isn't?"
        mc "Yeah..."
        mc "But I guess I'm the lucky here for having friends like you, Yuri, Sayori and Ryoma."
    elif ch1_winner == "Natsuki" and ch2_winner == "Natsuki" and ch3_winner == "Natsuki":
        c "...Or, I guess you're hanging more with the small pink girl now, isn't?"
        mc "Yeah..."
        mc "But I guess I'm the lucky here for having friends like you, Natsuki, Sayori and Ryoma."
    elif ch1_winner == "Monika" and ch2_winner == "Monika" and ch3_winner == "Monika":
        c "...Or, I guess you're hanging with Monika now, isn't?"
        mc "Yeah..."
        mc "But I guess I'm the lucky here for having friends like you, Sayori, Monika and Ryoma."
    else:
        mc "Well, if you say so..."
        mc "But I guess I'm the lucky here for having friends like you, Sayori, and Ryoma."
        pass
    mc "I don't know what kind of life would I have if weren't for all of you."
    c r1 mf "[player]..."
    c "..."
    if camilla_route_complete == True:
        c "I..."
        c e1b "I need to tell you something..."
        c e1a "Do you ever asked why I'm such \"obsessed\" with you, treating you like a child or something like that?"
        c r2 mb "I mean... Yeah, yesterday you already asked why I'm very gentile with you."
        mc "Ah-- Well..."
        c me "The reason is..."
        c r1 mh e1b "..."
        c mi e1h "AAAAHH--!!!"
        mc "No Camilla! If you don't feel in mood to answer that, don't push yourself, please!"
        c e1f mj "No!"
        c mi "I need to say it good damn it!"
        c l2 r2 md e1h b1b "*sighs*"
        c l1 r1 b1c me "I know about how your parents treated you in the past..."
        mc "What the...{w} But--{nw}"
        c e1f "Like 3 years ago..."
        c l5 r1 b1c "I heard a conversation between you and Sayori where you told her that you felt lucky by not having your parents closer."
        c "That you were used as a \"Tool\" of them...{w} \"A useless tool\" if I heard well."
        c r5 b1d ml "Like if you were nothing but an object for them."
        "It can't be..."
        c l4 r4 e1h mg "So after hear that, I realised why you always had a very violent attitude, why you're so withdrawn, and why you're like you don't give a fuck about your life."
        c l5 e1f b1c me "I knew...{w} That you never felt how real {i}love{/i} is..."
        c "I knew how your heart was so empty of love..."
        c r5 e1h "I knew I had to do something to fill it with love."
        c l2 r2 mb e1f "And for some reason, it worked everytime I gave some love to you."
        c ma "Everytime where you're sad, angry, worried or with any other negative mood... When I start to pamper you, your mood changes."
        mc "Ye-Yeah... T-That's true..."
        "I'm not fucking kidding, she's right."
        c l5 me "But at the same time..."
        c ma "After I've been pampering you for long time, it became a kind of \"habit\" so to speak."
        c l4 r4 e1h "Since then, I can't stop beign so gentile with you... Overprotecting you from bullies..."
        mc "And that's why I'm very glad that you're one of my best friends."
        mc "Your parents must feel very lucky having you has their daughter. I wish I would have a mother like yours and..."
        show camilla l1 r1 mh
        mc "C...Camilla...??"
        c e1i ml "Mother..."
        mc "Eh...?"
        c e1g me "[player], there's something else I have to say..."
        c r5 "Despite the fact that I have such mothership love in you... I..."
        c l5 e1i ml "I never knew how a mother's love is really."
        mc "What do you mean...?"
        c e1g l1 r1 mf "When I was 1 year old, my mom died in an incident happened in Latin America at the year 2000."
        c "So I never was able to know how my mom was except for the photos my dad showed me."
        c l5 "He always said she was a kind, lovable, cute, helpful, etc. person."
        c "She also took him out of criminal life after he saved her from an assault."
        c r5 e1i me "In resume; she was the perfect wife."
        c e1g "Her parents were a richful japanese family, living in Argentina in that then."
        c "After my mom died, my grandparents offered my dad the chance of taking us to live in Japan."
        c "Since he wanted a better life for me, he accepted."
        c e1i l4 r4 mg "Since then, we're living here now..."
        mc "Camilla..."
        c mh "My dad suffers an post-traumatic depression because his tragic past, and the only way to make him happy is he making me happy with anything."
        c l1 r2 e1g me "He bought me a lot of things; last-gen videogames consoles, mangas, merchandising of our favourite games, animes and etc., EVERYTHING."
        c r5 mf "But in the deep of my heart I know he's still not happy at all..."
        c e1i "He still misses my mom."
        c l5 ml "And...{w} I also miss her..."
        c "*sobs*"
        mc "Camilla..."
        mc "... ... ..."
        show camilla l1 r1 at face(y=600) with dissolve
        "I can't help but cuddle her strongly..."
        "Poor girl, I never thought that she and her family suffered a lot."
        "Her story makes mine looks like an insignificant crap."
        "But... if she was giving me love because of that, then I must do it too."
        c e1g me "[player]..."
        show camilla e1i
        "After she realises my act, she proceeds to cuddle me stronger as well."
        "She also cries stronger."
        mc "It's okay..."
        "As I'm hugging her, I proceed to caress her."
        "She already knows I'm very bad with words... So I hope it's enough to make her feel better."
        pause 3.0
        show camilla ma with dissolve
        "At least seems like it worked."
        c "You're such amazing person [player]..."
        c "Please, never change."
        mc "Don't worry Camilla..."
        pause 3.0
        "We hug each other for a while."
        "Until she releases me..."
        hide camilla with dissolve
        $ persistent.ch4_camilla_unlocked = True
        pass
    else:
        c "... ... ..."
        "All of sudden, Camilla is hugging me. Almost cuddling."
        c "You're such amazing person [player]..."
        c "Please, never change."
        mc "Don't worry Camilla..."
        pause 3.0
        "We hug each other for a while."
        "Until she releases me..."
        pass
    show camilla frontal uniform l1 r1 e1f b1c ma n2 hair_normal at t11 with dissolve
    c "{i}*pleasant sigh*{/i}"
    if persistent.ch4_camilla_unlocked == True:
        c "Thank you..."
        mc "You're welcome..."
        c "Listen, umm..."
        c "If you need some help with {i}anything{/i}, it includes your clubs activities..."
        c "Just give me a call and I will be there to help you."
        c "Consider that a favor for what have you done for me already~"
        mc "Camilla..."
        mc "Thank you!"
        mc "I don't know what would I do without you."
        c "Hehe~!"
    c "Well, I guess you must come back to your club, right?"
    mc "Oh shit, that's true!"
    c "Come on, I will accompany you~!"
    "Camilla says that with the same energy what Sayori usually uses."
    "That reminds me..."
    mc "Sure. Let's go."
    "I grab Camilla's hand."
    "She sweetly smiles when I do that."
    scene bg corridor
    with wipeleft_scene
    show camilla frontal uniform l1 r1 e1a b1c ma n2 hair_normal at t11 zorder 2
    mc "Here we are..."
    c "[player], ehm..."
    mc "Yeah...?"
    c "Umm..."
    c "..."
    c "Take care of Sayori, please."
    c "Send her my regards... Okay?"
    mc "Of course, Camilla. Thank you for everything."
    c "No problem..."
    c "Well, see ya~~!"
    show camilla at thide zorder 1
    hide camilla
    "Camilla smiles sweetly and lefts."
    stop music fadeout 3.0
    "Alright, let's get in!"
    $ HKBShowButtons()
    $ HKBHideButtons()
    jump ch3_start_end
    return

label ch3_start_end:
    if not renpy.music.get_playing(channel='music') == audio.t3:
        stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "..."
    if not renpy.music.get_playing(channel='music') == audio.t3:
        play music t3
    show monika 4b at t11 zorder 2
    m "Okay, everyone!"
    "After some time passes, Monika calls out to the clubroom."
    m "Why don't we share our poems now?"
    show monika at thide zorder 1
    hide monika
    "Before I know it, everything is back to normal."
    "Everyone goes to retrieve their poems, and I do the same."
    "I make eye contact with Monika, and she smiles at me. But I make a disconcerted face."
    "I wonder what she was talking about with Sayori..."
    "I have a bad feeling about that, but I don't want to jump in such conclussions so quickly."
    return


label ch3_main_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b at t32 zorder 2
    with wipeleft_scene
    play music t3
    m "...Okay, you three!"
    m "We're all done sharing poems, right?"
    m "Why don't we start figuring out--"
    show natsuki 3c at f31 zorder 3
    n "Hold on a second!"
    n "Is it just me, or did you say something strange just now?"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 4d "Eh...?"
    show monika at t32 zorder 2
    show yuri 1e at f33 zorder 3
    y "Something did sound a bit unusual..."
    y "That's right."
    y 1f "You deviated from your usual catchphrase when addressing the club."
    show yuri at t33 zorder 2
    mc "Yeah Monika, I agree with them."
    show monika 1n at f32 zorder 3
    m "C-Catchphrase?"
    m "I don't have a catchphrase..."
    show monika at t32 zorder 2
    mc "\"Okay, everyone!\" was your usual catchphrase, but you said \"Okay, you three!\" instead."
    show natsuki 4q at f31 zorder 3
    n "See? Even [player] noticed it."
    n "Jeez..."
    n "Why is the mood so weird today?"
    n "Look, even Yuri isn't immune to it."
    show natsuki at t31 zorder 2
    show yuri 4b at f33 zorder 3
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri at t33 zorder 2
    mc "Yuri, don't scare me like that please..."
    "I'm shivering, I don't know why..."
    show monika at f32 zorder 3
    m "In {i}your{/i} books, maybe!"
    show monika at t32 zorder 2
    mc "Look, the most different thing here is that Sayori isn't here."
    show yuri 2g at f33 zorder 3
    y "Ah..."
    y "...It seems you're right."
    show yuri at t33 zorder 2
    show monika 2r at f32 zorder 3
    m "Sigh..."
    m 2d "Sayori always helps lighten the mood a little bit, doesn't she?"
    m "It's almost like everyone's balance is thrown off a little when she's not around..."
    show monika at t32 zorder 2
    show natsuki 3k at f31 zorder 3
    n "Where the heck did she run off to, anyway?"
    n "I thought she just went to pee."
    show natsuki at t31 zorder 2
    show yuri 1l at f33 zorder 3
    y "Natsuki, please show some decency..."
    show yuri at t33 zorder 2
    show natsuki 4w at f31 zorder 3
    n "Oh, come on."
    show natsuki at t31 zorder 2
    mc "Ah, she actually wasn't feeling too well and went home early..."
    show yuri 2t at f33 zorder 3
    y "Is that so...?"
    y "I hope she's alright..."
    show yuri at t33 zorder 2
    show natsuki 5c at f31 zorder 3
    n "Seriously?"
    n "Of all the times to not go home with her, you pick the time she's not feeling well?"
    n "So much for you two being all lovey-dovey."
    show natsuki at t31 zorder 2
    mc "Ah--no!"
    mc "First of all, stop misunderstanding my friendship with Sayori!"
    mc "And second..."
    mc "She's kind of been avoiding me today, so I didn't want to force it..."
    show yuri 1g at f33 zorder 3
    y "Hooooh?"
    show yuri at t33 zorder 2
    "{i}That curious expression coming from Yuri, of all people??{/i}"
    show monika 1r at f32 zorder 3
    m "Calm down, girls...!"
    m 1d "I talked to her earlier, and everything is fine."
    show monika at t32 zorder 2
    mc "What did she say...?"
    show monika at f32 zorder 3
    show yuri 1e
    m 1a "Anyway, we need to figure out the rest of the festival preparations, so..."
    show monika at t32 zorder 2
    mc "Monika, answer me..."
    mc "What the heck did she said??"
    show monika at f32 zorder 3
    m "Let's decide what everyone will be doing this weekend."
    show monika at t32 zorder 2
    mc "MONIKA----!!!"
    show monika at f32 zorder 3
    m "What the hell do you want?!"
    m "...!"
    m "Oops, sorry. I didn't pretend to..."
    show monika at t32 zorder 2
    mc "It doesn't matter, just tell me whay did Sayori say to you... Please."
    show monika at f32 zorder 3
    m "I'm gonna tell you via chat later, okay?"
    m "For now, let's focus about the festival preparations... Please."
    show monika at t32 zorder 2
    mc "Hush! Okay..."
    show natsuki 4l at f31 zorder 3
    n "I already know what {i}I'm{/i} doing!"
    show natsuki at t31 zorder 2
    show monika 2b at f32 zorder 3
    m "That's right."
    m "Natsuki will be making cupcakes."
    m "But we might need a lot of them, and different flavors..."
    m "Can you handle that all by yourself, Natsuki?"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4z "Challenge accepted!"
    show natsuki 4a at t31 zorder 2
    show monika at f32 zorder 3
    m 1a "And as for myself..."
    m "I'm going to be printing and assembling all the poetry pamphlets."
    m "Sayori will be helping me design them."
    m "And as for Yuri..."
    m 1d "..."
    m 3n "Yuri, you can..."
    m "Ah... Um..."
    show monika at t32 zorder 2
    show natsuki 3c at f31 zorder 3
    n "...?"
    show natsuki at t31 zorder 2
    mc "...?"
    show monika 5 at f32 zorder 3
    m "Guys..."
    m "Can you help me come up with something for Yuri...?"
    show monika at t32 zorder 2
    show yuri 4c at f33 zorder 3
    y "I..."
    y "I'm useless..."
    show yuri at t33 zorder 2
    show monika 1g at f32 zorder 3
    m "N-No!"
    m "That's not it at all!"
    m "You're the most talented person here, you know!"
    show monika at t32 zorder 2
    mc "I agree."
    show natsuki 5g at f31 zorder 3
    n "..."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1g "N-Now Natsuki's pouting, too??"
    show monika at t32 zorder 2
    mc "Jeez, even I can tell things are even harder on you when Sayori's not around."
    show monika at f32 zorder 3
    m "Ah..."
    m "That may be the case..."
    m 1i "But if I can't also be a leader on my own, then I won't grow as a person."
    "Since when Monika is so humble?"
    m 2i "So, Yuri...!"
    m 2a "You have beautiful handwriting, you know?"
    m "So you should make some banners and decorations to help set the atmosphere."
    show monika at t32 zorder 2
    show yuri 4a at f33 zorder 3
    y "Atmosphere...?"
    y "Um, about that..."
    y "I..."
    y 2r "I love atmosphere!"
    show yuri 2l
    "Yuri's expression suddenly changes as she stares at her desk in focus and starts nodding to herself."
    show yuri at t33 zorder 2
    mc "Your mind is already racing, it's good..."
    show monika 2b at f32 zorder 3
    m "That's great!"
    m "You'll be a wonderful help, Yuri."
    m 2a "But anyway..."
    m "That just leaves you, [player]."
    show monika at t32 zorder 2
    mc "The one who is truly useless. Indeed."
    show monika 1k at f32 zorder 3
    m "Ahaha! Don't say that."
    m 1b "In fact..."
    m "Both Natsuki and Yuri have some pretty heavy tasks to handle."
    m "It would probably go a long way to give one of them a hand."
    m 1m "You could always help me out, as well..."
    m 1a "I would be really appreciative of that."
    show monika at t32 zorder 2
    mc "Ah--"
    mc "That's..."
    "Is Monika suggesting I spend the weekend with one of my club members?"
    "How on Earth are they going to respond to a suggestion like that...?"
    show yuri 1u at f33 zorder 3
    y "Ah..."
    y "I...suppose I wouldn't mind a bit of help..."
    show yuri at t33 zorder 2
    show natsuki 3c at f31 zorder 3
    n "Well, even if you don't know how to bake, there's always some dirty work I could give to you."
    n 3q "It's not like Monika's going to give me a choice, and you shouldn't be sitting on your butt anyway..."
    "Natsuki tries to mumble a bunch of excuses like that."
    show natsuki at t31 zorder 2
    show yuri 2k at f33 zorder 3
    y "Um..."
    y "If I recall, Natsuki..."
    y 2f "You mentioned that you would like to handle the baking on your own."
    y "[player] may not like to be around if you only make him out to be a nuisance..."
    y 2i "So therefore..."
    y "He may be more suited to assisting with the decorations."
    show yuri at t33 zorder 2
    "I guess she's right..."
    show natsuki 4e at f31 zorder 3
    n "Hold on! I never said that!"
    n 4h "How hard could it be to make a few decorations, anyway?"
    n "Sounds more like you're just making excuses for [player] to--"
    show natsuki at t31 zorder 2
    show yuri 3n at f33 zorder 3
    y "W-What are you saying?!"
    y "It will be extremely meticulous work..."
    show yuri at t33 zorder 2
    show natsuki 5w at f31 zorder 3
    n "And baking isn't?"
    n "Just what do you think--"
    show natsuki at t31 zorder 2
    show monika 2g at f32 zorder 3
    m "Guys, guys!"
    m "Let's settle down for a moment..."
    m 2d "In the end, I think it's up to [player] to decide how he'd like to contribute."
    m "Besides..."
    if ch1_winner != "Monika" and ch2_winner != "Monika" and ch3_winner != "Monika":
        m 5 "He hasn't really gotten the chance to spend any time with me yet, you know?"
    else:
        m 5 "We may know each other since last year, but we never had a chance to meet ourselves better, you know?"
    show monika at t32 zorder 2
    mc "We didn't had such chance because you didn't--"
    show monika at f32 zorder 3
    m "So I'm sure he's interested in--"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 4f "You {i}literally{/i} just said--"
    show natsuki at t31 zorder 2
    show yuri 2h at f33 zorder 3
    y "I-I'm surprised as well!"
    show yuri at t33 zorder 2
    show monika 1l at f32 zorder 3
    m "Sorry, sorry!"
    m "I was just saying, though..."
    show monika at t32 zorder 2
    show natsuki 4x at f31 zorder 3
    n "Jeez..."
    n "Can we just settle this already?"
    show natsuki at t31 zorder 2
    show monika 1e at f32 zorder 3
    m "Yeah..."
    m "[player], you're okay with this, right?"
    m 1a "In the end, it's up to you."
    show monika at t32 zorder 2
    mc "Ah..."
    mc "Of course."
    show natsuki 5g at f31 zorder 3
    n "Hmph."
    show natsuki at t31 zorder 2
    show yuri 1f at f33 zorder 3
    y "Very well..."
    show yuri at t33 zorder 2
    show monika 1a at f32 zorder 3
    m "In that case..."
    show monika at t32 zorder 2
    "Everyone looks straight at me."
    menu:
        "But of course, I'm going to go with--"
        "Natsuki.":
            call ch3_end_natsuki
        "Yuri.":
            call ch3_end_yuri
        "Monika.":
            call ch3_end_monika
        "Sayori...":
            call ch3_end_sayori
        "Camilla!" if camilla_route_complete:
            call ch3_end_camilla
    scene bg residential_day
    with wipeleft_scene
    $ ch4_name = ch4_scene.capitalize()
    if ch4_scene != "monika" and ch4_scene != "camilla":
        $ ch4_nameB = ch4_sceneB.capitalize()
    "I can't believe this!"
    #if ch4_name == "Camilla":
    #    "I'm gonna visit Camilla to her house on Sunday...?"
    #else:
    "[ch4_name] is going to be coming to my house on Sunday...?"
    if help_sayori:
        "Even though I would have preferred to do this with Sayori..."
        "My anxiety still shoots through the roof."
        "I guess I've gotten pretty used to handling her at this point..."
        "But who knows what might end up happening when we're outside of school?"
        "She even told me she was looking forward to it..."
        "I shake my head."
        "Why do I feel nervous that Sayori finds out about this?"
        "It's not like we feel {i}that{/i} way about each other..."
        "Besides, like Monika said, this is about the club."
        "I have nothing to worry about."
        "If I just go with it, then I'll have a good time."
    else:
        "My anxiety shoots through the roof."
        "Even though I've gotten pretty used to handling her at this point..."
        "There's no telling what might end up happening when we're outside of school."
        "More than that...she told me that she was looking forward to it."
        "Is this the chance I have to make something happen between us?"
        "...Or is it too early for that?"
        "Only time will tell..."
        "But until then, I won't be able to take my mind off it."
        "I seriously can't wait!"
    return

label ch3_end_sayori:
    $ help_sayori = True
    mc "I mean..."
    mc "If it's going to be anyone, then I prefer helping Sayori."
    mc "I mean, we're already neighbors, and--"
    show yuri 2f at f33 zorder 3
    y "But Monika said--"
    show yuri at t33 zorder 2
    show natsuki 4w at f31 zorder 3
    n "Monika said that Sayori was helping her!"
    n "Jeez..."
    n 4h "Do you really hate us that much?"
    show natsuki at t31 zorder 2
    mc "N-No!"
    show monika 1e at f32 zorder 3
    m "Sorry, I didn't mean for this to be difficult..."
    show monika at t32 zorder 2
    menu:
        m "Just think of the club, okay?"
        "Natsuki.":
            call ch3_end_natsuki
        "Yuri.":
            call ch3_end_yuri
        "Monika.":
            call ch3_end_monika
        "Camilla." if camilla_route_complete:
            call ch3_end_camilla
    return


label ch3_end_monika:
    if help_monika == None:
        $ help_monika = True
        mc "Well, I guess I should probably be helping Monika..."
        show monika 5 at f32 zorder 3
        m "Yay, you picked me!"
        show monika at t32 zorder 2
        show natsuki 3e at f31 zorder 3
        stop music fadeout 1.0
        n "Hold on one second!"
        show natsuki at t31 zorder 2
        show yuri 2r at f33 zorder 3
        y "Y-Yeah!"
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        play music t7
        n "Monika, you're the one who needs the least help out of all of us!"
        show natsuki at t31 zorder 2
        show monika 1d at f32 zorder 3
        m "Eh? But..."
        show monika at t32 zorder 2
        show yuri 1h at f33 zorder 3
        y "I agree with Natsuki."
        y 1l "Not only is your work already most suitable for one person..."
        y "But you already have Sayori as well."
        show yuri at t33 zorder 2
        show monika at f32 zorder 3
        m 1p "But [player] was the one who..."
        m "Ah..."
        show monika at t32 zorder 2
        show natsuki 3c at f31 zorder 3
        n "That doesn't matter."
        n "You were the one who scared him into picking you in the first place."
        n 3e "You're the club president, Monika."
        n "You're supposed to make responsible decisions for the club!"
        show natsuki at t31 zorder 2
        show yuri 2f at f33 zorder 3
        y "Monika, you shouldn't let any ulterior motives interfere with this decision."
        show yuri at t33 zorder 2
        show monika 2i at f32 zorder 3
        m "Ulterior motives?"
        m "W-What are you saying, Yuri?"
        m "In fact, it sounds like you guys are the ones with ulterior motives!"
        show monika at t32 zorder 2
        "I agree with Yuri, it's pretty weird that Monika insists on spend time with me on anything so fast..."
        show natsuki 1x at f31 zorder 3
        n "{i}Excuse{/i} me?"
        show natsuki at t31 zorder 2
        show monika at f32 zorder 3
        m "Otherwise...this wouldn't have been made into such a big deal in the first place!"
        show monika at t32 zorder 2
        show yuri 3r at f33 zorder 3
        y "That's...completely false, Monika!"
        show yuri at t33 zorder 2
        show natsuki 3e at f31 zorder 3
        n "Yeah!"
        n "We have a lot of work to do, you know!"
        n "We won't do as good of a job if you make us work alone."
        show natsuki at t31 zorder 2
        show monika 1p at f32 zorder 3
        m "Ah...maybe...that's true..."
        show monika at t32 zorder 2
        show yuri 2l at f33 zorder 3
        y "Think of the club, Monika..."
        y "If we want our event to succeed, then we need to appropriately distribute our resources."
        show yuri at t33 zorder 2
        show monika 3n at f32 zorder 3
        m "Um..."
        m "Ah..."
        show monika at t32 zorder 2
        show natsuki 4x at f31 zorder 3
        n "So are you going to do the right thing, {i}President{/i}?"
        show natsuki at t31 zorder 2
        show monika 1p at f32 zorder 3
        m "Okay, okay!"
        m "I get it!"
        stop music fadeout 1.0
        show natsuki 4g
        show yuri 2g
        m 1r "Sigh..."
        m 1g "It's...technically most logical for [player] to help one of you two."
        m "So..."
        m 1c "I guess...that's what we'll do."
        show monika at t32 zorder 2
        play music t3
        menu:
            m "Do you have a preference, [player]?"
            "Natsuki.":
                call ch3_end_natsuki
            "Yuri.":
                call ch3_end_yuri
            "Monika again.":
                call ch3_end_monika
            "Sayori..." if help_sayori == None:
                call ch3_end_sayori
            "Camilla." if camilla_route_complete:
                call ch3_end_camilla
    else:
        $ ch4_scene = "monika"
        stop music fadeout 5.0
        mc "Listen girls, it's nothing personal."
        mc "But all of you didn't gave me the chance to help Sayori so..."
        mc "I'll choose to help Monika so we can be all three together."
        mc "I'm so sorry..."
        n "Youuu...!"
        y "..."
        m "So it's decided then~!"
        n "It's {i}NOT{/i} fair!!!"
        y "I agree..."
        y "I didn't expected such attitude coming from you [player]."
        y "And...I thought you we're a different and nice person..."
        n "Yeah [player]! You're such an selfish asshole!"
        mc "I'm so sorry... For real! Please!"
        "Jeez... What's wrong with them?"
        m "Say one more thing about him and I'll have no option than kick all of you out."
        ny "Monika--!!!"
        n "How dare you...!!!"
        mc "No Monika, it was completely unnecesary."
        mc "It's my fault after all, my original plan was choose one of them but I choosed you instead because of Sayori."
        m "Well, it's not like you deserve to be treated like that in first place."
        "Look who says it..."
        m "I'm defending you, dummy."
        m "It's your own choice after all."
        mc "But that's not the right way."
        mc "I will not allow you do something to them because something of my business."
        mc "Come on, retract yourself about what did you said to Yuri and Natsuki!"
        "..."
        m "Fine..."
        m "I'm sorry girls. I--"
        hide natsuki
        hide yuri
        with wipeleft
        "Before we notice it, Natsuki and Yuri did just left the room."
        mc "What the..."
        play music t6 fadeout 1
        show monika 5 at f11
        m "Hmm...? Seems like we are the only ones remaining here."
        m "Hehehehe!"
        show monika at t11
        mc "Jesus Christ..."
        mc "What I've done?!"
        m 1a "No [player]. Don't worry."
        m "They just didn't take it so easy."
        m "Looks like they {i}REALLY{/i} wanted to spend time with you~"
        m "But once again, I showed up who rules in this school!"
        mc "Oh, come on Monika! Are you serious?"
        mc "You're talking like it's a big deal about spending time with me..."
        mc "ME! An selfish asshole who's unnable to help his own best friend and give a hand to people who really need it."
        mc "A loser who--"
        m "Enough!"
        m "Listen [player], stop talking crap about yourself."
        m "You must consider lucky for having me as your friend."
        m "And maybe... We can reach to something more else~"
        m "If you want, of course."
        mc "... ... ..."
        "Really? Seriously, I don't understand the {i}new{/i} Monika..."
        m "Anyway, I guess I must give you my number to be in contact."
        mc "Sure."
        "Monika and I exchange our phone numbers."
        m "Okay then, I'll be calling you."
        mc "Alright."
        m "Umm... I need to tell you something..."
        mc "What?"
        m "I will go to your house this weekend."
        mc "What?!"
        m "Yeah, it would be easier to work together if we are in the same place."
        m "And Sayori told me that you have high speed internet and, that you're living alone there..."
        mc "Did Sayori told you that???"
        "Oh my fucking god..."
        m "Yeah."
        m "And, well... My house is not so quiet at all. We could get distracted very easy."
        m "And if we work at distance, you'll be very lonely... At least I can be some company."
        m "Even we can have some fun after we finish, don't you think?"
        mc "Ahh- I guess..."
        m "It's decided then!"
        m "I'll see you this Sunday in your house~!"
        show monika at thide zorder 1
        hide monika
        mc "Alright. Bye Monika..."
    return

label ch3_end_natsuki:
    $ ch4_scene = "natsuki"
    $ ch4_sceneB = "yuri"
    mc "Well, baking sounds like it could be fun..."
    mc "And you guys made it sound like a lot of work, so it could probably use two people."
    show natsuki 4l at f31 zorder 3
    n "Don't worry!"
    n "Baking is a ton of fun!"
    n "You'll definitely agree!"
    show natsuki at t31 zorder 2
    show monika 1d at f32 zorder 3
    m "Eh?"
    m "Just a minute ago you were saying that--"
    show monika at t32 zorder 2
    show natsuki 1q at f31 zorder 3
    n "Th-That's because--!"
    n "..."
    n "...Never mind, okay?"
    show natsuki at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "Well, anyway..."
    m "You'll be fine by yourself, right, Yuri?"
    show monika at t32 zorder 2
    show yuri 1j at f33 zorder 3
    y "Of course."
    y "I'm used to it, after all..."
    show yuri 1g at t33 zorder 2
    show monika 1e at f32 zorder 3
    m "..."
    show monika at t32 zorder 2
    mc "..."
    if persistent.ch4_camilla_unlocked == True:
        mc "Hold on a second!"
        "Everyone" "Eeh??"
        mc "Yuri, you don't need to do the banner all of yourself, I have a friend who can help you with it."
        mc "She is a nice person, and if she knows that you're one of my closest friends and knows you really needs help, then she will be very, very helpful."
        mc "Without mention that she has very good painting skills as well..."
        y "Really?"
        y "Umm..."
        m "Please don't tell me you're talking about--"
        mc "Her name is Camilla. She promised me if I ask her any favor, she will always be there to help."
        mc "She will be very glad to help you with the banner Yuri, I swear..."
        y "Well, in that case..."
        y "Sure... I can accept some help."
        mc "I'm glad to hear that."
        mc "I will send her a SMS right now to meet you at the exit so you can start to know each other and coordinate everything."
        y "O-okay."
        show natsuki 3a at f31 zorder 3
        n "So, that's everything, right?"
        n "Anything else we need to talk about?"
        show natsuki at t31 zorder 2
        show monika 1a at f32 zorder 3
        m "No, I think that's it..."
        m "Are you guys excited?"
        show monika at t32 zorder 2
        show natsuki 1z at f31 zorder 3
        n "Yes!"
        n "Everything except the performance is gonna be awesome!"
        show natsuki 1a at t31 zorder 2
        mc "I don't think that really counts..."
        show monika at f32 zorder 3
        m "What about you, [player]?"
        show monika at t32 zorder 2
        mc "Me?"
        mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
        show monika 2b at f32 zorder 3
        m "That's good enough for me!"
        m "What about you, Yuri?"
        y "Ah--!"
        y "Sorry, I was spacing out..."
        y "I... I'm not used to work with strange people... T-That's all..."
        mc "Ehehehe..."
        "I pat her shoulder."
        mc "Don't worry about that. Trust me, once you met Camilla, you will be feel very comfortable~"
        "I said that with a smile."
        m "Yeah, whatever..."
        "Monika doesn't seems to be happy with my idea, but fuck her, I just want to help Yuri as I must help Natsuki."
        "Also, she will be working with Sayori, so why she's complaining?"
        y "Ehehe~"
        y "I guess I shall thank you for this [player]..."
        y "I mean, I didn't expected such thing... It's like..."
        mc "It's like you thought that you will had to do the banner all of yourself in another timeline?"
        y "Yeah... sort of..."
        mc "Ahaha, don't worry, I won't allow such thing."
        show yuri 2l at f33 zorder 3
        y "Okay then..."
        y 2i "I'm going to do my best."
        y "And all of us are going to make it a really great event."
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 5j "Yeah."
        show natsuki at t31 zorder 2
        show monika 2k at f32 zorder 3
        m "Yeah!"
        m 2b "I hope to see everyone do their best."
        m "But with that..."
        m "There's nothing more for today."
        m "So I guess it's time for us to head out."
        show monika at t32 zorder 2
        show natsuki 3k at f31 zorder 3
        n "Okay, but I'm staying here a bit longer."
        n "I barely got to do any reading today, so..."
        show natsuki at t31 zorder 2
        show monika 2a at f32 zorder 3
        m "Fair enough, there's nothing wrong with that."
        pass
    else:
        show monika at f32 zorder 3
        m 1n "That's...good..."
        "Even though Yuri is being melodramatic, it's a little hard to not feel bad..."
        show monika 1m at t32 zorder 2
        show natsuki 3a at f31 zorder 3
        n "So, that's everything, right?"
        n "Anything else we need to talk about?"
        show natsuki at t31 zorder 2
        show monika 1a at f32 zorder 3
        m "No, I think that's it..."
        m "Are you guys excited?"
        show monika at t32 zorder 2
        show natsuki 1z at f31 zorder 3
        n "Yes!"
        n "Everything except the performance is gonna be awesome!"
        show natsuki 1a at t31 zorder 2
        mc "I don't think that really counts..."
        show monika at f32 zorder 3
        m "What about you, [player]?"
        show monika at t32 zorder 2
        mc "Me?"
        mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
        show monika 2b at f32 zorder 3
        m "That's good enough for me!"
        m "What about you, Yuri?"
        m 2d "...Yuri?"
        show monika at t32 zorder 2
        show natsuki 3c at f31 zorder 3
        n "She's still sulking."
        show natsuki at t31 zorder 2
        show yuri 4b at f33 zorder 3
        y "..."
        show yuri at t33 zorder 2
        show natsuki 5n at f31 zorder 3
        n "..."
        "Natsuki starts pouting, too."
        n "It's not..."
        n 5m "I mean, it's not that big of a deal or anything..."
        show natsuki at t31 zorder 2
        mc "Well, it might not be just that..."
        show natsuki at f31 zorder 3
        n "...?"
        show natsuki at t31 zorder 2
        mc "I think that Yuri might just be feeling a little underappreciated in general."
        mc "Having to come up with something for her to do, and then nobody offering to help."
        show natsuki at f31 zorder 3
        n 5q "That doesn't mean..."
        n "..."
        n 5r "Uu..."
        show natsuki 5u
        "Natsuki glances back and forth between everyone with a worried expression."
        n 1u "Look..."
        "Natsuki goes over and puts her hands down on Yuri's shoulders."
        n 1h "Yuri."
        n "You really are the most talented one here."
        n "And..."
        n "And you're going to help make the event a lot more fun and welcoming."
        n 1q "I mean, the cupcakes will probably help a lot too..."
        n 3h "But you're gonna make the atmosphere special."
        n "That'll be really important for the way that people feel during the performances."
        n "So..."
        n 4w "You need to stop being dumb and give yourself a little more credit!"
        "Natsuki releases her hands and turns around to face the other direction."
        show natsuki at t31 zorder 2
        show yuri at f33 zorder 3
        y 4a "..."
        y "You didn't...really mean that, did you?"
        show yuri at t33 zorder 2
        show natsuki 5u at f31 zorder 3
        n "Um..."
        n "N-Not really, but..."
        show natsuki at t31 zorder 2
        "Yuri isn't the only one surprised."
        "Monika and I are also taken aback by Natsuki's words."
        "Natsuki, of all people, to be saying such encouraging things."
        "But I begin to understand."
        "Natsuki was trying to sound like Sayori."
        "Even if it didn't work perfectly, I can tell that she tried to say something Sayori would say at a time like this."
        "Because Sayori always helps everyone smile and feel good about themselves."
        show yuri 2l at f33 zorder 3
        y "I'm sorry...for being dumb."
        y 2i "I'm going to do my best."
        y "And all of us are going to make it a really great event."
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 5j "Yeah."
        show natsuki at t31 zorder 2
        show monika 2k at f32 zorder 3
        m "Yeah!"
        m 2b "I hope to see everyone do their best."
        m "But with that..."
        m "There's nothing more for today."
        m "So I guess it's time for us to head out."
        show monika at t32 zorder 2
        show natsuki 3k at f31 zorder 3
        n "Okay, but I'm staying here a bit longer."
        n "I barely got to do any reading today, so..."
        show natsuki at t31 zorder 2
        show monika 2a at f32 zorder 3
        m "Fair enough, there's nothing wrong with that."
        pass
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Monika and Yuri out the door as they chat between each other."
    play music t6 fadeout 1
    show natsuki 4g at t11 zorder 2
    n "Um, where are you going?"
    mc "Eh...?"
    n 4c "We still need to figure out our plans for this weekend."
    n "You literally would've gotten home and realized that you didn't even have a way to contact me."
    mc "Oh, that's true..."
    mc "I have no idea how that slipped my mind."
    n 2c "Jeez, good thing I stopped you."
    n "I'm giving you my number, okay?"
    n 2q "You'd better not make it weird or anything!"
    mc "Why would I do that...?"
    n 1s "Hmph..."
    "Natsuki gives me her number."
    n 1c "Okay..."
    n "I'm coming over on Sunday."
    n "I'll bring all the ingredients."
    mc "Wait!"
    mc "You're coming to {i}my{/i} house?"
    n 2c "Well, yeah."
    n "What's wrong with that?"
    mc "I mean..."
    mc "I just figured that since I'm the one helping, I would be going to your house..."
    n "Yeah, right."
    n 5x "Like I could have a guy over my house..."
    n "My dad would kill me."
    mc "Really?"
    mc "That's kinda strict, if you ask me."
    n 5r "Yeah, how do you think I feel?"
    n "I can't do anything when my dad is home..."
    n 2q "Anyway...I just needed to complain for a second."
    n 2c "We have each other's numbers now."
    n "That's all I needed from you."
    n "I guess I'll text you when I'm coming over."
    mc "Alright, fine by me."
    n "Yeah."
    n 4a "I'm really gonna show you why I love baking so much."
    n "So you'd better look forward to it."
    mc "Oh?"
    mc "Didn't you say you were just going to give me the dirty work?"
    n 1r "Well--!"
    n "I was...just saying that."
    n 1q "It's not like I could act like...in front of everyone..."
    n "That I was looking forward to this."
    mc "Wait, really??"
    n 5w "Well, kind of!"
    n "Just because...I never got to bake with someone else before."
    n 5h "That's all it is, so..."
    mc "Alright, I get it."
    mc "Sorry for overreacting."
    mc "Anyway, I'll be heading out now."
    mc "See you on Sunday."
    n 5m "Ah--"
    n "..."
    n 5u "...Never mind."
    return

label ch3_end_yuri:
    $ ch4_scene = "yuri"
    $ ch4_sceneB = "natsuki"
    mc "Well, I'll probably be most useful helping out Yuri..."
    show yuri at f33 zorder 3
    y 2n "M-Me...?"
    show yuri at t33 zorder 2
    show natsuki at f31 zorder 3
    n 4e "Are you serious?"
    n "Why would you--"
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1i "Natsuki."
    m "I can already tell you're about to say something mean."
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5r "N-No..."
    n "I was just saying--"
    n "Ugh..."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 2a "So, you'll be helping Yuri then, [player]?"
    show monika at t32 zorder 2
    mc "Yeah."
    mc "That's what I'm going to do."
    show yuri at f33 zorder 3
    y 1u "I'm glad."
    y "I have a bad habit of overthinking these sorts of things..."
    y "So I think your assistance will be very useful."
    show yuri at t33 zorder 2
    show monika at f32 zorder 3
    m "That's great to hear."
    m "Natsuki, will you be able to handle the baking yourself?"
    show monika at t32 zorder 2
    show natsuki at f31 zorder 3
    n 3w "I mean, yeah."
    n "I already said I would be fine."
    show natsuki at t31 zorder 2
    show monika at f32 zorder 3
    m 1i "Okay, okay..."
    "Everyone can tell that Natsuki is feeling a little sour."
    if persistent.ch4_camilla_unlocked == True:
        mc "Hold on a second!"
        "Everyone" "Eeh??"
        mc "Natsuki, you don't need to do the cupcakes all of yourself, I have a friend who can help you with it."
        mc "She is a nice person, and if she knows that you're one of my closest friends and knows you really needs help, then she will be very, very helpful."
        mc "Without mention that she has very good cooking skills as well..."
        n "Uh, really?"
        n "And who is your {i}friend{/i} exactly?"
        m "Please don't tell me you're talking about--"
        mc "Her name is Camilla. She promised me if I ask her any favor, she will always be there to help."
        mc "She will be very glad to help you with the cupcakes Natsuki, I swear..."
        n "Alright, since she's a girl I guess it's not a bad idea after all."
        mc "I'm glad to hear that."
        mc "I will send her a SMS right now to meet you at the exit so you can start to know each other and coordinate everything."
        n "But with one condition..."
        n "Tell her I want to bake the cupcakes in {i}her{/i} house."
        n "I'll bring all the ingredients."
        mc "Wait!"
        mc "You're coming to {i}her{/i} house?"
        n 2c "Well, yeah."
        n "What's wrong with that?"
        mc "I mean..."
        mc "I just figured that since she's the one helping, she would be going to your house..."
        n "Yeah, right."
        n 5x "Like I could have a \"visit\" over my house..."
        n "My dad would kill me."
        mc "Really?"
        mc "That's kinda strict, if you ask me."
        n 5r "Yeah, how do you think I feel?"
        n "I can't do anything when my dad is home..."
        n 2q "Anyway...I just needed to complain for a second."
        mc "So...is that everything we needed to go over?"
        show monika at f32 zorder 3
        m 1a "Yeah, that should be about it."
        m 2a "Are you guys excited?"
        show monika at t32 zorder 2
        show yuri at f33 zorder 3
        y 1i "Well, 'excited' may not be the right word..."
        y "But I suppose I'm looking forward to it a little bit."
        show yuri at t33 zorder 2
        show monika at f32 zorder 3
        m "Do you feel the same way, [player]?"
        show monika at t32 zorder 2
        mc "Me?"
        mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
        show monika at f32 zorder 3
        m 2b "That's good enough for me!"
        m 2a "What about you, Natsuki?"
        show monika at t32 zorder 2
        show natsuki at f31 zorder 3
        n 5s "..."
        show monika at t32 zorder 2
        mc "Ehehehe..."
        mc "Don't worry about that. Trust me, once you met Camilla, you will be feel very comfortable~"
        "I said that with a smile."
        m "Yeah, whatever..."
        "Monika doesn't seems to be happy with my idea, but fuck her, I just want to help Natsuki as I must help Yuri."
        "Also, she will be working with Sayori, so why she's complaining?"
        show natsuki at f31 zorder 3
        n 1h "I see..."
        n "Well, I kinda appreciated it."
        n 1u "I'm sorry...for making a big deal out of nothing."
        n 1m "But I'm going to say this."
        show natsuki at t31 zorder 2
        mc "Yeah?"
        show natsuki at f31 zorder 3
        n 4e "You guys better bet that my cupcakes are going to be the best part of the whole event!"
        show natsuki 4a at t31 zorder 2
        show yuri at f33 zorder 3
        y 2f "Ah..."
        y 1s "...We believe you."
        y "Right [player]?"
        show yuri at t33 zorder 2
        mc "Of course!"
        mc "And with Camilla's help, make sure that you will make the cupcakes the whole main event..."
        n "Yeah! I hope you're right..."
        show monika at f32 zorder 3
        m 2b "Yeah!"
        m "I hope to see everyone do their best."
        m "But with that..."
        m "There's nothing more for today."
        m "So I guess it's time for us to head out."
        show monika at t32 zorder 2
        show natsuki at f31 zorder 3
        n "Alright, let's get out of here, then."
        pass
    else:
        show monika at t32 zorder 2
        mc "So...is that everything we needed to go over?"
        show monika at f32 zorder 3
        m 1a "Yeah, that should be about it."
        m 2a "Are you guys excited?"
        show monika at t32 zorder 2
        show yuri at f33 zorder 3
        y 1i "Well, 'excited' may not be the right word..."
        y "But I suppose I'm looking forward to it a little bit."
        show yuri at t33 zorder 2
        show monika at f32 zorder 3
        m "Do you feel the same way, [player]?"
        show monika at t32 zorder 2
        mc "Me?"
        mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
        show monika at f32 zorder 3
        m 2b "That's good enough for me!"
        m 2a "What about you, Natsuki?"
        show monika at t32 zorder 2
        show natsuki at f31 zorder 3
        n 5s "..."
        show monika at t32 zorder 2
        show yuri at f33 zorder 3
        y 2h "Natsuki!"
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 1o "What??"
        n 1m "Why is everyone yelling at me?"
        n "I didn't even do anything...!"
        show natsuki 1n at t31 zorder 2
        show yuri at f33 zorder 3
        y 3n "N-no--!"
        y "That's not what I meant at all!"
        y 3o "A-Ah..."
        "Yuri anxiously glances between everyone in the room."
        y 2w "I-I'm sorry for this!"
        y 2v "I don't really know why [player] picked me..."
        y "And also..."
        y 2t "Your cupcakes are the best cupcakes I've ever had!"
        y "They go really well with my tea!"
        y "And nothing that I do for the event will compare to that, so..."
        y 4b "So..."
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 3q "I get it, I get it."
        n 3h "I'm kinda surprised, though..."
        show natsuki at t31 zorder 2
        show yuri at f33 zorder 3
        y "W-Why?"
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 3q "Um..."
        n "Well, I'm the one acting immature..."
        n "I already know that."
        n 5h "But you're trying to cheer me up all of a sudden..."
        show natsuki at t31 zorder 2
        show yuri at f33 zorder 3
        y "I-I know I'm not very good at it..."
        y 2v "I'm sorry if I said something bad!"
        "Natsuki isn't the only one surprised."
        "Monika and I are also taken aback by Yuri's words."
        "When she already has trouble with words, trying to cheer someone up must be far out of her own comfort zone."
        "But I begin to understand."
        "Yuri was trying to sound like Sayori."
        "Even if it didn't work perfectly, I can tell that she tried to say something Sayori would say at a time like this."
        "Because Sayori always helps everyone smile and feel good about themselves."
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 1h "No..."
        n "I kinda appreciated it."
        n 1u "I'm sorry...for making a big deal out of nothing."
        n 1m "But I'm going to say this."
        show natsuki at t31 zorder 2
        show yuri at f33 zorder 3
        y 2e "...?"
        show yuri at t33 zorder 2
        show natsuki at f31 zorder 3
        n 4e "You better bet that my cupcakes are going to be the best part of the whole event!"
        show natsuki 4a at t31 zorder 2
        show yuri at f33 zorder 3
        y 2f "Ah..."
        y 1s "...I believe you."
        show yuri at t33 zorder 2
        show monika at f32 zorder 3
        m 2b "Yeah!"
        m "I hope to see everyone do their best."
        m "But with that..."
        m "There's nothing more for today."
        m "So I guess it's time for us to head out."
        show monika at t32 zorder 2
        show natsuki at f31 zorder 3
        n "Alright, let's get out of here, then."
        pass
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Monika and Natsuki out the door as they chat between each other."
    play music t6 fadeout 1
    show yuri 2t at t11 zorder 2
    y "U-Um--!"
    mc "Eh?"
    "I turn around."
    y "Sorry..."
    y 2s "I realized that I don't have any way of contacting you this weekend..."
    mc "Oh, you're right."
    mc "I can't believe that slipped my mind."
    mc "Should I give you my phone number?"
    y 1a "I think...that would be the best way, yes."
    mc "Alright, then..."
    "Yuri and I exchange phone numbers."
    y "Okay."
    y "Then, I'll be stopping by your house on Sunday..."
    mc "Eh?"
    mc "My house?"
    y 2t "I-Is that a problem...?"
    mc "No, not at all..."
    mc "I just thought that I would be the one going to your house, since I'm the one helping you."
    y "Ah, I suppose that makes sense..."
    y "But, if you don't mind..."
    y 1u "I think I would prefer going to your house."
    mc "Alright."
    mc "In that case, it won't be a problem."
    "I decide not to press Yuri for a reason."
    "It's not like it should matter much either way, so I'll just need to make sure my room is clean."
    mc "I hope I manage to make myself useful in some way..."
    mc "I'm not nearly as creative as you are."
    y 1a "Don't underestimate yourself, [player]."
    y "I think that we'll make a very productive team."
    y 1u "Even if you only chose me because you felt bad or something..."
    mc "Wait...!"
    mc "You don't actually think that, do you?"
    y 4b "..."
    y "I...don't know."
    y "It's difficult to come up with any other reason you may have chosen me..."
    mc "You're forgetting the one reason with the most common sense!"
    mc "I chose to help you because that's what I want to do."
    y 2v "B-But..."
    "Yuri thinks to herself with an extremely tense expression."
    mc "Yuri...you're overthinking this."
    mc "You wanted me to point out when you're overthinking, right?"
    y "Eh...?"
    y 4 "I...didn't realize..."
    mc "I'm telling you, I want to."
    mc "That's all there is to it."
    mc "Do you believe me?"
    y 1t "I..."
    "Yuri thinks really hard again."
    "She looks straight into my eyes for a long while."
    y 3l "...I believe you!"
    "As if it took her tremendous effort, Yuri finally says that and relaxes her expression."
    y 3s "And I'm really looking forward to Sunday."
    mc "Yeah..."
    mc "I am too."
    show yuri at thide zorder 1
    hide yuri
    "After that exchange, I make my way out the door, and Yuri follows."
    return

label ch3_end_camilla:
    $ ch4_scene = "camilla"
    n "Who the heck is Camilla?!"
    y "Eh??"
    m "Are you serious, [player]???!!!"
    m "She's not even a club member, come on!"
    m "{i}You{/i} should only pick one of {i}us{/i} HERE--!!"
    mc "Sorry Monika, but I can't deal with that."
    m "Grrr--!!"
    mc "In fact, I have an idea..."
    mc "What if Yuri helps Natsuki with the cupcakes baking while Camilla helps me to make the banner?"
    ny "Eh?"
    y "But [player], the banner is my responsability..."
    n "Yeah, and I don't think that Yuri would be helpfull with--"
    mc "No!"
    mc "Natsuki, if you think Yuri is helpless, then don't even think about asking me for help because I'm literally worse."
    mc "And Yuri..."
    mc "Don't worry about the banner, Camilla is very good at painting. She will be very helpful, I promise."
    y "Umm..."
    mc "In fact, you should give me your phone number so I can show you the progress and see if it's okay."
    y "Well..."
    y "I guess it's alright then..."
    mc "Perfect!"
    mc "So... Yuri helps Natsuki with cupcakes baking, Camilla helps me with the banner making, and Sayori helps Monika printing and assembling all the poetry pamphlets."
    m "Uuuuu-!"
    n "Monika, are you okay?"
    m "Ah--"
    m "Yeah...yes...I'm okay..."
    m "I was just rambling, ahahahaha!"
    mc "Whatever. I think we're all ready to start."
    mc "Let's do this, for the Literature Club!"
    "I raise my fist up, but nobody does the same..."
    n "Okay, but Yuri..."
    n "Can we bake the cupcakes at your house?"
    n "I don't feel like it's a good idea do it at my house..."
    y "Eh? Why's that?"
    n "It doesn't matter."
    "Does Natsuki really has parental problems?"
    "That's reminds me...{nw}"
    y "Umm... If you say so..."
    y "But please, let's be careful and don't dirt anything."
    n "Whatever..."
    m "Okay girls, I see you all at the festival then..."
    m "I will go sooner to a meeting I have."
    m "See ya~"
    show monika at lhide
    hide monika
    "Monika rans away."
    n "Alright, let's get out of here, then."
    hide natsuki
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Yuri and Natsuki out the door as they chat between each other."
    stop music fadeout 1.0
    scene bg corridor
    with wipeleft_scene
    play music t6 fadeout 1
    "Shit, at this hour Camilla would be at her house now!"
    if fightingclub_activities >= 1:
        "Or maybe I can encounter her at the Mixed Martial Arts club instead."
        "I will call Camilla to check it out."
        "..."
        c "[player]?"
        mc "Hi Camilla... Listen, will you be at the Mixed Martial Arts club today?"
        c "Of course, I'm at the entrance right now honey."
        "Right, I can go directly there and talk to her. The dojo is only a few steps closer to the school."
        mc "Nice, because I have some news and I need to tell them personally to you."
        c "News? Nice! I can't wait...!"
        mc "Me neither to tell you Camilla, I see you there..."
        "{i}*click*{/i}"
        mc "Okay, let's go!"
        scene bg school_entrance
        with wipeleft_scene
        show camilla frontal sports l1 r1 e1a b1a mb n1 hair_normal at t11 zorder 2
        c "[player]~!"
        mc "Wow, Camilla! I though that you'll be at..."
        c "Yeah, but I was impatient and I decided to come directly here~"
        c "So tell me, what is this?"
        mc "Well um..."
        mc "Listen, will you be free at Sunday?"
        c "Of course, do you want to spend some time with me sweetheart?"
        mc "Well... sort of."
        mc "I need your help about an assigment for the literature club and..."
        c "Say no more!"
        c "I'm glad to help you~"
        c "Now tell me what should we do..."
        mc "Alright, the thing is..."
        mc "We have to do a banner and a few decorations for the festival this Monday."
        mc "Since you're very good at painting I think that you'll be very helpful for me."
        c "Crafts, eh? Of course I can help you with that darling~!"
        c "You picked the right person, ehehe!"
        mc "Ehehe, thank you very much."
        c "No problem, that's why I'm here..."
        c "By the way, do you wanna go to the Mixed Martial Arts Club with me?"
        menu:
            "Sure, let's go!":
                c "Yaaay~!"
                c "Let's go then."
                mc "Yeah!"
                call fightingclub
                $ fightingclub_closed = True
                $ accept_fightingclub_offer = "Yes"
                scene bg residential_day
                with wipeleft_scene
                $ stamina -= 5
                pass
            "I'm sorry but I have things to do...":
                c "Uuuuu~!"
                c "Too bad..."
                c "Don't worry then, the next time will be."
                mc "Okay then, see you this Sunday Camilla."
                mc "And thanks for offering your help. I really apreciate that..."
                c "Uhuhu~! You're welcome..."
                c "I'll be waiting for you~"
                pass
    else:
        "I need to call Camilla."
        "..."
        c "[player]?"
        mc "Hi Camilla... Listen, will you be free at Sunday?"
        c "Of course, do you want to spend some time with me sweetheart?"
        mc "Well... sort of."
        mc "I need your help about an assigment for the literature club and..."
        c "Say no more!"
        c "I'm glad to help you~"
        c "But where are you actually?"
        mc "I'm about to exit the school... why?"
        c "Because I'm at Ryoma's dojo, it's close to the school, I'm going to wait for you at the entrance so you can give me more details."
        mc "Alright then... I see you there."
        "{i}*click*{/i}"
        "Right, the Ryoma's Mixed Martial Arts club..."
        "I guess I need to enter in."
        mc "Okay, let's go!"
        scene bg school_entrance
        with wipeleft_scene
        show camilla frontal sports l1 r1 e1a b1a mb n1 hair_normal at t11 zorder 2
        c "[player]~!"
        mc "Hey Camilla~!"
        c "Tell me, tell me~! What should we do?"
        mc "Alright, the thing is..."
        mc "We have to do a banner and a few decorations for the festival this Monday."
        mc "Since you're very good at painting I think that you'll be very helpful for me."
        c "Crafts, eh? Of course I can help you with that darling~!"
        c "You picked the right person, ehehe!"
        mc "Ehehe, thank you very much."
        c "No problem, that's why I'm here..."
        c "By the way, do you wanna join in the Mixed Martial Arts Club?"
        c "We'll have a lot of fun, I promise~"
        menu:
            "Sure, let's go!":
                c "Yaaay~!"
                c "Let's go then."
                mc "Yeah!"
                call fightingclub
                $ fightingclub_closed = True
                $ accept_fightingclub_offer = "Yes"
                scene bg residential_day
                with wipeleft_scene
                $ stamina -= 5
                pass
            "I'm sorry but I have things to do...":
                c "Uuuuu~!"
                c "Too bad..."
                c "Don't worry then, the next time will be~"
                mc "Okay then, see you this Sunday Camilla."
                mc "And thanks for offering your help. I really apreciate that..."
                c "Uhuhu~! You're welcome..."
                c "I'll be waiting for you~"
                pass
    return
