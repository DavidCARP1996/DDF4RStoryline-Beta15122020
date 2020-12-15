label ch4_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    play music t6

    "It's already Sunday."
    if ch4_scene == "yuri":
        "I've been getting increasingly anxious about Yuri's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "Yuri is clearly an introvert and also an intimate person in general."
        "There's no doubt that she'll open up a little bit when it's just the two of us."
        "Meanwhile, we've even been texting occasionally."
        "She was extremely apprehensive at first, but it wasn't long before I was already learning more about her."
        "But putting Yuri aside..."
    elif ch4_scene == "natsuki":
        "I've been getting increasingly anxious about Natsuki's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "I wonder if she'll act any different when it's just the two of us?"
        "Meanwhile, she's been texting me a lot."
        "We sent each other one after exchanging numbers to double-check, but it turned into conversation."
        "She's almost a different personality on the phone, using tons of emoji and cute language."
        "She also really likes complaining about things, but I kind of saw that one coming."
        "But putting Natsuki aside..."
    elif ch4_scene == "camilla":
        "I've been getting increasingly anxious about visiting Camilla."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "Camilla doesn't hide her excitement about my visit, she's always saying me that she can't wait for my presence in her house."
        "I responds in the same way to keep her happy about this."
        "At the same time, I'm asking Yuri about her main idea of the banner I'll make with Camilla."
        "She gave me all the instructions in a large text, accompained with an sketch drawing of how she imagines the banner."
        "Fortunatelly, Camilla can understand such concept better than me, so I'm relieved that she will helping on it."
        "But putting Camilla aside..."
    elif ch4_scene == "monika":
        "I've been getting increasingly anxious about Monika's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "I can't believe that MONIKA herself is coming to my house."
        "I don't know what the whole school will think about it if she dares spread the gossip."
        "Meanwhile, we've even been texting occasionally."
        "She just doesn't stops with her exaggerated sympathy with me."
        "She's also sending me normie memes because she knows I'm into memes, but she doesn't know that these aren't my kind of humor."
        "But putting Monika aside..."
    else:
        "I've been getting increasingly anxious about Camilla's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "Honestly, I never had the chance to invite her or Ryoma in my house. The only person who paid me a visit all this time was always Sayori."
        "So I bought some food in case she wants to snack..."
        "Meanwhile, we've been texting a lot."
        "She's nice even via SMS, reading her messages she is obviously excited for the visit to my place."
        "But putting Camilla aside..."
    "I haven't heard a thing from Sayori since she left club early the other day."
    "It's not like we text each other all the time or anything..."
    "But I've been worried about her in the back of my mind."
    "Between what Sayori said, and what Monika said..."
    "Is it really okay for me to put Sayori's feelings aside when she might need me?"

    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    if ch4_scene == "camilla":
        "I decide to visit Sayori before visiting Camilla."
    else:
        "I decide to visit Sayori before [ch4_name] comes over."
    "Rather than asking, I simply tell her \"I'm coming over\", much like we've done in the past."
    "Once I reach Sayori's house, I knock on the door before entering it myself."
    "Again, we used to play so often that we've made it a habit of simply entering each other's houses like we were family."
    "Anyway, her family was like my \"family\" as well all this time...{w} I won't go into details about that.{nw}"
    scene black with wipeleft
    "The house is quiet."
    "Sayori isn't anywhere on the first floor, so I assume she's up in her room."
    "It's already strange of her not to run down and greet me."
    "I head up to her bedroom, where I finally find her."
    scene bg sayori_bedroom with wipeleft
    mc "Sayori?"
    play music t10
    show sayori 1ba  at t11 zorder 2
    s "Hi [player]~"
    show sayori 1by
    "I sit down in her room."
    "Sayori forces a smile, but it's easy to tell that she's different."
    "There's a minute of silence between us."
    s "You haven't come over like this in a long time, have you?"
    mc "Ah... I guess you're right."
    mc "It has been a long time."
    mc "Not much has really changed, has it?"
    "Sayori's room is as messy as it's always been."
    "I also recognize the same stuffed animals and wall decorations that she's had for years now."
    s 2bl "Ehehe~"
    s "If you came over more often, it wouldn't be such a mess."
    mc "That's because I end up cleaning it for you..."
    s 1bb "How come you suddenly wanted to come over today?"
    s "Aren't you supposed to see [ch4_name] today?"
    mc "Yeah, but..."
    if not ch4_sayoriknowsvisit:
        mc "...Wait, how did you know that?"
        "Sayori had already left by the time we decided that last meeting."
        s 1ba "Monika told me."
        s "It's only natural for her to keep me informed about the festival preparations, right?"
        mc "Ah, that's true..."
    if ch4_sayoriknowsvisit:
        mc "I'm still worried about you, so I decided to check up on you first."
        s "Hehe... You really worry too much about me, isn't?"
        mc "Of course."
    mc "But what about you?"
    if ch4_scene != "monika":
        mc "Aren't you going to be helping Monika today?"
        s 4bb "Of course!"
        s "But I'm just helping her online."
        s "We didn't plan to meet up or anything."
        mc "Ah, so it's just me and [ch4_name], then..."
        pass
    else:
        mc "Aren't you going to be helping us today?"
        s 4bb "Yeah, but..."
        s "Considering that you choosed help Monika as well."
        s "I would only be a hindrance between you two. So..."
        "What?!"
        mc "Sayori, you really mean that?!"
    s 1ba "Yep~"
    "There's more silence between us."
    show sayori 1bk
    "Sayori stares in a random direction."
    "Everything about her behavior is really uncharacteristic."
    "I finally get to the point."
    mc "I just...wanted to see how you were doing."
    mc "After you left on Friday."
    mc "When something's wrong, you can't hide it from me!"
    mc "I know you too well."
    mc "So..."
    "Sayori smiles, shaking her head."
    s 1bd "That's no good, [player]."
    mc "Eh?"
    s "Why can't it just be like it's always been?"
    s 1by "This is all my fault."
    s "If I didn't get so weak and accidentally express my feelings..."
    s 1bk "If I didn't make that stupid mistake years ago..."
    s "Then you wouldn't have been worried about me at all."
    s "You wouldn't have come here."
    s 1bd "You wouldn't have even been thinking about me right now."
    s "But this...is just my punishment, isn't it?"
    s "I'm getting punished for being so selfish."
    s "I think that's why the world decided to have you come over today."
    s "It just wants to torture me."
    s 4bq "Ehehe~"
    mc "Sayori!"
    show sayori 4bb
    "I grab Sayori by the shoulders."
    mc "What on Earth are you saying?!"
    mc "Are you listening to yourself right now?"
    mc "I know something happened to you."
    mc "There's no other explanation for you to be like this."
    mc "So tell me, already...!"
    mc "Until I know, I won't be able to stop thinking about it!"
    s 4bl "Ah..."
    s "Ahaha..."
    "Sayori gives me an empty smile."
    s 4by "You really put me in a trap, [player]."
    s "But..."
    s 1ba "You're wrong."
    s "Nothing happened to me."
    s "I've always been like this."
    s "You're just seeing it for the first time."
    mc "Seeing what?"
    mc "What are you talking about, Sayori?"
    s 1bq "Ehehe~"
    s 1ba "You're really just going to make me say it, aren't you, [player]?"
    s "I guess I have no choice this time."
    s 1bc "The thing is..."
    s "I've had really bad depression my whole life."
    s 1bb "Did you know that?"
    s "Why do you think I'm late to school every day?"
    s "Because most days, I can't even find a reason to get out of bed."
    s 1by "What reason is there to do anything when I fully know how worthless I am?"
    s "Why go to school?"
    s "Why eat?"
    s "Why make friends?"
    s "Why make other people put their energy and caring to waste by having them spend it on me?"
    s "That's what it feels like."
    s "And that's why I just want to make everyone happy..."
    s "Without anyone worrying about me."
    mc "..."
    "I'm in shock."
    "I can't even figure out how to respond."
    "How is it possible that Sayori kept this from me the entire time that I've known her?"
    "Did she really want so badly for me to just not think about her?"
    mc "...Why, Sayori?"
    s 1bg "Eh...?"
    mc "Why is it that you've never told me about this?"
    mc "It almost feels like I've been betrayed as your close friend."
    mc "Because if I knew, I would have done everything I could to support you!"
    mc "Even if there's only so much that I could do..."
    mc "I would have tried a little bit harder to make every day a little better for you."
    mc "That's why I'm your friend!"
    mc "All you had to do was tell me!"
    s 1bk "You don't understand at all, [player]."
    s "Why do you think I didn't tell you?"
    s 1bd "Because if I told you, then you would have to waste effort caring about me instead of doing important things."
    s "I don't want to be cared about."
    s "It's bittersweet, when people try to care about me."
    s 1ba "It feels nice sometimes."
    s "But it also feels like a bat being swung against my head."
    s 4bq "Ahaha~"
    s 4ba "That's why I wanted so badly for you to make friends with everyone else..."
    s "Helping everyone be happy together is the best thing for me."
    s 1bb "But then, I discovered something else, too."
    s "Seeing you make friends and get closer with everyone in the club..."
    s 1bk "It feels like a spear going through my heart."
    s "So, that's why."
    s "That's why I decided the world just wants to torture me."
    s 1by "Every path leads to nothing but hurt."
    s "Ahaha~"
    mc "You're right that I don't understand..."
    mc "I don't understand your feelings at all, Sayori."
    mc "But I don't need to understand."
    mc "Whatever it takes for me to help you stop hurting..."
    mc "That's what I'll do."
    s 1bd "No, [player]."
    s "There's nothing."
    s "Nothing at all."
    s "The only thing that could have helped is if everything could be like it always was."
    s 1bk "But I was selfish."
    s "I finally showed you what a horrible person I am."
    "Tears streak down Sayori's face."
    s 1bv "I made you join the literature club because I was selfish."
    s "And I was punished by my heart hurting in a way that I couldn't understand."
    s "And now you came here and I made you hurt, too."
    s 1bt "I'm just weak and selfish."
    s "That's all I am."
    s "And that's why I'm going to accept these punishments."
    s 1bv "Because I deserve every last one...!"
    "Without thinking, I once again grab Sayori's shoulders."
    "This time, I pull her into a tight embrace."
    scene black with dissolve_cg
    s "A-Ah--"
    s "[player]..."
    mc "Sayori."
    mc "I don't care if you feel selfish."
    mc "I'm really happy that you convinced me to join the club."
    mc "Seeing you every day makes it worthwhile enough."
    mc "If I make friends with everyone else, then that's just a bonus."
    mc "But please never underestimate how much I care about you."
    mc "I wouldn't have it any other way."
    s "[player]..."
    "Sayori isn't hugging me back."
    "Despite my arms being wrapped around her, Sayori's arms remain at her sides."
    "She starts sobbing next to my ear."
    s "No..."
    s "Don't do this...to me..."
    s "Please don't do this..."
    s "[player]..."
    s "I..."
    "Sayori barely manages to speak between her sobs."
    "I don't know if I'm doing the right thing."
    "But all I want is for her to know that I care."
    mc "If you have it in you to call yourself selfish, then you have to let me be selfish too."
    mc "No matter what it takes, I'll figure out what needs to change."
    mc "I'll make these feelings go away."
    mc "And if there's anything that you need me to do..."
    mc "Then you'd better tell me."
    mc "I'll get mad if you don't."
    s "..."
    s "I...don't know..."
    s "I don't know..."
    s "I don't know."
    "Gently, Sayori finally puts her arms around me in return."
    s "I don't know anything."
    s "It's all really scary..."
    s "I don't understand any of my feelings, [player]..."
    s "The only time I'm not feeling nothing is when I'm feeling pain."
    s "But..."
    s "Your hugs are so warm..."
    s "...And that's really scary, too."
    scene bg sayori_bedroom
    show sayori 1bv  at i11 zorder 2
    with dissolve_cg
    "Sayori lets me go."
    "As she does so, I let her go as well."
    mc "The festival is tomorrow."
    s 1bk "Yeah..."
    mc "It's going to be fun, right?"
    s "Yeah."
    mc "How would you like for me to spend it all with you?"
    s 1bh "U-Um..."
    s "Ah--"
    mc "It's what I want."
    mc "I promise."
    s 1bk "I..."
    s "I think that would be nice, then..."
    mc "Yeah."
    "Sayori wipes her eyes."
    "If I could spend the whole day here, I would."
    mc "Of all days, this has to be the one where I have other plans..."
    mc "Maybe I should cancel--"
    s 1bh "No, don't--!"
    s 1bg "Please don't..."
    s "If you did that...then I really wouldn't forgive you."
    mc "But..."
    if ch4_scene == "camilla":
        mc "It's almost time to be already in Camilla's house..."
    else:
        mc "It's almost time for [ch4_name] to meet me at my house..."
    mc "At the very least, do you want to come along and help out?"
    mc "It would be fun."
    "To my surprise, Sayori shakes her head."
    s 1bd "I'm sorry."
    s "I don't know if that would be very good for me today."
    s "You understand, right?"
    mc "Ah..."
    mc "It's...kind of hard for me to fully understand."
    mc "But I'm trying my hardest."
    s "It's okay."
    s "Don't worry too much about it."
    s 4ba "I'll see you tomorrow, okay?"
    mc "...Alright."
    mc "I look forward to it."
    scene bg residential_day with wipeleft_scene
    "I say goodbye to Sayori and exit her house."
    "On the way home, I find myself still feeling uneasy."
    if ch4_scene == "camilla":
        "But it's hard for me to keep thinking about it when I'm about to visit Camilla, too..."
    else:
        "But it's hard for me to keep thinking about it when [ch4_name] is about to come over, too..."
    "I think Sayori is right."
    "I shouldn't be worrying too much, and we're definitely going to have a great time tomorrow."
    "I should just focus on what's ahead of me!"
    call expression "ch4_exclusive_" + ch4_scene
    call ch4_end

    return


