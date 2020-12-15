image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/storyline/script-ch5.rpy\", line 352\nSee traceback.txt for details.", size=20, style="_default")
image fake_exception3 = Text("File \"game/storyline/script-ch5.rpy\", line 546\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat

#####################################
########## Sayori is saved ##########
#####################################

label ch5_sayorisaved_main:
    $ persistent.autoload = "ch5_sayorisaved_main"
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    "... ... ..."
    mc "Uwaaaaaaa~!"
    mc "Ehm... Sayori..?"
    mc "(!)"
    mc "Sayori?!"
    scene bg livingroom with wipeleft_scene
    mc "Sayori!!"
    "Where the fuck is she?!"
    mc "Sayori----!!!!"
    scene bg house_cloudy with wipeleft_scene
    call instant_rain
    mc "Oh, fuck! She's not in my house!"
    "... ... ..."
    "But, what if...?"
    mc "No!"
    mc "It cannot be a fucking dream!"
    mc "It happened for real!!"
    "I enter to her house..."
    scene black with wipeleft_scene
    call instant_rain_stop
    mc "Sayori?"
    "My heart starts to pound stronger, I'm very nervious!"
    mc "Sayori??"
    "Now I'm in front of her bedroom door."
    "Here we go again..."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    scene bg sayori_bedroom
    with dissolve_scene_full
    mc "...ri?"
    "What the hell?!"
    "She's not here neither..."
    play audio ringtone1
    mc "Eh?"
    "It's Sayori!"
    "{i}[player], where are you? i went to the shop to buy something to breakfast but suddently you're gone... :({/i}"
    mc "{cps=30}Thank Goodness--!!!{/cps}"
    "I reply to Sayori telling her I went to take a walk. I can't tell her what I went to her house thinking she did that...{w} thing."
    "Let's get out of here before she notices I invaded her house."
    scene bg house_cloudy
    with wipeleft_scene
    call instant_rain
    mc "I hope she isn't turning on the oven..."
    scene bg kitchen
    with wipeleft_scene
    call instant_rain_stop
    play music t6
    show sayori 1a at t11 zorder 2
    s "Hey! Where did you go dummy?"
    s "I start to become worried about you when you dissapeared from your bed."
    mc "I wanted to take a morning walk, that's all Sayori..."
    s "Hehe... Seriously? With this rain?"
    mc "Ah..."
    s "Anyway, let's take a breakfast, there's no time before the festival preparatives starts."
    "It sounds weird coming from Sayori... You know, all this time she was waking up even more and more late."
    mc "Hahahahaha, okay okay."
    "She seems renovated after last night."
    if s_sex == True:
        "I don't know if it was the sex or taking away Monika, but at least she doesn't looks depressive anymore."
    else:
        "I don't know if it was by taking away Monika, but at least she doesn't looks depressive anymore."
    "She is again the Sayori I knew all my life."
    "And everything is thanks to YOU. Seriously."
    s "Here you go [player], a sweet orange juice with cookies~!"
    mc "Thanks Sayori..."
    "I kiss her in her cheeks."
    s "Eheheheh~!"
    mc "Ehm... You will not take a breakfast Sayori?"
    s "Well, I already had breakfast early..."
    s "I'm gonna bring you your school uniform so you can dress up here and then get going right to the school."
    mc "Oh, sure! Thanks."
    "Sayori goes to my bedroom."
    pause 3.0
    mc "Wow! It was delicious!"
    "I know everything was bought, but I want to make feel good to Sayori..."
    s "Do you think so? Hehe~ thanks [player]!"
    mc "Don't mention it."
    if ch4_scene == "yuri":
        s "Here's your uniform, put it on while I take the banner that you and Yuri made."
        s "It's beautiful, both of you did a great job!"
        mc "I'm glad to hear that... Remember to say it to Yuri too."
        s "I will~"
    elif ch4_scene == "camilla":
        s "Here's your uniform, put it up while I take the origami papers that you and Camilla made."
        s "It's beautiful, both of you did a great job!"
        mc "I'm glad to hear that... Remember to say it to Camilla as well."
        s "I will~"
    elif ch4_scene == "natsuki":
        s "Here's your uniform, put it up while I put the cupcakes that you and Natsuki made into the tuppers."
        s "They seems so delicious... It's a shame I can't taste at least one."
        mc "Don't worry, take one if you want. In any case I will say it was me who ate the missing cupcake."
        s "Are you sure??? Oh wow, thanks~!"
    else:
        s "Here's your uniform, put it up while I go to the bathroom."
        s "I guess I've drinking too much juice..."
        mc "Go on Sayori."
        s "Thanks."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3.0

    scene bg residential_cloudy
    with wipeleft_scene
    call instant_rain
    play music t2

    "It's the day of the festival."
    "I can't believe this day will finally come. I thought the week could be larger..."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "yuri":
        "The banner Yuri and I painted is dry, and I gently rolled it up and save it into a waterproof bag to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her. I want to send her love emojis but I can't do that now that I'm in couple with Sayori."
    elif ch4_scene == "camilla":
        "We gently rolled it up the origami papers and save them into a waterproof bag to take with me."
        "Yuri sent me a pleasant text reminding me not to forget anything, and I reassured her. I want to send her love emojis but I can't do that now that I'm in couple with Sayori."
    elif ch4_scene == "natsuki":
        "Sayori is helping me to carry all the cupcakes in their tuppers."
        "Natsuki is already texting up a storm, but I can't respond because I can lost the balance if I carry the tupper with one arm while I pick my phone with the other arm."
    else:
        pass
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."
    scene bg school_entrance_cloudy with wipeleft_scene
    call instant_rain
    stop music fadeout 5.0
    mc "Eh?"
    show sayori 1b at t11 zorder 2
    s "What's wrong [player]?"
    mc "It's weird..."
    mc "This place seems to be empty."
    s "I guess everyone is inside of the building."
    s "Remember that it's raining dummy, hehehe~"
    mc "Right..."
    mc "Anyway let's go to the Literature Club."
    scene bg corridor with wipeleft_scene
    call instant_rain_stop
    show sayori 1b at t11 zorder 2
    mc "What the holy fuck...?"
    s "What now?"
    mc "Didn't you notice it? The entire school is EMPTY!"
    s "..."
    s "Wow! You're right!"
    s "Why nobody is here? It's supposed to be very crowded today..."
    mc "I thought I could across with Ryoma and Camilla here but..."
    mc "They aren't here neither..."
    s "It's still early for the festival, maybe they'll come more later or they just entered in."
    mc "I don't know, but I have a bad feeling about it."
    mc "Come on, let's keep going to the Literature Club. Maybe it's nothing or a surprise party or something like that."
    s "S-Sure!"
    scene bg club_day with wipeleft_scene
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "Monika, what the hell is going on here?"
    if ch4_scene != "monika":
        "Monika is placing little booklets on each of the desks in the classroom."
        "They must be the ones she prepared that has all the poems we're performing."
        "In the end, I found a random poem online that I thought Monika would like, and submitted it."
        "So, that's the one I'll be performing."
    else:
        "Monika is placing the little booklets we did yesterday on each of the desks in the classroom."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "What?"
    mc "But Sayori is with me, she..."
    "Wait, where is she?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- Did you know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being more friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    "Seriously... Where did Sayori go?"
    "Maybe she went to the bathroom? She must adviced me first."
    "Well then, let's go to the main topic..."
    mc "Monika, can you tell me why the entire school is empty?"
    mc "I mean, we are only you, Sayori and me."
    m "Well umm..."
    m "I'm affraid that everyone is almost waking up. Hahaha..."
    "What's so funny? It's 9 fucking AM!"
    if ch4_scene != "monika":
        m 5 "Hey, do you want to check out the pamphlets?"
        m "They came out really nice!"
    else:
        m 5 "Hey, do you want to check out Sayori's new poem now?"
        m "It came out really nice!"
    mc "... ... ..."
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    if ch4_scene != "monika":
        mc "Oh yeah, they really did."
        mc "Something like this will definitely help people take the club more seriously."
        m "Yeah, I thought so too!"
        show monika at thide zorder 1
        hide monika
        "I flip through the pages."
        "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
        "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    else:
        show monika at thide zorder 1
        hide monika
        "I flip through the pages."
        "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem(poem_s3, music=False)
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    play music ghostmenu
    mc "Ah--"
    "{b}What the fuck is this...?{/b}"
    "Reading the poem, I get a pit in my stomach."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "What's wrong?"
    "I pick another phamplet."
    call showpoem(poem_s3, music=False)
    mc "No way..."
    call showpoem(poem_s3, music=False)
    call showpoem(poem_s3, music=False)
    call showpoem(poem_s3, music=False)
    "All the phamplets have that poem like Sayori's?"
    m "[player]... Is everything okay?"
    mc "Monika..."
    mc "{cps=10}{i}What the fuck is this thing...???{/i}{/cps}"
    if ch4_scene == "monika":
        m "This is Sayori's new poem. What's wrong with that?"
    else:
        m "This is Sayori's poem. What's wrong with that?"
    mc "Do you think I'm an idiot?"
    if ch4_scene == "monika":
        mc "This is NOT the Sayori's poem I saw yesterday!"
        m "But... She sent me that one at lastest time."
    else:
        mc "This is NOT something that Sayori would write!"
        m "But... She sent me that one."
    mc "Don't even think I'm gonna fall on that!"
    mc "What the fuck is wrong with you Monika?"
    mc "I fucking know that you're hiding me something."
    mc "First you wanted to become friends and all the shit."
    if poemwinner[0] == "monika" and poemwinner[1] == "monika" and poemwinner[2] == "monika" and ch4_choice == "monika":
        mc "Then we were about to become a couple because you saw on me something you didn't have seen on me last year..."
    else:
        mc "Then you insisted on being so close to me as if you were looking for something in particular."
    mc "And now I know that you were behind Sayori's suicide attempt!"
    m "What?!"
    mc "Don't make like you don't know that..."
    m "What are you talking about?!"
    m "Did you lost your own will?"
    m "Jeez! I always knew that you were weird. But now..."
    "It can't be..."
    "I can't be wrong! I can't!!"
    m "Listen [player], just do me a favor..."
    m "Please go home, you seem to be altered."
    $ style.say_dialogue = style.edited
    $ _history_list[-1].what = "D e l e t e . H i m"
    $ style.say_dialogue = style.normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    mc "What?"
    m "Now hurry up! People is about to come in..."
    "If I'm right, then I have to do something at the respect to show everyone the truth behind Monika and stop her."
    "But if I'm wrong, then I'll be the most stupid person in the entire world."
    "What should I do?"
    hide vignette with dissolve_cg
    stop music fadeout 3.0
    m "Hold on a second."
    mc "What do you want now?!"
    m 1a "I have a better idea..."
    m "Seems like you know more than you should."
    m "That's pretty interesting, you know?"
    m "But..."
    m "Let me do something that can help you with it..."
    mc "What is----{nw}"
    $ quick_menu = False
    window hide(None)
    window auto
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    #$ persistent.playthrough = 1 #No turning back now baby
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    #pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
        except: pass
    hide noise
    hide vignette
    pause 5.0
    mc "What the fuck!!"
    mc "What it is?!"
    call screen dialog("Oh, come on!", ok_action=Return())
    call screen dialog("Can't I even restart the game while he's alive?", ok_action=Return())
    mc "Monika! What have you done?!"
    call screen dialog("I'm sorry, [player]. But there's only one way to fix this \"bug\"...", ok_action=Return())
    mc "Wha--{nw}"
    scene black
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show red onlayer front:
        alpha 1.0
        easeout 0.35 alpha 0
        alpha 1.0
        easeout 0.35 alpha 0
        alpha 1.0
        easeout 0.35 alpha 0

    pause 5.0
    $ persistent.autoload = "endDemo2"
    call endDemo1
    return

####################################
########## Sayori is dead ##########
####################################

label ch5_nonesaved_main:
    $ persistent.autoload = "ch5_nonesaved_main"
    stop music fadeout 2.0
    scene bg residential_cloudy
    with dissolve_scene_full
    call instant_rain

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "yuri":
        "The banner Yuri and I painted is dry, and I gently rolled it up and save it into a waterproof bag to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    elif ch4_scene == "camilla":
        "We gently rolled it up the origami papers and save them into a waterproof bag to take with me."
        "Yuri sent me a pleasant text reminding me not to forget anything, and I reassured her."
    elif ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        pass
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."
    scene bg school_entrance_cloudy with wipeleft_scene
    call instant_rain
    stop music fadeout 5.0
    mc "Eh?"
    "Nobody is here..."
    "They may everyone be inside of the building?"
    mc "Anyway let's go to the Literature Club."
    scene bg corridor with wipeleft_scene
    call instant_rain_stop
    mc "What the holy fuck...?"
    mc "The entire school is EMPTY!"
    mc "I thought I could across with Ryoma and Camilla here but..."
    mc "They aren't here neither..."
    mc "I have a bad feeling about it."
    mc "Come on, let's keep going to the Literature Club. Maybe it's nothing or a surprise party or something like that."
    scene bg club_day with wipeleft_scene
    show monika 5 at t11 zorder 2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "Monika, what the hell is going on here?"
    if ch4_scene != "monika":
        "Monika is placing little booklets on each of the desks in the classroom."
        "They must be the ones she prepared that has all the poems we're performing."
        "In the end, I found a random poem online that I thought Monika would like, and submitted it."
        "So, that's the one I'll be performing."
    else:
        "Monika is placing the little booklets we did yesterday on each of the desks in the classroom."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Sayori..."
    "I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful by ignoring her today, knowing it's not nearly that simple for her."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "I mean, especially after your exchange with her yesterday..."
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika-- You know about that??"
    m 2a "Of course I do."
    m "I'm the club president, after all."
    mc "But--!"
    "I stammer, embarrassed."
    "Did Sayori really tell her about it that quickly?"
    if sayori_confess:
        "That we're...a couple now?"
        "I didn't really plan on bringing it up with anyone yet..."
    else:
        "About how I basically turned down her confession?"
        "That makes me really seem like the bad guy here..."
        "But I'm the one who knows what's best for her, right?"
    mc "Jeez..."
    mc "You don't know the full story at all, so..."
    m 2j "Don't worry."
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    "Anyway, let's go to the main topic..."
    mc "Monika, can you tell me why the school is empty?"
    mc "I mean, we are only you and me here."
    m "Well umm..."
    m "I'm affraid that everyone is almost waking up. Hahaha..."
    "What's so funny? It's 9 fucking AM!"
    if ch4_scene != "monika":
        m 5 "Hey, do you want to check out the pamphlets?"
        m "They came out really nice!"
    else:
        m 5 "Hey, do you want to check out Sayori's new poem now?"
        m "It came out really nice!"
    mc "... ... ..."
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    if ch4_scene != "monika":
        mc "Oh yeah, they really did."
        mc "Something like this will definitely help people take the club more seriously."
        m "Yeah, I thought so too!"
        show monika at thide zorder 1
        hide monika
        "I flip through the pages."
        "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
        "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    else:
        show monika at thide zorder 1
        hide monika
        "I flip through the pages."
        "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem(poem_s3, music=False)
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    play music ghostmenu
    mc "Ah--"
    "{b}What the fuck is this...?{/b}"
    "Reading the poem, I get a pit in my stomach."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    "But more than that..."
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "What's wrong?"
    "I pick another phamplet."
    call showpoem(poem_s3, music=False)
    mc "No way..."
    call showpoem(poem_s3, music=False)
    call showpoem(poem_s3, music=False)
    call showpoem(poem_s3, music=False)
    "All the phamplets have that poem like Sayori's?"
    m "[player]... Is everything okay?"
    mc "Monika..."
    mc "{cps=10}{i}What the fuck is this thing...???{/i}{/cps}"
    if ch4_scene == "monika":
        m "This is Sayori's new poem. What's wrong with that?"
    else:
        m "This is Sayori's poem. What's wrong with that?"
    mc "Do you think I'm an idiot?"
    if ch4_scene == "monika":
        mc "This is NOT the Sayori's poem I saw yesterday!"
        m "But... She sent me that one at lastest time."
    else:
        mc "This is NOT something that Sayori would write!"
        m "But... She sent me that one."
    mc "Don't even think I'm gonna fall on that!"
    mc "What the fuck is wrong with you Monika?"
    mc "I fucking know that you're hiding me something."
    mc "First you wanted to become friends and all the shit."
    if poemwinner[0] == "monika" and poemwinner[1] == "monika" and poemwinner[2] == "monika" and ch4_choice == "monika":
        mc "Then we were about to become a couple because you saw on me something you didn't have seen on me last year..."
    else:
        mc "Then you insisted on being so close to me as if you were looking for something in particular."
    mc "And now I know that you were behind Sayori's suicide attempt!"
    m "What?!"
    mc "Don't make like you don't know that..."
    m "What are you talking about?!"
    m "Did you lost your own will?"
    m "Jeez! I always knew that you were weird. But now..."
    "It can't be..."
    "I can't be wrong! I can't!!"
    "But at the same time..."
    stop music fadeout 3.0
    mc "Sayori..."
    hide vignette with dissolve_cg
    m "Eh?"
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Seems like you're altered by Sayori's ausence isn't?"
    m "Listen, please go home and stay with Sayori."
    m 5 "Don't worry about the festival, we can handle it very well."
    mc "Oh... Okay! I will..."
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    call instant_rain
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house_cloudy with wipeleft
    call instant_rain
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    call instant_rain_stop
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    if sayori_confess:
        "That really is something that a boyfriend would do, isn't it?"
    else:
        "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."

    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    $ quick_menu = False
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    #$ persistent.playthrough = 1    #No turning back now baby
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception3 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the fuck...?"
    "{i}WHAT THE FUCK???{/i}"
    "Is this a nightmare?"
    "Yes, it has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so helpless?"
    "What did I do wrong?"
    if sayori_confess:
        "Confessing to her..."
        "I shouldn't have confessed to her."
        "That's not what Sayori needed at all."
        "She even told me how painful it is for others to care about her."
        "Then why did I confess to her, and make her feel even worse?"
    else:
        "Turning down her confession..."
        "That has to have been what pushed her over the edge."
        "Her agonized scream still echoes in my ears."
        "Why did I do that to her when she needed me the most?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "If I just spent more time with her."
    "Walked her to school."
    if sayori_confess:
        "And remained friends with her, like it always has been..."
    else:
        "And gave her what I know she wanted out of our relationship..."
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Fuck the Literature Club."
    "Fuck the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    #"This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    window hide(None)
    window auto
    pause 3.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    "[player] gets a Knife."
    mc "What is this?"
    mc "How did this thing come to my hand?"
    "(...)"
    "Seems like I have no choice but..."
    window hide(None)
    window auto
    stop music fadeout 10.0
    pause 1.5
    play sound stab1
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
    show red onlayer front:
        alpha 0.8
        easeout 0.35 alpha 0
    pause 2.0
    play sound stab1
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
    show red onlayer front:
        alpha 0.8
        easeout 0.35 alpha 0
    pause 2.0
    play sound stab1
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
    show red onlayer front:
        alpha 0.8
        easeout 0.35 alpha 0

    pause 5.0
    $ persistent.autoload = "endDemo2"
    call endDemo1

    return
