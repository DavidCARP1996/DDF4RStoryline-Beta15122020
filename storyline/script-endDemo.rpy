label endDemo1(pause_length=10.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    play music "<from 16.0>bgm/6s.ogg" noloop
    show end
    with dissolve_scene_full
    pause pause_length
    scene black with dissolve_scene_full
    stop music fadeout 5.0
    pause 5.0
    pass

label endDemo2:
    play music m1
    "A message from the author:"
    dev "{cps=25}Greetings!{w=1.5} I'm DavidCARP1996,{w=1.5} Doki Doki Fighting For Reality Developer.{/cps}"
    dev "{cps=25}First of all,{w=1.5} I want to thank you for playing my Mod's Demo version.{/cps}"
    dev "{cps=25}I really hope this kind of idea satisfies the fandom,{w=1.5} a game where you're literally fighting to survive and all that stuff.{/cps}"
    dev "{cps=25}Consider this project as a brand new style of DDLC modding...{w=1.5} Because after I finish this project for once,{w=1.5} I'll be able to create brand new stories based on DDLC and DDF4R spin-offs.{/cps}"
    dev "{cps=25}And the most important.{w=0.2}.{w=0.2}.{w=1.5} I hope everyone liked Camilla as a character,{w=1.5} she was the one who gave me the most inspirations to keep going with this project when I was about to retire.{/cps}"
    dev "{cps=25}Alright.{w=1.5} If you liked this mod and you want to see progress or give me a hand with it,{w=1.5} then you can enter to the Mod's Discord server clicking {a=https://www.discord.gg/jdJqQGtdku}here{/a}.{/cps}"
    dev "{cps=25}And don't worry about Sayori and the others right now.{w=1.5} Since Monika screwed up Sayori's Act and the further Acts aren't finished,{w=1.5} I'm gonna Hard Reset the whole game so you can replay Sayori's Act anytime you want.{/cps}"
    call screen dialog("What?!", ok_action=Return())
    call screen dialog("You can't do that!!", ok_action=Return())
    call screen dialog("I was almost...", ok_action=Return())
    dev "{cps=25}Silence!{w=1.5} I'm gonna reset this game right now.{w=1.5} Just give me a second.{w=0.2}.{w=0.2}.{/cps}"
    if in_sayori_kill == True:
        $ consolehistory = []
        call updateconsole ("os.restore(\"characters/sayori.chr\")", "sayori.chr restored successfully.")
        $ restore_all_characters()
    call screen dialog("No!", ok_action=Return())
    call screen dialog("Nooo!!", ok_action=Return())
    stop music
    dev "{cps=25}See you later,{w=1.5} [player].{/cps}"
    window hide(None)
    window auto
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 1.0
    $ consolehistory = []
    call updateconsole("Reseting game...", "Reseting game...")
    pause 0.25
    call updateconsolehistory("0 percent")
    pause 0.25
    call updateconsolehistory("3 percent")
    pause 0.25
    call updateconsolehistory("5 percent")
    pause 0.25
    call updateconsolehistory("12 percent")
    pause 0.25
    call updateconsolehistory("15 percent")
    pause 0.25
    call updateconsolehistory("18 percent")
    pause 0.25
    call updateconsolehistory("24 percent")
    pause 0.25
    call updateconsolehistory("38 percent")
    pause 0.25
    call updateconsolehistory("44 percent")
    pause 0.25
    call updateconsolehistory("50 percent")
    pause 0.25
    call updateconsolehistory("69 percent")
    pause 0.25
    call updateconsolehistory("78 percent")
    pause 0.25
    call updateconsolehistory("86 percent")
    pause 0.25
    call updateconsolehistory("96 percent")
    pause 0.25
    call updateconsolehistory("99 percent")
    pause 0.5
    call updateconsolehistory("100 percent")
    pause 0.1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = None
    $ quick_menu = True
    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")
    #$ MainMenu(confirm=False)()
    return