label ch4_exclusive_natsuki:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene
    "I spend only a few minutes back at home anxiously awaiting Natsuki's arrival."
    "Before I know it, she texts me to let me know she's outside the front door."
    "Without delay, I open the front door to let her in."
    show natsuki 2bj at t11 zorder 2
    mc "..."
    n "'Sup?"
    mc "...Hey."
    "I don't know what I was expecting, but seeing Natsuki in something other than her school uniform totally threw me off."
    "Seeing her in such cute clothes makes the uniform seem totally unfitting in comparison."
    n 4bc "Jeez, don't make it feel so awkward already!"
    n "It's gonna be a long afternoon, so don't be weird just because you're not used to seeing me outside of school."
    n "Anyway, I'm coming in."
    scene bg kitchen
    show natsuki 1bj at t11 zorder 2
    with wipeleft
    mc "I see you brought a lot of stuff..."
    "Natsuki is carrying a large bag that is probably full of baking supplies."
    n 2bj "Well, I didn't want to come all this way to find out that your kitchen isn't equipped for the job."
    n "You bought everything I asked you to, right?"
    mc "Yeah, I did."
    "Yesterday, Natsuki asked me to buy a bunch of ingredients if I didn't already have them at home."
    n 2bl "Good!"
    n "Glad I could count on you to do your part."
    mc "Well...of course."
    "I'm surprised to hear Natsuki suddenly say that, rather than something snarky like she usually does."
    "Could it be that she is a little different outside of school after all?"
    mc "Anyway, let's go to the kitchen..."
    n 2by "What, you're not even gonna offer to take this heavy bag from me?"
    n "Where's your hospitality, [player]?"
    mc "Come on..."
    mc "Since when did I need to be a gentleman?"
    "I grab the bag Natsuki holds out to me."
    mc "Ghk--"
    mc "This is ridiculously heavy--!"
    n 4bz "Ahaha!"
    n "I carried that all the way here."
    n 4bl "Are you impressed?"
    mc "I see now..."
    mc "Yeah, I am impressed, Natsuki."
    mc "It seems like I always underestimate you."
    n 4by "Ehehe~"
    n "It's because I'm so small, isn't it?"
    n 4ba "You jerk."
    "Natsuki hits a fist into my chest."
    mc "Hey, hey."
    mc "Your size has nothing to do with it."
    mc "Do you really hate being small that much?"
    n 1bk "Eh?"
    n "Um..."
    n 1bc "It's not like I hate it..."
    n "I mean, sometimes I like proving people wrong when they only think I'm worth my size."
    n 1ba "It's fun when I get to be small and also better than other people."
    n "But..."
    n 5bw "...Jeez, never mind!"
    n "What are you making me say?"
    n 5bq "Don't think you can make me talk about weird things just because we're not at school!"
    n "Are we getting started, or what? There's a lot of stuff I gotta teach you."
    mc "Ahaha."
    n 5bn "What??"
    mc "That's a little bit more like you."
    mc "You're more fun when you just speak your mind like that."
    n 1bm "H-Hey!"
    n "Now you {i}are{/i} treating me like a kid!"
    n "I was just trying to be a little nicer to you, you know."
    n 1br "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--"
    n 1bo "A-Ah--"
    "Natsuki catches her words, and her face turns red."
    mc "Natsuki..."
    n 1bp "Forget it!"
    n "I didn't say anything!"
    mc "I should apologize."
    n 1bh "Eh?"
    mc "I appreciate that you were trying to be nicer."
    mc "I should have been a little more considerate, too."
    mc "But also..."
    mc "If that's what you're thinking, then you should know that there are tons of guys who are into body types like yours."
    n 1bq "Ah..."
    n "How would...you know that, anyway?"
    mc "Just trust me on this one."
    n "..."
    n 5bx "...Gross."
    mc "Hey!"
    mc "Was that to me?"
    n 5bw "Who else?"
    mc "Man..."
    mc "Let's just get started already."
    n 2bl "Ahaha!"
    n "You get all sour when a girl calls you gross."
    n 2bd "I finally found your weakness, [player]."
    "Natsuki smiles deviously."
    mc "Please spare me..."
    "Well, if Natsuki decides to dish out more insults like that, there's no way I'm not fighting back."
    "But she's satisfied enough for now, finally starting to pull things out of her bag so we can get started."

    scene bg kitchen
    with wipeleft_scene
    "Before long, the whole kitchen is a mess."
    "Spoons, dirty bowls, flour, spilled fluid, and plastic bags are strewn about every countertop."
    "The mixer isn't big enough to make all the batter at once, so we've had to do it several times."
    "Meanwhile, Natsuki is babysitting all of my movements to make sure I don't mess up her precious baking."
    show natsuki 2bk at t11 zorder 2
    n "[player], where did you put the food coloring?"
    n "The batter's going in the oven soon, so I need to fill the trays."
    mc "I think it's still in the bag next to the table."
    mc "What are you using it for?"
    n 4bl "To color the batter, of course!"
    n 4bj "I'm making each tray a different color."
    n "That way, even if the flavors aren't different, everyone can still pick their favorite."
    mc "Ah, that's a cute idea."
    mc "Are we doing anything like that with the icing?"
    n 4bk "Do you want to?"
    mc "Ah..."
    mc "You're asking me?"
    mc "I don't really have a preference, so..."
    n 1bm "Come on..."
    n "You're not putting any heart into this at all!"
    n "Can't you at least try to have fun?"
    mc "I'm having fun..."
    "I'm not really sure what Natsuki is trying to get out of me."
    "Meanwhile, I see her separate the batter into smaller bowls and put a few drops of food coloring into each."
    mc "Ah, that does look pretty cool."
    n 2bj "See?"
    n "It's not like baking is just about following instructions."
    n "The presentation is where you get to be creative and have the most fun."
    n "It's a million times more worth it in the end if just looking at it makes everyone's eyes lighten up."
    mc "Like the ones you made on my first day, huh?"
    "I recall Natsuki proudly presenting her cat-shaped cupcakes, and Sayori and Monika's delighted expressions."
    "I wonder if I can make Natsuki proud like that, too."
    mc "Yeah..."
    mc "Maybe I will use the food coloring, then."
    n "Sounds like you're starting to understand."
    n "Just make sure you completely finish mixing the icing before you mess with the food coloring."
    mc "Yeah, it's getting there."
    "We were using the electric mixer for the batter, so I got stuck with a whisk and a huge bowl for the icing."
    n 4bc "Eh?"
    n "The icing's still all lumpy!"
    n "Are you even trying?"
    mc "Well, yeah..."
    mc "It'll just take a little longer."
    n 4bg "Jeez, I'll be here all night if you do it like that."
    n "Here, look."
    "Natsuki grabs the whisk from me and uses her other hand to tilt the bowl back."
    n 4be "You really need to...beat...the crap out of it!"
    "After a few seconds, the consistency of the icing has already improved."
    n 4ba "See?"
    "As if to emphasize, Natsuki sticks a finger in the icing and pops it in her mouth."
    "I reluctantly start to do the same."
    n 1bh "Hey!"
    "Natsuki suddenly grabs my wrist."
    n 4bh "I don't want {i}your{/i} gross fingers in my icing."
    mc "Your icing, eh?"
    mc "Are you forgetting who did all the work?"
    "I start to fight back, trying to inch my finger toward the bowl."
    n 4by "Don't make me beat the crap out of you next!"
    mc "I'd like to see you try!"
    "I push harder, just enough for my finger to reach the icing."
    "I triumphantly scoop some with my finger just as Natsuki tugs with all her might."
    mc "Ah--!"
    "The force of Natsuki pulling me causes me to stumble, making her stumble in turn."
    n 1bx "Gross!"
    n "You got it on my face!"
    mc "Whose fault is that?!"
    "There's a big glob of icing on Natsuki's cheek."
    n 1bw "Nnn--"
    "She tries to reach it with her tongue, but it's too far away."
    n 1br "Jeez..."
    n "You know what?"
    n 4bd "Take this!"
    "Natsuki instead wipes it off with her finger before shoving her finger toward my own face."
    mc "You wish--!"
    "I'm faster."
    "I grab her wrist with my hand before it reaches my face."
    "Natsuki tries to use her other hand to fight back, but I grab that one as well."
    $ persistent.clear[10] = True
    scene n_cg3_base
    show n_cg3_exp1
    show n_cg3_cake
    with dissolve_cg
    n "Ahahaha! Stop!"
    mc "Not until you apologize for calling me gross!"
    n "Fine, fine!"
    n "I'm sorry for calling you gross."
    n "You know I don't mean it."
    n "It's just fun seeing you react to it."
    n "...You do that to me all the time, you know!"
    n "Saying dumb things just to get a reaction out of me."
    n "You really shouldn't tease girls like that."
    mc "Is that so?"
    mc "In that case, I probably shouldn't do this, either..."
    show n_cg3_cake at cgfade
    hide n_cg3_cake
    "I take Natsuki's finger and put it in my mouth, licking off the icing."
    show n_cg3_exp1 at cgfade
    show n_cg3_exp2 at cgfade
    hide n_cg3_exp1
    n "W-W-What--?"
    n "D-Did you seriously just--"
    n "A-Ah--"
    "Natsuki is so surprised that she can't even figure out how to get mad at me."
    "Her face is entirely red."
    hide n_cg3_exp2
    n "[player]..."
    n "You really shouldn't do that kind of thing to girls...unless you really like them..."
    n "You know that...right?"
    mc "..."
    "What kind of question is she asking me, just like that?"
    "How did the mood turn to this so quickly?"
    mc "I..."
    "Natsuki gazes at me in silence."
    "I notice her shallow breaths."
    "Why am I starting to feel dizzy...?"
    n "Eh?!"
    scene bg kitchen with dissolve_cg
    "Out of nowhere, the fire alarm starts going off."
    "Natsuki rushes over to the oven."
    mc "Is something burning?"
    mc "I thought you didn't put the cupcakes in yet."
    show natsuki 1bw at t11 zorder 2
    n "{i}*Cough*{/i}"
    n "No wonder..."
    n 1bb "You left a dirty tray in here, dummy!"
    n "How could you make a mistake like that?"
    mc "You should have checked before turning the oven on!"
    n 1bs "Don't blame me for your mistakes!"
    n "Jeez..."
    "Natsuki uses an oven mitt to grab the blackened tray out of the oven."
    "She sets it on top of the stove."
    "In another moment, the fire alarm stops."
    n 1bq "Anyway..."
    n "I'm...putting them in the oven now."
    mc "Yeah..."
    "The tension from the moment before still lingers over our heads."
    "But the moment has already been lost."
    "I watch as Natsuki slides the cupcake trays into the oven."
    "Then, I reluctantly pick up the whisk and continue with the icing, like nothing ever happened."

    scene bg kitchen
    show natsuki 4bz at t11 zorder 2
    with wipeleft_scene
    n "Ahh, that smells so good!"
    "The cupcakes are ready to be pulled out of the oven."
    "As soon as Natsuki opens the oven door, a blast of sweet-smelling warm air fills the room."
    n 4bl "Look at how cute they all look!"
    "She proudly shows off the different-colored cupcakes in each of the trays."
    mc "They'll look even better once we add the icing."
    n 2ba "Not like you need to tell {i}me{/i} that!"
    n "I brought decorating stuff, so I hope you can get creative."
    n "Here, scoop the icing into these bags."
    "Natsuki hands me some plastic bags."
    n 2bj "I have these nozzles that will make it look nice and fluffy."
    n "This one can even make flowers!"
    n "We probably won't be using it this time, though."
    mc "What's this one for?"
    "I pick up one of the nozzles that has a much thinner tip than the others."
    n 4bk "That one's really thin, so you can use it to make stripes or other patterns."
    n "But you can also use it to write stuff on a cake."
    n "Like, 'happy birthday!' or whatever."
    mc "Huh, I see..."
    mc "That gives me an idea, actually."
    n "Eh?"
    mc "Well, it's a literature event, right?"
    mc "We could make it more literature-themed by writing a different word on each of the cupcakes."
    mc "It would be fun to see people choose their cupcake based on a word they like."
    n 1bq "Uu..."
    mc "Hm?"
    n "I was kind of expecting you to say something really stupid..."
    n 1bs "But that's actually...a really cute idea, so..."
    mc "Ahaha."
    mc "Maybe I'm getting it from you."
    n 5bh "W-What's that supposed to mean?"
    n "I'm not cute!"
    mc "Come on..."
    mc "We're not at school, nobody's judging."
    mc "You can't dress and act like this and not expect me to think you're cute."
    n 5bs "W-Well..."
    "Natsuki's voice trails off."
    n "Same with you..."
    mc "Eh?"
    mc "Did you say something?"
    n 1bw "N-No, nothing!"
    n "Let's just do the icing!"
    "Natsuki picks up the pace and fastens a nozzle onto each of the bags."
    n 1bh "There's a lot to do, so we shouldn't be wasting time!"
    n "Here, I'll show you how to do it."
    "Without giving me a chance to think about before, Natsuki quickly moves on."
    "She shows me how to apply the icing, and then we each get to work."

    scene bg kitchen with wipeleft_scene
    "When we're finally finished, Natsuki puts them all side by side to admire our work."
    show natsuki 4bl at t11 zorder 2
    n "Look at how pretty they are together!"
    mc "Yeah, they are, aren't they?"
    n 1bm "Uu... I wish I could have one now!"
    mc "Well, there's no reason you can't, right?"
    mc "I don't see any harm in that."
    n 1bc "Well, yeah, but..."
    n "My dad's making dinner tonight, so I really need to save my appetite."
    mc "Ahaha."
    mc "Sayori's the exact opposite in that regard."
    mc "If she was here, we'd probably be down ten cupcakes already."
    mc "And she would still eat dinner."
    n 4bg "Come on, that's just unhealthy!"
    n 4bs "Besides, when my dad cooks, I need to eat as much of it as I can..."
    n 4bq "...Well, anyway!"
    n 4bc "I was hoping we would have time for manga, but I need to be home for dinner..."
    mc "Ah, already?"
    mc "That's a shame."
    n 1bg "It's your fault for working so slowly!"
    n "You should have thought about that."
    n "It's not like you'll always have this chance."
    mc "Man..."
    "As usual, Natsuki places the blame on me."
    n 2bk "You can bring the cupcakes tomorrow, right?"
    n "If you and Sayori each carry some, then you can probably do it in one trip."
    mc "Yeah, I can do that."
    mc "And don't worry, I won't let her eat any."
    n 2ba "Ahaha."
    n "I wish she would listen to me the way she listens to you."
    mc "Ah..."
    mc "Yeah."
    show natsuki at thide zorder 1
    hide natsuki
    "I again think back to the conversation I had with Sayori earlier today."
    "I felt so helpless."
    "Sayori always does listen to me, but at that point it felt like she couldn't listen to me at all."
    show natsuki 4bl at t11 zorder 2
    n "Okay, I'm all packed up."
    n "Good work today!"
    mc "You too."
    mc "I'll walk you out...I guess."

    scene bg house with wipeleft_scene
    "Just like that, Natsuki is already about to leave."
    "It feels like the afternoon went by in a flash."
    "More than that..."
    "Did I even take the opportunity to get closer to her, like I wanted?"
    show natsuki 1bh at t11 zorder 2
    n "Well..."
    n "I guess I'll be off, then..."
    n 1bq "Thanks for all the help and everything..."
    n "I'll see you tomorrow."
    mc "Wait, Natsuki."
    n 1bh "Eh?"
    mc "What you said before...about not always having this chance."
    mc "It doesn't have to be that way at all!"
    mc "I had fun today."
    mc "You showed me how fun baking can be, like you wanted."
    mc "But aside from that..."
    mc "You can come over anytime, okay?"
    mc "I think that if possible, I'd like to spend more time like this."
    mc "If you want to read manga, or go out somewhere--"
    n 1bm "Um--"
    n "Do you...really mean that?"
    "Natsuki looks at me tensely, like she's trying to hide her expression."
    mc "Yeah."
    mc "I want to spend more time with you."
    n 1bq "[player]..."
    n "I thought you only cared about getting this done..."
    n 1br "Uu..."
    n 1bn "I'm sorry I had to leave so early today."
    n "I really didn't want to!"
    n "I would really...stay here longer if I could."
    n "I feel the same way as you, so..."
    stop music fadeout 2.0
    show natsuki 1bi at face with dissolve
    "Natsuki suddenly gets closer to me."
    mc "Wait, Natsuki--"
    "Standing inches from me, Natsuki looks up at me."
    "I feel her fingers gently clutch at the sides of my shirt, as if holding onto me."
    "Her rose-colored cheeks and matching eyes fill my vision, along with her slightly-parted lips."
    "What is happening...?"
    "My head starts to go dizzy as I feel her soft breaths against me."
    n 1bh "I've felt it..."
    n "For a while now..."
    n 1bo "--!!"
    show natsuki at t11 zorder 2
    "Natsuki suddenly jumps back."
    n "S-Sayori?!"
    mc "Eh?!"
    show natsuki at t22 zorder 2
    show sayori 1bl  at f21 zorder 3
    s "Ah..."
    s "H-Hi, [player]..."
    mc "Sayori--!"
    mc "Just now, we weren't--"
    s 1bq "Ehehe~"
    s "It's okay, [player]."
    s 1ba "I just stopped by to say hi~"
    show sayori at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5bq "A-Ah..."
    n "Well..."
    n 5bw "Y-You should have come a little earlier!"
    n "I'm already on my way out, so..."
    show natsuki at t22 zorder 2
    show sayori at f21 zorder 3
    s 1bh "Aw, really?"
    s "That's too bad..."
    show sayori at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2bq "Yeah, well..."
    n "I'll still see you at the festival tomorrow, so it's fine."
    n 2bb "Just don't eat any cupcakes before then!"
    n "Anyway, later!"
    show natsuki at lhide
    hide natsuki
    "Clearly flustered, Natsuki hurries off, and Sayori waves goodbye."
    return

