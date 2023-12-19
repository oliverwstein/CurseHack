'''
    attack_type is one of:

        AT_NONE         /* passive monster (ex. acid blob) */
        AT_CLAW         /* claw (punch, hit, etc.) */
        AT_BITE         /* bite */
        AT_KICK         /* kick */
        AT_BUTT         /* head butt (ex. a unicorn) */
        AT_TUCH         /* touches */
        AT_STNG         /* sting */
        AT_HUGS         /* crushing bearhug */
        AT_SPIT         /* spits substance - ranged */
        AT_ENGL         /* engulf (swallow or by a butt) */
        AT_BREA         /* breath - ranged */
        AT_EXPL         /* explodes - proximity */
        AT_GAZE         /* gaze - ranged */
        AT_TENT         /* tentacles */
        AT_WEAP         /* uses weapon */
        AT_MAGC         /* uses magic spell(s) */

    damage_type is one of:

        AD_PHYS         /* ordinary physical */
        AD_MAGM         /* magic missiles */
        AD_FIRE         /* fire damage */
        AD_COLD         /* frost damage */
        AD_SLEE         /* sleep ray */
        AD_DISN         /* disintegration (death ray) */
        AD_ELEC         /* shock damage */
        AD_DRST         /* drains str (poison) */
        AD_ACID         /* acid damage */
        AD_SPC1         /* for extension of buzz() */
        AD_SPC2         /* for extension of buzz() */
        AD_BLND         /* blinds (glowing eye) */
        AD_STUN         /* stuns */
        AD_SLOW         /* slows */
        AD_PLYS         /* paralyses */
        AD_DRLI         /* drains life levels (Vampire) */
        AD_DREN         /* drains magic energy */
        AD_LEGS         /* damages legs (xan) */
        AD_STON         /* petrifies (Medusa, Cockatrice) */
        AD_STCK         /* sticks to you (Mimic) */
        AD_SGLD         /* steals gold (Leppie) */
        AD_SITM         /* steals item (Nymphs) */
        AD_SEDU         /* seduces & steals multiple items */
        AD_TLPT         /* teleports you (Quantum Mech.) */
        AD_RUST         /* rusts armour (Rust Monster)*/
        AD_CONF         /* confuses (Umber Hulk) */
        AD_DGST         /* digests opponent (trapper, etc.) */
        AD_HEAL         /* heals opponent's wounds (nurse) */
        AD_WRAP         /* special "stick" for eels */
        AD_WERE         /* confers lycanthropy */
        AD_DRDX         /* drains dexterity (Quasit) */
        AD_DRCO         /* drains constitution */
        AD_DRIN         /* drains intelligence (mind flayer) */
        AD_DISE         /* confers diseases */
        AD_DCAY         /* decays organics (Brown pudding) */
        AD_SSEX         /* Succubus seduction (extended) */
        AD_DETH         /* for Death only */
        AD_PEST         /* for Pestilence only */
        AD_FAMN         /* for Famine only */
        AD_CLRC         /* random clerical spell */
        AD_SPEL         /* random magic spell */
        AD_RBRE         /* random breath weapon */
        AD_SAMU         /* hits, may steal Amulet (Wizard) */
        AD_CURS         /* random curse (ex. gremlin) */
'''