label fightingclub_day3_battle1:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ no_death_battle = True
    $ fightingclub_battle = True
    $ fightingclub_day3_battle1_victory = False

    # Define los stats del MC (los reinicia, bufferea o nerfea dependiendo la ocasión).
    $ mc_atk = mc_atk_base
    $ mc_def = mc_def_base
    $ mc_spd = mc_spd_base
    $ mc_mat = mc_mat_base
    $ mc_mdf = mc_mdf_base
    $ mc_evasion = mc_evasion_base

    # Define al rival.

    $ enemy = "Takeshi"
    $ enemy_lv = 1
    $ enemy_hp_max = 50
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 7
    $ enemy_def_base = 9
    $ enemy_spd_base = 4
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    stop music fadeout 2.0
    show takeshi at t11 zorder 2
    pause 2.0
    show screen stats with dissolve
    play music demobattle
    "Fight!"

    # Aquí comienza la pelea.

    while (mc_hp > 0) and (enemy_hp > 0):

        $ mc_evasion_rate = renpy.random.randint(1, 100)
        $ mc_critical_rate = renpy.random.randint(1, 100)
        $ enemy_critical_rate = renpy.random.randint(1, 100)

        if mc_spd > enemy_spd:
            call Hud
            if enemy_hp > 0:
                call enemy_turn
            else:
                pass
        else:
            call enemy_turn
            if mc_hp > 0:
                call Hud
            else:
                pass

        $ autorecovering_rate = renpy.random.randint(1, 100)
        if mc_hp <= 0 and autorecovering_rate <= 50:
            $ mc_hp = 0
            mc "I... I won't give up!"
            $ mc_hp = mc_hp_max / 2
            "[player] restored 50\% of HP!"
            enemy "What?!"

    #
    ####

label fightingclub_day3_battle1_end:

    $ exp_earned = 100
    $ money_earned = 100
    if enemy_hp <= 0:
        $ total_npc_defeated += 1
        $ fightingclub_day3_battle1_victory = True
        hide takeshi
        with Dissolve(.5)

    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    hide takeshi
    stop music fadeout 1
    return

##########################################################################
######################################################################################

label fightingclub_day3_battle2:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ no_death_battle = True
    $ fightingclub_battle = True
    $ fightingclub_day3_battle2_victory = False

    # Define los stats del MC (los reinicia, bufferea o nerfea dependiendo la ocasión).
    $ mc_atk = mc_atk_base
    $ mc_def = mc_def_base
    $ mc_spd = mc_spd_base
    $ mc_mat = mc_mat_base
    $ mc_mdf = mc_mdf_base
    $ mc_evasion = mc_evasion_base

    # Define al rival.

    $ enemy = "Opponent"
    $ enemy_lv = 5
    $ enemy_hp_max = 150
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 8
    $ enemy_def_base = 14
    $ enemy_spd_base = 5
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    stop music fadeout 2.0
    show trainee1 at t11 zorder 2
    pause 2.0
    show screen stats with dissolve
    play music demobattle
    "Fight!"

    # Aquí comienza la pelea.

    while (mc_hp > 0) and (enemy_hp > 0):

        $ mc_evasion_rate = renpy.random.randint(1, 100)
        $ mc_critical_rate = renpy.random.randint(1, 100)
        $ enemy_critical_rate = renpy.random.randint(1, 100)

        if mc_spd > enemy_spd:
            call Hud
            if enemy_hp > 0:
                call enemy_turn
            else:
                pass
        else:
            call enemy_turn
            if mc_hp > 0:
                call Hud
            else:
                pass

        $ autorecovering_rate = renpy.random.randint(1, 100)
        if mc_hp <= 0 and autorecovering_rate <= 50:
            $ mc_hp = 0
            mc "I... I won't give up!"
            $ mc_hp = mc_hp_max / 2
            "[player] restored 50\% of HP!"
            enemy "What?!"

    #
    ####

label fightingclub_day3_battle2_end:

    $ exp_earned = 350
    $ money_earned = 200
    if enemy_hp <= 0:
        $ total_npc_defeated += 1
        $ fightingclub_day3_battle2_victory = True
        hide trainee1
        with Dissolve(.5)

    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    hide trainee1
    stop music fadeout 1
    return

##########################################################################
######################################################################################