label ch4_exclusive_yuri:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene
    "As I approach my house, I see something that makes me feel a moment of panic."
    mc "Yuri--?"
    show yuri 2bq at t11 zorder 2
    y "Ah..."
    y "Thank goodness..."
    mc "You're a little early..."
    mc "I'm sorry I wasn't home yet!"
    mc "Were you waiting for a long time?"
    y 1bf "No, I just got here."
    y 1bh "But I started to get really nervous when nobody answered the doorbell..."
    mc "You always could have texted me."
    mc "If I had known, I would have reassured you and hurried more on my way home."
    y 2bv "Ah...I suppose that's true..."
    y "I didn't think of that...for some reason."
    mc "Anyway...let's go inside."
    mc "I see you brought a lot of stuff with you."
    y 1ba "That's right."
    y "And did you manage to find everything I asked you to buy as well?"
    mc "Yeah, pretty much."
    mc "At least, I hope I got everything right."
    y "I'm sure it will be fine."
    scene bg bedroom with wipeleft
    "I take Yuri to my room."
    "The first thing she does is glance around curiously, which makes me feel anxious."
    show yuri 2bm at t11 zorder 2
    y "It's so clean..."
    mc "Ahaha..."
    mc "I cleaned it before you came over, so..."
    y 2ba "That's very considerate of you to do."
    mc "Ah, no..."
    mc "I would be really embarrassed for my room to be a mess while you were here."
    y 1ba "Hmm..."
    y "Well, I do enjoy cleaning..."
    y "I would have gladly helped you clean."
    mc "Ah--"
    mc "That would be even more embarrassing!"
    show yuri 1be
    mc "Wait, don't look in there--!"
    "I snatch Yuri's wrist, which was in the process of opening a desk drawer of mine."
    y 3bn "A-Ah..."
    y "I'm sorry...!"
    y 4bb "I wasn't thinking for some reason..."
    y "I was just spacing out!"
    mc "It's fine, it's fine..."
    "I let go of Yuri's wrist."
    show yuri 1bl
    "She puts both of her hands firmly in her lap, as if making sure she's keeping track of them."
    mc "So, um..."
    mc "Should we...get started?"
    y 2bu "Ah..."
    y "Yes..."
    y 2bf "Um, I have a few things planned that you can help with..."
    y "Decorations and other atmospheric enhancements."
    mc "Atmospheric enhancements...?"
    y 1ba "You know..."
    y "Mood lighting, aromatherapy candles..."
    mc "Oh, wow."
    mc "I didn't know you planned on taking it that far."
    y 1bc "Of course."
    y "I want to help take our guests to a faraway place."
    y 1ba "Although many will stop by just out of curiosity..."
    y 1bj "And for...cupcakes, I guess..."
    y 1ba "I'm determined to provide an experience that will leave them wanting more."
    mc "That's great."
    mc "It's easy to forget that you're a pretty intense person."
    y 1bt "Ah--"
    y 2bt "Intense...?"
    mc "I guess that's the best way to put it."
    y "Is that...a bad thing?"
    mc "No, not at all."
    mc "It's something that I like about you, actually."
    y 3bu "I-Is that so...?"
    y "That makes me feel relieved..."
    y "And kind of happy..."
    mc "Yeah, no need to be so anxious."
    mc "You can relax a little."
    y 3bl "Relax..."
    y 1bf "I brought some things for relaxation."
    y "I was going to use them during the poetry event..."
    mc "Oh yeah? Like what?"
    y "Let's see..."
    "Yuri rummages through her bag."
    "She pulls out a few candles and a wooden cylinder-shaped object."
    y "I did some shopping on the way here, so I happen to have these in my bag."
    y "I planned to cover the windows in black paper and use the candles to light the room."
    y 1ba "I think that would be amazing, don't you?"
    mc "Yeah, that would be really neat."
    mc "What's that wooden thing, though?"
    y 1bf "Oh, this?"
    y "It's a diffuser for essential oils."
    y "How familiar are you with aromatherapy?"
    mc "Not familiar at all..."
    y 1ba "Ah, is that so?"
    y "It's one of my favorite contributors to a positive atmosphere."
    y "Depending on the oils or herbs you choose, you can change the mood of the air itself."
    y "You can even feel it permeate through your body."
    y 3bm "Relaxation, positive energy, romance, reflection..."
    y "It's almost like magic."
    show yuri 3ba
    "Yuri takes the cylinder and pushes a switch on the bottom."
    "In just a moment, a thin ray of vapor begins to spout through a small hole on the top."
    mc "Wow, that smells wonderful."
    mc "What kind of mood is that one for?"
    y 1ba "This is a Jasmine essential oil."
    y "It smells a little sweet and flowery, right?"
    mc "Yeah, that's a good way to describe it."
    y 1bb "I chose Jasmine for the event because it provides more than relaxation."
    y "Jasmine enhances your emotions and helps you feel them flow through your body."
    y 1bu "You feel warmer, and your heart pounds more heavily."
    y 1ba "Don't you think that will be perfect for sharing our poems?"
    mc "It does sound suitable..."
    mc "But you seem to know a lot about this, so I'll trust your opinion with anything."
    show yuri 1bc
    "Yuri smiles gently, clearly enjoying herself."
    "She again reaches into her bag and pulls out several spools of thin ribbon."
    show yuri 1ba
    mc "What are those for?"
    y 1bf "Well..."
    y "Did you purchase the origami paper I asked you to get?"
    mc "Yeah, I have it over here..."
    y "We won't be using the paper for folding origami."
    y "What I'd like to do is write a different kanji character on each paper."
    y "We'll need about a hundred of them."
    mc "Oh yeah?"
    mc "What will those be used for?"
    y 2bf "Well, I'm going to cut pieces of ribbon to hang from the doorway of the classroom."
    y "Then, we can fasten the kanji paper onto the ribbons to create a doorway curtain."
    y 2bm "Wouldn't that be beautiful?"
    y "It would also catch the eye of those passing by the room..."
    y 2ba "It may attract some to peek inside."
    mc "That's really creative!"
    mc "I had no idea you'd be so good at this, Yuri."
    y 4ba "Is...that so?"
    y "Well, I suppose I do get a little intense...as you'd put it."
    y 3bu "Uhuhu."
    "Yuri giggles with red cheeks."
    "Is it just me, or is she more relaxed when it's just the two of us?"
    "Or maybe it's the excitement she feels from sharing something that she enjoys."
    y 1ba "Here's a marker, [player]."
    y "You can write any characters you want."
    y "I'll help you once I finish cutting the ribbons."
    mc "Ah, alright."
    "Sitting on the floor together, the two of us get to work."
    "I carefully draw a different character on each paper, doing my best to manage my bad handwriting."
    "Yuri unravels a long strand of red ribbon to her desired length."
    "Then, she reaches into her bag once more and pulls out a pocket knife."
    mc "Eh...?"
    "The knife is strangely beautiful."
    "The silver handle has an intricate pattern of waves etched into it."
    "The blade itself is gently tinted blue."
    mc "That's no ordinary pocket knife..."
    mc "It looks really fancy."
    y 4bb "A-Ah..."
    y "Well..."
    "Embarrassed, Yuri looks away."
    mc "What is it?"
    y "You're going to think it's weird..."
    mc "Yuri, whatever it is, I have no reason to judge."
    mc "To each their own, you know?"
    y "If you promise you won't be weirded out..."
    mc "Yeah, I promise."
    y 2bi "Alright..."
    y "The thing is, I'm kind of into knives..."
    y "They're just...so pretty..."
    y 2bv "I-I can't help it!"
    y "I don't know what it is..."
    y "The combination of craftsmanship and feeling of danger, maybe..."
    y 4bb "Uu, what am I saying...?"
    y "Please don't think I'm weird for this..."
    mc "Ahaha."
    y "You're laughing at me..."
    mc "No, I'm not laughing at you."
    mc "It's just funny how nervous you got about sharing."
    mc "It's...well, it's an interesting thing to be into, I guess."
    mc "But I think it kind of suits you."
    y 2bt "Suits me...?"
    mc "Yeah... It's kind of intense. Ahaha."
    mc "Besides, it's a really cool-looking knife, I can't deny that."
    y 2bu "It is, isn't it...?"
    "Yuri relaxes her expression once again."
    y 1ba "Would you like to hold it?"
    mc "Sure, I'll check it out."
    "Yuri carefully hands me the knife, with the handle facing me."
    "I take it and turn it around in my hands."
    "It feels heavy, and extremely solid."
    "Where do you even get a knife like this...?"
    "Curious of its sharpness, I feel the point of the knife with my index finger."
    mc "Ow--!"
    y 3bn "[player]--!!"
    y "Why did you do that?!"
    mc "I didn't expect it to be that sharp...!"
    mc "I barely touched it at all."
    y "I-It's my fault!"
    y 3bo "I should have warned you..."
    y "This knife is extremely sharp..."
    y "It can cut through skin like it's paper."
    y 2bv "Oh no..."
    "A small drop of blood trickles down the side of my finger."
    "Yuri takes my hand and gives the wound a closer look."
    y 2bt "Ah..."
    "She stares at it and noticeably fidgets."
    mc "If you're squeamish, I'll go wash it off now--"
    mc "A-Ah!"
    "Without warning, Yuri puts my finger in her mouth and licks the wound."
    "I feel her tongue curl around my finger."
    "Startled, I instinctively pull my hand back."
    y "O-Oh..."
    y 3bo "P-Please forgive me!"
    y "I wasn't thinking!"
    y 4bc "I..."
    "Yuri lowers her head, her face burning up."
    mc "Yuri..."
    y "That's the most embarrassing thing I've ever done..."
    y "How could I do something like that??"
    y "I'm sorry, I'm sorry..."
    mc "Ah..."
    "Sure, it was a little weird, and it took me by surprise..."
    "But I guess she was just trying to help, right...?"
    mc "Yuri, I think you're overreacting a little..."
    y "Uuuh..."
    "She doesn't lift her head."
    "What if she doesn't recover from this for the rest of the afternoon?"
    mc "Alright, you know what..."
    "This might be a stupid thing to do, but I do it anyway."
    "I take Yuri's hand and lick her index finger in return."
    show yuri 3bn at h11
    y "[player]--!!"
    y "D-Did you really just do that?"
    mc "N-Now we're even..."
    y 3bv "..."
    "Yuri just looks at me like I did something wrong."
    mc "Ahaha..."
    mc "I knew that would be a bad idea..."
    "If not for the sweet aroma of the Jasmine oil, the air would be extremely heavy right now."
    y 1bu "You're so weird, [player]."
    "Yuri giggles shyly."
    mc "Eh...?"
    "Yuri calling {i}me{/i} weird?"
    "I have no response to that..."
    y 1bf "Where do you keep your bandages?"
    mc "Ah..."
    mc "I don't think I need one, actually."
    mc "It was a tiny cut."
    mc "Look, it already stopped bleeding."
    y 1ba "I see..."
    y "That's relieving."
    "The tension is quickly lifted."
    "We each resume our respective activities."
    "I watch Yuri's knife cut through the ribbon like it's nothing but air."
    "Meanwhile, I continue to make progress on the kanji."

    scene bg bedroom with wipeleft_scene
    "After we finish attaching the paper to the ribbons, we lay them all out side by side."
    "It looks better than I expected and will be very effective as a door curtain."
    mc "It looks great."
    mc "Good thinking coming up with this, Yuri."
    show yuri 1bq at t11 zorder 2
    y "Ah, thanks..."
    y "It's just something I saw online, really."
    y 1ba "Are you ready to move onto the next task?"
    mc "Yeah, let's do it."
    mc "What do you have in mind?"
    y "I'd like to create a banner."
    y "That's why I asked you to buy the paint tablets."
    mc "Ah, that's right."
    "One of the items Yuri had asked me to buy was a kit of watercolor paint tablets."
    y 1bf "We'll need about six cups of water to put each of the tablets in."
    y "Do you mind fetching those for us?"
    mc "Of course not."
    mc "Six cups of water..."
    mc "I'll be right back in a minute."
    y 1ba "Thank you very much."
    y 2bf "Oh, and just a little bit of water is okay."
    y "If you fill the cups too much, it will be too diluted."

    scene bg bedroom with wipeleft_scene
    "Taking Yuri's advice, I decide to use small plastic bathroom cups rather than full-sized glasses."
    "I put them on a plate to catch any paint that drips, then bring it back into my room."
    mc "Yuri?"
    show yuri 1bd at t11 zorder 2
    y "Yes?"
    "I come in to see Yuri quickly unrolling her sleeve, pulling it back over her arm."
    mc "Ah, nothing..."
    mc "Your face is a little red."
    mc "Is it too hot in here, or anything?"
    y 3bq "Ah--"
    y "No, not at all!"
    y "There's nothing wrong, so..."
    y "Let's mix the paint."
    "Yuri hurriedly dismisses me and takes it upon herself to unwrap the tablets, dropping them into the cups."
    y 1ba "So..."
    y "I thought we would do something simple that would look very nice."
    y "I'd like to paint a gradient across the banner..."
    y "Starting with the colors for a sunrise, then daytime, then sunset and nighttime."
    y "Once it dries, I'll write an inspirational quote across the banner."
    y "We can hang it on the wall behind the podium at the front of the classroom."
    mc "Ah, neat."
    mc "What are you going to write?"
    y 2bm "Well..."
    y "...It will be more fun to surprise you."
    "Yuri smiles at me."
    mc "If you say so..."
    show yuri at thide zorder 1
    hide yuri
    "After rolling out the banner, Yuri and I kneel on opposite sides so we don't get in the way of each other."
    "Yuri uses a brush and adds a few dots of different colors across the banner to serve as a color guide when we paint."
    mc "This kind of reminds me of elementary school..."
    "Painting on a banner with watercolors feels a lot like the art class projects we had back then."
    "It's relaxing."
    show yuri 2bt at t11 zorder 2
    y "Ah..."
    y "I'm sorry if this feels too childish...!"
    mc "No, I didn't mean that at all."
    mc "It's kind of fun, you know?"
    y 1bs "...Yeah."
    y "It is fun."
    y "I'm glad you feel that way, too."
    "Yuri stops painting for a moment, thinking to herself."
    y 2bl "For me..."
    y "I don't need to go out and do crazy things to have fun."
    y "In fact, I usually don't even want to."
    y 2bf "I just like when I can spend time with one other person..."
    y "Even if it's something simple, like reading - it doesn't even matter if we don't talk much."
    y 2ba "Just having a friend next to me makes things feel a little bit nicer."
    y "I think that's all it takes for me to be happy."
    mc "Is that so...?"
    "Even if Yuri and I are quite different, I can understand where she's coming from."
    "I feel that way about things like anime and games, where simply sharing the experience with someone can make me happy."
    mc "I think I feel the same way."
    "Yuri smiles gently."
    y 1bm "I knew you'd understand..."
    "Yuri leans over the banner to grab an unused paintbrush."
    "But I move at the same time, causing my head to bump into hers."
    y 3bn "Kya--!"
    mc "S-Sorry!"
    "Yuri reels back, and I quickly lift my hands in surprise."
    mc "Are you hurt?"
    y 2bv "N-No, I'm not hurt."
    y "It just startled me...that's all."
    y "Sorry, I should have asked you to get it for me..."
    mc "It's not your fault."
    mc "Ah, your face..."
    "There are droplets of paint on Yuri's face and neck."
    y 2bt "Is there something on my face?"
    mc "Yeah, I accidentally got paint on you..."
    mc "Sorry, it's totally my fault!"
    mc "I'll get a towel right away."
    show yuri at thide zorder 1
    hide yuri
    "I rush out and fetch a small towel, then I dampen it with hot water."
    "I return to my room and kneel back down in front of her."
    $ persistent.clear[9] = True
    scene y_cg3_base with dissolve_cg
    mc "Here..."
    "I pat down Yuri's face and neck with the towel."
    show y_cg3_exp1 at cgfade
    y "Ah--"
    mc "Is something wrong?"
    y "It's hot...I just didn't expect it."
    mc "Sorry..."
    mc "I didn't want to use cold water."
    "Having finished, I start to retract my hand."
    "But Yuri suddenly holds my wrist."
    hide y_cg3_exp1
    y "Wait--"
    mc "Eh?"
    show y_cg3_exp1 at cgfade
    y "Just...for a little longer."
    y "It feels really nice..."
    mc "Ah..."
    "I keep my hand still against Yuri's neck."
    hide y_cg3_exp1
    "She looks into my eyes."
    "It's an intense expression that I recognize from when she reads her books..."
    "Almost as if she's lost in a daze, enveloped by her own thoughts."
    "She breathes gently, half through slightly-parted lips."
    "What is happening...?"
    "Is it the aroma of the Jasmine oil giving me this dizzy feeling?"
    "Yuri's gentle fingers, wrapped around my wrist, send a tingling sensation through my arm."
    "And suddenly, her face seems to be much closer to mine than it was just a moment ago..."
    y "Ah..."
    "Yuri slowly pulls away."
    y "Sorry..."
    y "I've been feeling a little light-headed today."
    y "I didn't mean to space out..."
    mc "I-It's fine..."
    scene bedroom with dissolve_cg
    "The moment is over as soon as it began."
    "Yuri picks up her brush again."
    "But her movements seem clumsier, like she's unable to focus."
    "I remain silent, forced to ignore the event that just transpired."
    "I hesitantly retrieve my own brush and continue following Yuri's example."

    scene bedroom with wipeleft_scene
    mc "That should do it..."
    "I finish filling the night sky with white dots that looks like stars."
    "Looking at the banner as a whole, it's very pretty and natural-looking."
    show yuri 1ba at t11 zorder 2
    y "I think it came out better than I expected."
    y "I'm really happy with the results."
    mc "Yeah, me too."
    mc "Are you going to add the lettering now?"
    y 1bf "Ah, not yet..."
    y "It needs to dry first."
    mc "That's true, but won't that take a while?"
    y 2bh "Well..."
    y "Perhaps it would be best to leave it here, then have you bring it in the morning."
    y 2bf "I can do the lettering in the classroom before our event starts."
    y "Is that okay?"
    mc "That's totally fine."
    y 1ba "Wonderful."
    y "In that case..."
    y "I don't think there's anything more for us to do here."
    mc "Phew."
    y 1bc "Ahaha."
    y "You say that like you're glad it's over."
    y 1ba "Was I wrong to assume that you were at least enjoying yourself a little bit?"
    mc "Ah, no, it's not that."
    mc "I'm just glad that we managed to get everything done."
    y 2ba "I see."
    y "I am, too."
    y "I was a little concerned about time..."
    y "I need to start making dinner soon."
    mc "Ah..."
    mc "So you don't have any time left?"
    "I was secretly hoping we would have extra time after finishing the work..."
    y 2bl "Well..."
    y "..."
    "Yuri thinks to herself."
    y 3bv "I-I think it would be too irresponsible of me to wait much longer..."
    y "I'm sorry!"
    y "I was hoping there would be more time as well..."
    mc "It's probably my fault."
    mc "Sorry for being such a slow worker."
    y 1bt "No, it's not your fault at all."
    y "And...the important thing is that we got everything done, right?"
    mc "Yeah..."
    y 1bu "So..."
    y "I shouldn't be disappointed...or anything."
    "Gathering all her things, Yuri seems to look a little downcast."
    "I understand why."
    "It sounded like she rarely gets the opportunity to spend time with friends in a relaxed environment."
    "But that doesn't mean this is the last time it can happen..."

    scene bg house with wipeleft_scene
    "Once Yuri packs up, I walk her out the front door."
    show yuri 1ba at t11 zorder 2
    y "Thank you very much for having me today."
    mc "No problem, I'm glad I was able to help."
    mc "Just let me know if there's anything else you need me to bring tomorrow."
    y "I will."
    y 1bu "Well, then..."
    "Yuri fidgets."
    y 2bu "I guess...I'll see you tomorrow."
    mc "Wait--"
    show yuri 2bt
    "I kind of say that without thinking."
    mc "About today..."
    mc "It's fine that we didn't have as much time as we wanted."
    mc "Because we can do this again."
    mc "Whenever you want, you can come over, or we can go out somewhere--"
    mc "Ah, I forgot you don't like going out much--"
    show yuri 2bs
    "As I stumble over my words, Yuri simply smiles bashfully."
    mc "Anyway..."
    mc "You know what I'm trying to say, so..."
    y 1bs "You're very thoughtful, [player]."
    "Yuri takes a step closer to me, then briefly squeezes my hand."
    show yuri 2bs at face(y=600) with dissolve
    stop music fadeout 2.0
    y "I kind of like that about you..."
    mc "Well..."
    "How am I supposed to respond to that?"
    "But I don't even get a chance to, as Yuri suddenly pulls back."
    show yuri 3bn at t11 zorder 2
    y "S-Sayori--?"
    mc "Eh?!"
    show sayori 1bl  at f21 zorder 3
    show yuri at t22 zorder 2
    s "Ah..."
    s "H-Hi, [player]..."
    mc "Sayori--!"
    mc "Just now, we weren't--"
    s 1bq "Ehehe~"
    s "It's okay, [player]."
    s 1ba "I just stopped by to say hi~"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 3bq "U-Um..."
    y "Well, it's nice to see you..."
    y 3bv "I'm sorry, but I'm already on my way to leave!"
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1bh "Aw, really?"
    s "That's too bad..."
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 2bt "I'm sorry..."
    y "But we'll all be together at the festival tomorrow, so..."
    y "So that's fine, right?"
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 4bq "Of course!"
    "Sayori beams."
    show sayori 4ba
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 4bc "Y-Yeah, so..."
    y "I'll see you tomorrow!"
    show yuri at lhide
    hide yuri
    "Clearly embarrassed, Yuri hurries off."
    "Sayori waves goodbye after her."
    return

label ch4_exclusive_monika:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene
    "As I approach my house, I see something that makes me feel a moment of panic."
    show monika 1a at t11 zorder 2
    m "Oh hello there [player]."
    mc "Monika?"
    m "What? There's something wrong?"
    mc "Well, why are you wearing your uniform?"
    m "Ehh??"
    m "Ah--Ahahahahaha!"
    m "I'm so sorry!"
    m "I... I forgot that I wasn't coming to the school."
    "Very suspicius..."
    mc "Anyway, come in please."
    mc "And let's get started."
    m "Sure!"
    scene bg livingroom with wipeleft_scene
    mc "Did you brought everything we need to work, right?"
    m "Yes."
    m "Even I printed all the poems before coming here."
    mc "Cool!"
    mc "Because I don't have a printer, ahaha!"
    m "Ahahahahaha!"
    m "You're so funny [player]..."
    mc "Eheh... Well..."
    "Monika pulls a pile of papers from her bag. Those must be all the poems to be shown at the festival."
    m "Impressed?"
    mc "How many pamphlets we have to make exactly?"
    m "25. Since that's the amount of tables we can have in the room."
    mc "Oh, I see..."
    m "All the poems are ordered by the club members, however, we need one poem from each member for each pamphlet."
    mc "Understood."
    "(...)"
    "It's pretty funny to see my poem printed as the first one."
    "I mean, it's supposed that I'll be the lastest on Monika's list."
    "After mine's follows Monika's poem, Natsuki's, Yuri's..."
    "...and for some reason Sayori's poem is the last one."
    mc "Excuse me, Monika..."
    m "Yes?"
    mc "In which order you wanna do the poems in the pamphlets?"
    m "Which order you're seeing there?"
    mc "Because...{w} I don't like the idea of seeing my poem as the first one."
    m "Really?"
    m "Such low confidence of yourself, [player]!"
    mc "You can consider that, but I think the first one to be shown is Yuri's poem. Isn't?"
    m "Hmm..."
    m "Maybe..."
    mc "In fact, I've been thinking this order:"
    mc "Yuri{w}, Natsuki{w}, Sayori{w}, yours{w}, and mine."
    m "As you wish then."
    "So, those will be:"

    call showpoem(poem_y2, music=False)

    call showpoem(poem_n2, music=False)

    call showpoem(poem_s2, music=False)

    call showpoem(poem_m2, music=False)

    call showpoem(poem_mc4, music=False)

    "You may wonder what kind of \"poem\" is mine..."
    "Well, I just picked one online and sent it to Monika to make fun on her."
    "I don't know if she accepted it on purpose knowing that I am {i}the author{/i}, or what, but whatever."
    m "So..."
    m "What do you think?"
    "She's showing me an already made pamphlet."
    mc "Oh yeah, it's really nice."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"

    "Developer" "WARNING: THIS SCENE IS NOT FINISHED YET. SO NOW WE'LL JUMP TO THE END OF THIS SCENE WHICH WAS... WELL... THE FIRST THING I'VE MADE HERE LOL."


    #$ persistent.clear[11] = True

    scene bg house with wipeleft_scene

    show monika 1a at t11 zorder 2

    m "Before I leave, I need to do something..."
    mc "What is it?"
    m "I need to thank you."
    mc "That was nothing, really{nw}"
    m "I can't believe I'm finally in front of {i}you{/i}."
    mc "Uh...What?!"
    mc "What are you talking abou{nw}"

    window hide(None)
    window auto
    $ quick_menu = False
    $ save_load_disabled = True
    play music hb
    show black:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat
    show layer master at heartbeat
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show room_glitch zorder 1:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    m "It's just us now.{fast}"
    hide room_glitch
    show monika 1 at face(y=600) with dissolve
    m "Come with me!"
    m "Let's be happy forever!"
    mc "Monika?!"
    m "I can't wait to spend every day like this..."
    m "With you."
    mc "Monika what the fuck are you doing...???{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 1:
        xoffset -10
        0.1
        xoffset 0
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 1.0
    $ pause(0.3)
    stop sound
    m "Forever and ever..."
    mc "AAAAAAAAAAAaaaaaaaaaHHHHHHHHHhhhhhh----!!!!!!"
    "{i}WHAT THE FUCK IS SHE DOING--???!!!{/i}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide monika
    show monika 1a onlayer screens zorder 101 at face(y=600)
    m "F"
    m "o"
    m "r"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    m "e"
    m "v"
    m "e"
    show layer master
    hide black
    stop music fadeout 2.0
    show monika forward uniform ldown rdown s_scream onlayer screens zorder 101 at face(y=600)
    show sayori glitch at t21 zorder 2
    s "Hi~!"
    m "S-Sayori?!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    $ quick_menu = True
    $ save_load_disabled = False
    scene bg house
    hide monika onlayer screens
    show monika forward uniform ldown rdown b1b e2a me n4 at face(y=600) zorder 3
    show sayori 1bl at f21 zorder 2
    s "Ah..."
    s "H-Hi, [player]..."
    show sayori at t21
    m "..."
    mc "{i}WhatthefuckareyoudoingMonika?!{/i}"
    "Monika is strangling my head strongly, it's hurting a lot...!"
    show monika at t22 zorder 2
    "Suddenly she lets go of me."
    show sayori 3bc at f21 zorder 3
    s "Ehm... Is something wrong here?"
    show sayori at t21 zorder 2
    show monika at f22 zorder 3
    m "Ehh..."
    m 1l "No. It's nothing Sayori I just..."
    m 1n "I was just playing with [player], that's all!"
    show monika at t22 zorder 2
    mc "Monika, don't lie!"
    show sayori at f21 zorder 3
    s 1bq "Ehehe~"
    s "It's okay, [player]."
    s 1ba "I just stopped by to say hi~"
    show sayori at t21 zorder 2
    show monika 2l at f22 zorder 3
    m "And I'm just about to back home."
    show monika at t22 zorder 2
    show sayori at f21 zorder 3
    s 1bh "Aw, really?"
    s "That's too bad..."
    show sayori at t21 zorder 2
    show monika 5 at f22 zorder 3
    m "Okay then, see you tomorrow [player]~"
    mc "Hold on a sec--{nw}"
    show monika at lhide
    hide monika
    "Monika hurries off without giving explanations."
    "Sayori waves goodbye after her."
    mc "What the fuck.................."
    return