label fightingclub_day3_battle3:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ no_death_battle = True
    $ fightingclub_battle = True
    $ fightingclub_day3_battle3_victory = False

    # Define los stats del MC (los reinicia, bufferea o nerfea dependiendo la ocasión).
    $ mc_atk = mc_atk_base
    $ mc_def = mc_def_base
    $ mc_spd = mc_spd_base
    $ mc_mat = mc_mat_base
    $ mc_mdf = mc_mdf_base
    $ mc_evasion = mc_evasion_base

    # Define al rival.

    $ enemy = "Opponent"
    $ enemy_lv = 7
    $ enemy_hp_max = 150
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 13
    $ enemy_def_base = 13
    $ enemy_spd_base = 13
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    stop music fadeout 2.0
    show trainee2 at t11 zorder 2
    pause 2.0
    show screen stats with dissolve
    play music demobattle
    "Fight!"

    # Aquí comienza la pelea.

    while (mc_hp > 0) and (enemy_hp > 0):

        $ mc_evasion_rate = renpy.random.randint(1, 40)
        $ mc_critical_rate = renpy.random.randint(1, 100)
        $ enemy_critical_rate = renpy.random.randint(1, 100)

        if mc_spd > enemy_spd:
            call Hud
            if enemy_hp > 0:
                call enemy_turn
            else:
                pass
        else:
            call enemy_turn
            if mc_hp > 0:
                call Hud
            else:
                pass

        $ autorecovering_rate = renpy.random.randint(1, 100)
        if mc_hp <= 0 and autorecovering_rate <= 50:
            $ mc_hp = 0
            mc "I... I won't give up!"
            $ mc_hp = mc_hp_max / 2
            "[player] restored 50\% of HP!"
            enemy "What?!"

    #
    ####

label fightingclub_day3_battle3_end:

    $ exp_earned = 190
    $ money_earned = 250
    if enemy_hp <= 0:
        $ total_npc_defeated += 1
        $ fightingclub_day3_battle3_victory = True
        hide trainee2
        with Dissolve(.5)

    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    hide trainee2
    stop music fadeout 1
    return

##########################################################################
######################################################################################

label fightingclub_day3_battle4:

    # Deshabilita el Skip y el sistema de Guardar/Cargar.

    $ _skipping = False
    $ no_death_battle = True
    $ fightingclub_battle = True
    $ fightingclub_day3_battle4_victory = False

    # Define los stats del MC (los reinicia, bufferea o nerfea dependiendo la ocasión).
    $ mc_atk = mc_atk_base
    $ mc_def = mc_def_base
    $ mc_spd = mc_spd_base
    $ mc_mat = mc_mat_base
    $ mc_mdf = mc_mdf_base
    $ mc_evasion = mc_evasion_base

    # Define al rival.

    $ enemy = "Ryoma"
    $ enemy_lv = 10
    $ enemy_hp_max = 250
    $ enemy_hp = enemy_hp_max
    $ enemy_mp_max = 0
    $ enemy_mp = enemy_mp_max
    $ enemy_atk_base = 21
    $ enemy_def_base = 17
    $ enemy_spd_base = 22
    $ enemy_mat_base = 0
    $ enemy_mdf_base = 0

    $ enemy_atk = enemy_atk_base
    $ enemy_def = enemy_def_base
    $ enemy_spd = enemy_spd_base
    $ enemy_mat = enemy_mat_base
    $ enemy_mdf = enemy_mdf_base

    $ enemy_current_weapon = None

    # Comienza el dialogo

    stop music fadeout 2.0
    show ryoma 1 at t11 zorder 2
    pause 2.0
    show screen stats with dissolve
    play music demobattle
    "Fight!"

    # Aquí comienza la pelea.

    while (mc_hp > 0) and (enemy_hp > 0):

        $ mc_evasion_rate = renpy.random.randint(1, 40)
        $ mc_critical_rate = renpy.random.randint(1, 100)
        $ enemy_critical_rate = renpy.random.randint(1, 100)

        if mc_spd > enemy_spd:
            call Hud
            if enemy_hp > 0:
                call enemy_turn
            else:
                pass
        else:
            call enemy_turn
            if mc_hp > 0:
                call Hud
            else:
                pass

        $ autorecovering_rate = renpy.random.randint(1, 100)
        if mc_hp <= 0 and autorecovering_rate <= 50:
            $ mc_hp = 0
            mc "I... I won't give up!"
            $ mc_hp = mc_hp_max / 2
            "[player] restored 50\% of HP!"
            enemy "What?!"

    #
    ####

label fightingclub_day3_battle4_end:

    $ exp_earned = 500
    $ money_earned = 100
    if enemy_hp <= 0:
        $ total_npc_defeated += 1
        $ fightingclub_day3_battle4_victory = True
        hide ryoma
        with Dissolve(.5)

    call battle_results

    hide screen stats
    with Dissolve(.5)
    $ _skipping = True
    $ enemy_hp = enemy_hp_max
    hide screen levelup_stats_hud
    hide screen battle_hud
    hide ryoma
    stop music fadeout 1
    return