label ch4_exclusive_camilla:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene
    "Alright then, it's time to come visit Camilla now..."
    "I hope I have enough time."
    scene bg camilla_house with wipeleft_scene
    "Here we are..."
    "I ring the bell."
    "Camilla said she will be shopping the materials we'll need to make the banner. So I'm about to met her dad."
    "For some reason, I'm pretty nervious..."
    show camilladad l1 r2 e1a b1b mb at t11 zorder 2
    cdad "Ah, you must be [player]."
    mc "Eh?"
    mc "Y-Yeah sir, I'm [player], nice to meet you."
    cdad e1a b1a ma "Come in, please."
    mc "Sure, thanks."
    scene bg camilla_livingroom with wipeleft_scene
    "I sit down at the coach watching at the TV."
    "They have a Game Station 4 with a Car Thief V box, I wonder if he will let me play it..."
    "Nah, better not. I'm here because I need to make Yuri's banner with Camilla's help. Not to play videogames!"
    cdad "I have... Multi-fruit juice, cola soda or beer. What do you wanna drink?"
    menu:
        mc "Well..."

        "Beer":
            pass
        "Juice":
            pass
        "Soda":
            pass
    cdad "Alright."
    "..."
    show camilladad l1 r2 e1a b1a ma at t11 zorder 2
    cdad "There you go."
    cdad "And there's some snacks too."
    mc "Thank you very much."
    cdad l2 mb "You know...{w} Camilla doesn't stops talking about you."
    mc "Really?"
    cdad l1 b1b "Yeah, seems like she has a lot of interests on your friendship."
    if camilla_route_complete == True and persistent.ch4_camilla_unlocked == True:
        cdad "More than that, seems like you two are a \"couple\". So to speak."
        mc "*gasp*"
        "Do-Does he really mean that? Jeez, I don't know how to answer that..."
    mc "Well..."
    cdad l2 e1c mc "I know that you two know each other since a long time ago."
    cdad "And seems like you're the kind of person of her interests."
    cdad l1 ma e1a b1a "But, I need to know some things about you..."
    mc "Ah..."
    cdad e1b mb b1b "At least I know you two likes the same things, the same games, anime, series, soccer club, etc."
    cdad e1a md b1c "But what about your school average?"
    cdad "What about your {i}past{/i}?"
    mc "*gulp*"
    "That last one..."
    mc "Well, let's say my school average is \"okay\", I have good notes and..."
    mc "Umm... I guess you already know that I'm not very popular there..."
    cdad me e1b "I know about your {i}accident{/i} 2 years ago."
    cdad "That one where you saved one of your friends at the cost of losing the school's respect."
    cdad b1b "Yeah, Camilla told me that."
    mc "Aha...!"
    mc "And about my past..."
    mc "I don't have to much to speak..."
    show camilladad r1 e1a md
    mc "My relationship with my parents wasn't the best ever."
    mc "In fact, I'm actually living with Sayori's parents, I take care of her while they're doing business trip."
    mc "They bought the same house I used to live when I and Sayori were children."
    mc "When I wanted to stay, my parents didn't care at all and \"gifted\" me to Sayori's parents."
    mc "That house was supposed to be a gift for Sayori when she reachs the age of 18, however, I took her {i}gift{/i} instead."
    mc "But what can I say? My life wasn't the worse until...{w=1.0} You know...{w=1.0} The accident..."
    cdad b1e "I see..."
    cdad r2 e1b "It's not your fault that your parents didn't care about you."
    cdad b1d "My parents were the worse ever."
    cdad me "I had to escape from their home at the age of 25 because I wouldn't handle them."
    mc "Really?"
    cdad r1 e1a "Yeah, as I said."
    cdad e1b "They didn't wanted me having my own life, my own job and my own house, they wanted me to serve them until the death."
    cdad "Threating me like a damned slave..."
    cdad e1a b1c md "I had no choice but took my stuffs and ran away."
    cdad r2 "After that, I was living exiled in the streets, taking the criminal life."
    cdad b1a "However, I didn't did the same things like any accurate criminal."
    cdad "I mostly have been hunting down other criminals instead."
    cdad l2 ma b1b "And that's how I met Camilla's mother."
    mc "Wow..."
    cdad e1b mc "She was different to any other person I saved."
    cdad l1 e1a "At my native country, people only gave me the thanks or gave me some money."
    cdad e1b b1e "But she... She gave me her heart instead..."
    cdad e1a mb "She was so glad that I saved her that she invited me to her house and meet me to her parents."
    cdad "They also gave me a new home and a decent job to leave my criminal life. And I did accepted it of course."
    mc "Nice!"
    #cdad "Funnily enough, a contact of mine talked to me about a great \"score\". I rejected it because I finally had a new life."
    cdad "Camilla's mother and I formed a family, everything was perfect."
    stop music fadeout 3.0
    cdad r1 b1c e1b me "Until..."
    mc "(...)"
    if camilla_route_complete == True and persistent.ch4_camilla_unlocked == True:
        play music t9
        cdad e1d b1e md "We've been attacked by a group of robbers when Camilla was only 1 year old."
        cdad "They... Shooted Camilla's mother for no reason..."
        cdad "I chased them of course, I still had a gun between my clothes."
        cdad e1b "However... She..."
        mc "I'm so sorry..."
        mc "Camilla told me everything."
        mc "In that moment I didn't knew how to answer... However I just hugged her to comfort her."
        mc "I knew the pain at her words and her eyes, I almost cried as well."
        mc "It's very difficult to get over such moment."
    else:
        cdad b1a e1a md "Ah... I guess I shouldn't talk about that..."
        mc "It's okay."
        mc "I suppouse it's a very personal thing to talk with someone like me."
        mc "In fact, if Camilla never told me about {i}that{/i} I suppouse it's for something."
        mc "She always tells me anything."
        if persistent.ch4_camilla_unlocked == True:
            "I know about he's widower. But seems like they can only tell me the full story if I gain more confidence from Camilla."
        else:
            "It looks like they're hiding me something... He's divorced? Widower?"
            "Seems like they can only tell me the full story if I gain more confidence from Camilla."
    cdad b1a e1a ma "Thank you..."
    cdad e1c "At least I know now that she was right about that you're such kind person."
    mc "No problem."
    mc "I'm doing my best anyway..."
    cdad b1e mb "I'm sorry but I guess we shall change the topic."
    stop music fadeout 1.0
    mc "Yes, I understand."
    play music t6 fadeout 1.0
    cdad e1a b1b mc "I can't help but see you looking straight to the Car Thief 5 box."
    mc "Ah--!"
    cdad e1e "Do you wanna play? You're welcome."
    mc "Well, umm..."
    show camilladad e1a
    c "Daddy~! I'm here~!"
    mc "Eh?"
    show camilladad at t22
    show camilla frontal casual l1 r1 e1j b1a mb n1 hair_normal at f21 zorder 2
    c "[player]~! You're here~!"
    c e1c "Welcome to my house!"
    show camilla at t21
    mc "Thanks~!"
    "Camilla carries a huge bag with all the supplies we need to make the banner for the festival."
    "We really need to work with all that stuff?"
    show camilladad r1 b1c md at f22
    cdad "Darling... That bag is big!"
    cdad l2 "How could you carry that from the shop?"
    show camilla l2 r2 ma at f21
    show camilladad at t22
    c "Ehehe~! Don't worry about me daddy."
    c l3 e1d b1d mc "You already trained me for such situations, remember?"
    show camilla at t21
    show camilladad l1 b1e e1d mb at f22
    cdad "Ah, yeah, but..."
    "He grabs the bag."
    show camilla l1 r1 b1b e1a md
    cdad e1a md "It's pretty heavy..."
    show camilladad at t22
    mc "Let's see..."
    "(!)"
    show camilladad e1a b1a
    show camilla b1a
    mc "Jesus Christ, it's heavy!"
    show camilla r2 ma at f21
    c "Don't worry, while we can do the banner without difficults I don't care how heavy the bag is."
    c l3 r3 mb "In fact, remember that thanks to this I can protect you from that stupid bully~"
    show camilla at t21
    mc "Well..."
    show camilla l4 r4 e1c ma
    show camilladad r2 b1e e1c mc at f22
    cdad "Ahahahaha... At the beggining I didn't expected that Camilla were such strong woman."
    cdad e1d mb "I'm so proud of her..."
    show camilladad at t22
    mc "Indeed."
    show camilladad ma e1a
    show camilla mc at f21
    c "Ehehe~ Thanks daddy..."
    c l1 r1 e1a b1b mb "I'm doing my best anyway."
    c "By the way, [player]."
    c r2 e1d "Do you wanna play some games with me first? Or let's do the banner instead?"
    c "It's your choice~"
    show camilla at t21
    mc "We shall priorize the banner, isn't?"
    show camilla r1 e1a ma
    mc "After that, we can play some games if we have time."
    show camilla at f21
    c "Okay then..."
    show camilla at t21
    show camilladad e1d b1a md at f22
    cdad "Shall I go...?"
    show camilla l4 r4 mc b1a at f21
    show camilladad at t22
    c "Don't worry daddy, we'll be working at my bedroom."
    show camilla at t21
    show camilladad e1a ma at f22
    cdad "Oh... Okay then."
    cdad l2 b1b "If you need something, just call me, okay?"
    show camilla e1c at f21
    show camilladad at t22
    c "Sure~!"
    c l5 r5 mb e1j "Let's go [player]."
    show camilla at t21
    mc "Sure."
    scene bg camilla_bedroom with wipeleft_scene
    show camilla frontal casual l5 r5 e1a b1a ma n1 hair_normal at t11
    c "Alright! Now we are ready to start~"
    mc "Okay, just let me tell Yuri about the supplies you bought. So we can know how shall we start."
    c e1c mb b1b "Okay."
    "..."
    mc "She says that's more supplies than needed, but they will be very handy anyway."
    c l2 r2 ma e1a "Perfect!"
    c b1f "And... what about Yuri and her partner?"
    mc "She and Natsuki already started to bake the cupcakes."
    c b1b "And about Sayori and..."
    mc "I don't know, Sayori is offline for some reason and I don't have how to contact Monika."
    c l1 r1 b1c mf "Jesus..."
    "I wonder if it's a good time to tell Camilla about Sayori's depression..."
    "Nah, it may ruin the enjoyable atmosphere."
    c l5 r5 me "I hope she's okay."
    mc "Well, I visited before coming here and..."
    "Wait, if I tell Camilla about Sayori's depression, then I will ruin this nice moment together!"
    mc "...she's okay."
    mc "So don't worry about her, I would know if something is wrong with her."
    c l1 r1 ma b1b "Okay then."
    "{i}*phew*{/i}"
    mc "So, let's take a look on the indications Yuri sent me."
    c e1c b1a "Yeah."
    mc "First, Yuri says we have to write a different kanji character on each origami paper. We can write any characters we want."
    mc "Like... about a hundred of them?!"
    c l2 mc "No problem~!"
    mc "Also, we have to cut pieces of ribbon to hang from the doorway of the classroom."
    mc "Then, we can fasten the kanji paper onto the ribbons to create a doorway curtain."
    c e1a mb "It sounds very nice..."
    c r3 b1d e1e "I bet your club will be at the Top of the festival this year!"
    mc "You really mean that?"
    c b1a e1a "Of course!"
    c r2 ma "Now, let's start working."
    c l4 r4 mb "Let me draw the kanji characters, you take care of the ribbon cutting."
    mc "Sure."
    "Sitting on the floor together, the two of us get to work."
    "Camilla starts drawing different characters on each paper."
    "I unravels a long strand of red ribbon to Yuri's desired length."

    scene bg camilla_bedroom with wipeleft_scene
    "After we finish attaching the paper to the ribbons, we lay them all out side by side."
    "It looks better than I expected and will be very effective as a door curtain."
    mc "It looks great."
    show camilla frontal casual l2 r2 e1c b1a mb n2 hair_normal at t11
    c "Yeah, and I love it!"
    c l5 r5 "Yuri seems to be a genius~!"
    mc "Indeed..."
    "(...)"
    show camilla e1a b1b md n1
    mc "I sent a picture of the kanji characters curtain to Yuri."
    mc "And Yuri says that she likes the results of it."
    c l5 r5 mb e1c b1a "Yaaay~!"
    c l2 r2 e1a "So... What's next?"
    mc "Well, the second thing to do is a banner."
    c l1 ma b1b "Oh, then that's why she asked for the paint tablets..."
    mc "That's right."
    "One of the items Yuri had asked me to buy was a kit of watercolor paint tablets."
    mc "The instructions also says: We'll need about six cups of water to put each of the tablets in."
    c r1 mb e1c "Water?{w} Give me a second please, I will bring the water cups."
    mc "Sure."
    show camilla at thide
    hide camilla
    "Camilla goes out of her bedroom."
    "(...)"
    "Just look at this!"
    "She has all the volumes of Soccer Champions manga, all the Gems of the Dragon sagas, Agent Kidd, Alchemy Bros., etc."
    "I wonder how Natsuki would react if she see this..."
    "My God! Look that Gaming Computer!"
    "A Razor 7?! A eNvy GFX-1720 (that GPU bigger than)...?! Aaaah--!"
    "I wonder what kind of games she has at her digital library..."
    "I'm resisting the urge to turn it on!"
    "But, just look at that Game Station 2, and look at those legendary games!"
    c "[player], can you open the door please?"
    mc "Sure!"
    "The tour is over."
    show camilla frontal casual l1 r1 e1a b1a md n1 hair_normal at t11
    "She's carrying a large plate with six plastic cups of water with both hands."
    c b1c mb n2 "Judging your expression, seems like you've been peeking my collections, ehehe~!"
    mc "Ah--!"
    mc "Ahahahaha! That's right, you caught me!"
    c r2 b1a e1c ma n1 "My dad was a such fan of most of these manga collection, and I inherited it."
    c l4 r4 e1d "And... Apart from the Game Station 2 and 4, I still have an Game Station 1 with a box full of games for it as well."
    c "Do you wanna see it a while?"
    mc "Sure."
    c l1 r1 e1c "Good!"
    "Camilla pulls a huge box from one of her wardrobes. It says \"GS1\"."
    c l2 r2 e1a b1b mb "There you go..."
    mc "Amazing!"
    show camilla ma
    mc "And all those games..."
    mc "Cool!"
    c l4 r4 e1c b1c "Hehe~"
    c mb "Thanks to my dad I have all this stuff."
    mc "Hehe..."
    mc "You're so lucky, I would kill for have all this."
    c l1 r1 e1a n4 "[player]...!"
    mc "Eh... Did I said something wrong--?"
    mc "Uu, I exaggerated a lot with that \"kill\" thing..."
    mc "I'm so sorry..."
    c ma r2 "No problem."
    mc "Also, I think we're getting distracted..."
    mc "Now that you bring up the cups of water, let's keep going with the banner."
    c l3 r3 b1b mb n1 "Of course, let's go~!"
    show camilla at thide
    hide camilla
    "Seems like Camilla didn't care about what I said before."
    "We start to mix the paint. Unwraping the tablets and dropping them into the cups."
    show camilla frontal casual l2 r2 e1a b1b mb n1 hair_normal at t11
    c "So... What should we do now?"
    show camilla ma
    mc "Well, Yuri says she'd like to paint a gradient across the banner..."
    mc "Starting with the colors for a sunrise, then daytime, then sunset and nighttime."
    mc "And once it dries, we'll have to write an inspirational quote across the banner."
    c mb "Cool!"
    c "And what should we write on it?"
    mc "Well..."
    "I show her the text Yuri sent to me for the banner making."
    c l5 r5 b1a "Got it!"
    show camilla at thide
    hide camilla
    "After rolling out the banner, Camilla and I kneel on opposite sides so we don't get in the way of each other."
    "Camilla uses a brush and adds a few dots of different colors across the banner to serve as a color guide when we paint."
    mc "This kind of reminds me of elementary school..."
    "Painting on a banner with watercolors feels a lot like the art class projects we had back then."
    "It's relaxing."
    show camilla frontal casual l1 r1 e1c b1c mb n3 hair_normal at t11
    c "Ehehe~! Yeah right?"
    c r2 e1d "But it's still kind of fun."
    c l4 r4 e1c b1a ma n2 "Even more doing it with you~"
    mc "Ah-- Yes! I agree..."
    "We both smiles shamely."
    c l1 r1 b1c e1a "Uhuhu..."
    c "You're so cute~"
    mc "Ah...Thank you... Hehe!"
    scene bg camilla_bedroom with wipeleft_scene
    "A few time passes and we're almost done."
    "I finish filling the night sky with white dots that looks like stars."
    "Looking at the banner as a whole, it's very pretty and natural-looking."
    show camilla frontal casual l5 r5 e1j b1b md n1 hair_normal at t11
    c "It's beautiful..."
    mc "Of course it is..."
    "Now we finished the paintings, but there's a problem..."
    c l2 r2 b1c e1a ma "Well, I suppose we have to leave it dry to add the lettering."
    mc "Yeah..."
    mc "How much you think we shall to wait?"
    c l1 r1 b1b me "I don't know..."
    mc "Anyway, just let me send a picture of it to Yuri to show her the progress."
    c ma "Yeah, go on."
    "... ... ..."
    show camilla e1j b1a
    mc "She says she loves it."
    c l5 r5 e1c mb n2 "Excellent!"
    mc "Well, what should we do until it dries?"
    c l1 r2 e1a ma n1 "Well, we have enough time to have some fun, so..."
    mc "Oh, that's true! We could use the time to..."
    mc "Umm......."
    c r1 mb "Eat something?"
    c "Watch a TV show?"
    c "Read mangas?"
    c e1j "Play soccer?"
    c "Play videogames?"
    c "Watch anime?"
    c l5 r5 mc n2 "Go swimming?"
    c "Play wrestling?"
    c e1c "Trust me, there's a lot of fun things we can do in my house!"
    mc "Aahh... What's your best suggestion?"
    c l2 r2 b1c e1a mb "There's two things I always wanted to do with you..."
    c "We shall go swimming or play some wrestling."
    c l4 r4 e1c n4 mc "But since today is not so hot like Thursday to swim, I guess wrestling is the only choice."
    mc "There's no problem for me."
    mc "But I hope your dad is okay if we do a little brawl..."
    c l3 r3 b1a e1a ma n2 "It's okay... We can ask him if you want~"
    mc "If in case, let's go."
    scene bg camilla_livingroom with wipeleft_scene
    show camilla frontal casual l4 r4 e1a b1c mb n2 hair_normal at f21
    show camilladad l1 r1 e1a b1a ma at t22
    c "Daddy... It's okay if [player] and I play some wrestling?"
    show camilla at t21
    show camilladad b1b md at f22
    cdad "What?"
    cdad b1a e1d "Oh, you mean like training?"
    show camilla b1b ma at f21
    show camilladad at t22
    c "Of course."
    show camilla at t21
    show camilladad b1e r2 e1c ma at f22
    cdad "Oh well, I guess there's no problem."
    cdad l2 e1e "Just be careful, please."
    show camilladad at t22
    mc "We will, thank you sir!"
    show camilla l3 r3 e1c b1b mb at f21
    c "Thanks daddy~!"
    show camilla at t21
    show camilladad l1 e1c ma at f22
    cdad "No problem."
    show camilladad at thide
    hide camilladad
    show camilla r2 e1d b1f at t11
    c "So, let's play at my bedroom then."
    mc "Sure."
    scene bg camilla_bedroom with wipeleft_scene
    show camilla frontal casual l3 r3 e1a b1d mc n1 hair_normal at t11
    c "Are you ready?"
    mc "Yes."
    c e1j mb "Hiyaa~~!!!"
    show camilla at thide
    hide camilla
    "I thought we'll start a battle scene or something like that, but no, that's because we are fighting lightly."
    "I'm very soft with her... And seems like she's soft with me as well."
    pause 3.0
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "Then Camilla does a fake hit."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "I return it in the same way."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 1.0
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 1.0
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 1.0
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "Until I grab her to do a wrestling lock."
    show camilla frontal casual l5 r5 e1k b1c ml n4 hair_normal at t11
    c "Kyaaa~~!!"
    "Now I will drop her safely to her bed."
    show camilla at thide
    hide camilla
    play sound fall
    "And do the pin."
    mc "1...{w=1.0}2...{w=1.0}"
    show camilla frontal casual l3 r3 e1j b1d mb n4 hair_normal at t11
    mc "What the...?!"
    c "Gotcha!"
    "She reversed it and now she's doing a submission lock!"
    "I'm trying to reverse it without hurting her, but it's not use, she's very strong!"
    mc "Hnnngh--!!"
    "I have an idea, but she may not like it..."
    "I calculate the falling to prevent hurting her bad and..."
    show camilla frontal casual l3 r3 e1j b1d ml n4 hair_normal at thide
    hide camilla
    play sound fall
    "I use my body to fall my weight against her to the bed."
    c "Ooooofff...!"
    "And now I grab her arms."
    show camilla frontal casual l5 r5 e1a b1c me n4 hair_normal at t11
    mc "Gotcha!"
    c b1d mb "Heh! I don't think so..."
    show camilla at thide
    hide camilla
    "She uses her legs to push me out..."
    mc "Uwaaaaaa--!!"
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
    "She pushes me too strong that I fall directly to the floor."
    show camilla frontal casual l5 r5 e1l b1c ml n4 hair_normal at t11
    c "Oh my god!"
    c mi "OH MY GOD--!!!"
    c "[player!u]!!!"
    mc "I'm...fine..."
    c ml "Jesus Christ! I'm so sorry! I didn't pretend to..."
    mc "Nah... It's okay..."
    c mf e1a "Come here..."
    #$ persistent.clear[x] = True
    scene bg camilla_bedroom with dissolve_cg
    "Then she's carrying me like if I were badly wonded and unable to move."
    "I can't help but see her worried expression."
    mc "I'm okay Camilla, seriously..."
    c "No."
    c "That falling would have left you unconscious!"
    c "It's my fault! And now I must take care of you..."
    mc "Camilla..."
    "She's carrying me back to her bed."
    "She attempts to lie my body down there."
    "However, I stand sit at the bed holding my arm over her shoulders."
    mc "Hehe... You worries too much about me."
    "I say it with a smile."
    c "Of course [player]."
    c "You're very special for me."
    mc "I see..."
    "Now it's my chance!"
    mc "I hope {i}this{/i} doesn't bother you..."
    c "Wha..........{nw}"
    "With my left arm I grab Camilla's legs."
    "Now I'm ready to finish this one and for all..."
    mc "Were we go! A surprise back suplex!"
    c "[player]! What are you doin--{nw}"
    play sound fall
    "The trick worked!"
    "Now I use the left arm to grab Camilla to do the last pinfall."
    mc "1!{w=1.0} 2!{w=1.0} 3! Ring ring riiing!!!"
    c "[player]...!"
    c "Did you really did that??"
    mc "Ahahahaha! I saw the opportunity and I--"
    mc "Ouch!"
    c "Heh! The karma acted pretty fast, isn't?"
    mc "Oof...! Yeah, I think so..."
    c "Just lay down until I pick up some medical stuff for this pain of yours."
    mc "No, wait!"
    mc "I guess we layed down it's actually healing me..."
    mc "Just stay with me please, at least let's take a rest, okay?"
    c "Uh... Seems like it's true..."
    c "Okay, let's take a little rest."
    "She's cuddling me."
    "I do the same with her."
    "We remain like this for a while..."
    scene bg camilla_bedroom with dissolve_cg
    show camilla frontal casual l1 r1 e1a b1c ma n2 hair_normal at t11
    c "That was nice."
    mc "Yeah..."
    c me "Are you still hurted?"
    mc "Let's see..."
    "(...)"
    mc "Just a bit."
    c r2 mk "Umm..."
    show camilla e1l b1a n4
    cdad "Camilla, [player], is everything okay?"
    c r2 mb e1c b1c "Yes daddy~!"
    show camilla ma
    mc "Of course sir!"
    cdad "Good then."
    show camilla l5 r5 b1a e1j mb n2
    cdad "I'm advising you that I bought some ice creams and pizza."
    cdad "Come here if you wanna eat."
    show camilla e1c at h11
    c "Yaaaaaay~!!"
    c e1j "Come on [player]~!"
    mc "Nice! Let's go!"
    scene bg camilla_livingroom with wipeleft_scene
    "Before coming to eat, I checked the banner to see if it's dry, but it needs more time..."
    show camilladad l1 r2 e1a b1b mb at t22
    show camilla frontal casual l5 r5 e1j b1a md n2 hair_normal at t21
    c "Wooooooooooo...."
    show camilla e1c mb at h21
    c "Thanks daddy~!"
    show camilla at t21
    show camilladad e1c b1e at f22
    cdad "Hehe, no problem..."
    cdad "Just enjoy it."
    show camilladad at t22
    mc "Sure, thanks!"
    hide camilla
    hide camilladad
    with wipeleft
    "I take a sit closer to Camilla, seems like they placed the three chairs on purpose LOL."
    "The table has three mozzarella pizza boxes, four bottles of soda, and two 1kg ice cream pots with variety of flavors are saved at the fridge."
    "All of them are high quality brands."
    "I start to pick one portion of pizza."
    show camilladad l1 r1 e1c b1b ma at t22
    show camilla frontal casual l1 r1 e1c b1a ma n1 hair_normal at t21
    mc "Wow! Delicious!"
    "Both nods in agreement."
    show camilladad at thide
    hide camilladad
    show camilla at thide
    hide camilla
    "I wanted to keep my eating speed at moderate, but I notice how they eat the pizza pretty fast, just like me!"
    "So, I shall consider doing the same. After all there's one pizza box for each one, right?"
    pause 2.0
    "Surprisingly, we all three ate all the 8 portions of pizza from each box."
    "We also empty one and half of the soda bottles."
    show camilla frontal casual l5 r5 e1j b1a ma n2 hair_normal at t21
    show camilladad l2 r1 e1c b1b mb at f22
    cdad "So, now it's time for ice cream..."
    show camilla l5 r5 e1c mb at h21
    show camilladad at t22
    c "Yeah~~!!"
    show camilla at t21
    show camilladad l1 e1e
    cdad "Hold on."
    show camilladad at thide
    hide camilladad
    show camilla at t11
    "I can't wait for taste the ice cream...!"
    show camilla l1 r1 e1a ma n2
    mc "Eh?"
    "Camilla grabs my left hand."
    "All what she's doing is smiling sweetly..."
    "She may be.......?"
    "Wait!"
    "What would her dad think if I go \"straight\"?"
    mc "Eh...hehehe!"
    "Her smile is getting more satisfactory than before."
    show camilla e1a b1b ma n2 at face(y=600) with dissolve
    "We look each other like there's nothing else in the round."
    "It's hypnotic..."
    "She seems to be hypnotized as well..."
    show camilla e1l b1a me
    cdad "Here comes the ice cream~!"
    show camilladad l1 r1 e1c b1b mb at t22
    show camilla at t21
    "After we heard Camilla's dad calling, we both retreat scared."
    show camilladad r2 b1a e1a md at f22
    cdad "Is... everything okay?"
    show camilla mb e1c b1c n4 at f21
    show camilladad at t22
    c "Why, yeah of course daddy...!"
    show camilla e1l b1a mf n2 at t21
    show camilladad l2 b1b at f22
    cdad "Both are blushing, you're red like a tomato..."
    show camilla l4 r4 mb e1c b1c n4 at f21
    show camilladad at t22
    "Camilla & [player]" "Ah... Ahahahaha!"
    show camilla at t21
    mc "We...We are excited about that ice cream we're about to eat... that's all."
    show camilla mb at f21
    c "Y-Yeah..."
    show camilla at t21
    "Really? That was the best thing I could said? I feel stupid now!"
    show camilladad l1 b1e e1c mb at f22
    cdad "Ah...! Ehehe, I see..."
    cdad b1b e1a ma "In that case, there you go~!"
    show camilladad at t22
    show camilla l5 r5 e1j b1a ma n2 hair_normal at t21
    "Slush mint... Swiss chocolate... Tramontana..."
    "Lemon... Strawberry cream... and more Tramontana..."
    mc "Oh my goood~!"
    mc "Can I...?"
    show camilladad b1b e1c mb at f22
    cdad "Of course."
    show camilladad at t22
    "I take a spoonful of tramontana."
    show camilla mb
    mc "Hmmmmmmm~~!!"
    mc "Majestic!"
    "And now slush mint."
    mc "So delicious~~!!"
    show camilladad ma at f22
    cdad "Ehehe..."
    show camilla l4 r4 e1a mb n1 at f21
    show camilladad at t22
    c "Yeah, right?"
    c e1c "My dad and I always eat that ice cream brand~"
    show camilla at t21
    show camilladad e1a at f22
    cdad "Indeed."
    scene bg camilla_livingroom with wipeleft_scene
    "We finished the all the ice cream pots!"
    "The next time I want to eat ice cream, I'm gonna ask that brand."
    play sound ringtone1
    mc "Eh?"
    show camilla frontal casual l1 r1 e1a b1b md n1 hair_normal at f21
    show camilladad l1 r2 e1a b1a ma at t22
    c "What's the matter [player]?"
    show camilla at t21
    mc "It's Yuri."
    show camilla me b1a
    mc "She's asking about the banner..."
    mc "Also she says that they're done with the cupcakes baking."
    show camilla e1b b1c mf at f21
    c "Uuuuuh-! We lose..."
    show camilla at t21
    mc "Don't worry Camilla."
    show camilla l2 r2 e1a b1d ma at f21
    c "You're right."
    c b1a e1c mc "We had a lot of fun after all."
    show camilla at t21
    mc "That's what I was about to say hehe..."
    show camilla l1 r1 mb e1a at f21
    c "Let me check if the banner is dry already."
    show camilla at t21
    mc "Sure."
    show camilla at thide
    hide camilla
    show camilladad r1 mb b1a at t11
    cdad "So... [player]..."
    mc "Eh?"
    cdad e1d b1b "About your relationship with Camilla..."
    "*gulp*"
    cdad l2 r1 b1e e1c mc "I never saw Camilla so happy with anyone else who weren't me."
    cdad r2 b1b e1e ma "Seems like you earned her heart."
    mc "Y-Yes... I've been thinking the same..."
    cdad l1 r1 e1b mb "You know, after I won Camilla's mother heart, her parents gave me the chance to get a better life than I had before."
    cdad l2 b1a e1a "If you really consider making Camilla happy for me, then I'll do the same with you."
    mc "I will do my best. I promise!"
    show camilladad l1 b1b md
    mc "Since I met her, she always pampered me no matter what."
    mc "I've always wondering why she was so kind with me."
    if camilla_route_complete == True and persistent.ch4_camilla_unlocked == True:
        mc "But after she confessed me the truth behind that, I knew that she loved me all this time."
        mc "I'm very glad for having such person so close to me..."
    else:
        mc "Now I realised that she loved me all this time, I still don't know why exactly."
        mc "But I'm very glad for having such person so close to me..."
    cdad ma "That's what I wanted to hear."
    c "I'm baaack~!"
    show camilla frontal casual l1 r1 e1a b1c ma n3 hair_normal at f21
    show camilladad at t22
    c "The banner {i}still{/i} needs to dry unfortunatelly."
    c "Seems like it will completely dry at night."
    show camilla at t21
    mc "Ohh..."
    "It's like 17 PM..."
    show camilla l4 r4 b1b e1c mb n1 at f21
    c "But don't worry, I will try to write the text Yuri suggested tonight."
    c e1d "And I will bring it to your club tomorrow~"
    show camilla at t21
    mc "Yeah... We can do that..."
    mc "Just let me tell Yuri about that."
    show camilla e1a ma
    "(...)"
    mc "She says it's okay."
    mc "But she also suggests that you can let it as it is and she will write the text at the festival, but bringing it sooner of course."
    show camilla l1 r1 mg at f21
    c "Hmm..."
    c "Yeah..."
    c r2 b1a e1c mb "But nah, tell her that don't worry, I will write the text so she's doesn't need to rush."
    show camilla at t21
    mc "Okay then..."
    show camilla ma
    show camilladad r2 e1b b1b mb at f22
    cdad "Well [player]..."
    cdad e1a "It was nice meeting you."
    show camilladad at t22
    mc "Likewise sir."
    show camilla l4 r4 e1c b1a mb n2 at f21
    c "Daddy, can I walk [player] home?"
    show camilla at t21
    show camilladad e1c mc at f22
    cdad "Sure! Go on."
    show camilla mc at f21
    show camilladad at t22
    c "Thank you~~!"
    show camilla at t21
    mc "Hehehe~ That wasn't so neecesary, but thanks Camilla."
    show camilla l1 r2 e1a ma at f21
    c "No problem~!"
    c "Let's go."
    mc "Yeah!"
    scene bg camilla_house with wipeleft_scene
    show camilla frontal casual l1 r1 e1a b1b ma n1 hair_normal at t21
    show camilladad l1 r1 e1a b1a ma at t22
    mc "Okay Mister, thank you for everything!"
    mc "We'll see you later, I hope."
    show camilladad r2 e1c b1b mb at f22
    cdad "Thanks to you for coming!"
    cdad "See ya~!"
    cdad e1e mc "And good luck with the festival!"
    show camilladad at t22
    mc "Thanks!"
    scene bg house with wipeleft_scene
    "During all the trip, we haven't let go of our hands."
    show camilla frontal casual l1 r1 e1a b1a ma n2 hair_normal at t11
    mc "Here we are..."
    mc "Thank you Camilla."
    "And now we are holding our free hands."
    show camilla at face(y=600) with dissolve
    stop music fadeout 5.0
    "And she comes closer."
    "I can feel a heavy breathing, like her heart is pounding stronger by beign so close to me..."
    "I also feel the same..."
    show camilla b1b with dissolve
    c "[player]..."
    mc "Yeah..."
    mc "That thing...{w} we left pending at your house..."
    c "Yeah..."
    show camilla e1b b1b md with dissolve
    "Now it's time!"
    "I also proceed to kiss..."
    "However..."
    show camilla e1l b1a me n4
    c "S-Sayori--?"
    mc "Eh?!"
    show sayori 1bl at f21 zorder 3
    show camilla l5 r5 b1c ml at t22 zorder 2
    s "Ah..."
    s "H-Hi, [player]..."
    show sayori at t21
    mc "Sayori--!"
    mc "Just now, we weren't--"
    show sayori at f21
    s 1bq "Ehehe~"
    s "It's okay, [player]."
    s 1ba "I just stopped by to say hi~"
    show sayori at t21 zorder 2
    show camilla at f22 zorder 3
    c e1a "U-Um..."
    c l1 r2 mb "Well, it's nice to see you..."
    c r4 e1c "I'm sorry, but I need to go back home! I gotta help my dad with... something..."
    show camilla at t22 zorder 2
    show sayori at f21 zorder 3
    s 1bh "Aw, really?"
    s "That's too bad..."
    show sayori at t21 zorder 2
    show camilla at f22 zorder 3
    c l4 e1b mf "I'm sorry..."
    c r1 e1a mb "But don't worry guys, we'll all see together at the festival tomorrow because I gotta bring up the banner~!"
    c "That's fine, right?"
    show camilla at t22 zorder 2
    show sayori at f21 zorder 3
    s 4bq "Of course!"
    "Sayori beams."
    show sayori 4ba
    show sayori at t21 zorder 2
    show camilla n2 at f22 zorder 3
    c l2 "Well then..."
    c l4 r4 e1c b1a mc "I'll see you tomorrow guys!"
    c "... ... ..."
    c l1 r1 e1a b1b ma "And [player]..."
    show camilla e1b md at face(y=600) with dissolve
    "*muack*"
    show camilla l4 r4 e1c mb at f22
    c "See you later darling~!"
    mc "Y-Yeah, see you later Camilla... And thanks~!"
    show camilla at lhide
    hide camilla
    "Before running away, Camilla kissed my left cheek."
    "Sayori waves goodbye after her."
    show sayori at t11
    s "Ehehe~!"
    s "She's so nice, isn't?"
    mc "Of course she is..."
    "... ... ..."
    return

label ch4_end:
    play music t10 fadeout 2.0
    show sayori 1ba at t11 zorder 2
    mc "Sayori--"
    mc "I thought you didn't want to come over today!"
    s 2bl "Ahaha, well..."
    s "I tried staying in my room..."
    s "But my imagination was being really mean to me..."
    s 1by "So I had to come here and see it for myself."
    mc "See what?"
    mc "What are you talking about?"
    s "You know..."
    s "How much fun you were having with [ch4_name]."
    s "And how close you got to her."
    s 1bt "It makes me...really happy..."
    s "That you've made such good friends."
    s "That's all that matters to me."
    "Tears start to fall down Sayori's face."
    s 4bv "That's all that matters to me--!"
    s "Why am I feeling this way, [player]?"
    s "I'm supposed to be happy for you."
    s 4bw "Why does it feel like my heart is splitting in half?"
    s "It hurts so much..."
    s "Everything hurts so much..."
    s "This would be so much better if I could just disappear!"
    mc "Sayori, don't say that!"
    s 1bw "It's true, [player]!"
    s "If I wasn't here, then you wouldn't have to waste your sympathy on me!"
    s "You wouldn't have to put up with me being selfish!"
    s 1bv "Monika was right..."
    s "I should just..."
    "Monika...?"
    menu:
        "It can be..."

        "Let her speak.":
            s "... just..."
            s "... ... ..."
            mc "Sayori? Tell me what did Monika said to you?"
            pass
        "Monika was right about what?":
            mc "Monika was right about what?"
            pass
    s "..."
    "I don't like this, I don't know why but I felt shivers when Sayori mentioned Monika."
    mc "Sayori..."
    mc "What I said before is true."
    mc "I'm not going to let this continue."
    mc "Caring about you like this isn't the burden your mind is making it out to be."
    mc "It's something that makes me happy."
    mc "It's something that I wouldn't trade for anything else."
    mc "So, even if it takes an entire lifetime..."
    mc "I'm going to be by your side until you don't feel any more pain."
    s 1bk "B-But..."
    "Sayori looks away."
    "I put a hand on her shoulder to reassure her."
    s "I'm scared, [player]..."
    s "I'm really scared..."
    mc "What are you scared of, Sayori?"
    s "I'm scared that..."
    s "That I might like you more than you like me..."
    mc "Sayori...?"
    s 1bu "It's true, isn't it?"
    s "I was weak and started to like you too much..."
    s "I did this to myself."
    s "[player]..."
    s 4bw "I like you so much that I want to die!"
    s "That's how I feel!"
    s 2bv "And...and..."
    mc "That's enough, Sayori..."
    mc "I don't want you to hurt anymore."
    "I slide my hand down Sayori's arm and squeeze her hand in my own."
    mc "Do you remember how I said I always know what's best for you?"
    mc "Do you still believe me?"
    "Wordlessly, Sayori nods."
    mc "Even if you don't understand all of your own feelings..."
    mc "I know what you need the most right now."
    mc "And that's what I'm going to give to you."
    show black zorder 4 with dissolve_cg

    menu:
        mc "Sayori..."

        "I love you.":
            $ sayori_confess = True
            hide black with dissolve_cg
            call ch4_end_yes
        "You'll always be my dearest friend." if not persistent.mount_achieved:
            $ sayori_confess = False
            hide black with dissolve_cg
            call ch4_end_no

    return

label ch4_end_yes:
    mc "I love you."
    s 1bv "Eh--?"
    mc "Those are my true feelings."
    mc "So...there's no way you could like me more than I like you."
    mc "I should have realized it sooner."
    mc "But spending time with everyone at the club..."
    mc "Making new friends..."
    mc "And having fun with you every day..."
    mc "It helped me realize that you are truly the most important person to me."
    mc "That's why I'll accept any of your burdens."
    mc "As long as we continue like this every day..."
    mc "With you by my side..."
    mc "Then I know we'll both be happy."
    s "[player]..."
    $ persistent.clear[8] = True
    scene s_cg3 with dissolve_cg
    "Suddenly, Sayori wraps her arms tightly around me."
    s "[player]..."
    s "Is this...really okay?"
    mc "Yeah."
    "I hold Sayori in my arms and pull her closer."
    mc "You'll never have to let go of me again."
    s "I love you, [player]..."
    s "I want to be with you forever."
    mc "Me too."
    s "..."
    "I feel Sayori's grip around me weaken a little bit."
    s "What is this...?"
    mc "Sayori...?"
    s "I'm supposed to be happy right now..."
    s "I always thought this would be the happiest moment for me."
    s "But why...?"
    s "Even now..."
    s "Why won't the rainclouds go away?"
    s "They're not going away at all, [player]..."
    mc "It's okay, Sayori..."
    mc "It might take some time for things to get better again."
    mc "But no matter how long it takes, I'll be there every step of the way."
    mc "That's all that matters right now."
    s "O-Okay..."
    s "I...trust you..."
    scene bg house
    show sayori 1bv  at i11 zorder 2
    with dissolve_cg
    "Sayori and I slowly release each other."
    mc "So..."
    mc "I guess that makes the festival tomorrow...our first date, huh?"
    s 1by "Ehehe..."
    s "What are you saying?"
    s "I don't want to think about those things, you know?"
    s "I want everything to be the same as it always has been."
    s "Even if we really are...a couple."
    s 1bk "I don't know if I could handle anything more right now..."
    s "It's really new and scary to me."
    mc "I understand."
    mc "We'll go at whatever pace suits you best."
    s 1bd "Hey, [player]..."
    "Sayori gazes at me once again, smiling sadly."
    s 4bd "Even if I get really, really sad..."
    s "This is the best thing for me...right?"
    mc "Eh...?"
    "I don't really understand what Sayori means by that."
    mc "Are you saying that this is making you feel sad, Sayori?"
    s 4bk "I-I don't know..."
    s "I don't understand what I'm feeling."
    s "It felt like a bunch of thorns when you told me you love me..."
    s 4bd "But that's why I want to trust you."
    s "You know what's best for me..."
    mc "...Yeah."
    mc "I do."
    mc "That's my promise."
    show sayori at thide zorder 1
    hide sayori
    "I say that, but in reality, I've never felt more uncertain when it comes to Sayori."
    "I know that I love her, and she loves me."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "Is that what Sayori meant by not wanting anything to change?"
    "I don't know."
    "But I know that I'll give it everything I've got."
    "Sayori is the most important person to me."
    "And I'll do whatever it takes to have a happy future with her."
    return


label ch4_end_no:
    mc "You'll always be my dearest friend."
    mc "What you need most is for things to be like they've always been."
    mc "Monika told me the truth..."
    mc "She told me how much happier you seemed after I joined the club."
    mc "I know you're struggling with some really difficult feelings right now."
    mc "But..."
    mc "Please trust me that I know what's best...and what will make you happy in the end."
    mc "I promise I'll help get things back to the way they were."
    s 1bt "I..."
    s "I...see..."
    "Sayori forces a smile through an incredibly pained expression."
    s "Ahaha..."
    s "Is this what it feels like...to get stabbed in the chest?"
    s "I should write a poem about this..."
    mc "Sayori--"
    s "It's okay."
    s "This is just my punishment...remember?"
    s "For being so selfish..."
    s "So please..."
    s "Please don't worry about these stupid feelings."
    s "I know you're right."
    s "I knew this whole time that there's no happiness down that path."
    s "That's why I came here..."
    s "Just so I could get the answer I needed to hear."
    s "And the other thing..."
    s "You're also right that I just want it to go back to the way it was."
    s "I realize that now."
    s "You really do know me better than anyone, [player]."
    s 4bv "I'll trust you with anything..."
    s "Anything at all..."
    s "So..."
    show sayori at thide zorder 1
    hide sayori
    "Sayori's smile finally breaks."
    "All of a sudden, she turns around and drops to her knees."
    s "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
    "Clutching her head with both hands, she screams as loudly as she can."
    "I'm so shocked that I don't know how to react."
    show sayori 4bt  at t11 zorder 2
    s "..."
    show sayori at lhide
    hide sayori
    "Sayori looks over her shoulder and flashes me one more weak smile before turning around and running off."
    mc "Sayori!"
    "..."
    "I'm left helplessly standing in the front of my house."
    "Why am I feeling so horrible about this?"
    "There's nothing more that I could have done."
    "The most I can do is support Sayori through her feelings and help her on the path that's right."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "I'm going to give it everything I've got."
    "Sayori will always be my dearest friend."
    "And I'll do whatever it takes to put a smile on her face every day."

    return
