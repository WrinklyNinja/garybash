# -*- coding: utf-8 -*-

# Wrye Flash
# Module for Fallout New Vegas definitions.
# When Flash decides what game it should run for, it should then import this module as
# import falloutnv as game
# All code changes made during the merge reference this game module alias instead of a specific game.

# Where possible, variable names are the same as used in Bash's game-specific python files.

#--The main plugin Wrye Bash should look for
masterFiles = [
    u'FalloutNV.esm',
    ]

#--INI files that should show up in the INI Edits tab
iniFiles = [
    u'FalloutPrefs.ini',
    u'Fallout_default.ini',
    ]

#--URL to the Nexus site for this game
nexusUrl = u'http://www.newvegasnexus.com'
nexusName = u'New Vegas Nexus'
nexusKey = 'bash.installers.openNewVegasNexus'
    
#--Script Extender information
class se:
    shortName = u'NVSE'                      # Abbreviated name
    longName = u'Fallout Script Extender'   # Full name
    exe = u'nvse_loader.exe'                 # Exe to run
    steamExe = u'nvse_loader.dll'           # Exe to run if a steam install
    url = u'http://nvse.silverlock.org/'     # URL to download from
    urlTip = u'http://nvse.silverlock.org/'  # Tooltip for mouse over the URL
    
#--Game ESM/ESP/BSA files
bethDataFiles = set((
    #--Vanilla
    'falloutnv.esm',
    r'fallout - meshes.bsa',
    r'fallout - misc.bsa',
    r'fallout - sound.bsa',
    r'fallout - textures.bsa',
    r'fallout - textures2.bsa',
    r'fallout - voices1.bsa',
    #--Preorder Packs
    r'caravanpack.esm',
    r'caravanpack - main.bsa',
    r'classicpack.esm',
    r'classicpack - main.bsa',
    r'mercenarypack.esm',
    r'mercenarypack - main.bsa',
    r'tribalpack.esm',
    r'tribalpack - main.bsa',
    #--DLCs
    r'deadmoney.esm',
    r'deadmoney - main.bsa',
    r'deadmoney - sounds.bsa',
    r'honesthearts.esm',
    r'honesthearts - main.bsa',
    r'honesthearts - sounds.bsa',
    r'oldworldblues.esm',
    r'oldworldblues - main.bsa',
    r'oldworldblues - sounds.bsa',
    r'lonesomeroad.esm',
    r'lonesomeroad - main.bsa',
    r'lonesomeroad - sounds.bsa',
    ))
allBethFiles = set((
    #vanilla
    r'Credits.txt',
    r'CreditsWacky.txt',
    r'Fallout - Meshes.bsa',
    r'Fallout - Misc.bsa',
    r'Fallout - Sounds.bsa',
    r'Fallout - Textures.bsa',
    r'Fallout - Textures2.bsa',
    r'Fallout - Voices1.bsa',
    r'FalloutNV.esm',
    r'Update.bsa',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_City_Full.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_City_Perc.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Full(alt1).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Full.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc(alt2).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_City_Full.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_City_Perc.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Full(alt1).mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Full.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Perc.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_City_Full.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_City_Perc.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_Rural_Full.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_Rural_Perc.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_City_Full.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_City_Perc.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_Rural_Full.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_Rural_Perc.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_City_Full.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_City_Perc.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_Rural_Full.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_Rural_Perc.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_City_Full.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_City_Perc.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Full(alt1).mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Full.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Perc.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_City_Full.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_City_Perc.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_Rural_Full.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_Rural_Perc.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_City_Full.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_City_Perc.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_Rural_Full.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_Rural_Perc.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_1Low(alt).mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_1Low.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_2Mid.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_3High.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_1Low(alt1).mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_1Low.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_2Mid.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_3High.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_1Low.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_2Mid(alt1).mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_2Mid.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_3High.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_1Low.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_2Mid.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_3High.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_1Low.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_2Mid(alt1).mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_2Mid.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_3High.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_1Low.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_2Mid.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_3High.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_1Low.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_2Mid.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_3High.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_1Low.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_2Mid.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_3High.mp3',
    r'Music\Fallout1and2\Fallout\01MetallicMonks.mp3',
    r'Music\Fallout1and2\Fallout\02DesertWind.mp3',
    r'Music\Fallout1and2\Fallout\03ATradersLife.mp3',
    r'Music\Fallout1and2\Fallout\04TheVaultoftheFuture.mp3',
    r'Music\Fallout1and2\Fallout\05IndustrialJunk.mp3',
    r'Music\Fallout1and2\Fallout\06MoribundWorld.mp3',
    r'Music\Fallout1and2\Fallout\07VatsofGoo.mp3',
    r'Music\Fallout1and2\Fallout\08CityoftheDead.mp3',
    r'Music\Fallout1and2\Fallout\09SecondChance.mp3',
    r'Music\Fallout1and2\Fallout\10UndergroundTroubles.mp3',
    r'Music\Fallout1and2\Fallout\11CityofLostAngels.mp3',
    r'Music\Fallout1and2\Fallout\12FollowersCredo.mp3',
    r'Music\Fallout1and2\Fallout\13RadiationStorm.mp3',
    r'Music\Fallout1and2\Fallout\14AcolytesoftheNewgod.mp3',
    r'Music\Fallout1and2\Fallout\15FlameoftheAncientWorld.mp3',
    r'Music\Fallout1and2\Fallout\16KhansofNewCalifornia.mp3',
    r'Music\Fallout1and2\Fallout2\Arroyo.mp3',
    r'Music\Fallout1and2\Fallout2\Modoc.mp3',
    r'Music\Fallout1and2\Fallout2\NewReno.mp3',
    r'Music\Fallout1and2\Fallout2\Redding.mp3',
    r'Music\Fallout1and2\Fallout2\SanFrancisco.mp3',
    r'Music\Fallout1and2\Fallout2\VaultCity.mp3',
    r'Music\Fallout1and2\Fallout2\Worldmap1.mp3',
    r'Music\Fallout1and2\Fallout2\Worldmap2.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_1Low.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_2Mid.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_3High.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_1Low.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_2Mid.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_3High.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_1Low.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_2Mid.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_3High.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_1Low.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_2Mid.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_3High.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_1Low.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_2Mid.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_3High.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_1Low.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_2Mid.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_3High.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_1Low.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_2Mid.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_3High.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_1Low.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_2Mid.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_3High.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_1Low.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_2Mid.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_3High.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_1Low.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_2Mid.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_3High.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_1Low.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_2Mid.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_3High.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_1Low.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_2Mid.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_3High.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_1Low.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_2Mid.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_3High(alt1).mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_3High.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_1Low.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_2Mid.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_3High(alt1).mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_3High.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_1Low.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_2Mid.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_3High.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_1Low.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_2Mid.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_3High.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_1Low.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_2Mid.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_3High(alt1).mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_3High.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_1Low.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_2Mid.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_3High.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_1Low.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_2Mid.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_3High.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_1Low.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_2Mid.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_3High.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_1Low.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_2Mid.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_3High.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_1Low.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_2Mid.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_3High.mp3',
    r'Music\OLD\FO1\mus_FO1_AcolytesOfTheNewGod.mp3',
    r'Music\OLD\FO1\mus_FO1_CityOfLostAngels.mp3',
    r'Music\OLD\FO1\mus_FO1_CityOfTheDead.mp3',
    r'Music\OLD\FO1\mus_FO1_DesertWind.mp3',
    r'Music\OLD\FO1\mus_FO1_FlameOfTheAncientWorld.mp3',
    r'Music\OLD\FO1\mus_FO1_IndustrialJunk.mp3',
    r'Music\OLD\FO1\mus_FO1_MetallicMonks.mp3',
    r'Music\OLD\FO1\mus_FO1_RadiationStorm.mp3',
    r'Music\OLD\FO1\mus_FO1_SecondChance.mp3',
    r'Music\OLD\FO1\mus_FO1_TheVaultOfTheFuture.mp3',
    r'Music\OLD\FO1\mus_FO1_UndergroundTrouble.mp3',
    r'Music\OLD\FO2\mus_FO2_Modoc.mp3',
    r'Music\OLD\FO2\mus_FO2_Redding.mp3',
    r'Music\OLD\FO3\mus_FO3_Base2.mp3',
    r'Music\OLD\FO3\mus_FO3_Base3.mp3',
    r'Music\OLD\FO3\mus_FO3_Base5.mp3',
    r'Music\OLD\FO3\mus_FO3_Death.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon1.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon2.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon3.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore1.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore3.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore4.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore5.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore6.mp3',
    r'Music\SCR\mus_SCR_DeathStinger.mp3',
    r'Music\SCR\mus_SCR_DocMitchell.mp3',
    r'Music\SCR\mus_SCR_GoodspringsStinger.mp3',
    r'Music\SCR\mus_SCR_Muzak.mp3',
    r'Music\SCR\mus_SCR_MuzakRadio.mp3',
    r'Music\SCR\mus_SCR_VegasStinger.mp3',
    r'Music\SCR\mus_SCR_VictorySinger(alt1).mp3',
    r'Music\SCR\mus_SCR_VictorySinger(alt2).mp3',
    r'Music\SCR\mus_SCR_VictorySinger.mp3',
    r'Music\Special\EndCredits.mp3',
    r'Music\Special\MainTitle.mp3',
    r'Music\Special\mus_endgameslideshow.mp3',
    r'Music\Special\mus_endgametransitionstinger.mp3',
    r'Music\Special\mus_hailchief.mp3',
    r'Shaders\shaderpackage002.sdp',
    r'Shaders\shaderpackage003.sdp',
    r'Shaders\shaderpackage004.sdp',
    r'Shaders\shaderpackage006.sdp',
    r'Shaders\shaderpackage007.sdp',
    r'Shaders\shaderpackage009.sdp',
    r'Shaders\shaderpackage010.sdp',
    r'Shaders\shaderpackage011.sdp',
    r'Shaders\shaderpackage012.sdp',
    r'Shaders\shaderpackage013.sdp',
    r'Shaders\shaderpackage014.sdp',
    r'Shaders\shaderpackage015.sdp',
    r'Shaders\shaderpackage016.sdp',
    r'Shaders\shaderpackage017.sdp',
    r'Shaders\shaderpackage018.sdp',
    r'Shaders\shaderpackage019.sdp',
    r'Sound\songs\radionv\MUS_Aint_That_A_Kick_In_the_Head.mp3',
    r'Sound\songs\radionv\MUS_American_Swing.mp3',
    r'Sound\songs\radionv\MUS_Big_Iron.mp3',
    r'Sound\songs\radionv\MUS_Blues_For_You.mp3',
    r'Sound\songs\radionv\MUS_Blue_Moon.mp3',
    r'Sound\songs\radionv\MUS_Cobwebs_and_Rainbows.mp3',
    r'Sound\songs\radionv\MUS_Concerto_For_2_Vl_Str_In_D_Minor.mp3',
    r'Sound\songs\radionv\MUS_Concerto_Grosso_In_B_Minor_Allegro_01.mp3',
    r'Sound\songs\radionv\MUS_Concerto_Grosso_In_B_Minor_Allegro_02.mp3',
    r'Sound\songs\radionv\MUS_EddyArnold_Rca_ItsASin.mp3',
    r'Sound\songs\radionv\MUS_Flower_Duet_Lakm_KPM.mp3',
    r'Sound\songs\radionv\MUS_Four_Seasons_No_4_The_Winter.mp3',
    r'Sound\songs\radionv\MUS_Goin_Under.mp3',
    r'Sound\songs\radionv\MUS_Hallo_Mister_X.mp3',
    r'Sound\songs\radionv\MUS_Happy_Times.mp3',
    r'Sound\songs\radionv\MUS_Heartaches_by_the_Number.mp3',
    r'Sound\songs\radionv\MUS_HomeOnTheWastes.mp3',
    r'Sound\songs\radionv\MUS_In_The_Shadow_Of_The_Valley.mp3',
    r'Sound\songs\radionv\MUS_Its_A_Sin_To_Tell_A_Lie.mp3',
    r'Sound\songs\radionv\MUS_I_m_Movin_Out.mp3',
    r'Sound\songs\radionv\MUS_I_m_So_Blue.mp3',
    r'Sound\songs\radionv\MUS_Jazz_Blues_GT.mp3',
    r'Sound\songs\radionv\MUS_Jazz_Club_Blues_CAS.mp3',
    r'Sound\songs\radionv\MUS_Jingle_Jangle_Jingle.mp3',
    r'Sound\songs\radionv\MUS_Joe_Cool_CAS.mp3',
    r'Sound\songs\radionv\MUS_Johnny_Guitar.mp3',
    r'Sound\songs\radionv\MUS_Lazy_Day_Blues.mp3',
    r'Sound\songs\radionv\MUS_Let_s_Ride_Into_The_Sunset_Together.mp3',
    r'Sound\songs\radionv\MUS_Lone_Star.mp3',
    r'Sound\songs\radionv\MUS_Love_Me_As_Though_No_Tomorrow.mp3',
    r'Sound\songs\radionv\MUS_Mad_About_The_Boy.mp3',
    r'Sound\songs\radionv\MUS_Manhattan.mp3',
    r'Sound\songs\radionv\MUS_NewVegasValley.mp3',
    r'Sound\songs\radionv\MUS_Piano_Concerto_No_21__Elvira_Madigan.mp3',
    r'Sound\songs\radionv\MUS_Ride_Of_The_Valkyries_01.mp3',
    r'Sound\songs\radionv\MUS_Roundhouse_Rock.mp3',
    r'Sound\songs\radionv\MUS_Sit_And_Dream.mp3',
    r'Sound\songs\radionv\MUS_Sleepy_Town_Blues_CAS.mp3',
    r'Sound\songs\radionv\MUS_Slow_Bounce.mp3',
    r'Sound\songs\radionv\MUS_Slow_Sax_KOS.mp3',
    r'Sound\songs\radionv\MUS_Somethings_Gotta_Give.mp3',
    r'Sound\songs\radionv\MUS_Spring_Song_KPMC.mp3',
    r'Sound\songs\radionv\MUS_Stars_Of_The_Midnight_Range.mp3',
    r'Sound\songs\radionv\MUS_Strahlende_Trompete.mp3',
    r'Sound\songs\radionv\MUS_StreetsOfNewReno.mp3',
    r'Sound\songs\radionv\MUS_Von_Spanien_Nach_S_damerika.mp3',
    r'Sound\songs\radionv\MUS_Where_Have_You_Been_All_My_Life.mp3',
    r'Sound\songs\radionv\MUS_Why_Dont_You_Do_Right.mp3',
    r'Video\FNVIntro.bik',
    #Preorder Packs
    r'CaravanPack - Main.bsa',
    r'CaravanPack.esm',
    r'CaravanPack.nam',
    r'ClassicPack - Main.bsa',
    r'ClassicPack.esm',
    r'ClassicPack.nam',
    r'MercenaryPack - Main.bsa',
    r'MercenaryPack.esm',
    r'MercenaryPack.nam',
    r'TribalPack - Main.bsa',
    r'TribalPack.esm',
    r'TribalPack.nam',
    #DLCs
    r'DEADMONEY.NAM',
    r'DeadMoney - Main.bsa',
    r'DeadMoney - Sounds.bsa',
    r'DeadMoney.esm',
    r'HONESTHEARTS.NAM',
    r'HonestHearts - Main.bsa',
    r'HonestHearts - Sounds.bsa',
    r'HonestHearts.esm',
    r'LONESOMEROAD.NAM',
    r'LonesomeRoad - Main.bsa',
    r'LonesomeRoad - Sounds.bsa',
    r'LonesomeRoad.esm',
    r'OLDWORLDBLUES.NAM',
    r'OldWorldBlues - Main.bsa',
    r'OldWorldBlues - Sounds.bsa',
    r'OldWorldBlues.esm',
    r'DLCList.txt',
    ))


#--Bash Tags supported by this game
allTags = sorted(('Body-F', 'Body-M', 'Body-Size-M', 'Body-Size-F', 'C.Climate', 'C.Light', 'C.Music', 'C.Name', 'C.RecordFlags',
                  'C.Owner', 'C.Water','Deactivate', 'Delev', 'Eyes', 'Factions', 'Relations', 'Filter', 'Graphics', 'Hair',
                  'IIM', 'Invent', 'Names', 'NoMerge', 'NpcFaces', 'R.Relations', 'Relev', 'Scripts', 'ScriptContents', 'Sound',
                  'Stats', 'Voice-F', 'Voice-M', 'R.Teeth', 'R.Mouth', 'R.Ears', 'R.Head', 'R.Attributes-F',
                  'R.Attributes-M', 'R.Skills', 'R.Description', 'Roads', 'Actors.Anims',
                  'Actors.AIData', 'Actors.DeathItem', 'Actors.AIPackages', 'Actors.AIPackagesForceAdd', 'Actors.Stats',
                  'Actors.ACBS', 'NPC.Class', 'Actors.CombatStyle', 'Creatures.Blood',
                  'NPC.Race','Actors.Skeleton', 'NpcFacesForceFullImport', 'MustBeActiveIfImported',
                  'Deflst', 'Destructible', 'WeaponMods'))

                  
# Installer -------------------------------------------------------------------
# ensure all path strings are prefixed with 'r' to avoid interpretation of
# accidental escape sequences
ignoreDataFiles = set((
#    r'NVSE\Plugins\Construction Set Extender.dll',
#    r'NVSE\Plugins\Construction Set Extender.ini'
    ))
 ignoreDataDirs = set((
#    r'NVSE\Plugins\ComponentDLLs\CSE',
    r'LSData'
    ))

# Tes3 Group/Top Types -------------------------------------------------------------

#--Top types in FalloutNV order.
topTypes = ['GMST', 'TXST', 'MICN', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'HAIR', 'EYES',
    'RACE', 'SOUN', 'ASPC', 'MGEF', 'SCPT', 'LTEX', 'ENCH', 'SPEL', 'ACTI', 'TACT',
    'TERM', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'STAT', 'SCOL',
    'MSTT', 'PWAT', 'GRAS', 'TREE', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'CREA', 'LVLC',
    'LVLN', 'KEYM', 'ALCH', 'IDLM', 'NOTE', 'PROJ', 'LVLI', 'WTHR', 'CLMT', 'REGN',
    'NAVI', 'CELL', 'WRLD', 'DIAL', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR', 'ANIO',
    'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD', 'ADDN',
    'COBJ', 'AVIF', 'RADS', 'CAMS', 'CPTH', 'VTYP', 'IPCT', 'IPDS', 'ARMA', 'ECZN',
    'MESG', 'RGDL', 'DOBJ', 'LGTM', 'MUSC', 'IMOD', 'REPU', 'RCPE', 'RCCT', 'CHIP',
    'CSNO', 'LSCT', 'MSET', 'ALOC', 'CHAL', 'AMEF', 'CCRD', 'CMNY', 'CDCK', 'DEHY',
    'HUNG', 'SLPD',
    # Unused types in falloutNV. (dummy)
    'SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA',
    ]

# Fo3 added
# ['BPTD', 'VTYP', 'MUSC', 'FLST', 'PWAT', 'MICN', 'AVIF', 'NOTE', 'TERM', 'ASPC',
#  'PERK', 'HDPT', 'TXST', 'DOBJ', 'NAVI', 'EXPL', 'IPDS', 'IDLM', 'ARMA', 'LVLN',
#  'MSTT', 'IMAD', 'TACT', 'RGDL', 'CPTH', 'IMGS', 'MESG', 'DEBR', 'LGTM', 'SCOL',
#  'ECZN', 'CAMS', 'RADS', 'PROJ', 'IPCT', 'ADDN', 'COBJ' ]
# NV added
# ['IMOD', 'REPU', 'RCPE', 'RCCT', 'CHIP', 'CSNO', 'LSCT', 'MSET', 'ALOC', 'CHAL',
#  'AMEF', 'CCRD', 'CMNY', 'CDCK', 'DEHY', 'HUNG', 'SLPD' ]
# Oblivion specifics
# ['SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA']


#------------------------------------------------------------------------------
class MreActi(MelRecord):
    """Activator record."""
    classType = 'ACTI'
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FULL','full'),
        MelModel(),
        MelFid('SCRI','script'),
        MelDestructible(),
        MelFid('SNAM','soundLooping'),
        MelFid('VNAM','soundActivation'),
        MelFid('INAM','radioTemplate'),
        MelFid('RNAM','radioStation'),
        MelFid('WNAM','waterType'),
        MelString('XATO','activationPrompt'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreAmmo(MelRecord):
    """Ammo (arrow) record."""
    classType = 'AMMO'
    _flags = Flags(0L,Flags.getNames('notNormalWeapon'))
    class MelAmmoDat2(MelStruct):
        """Handle older trucated DAT2 for AMMO subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 20:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 12:
                unpacked = ins.unpack('IIf',size,readId)
            else:
                raise "Unexpected size encountered for AMMO:DAT2 subrecord: %s" % size
            unpacked += self.defaults[len(unpacked):]
            setter = record.__setattr__
            for attr,value,action in zip(self.attrs,unpacked,self.actions):
                if callable(action): value = action(value)
                setter(attr,value)
            if self._debug: print unpacked
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FULL','full'),
        MelModel(),
        MelString('ICON','largeIconPath'),
        MelString('MICO','smallIconPath'),
        MelFid('SCRI','script'),
        MelDestructible(),
        MelFid('YNAM','soundPickup'),
        MelFid('ZNAM','soundDrop'),
        MelStruct('DATA','fB3sIB','speed',(_flags,'flags',0L),('unused1',null3),'value','clipRounds'),
        MelAmmoDat2('DAT2','IIfIf','projPerShot',(FID,'projectile',0L),'weight',(FID,'consumedAmmo'),'consumedPercentage'),
        MelString('ONAM','shortName'),
        MelString('QNAM','abbrev'),
        MelFids('RCIL','effects'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed() 

#------------------------------------------------------------------------------
class MreArmo(MelRecord):
    """Armor record."""
    classType = 'ARMO'
    _flags = MelBipedFlags(0L,Flags.getNames())
    _generalFlags = Flags(0L,Flags.getNames(
        (5,'powerArmor'),
        (6,'notPlayable'),
        (7,'heavyArmor')
    ))
    _etype = Flags(0L,Flags.getNames(
        'alcohol','bigGuns','bodyWear','chems','energyWeapons','food','handWear','headWear',
        'meleeWeapons','mine','none','smallGuns','stimpack','thrownWeapons','unarmedWeapon'
    ))
    
    class MelArmoDnam(MelStruct):
        """Handle older trucated DNAM for ARMO subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 12:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 4:
                unpacked = ins.unpack('=HH',size,readId)
            else:
                raise "Unexpected size encountered for ARMO subrecord: %s" % size
            unpacked += self.defaults[len(unpacked):]
            setter = record.__setattr__
            for attr,value,action in zip(self.attrs,unpacked,self.actions):
                if callable(action): value = action(value)
                setter(attr,value)
            if self._debug: print unpacked, record.flags.getTrueAttrs()

    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FULL','full'),
        MelFid('SCRI','script'),
        MelFid('EITM','objectEffect'),
        MelStruct('BMDT','=2I',(_flags,'bipedFlags',0L),(_generalFlags,'generalFlags',0L)),
        MelModel('maleBody'),
        MelModel('maleWorld',2),
        MelString('ICON','maleLargeIconPath'),
        MelString('MICO','maleSmallIconPath'),
        MelModel('femaleBody',3),
        MelModel('femaleWorld',4),
        MelString('ICO2','femaleLargeIconPath'),
        MelString('MIC2','femaleSmallIconPath'),
        MelString('BMCT','ragdollConstraintTemplate'),
        MelDestructible(),
        MelFid('REPL','repairList'),
        MelFid('BIPL','bipedModelList'),
        MelStruct('ETYP','I',(_etype,'etype',0L)),
        MelFid('YNAM','soundPickUp'),
        MelFid('ZNAM','soundDrop'),
        MelStruct('DATA','=IIf','value','health','weight'),
        MelArmoDnam('DNAM','=HHfI','ar','flags','dt',('unknown',0L)), # AR is multiplied by 100.
        MelStruct('BNAM','I',('overridesAnimationSound',0L)),
        MelStructs('SNAM','IB3sI','animationSounds',(FID,'sound'),'chance',('unused','\xb7\xe7\x0b'),'type'),
        MelFid('TNAM','animationSoundsTemplate'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreCont(MelRecord):
    """Container record."""
    classType = 'CONT'
    _flags = Flags(0,Flags.getNames(None,'respawns'))
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FULL','full'),
        MelModel(),
        MelFid('SCRI','script'),
        MelGroups('items',
            MelStruct('CNTO','Ii',(FID,'item',None),('count',1)),
            MelOptStruct('COED','IIf',(FID,'owner',None),(FID,'glob',None),('condition',1.0)),
        ),
        MelDestructible(),
        MelStruct('DATA','=Bf',(_flags,'flags',0L),'weight'),
        MelFid('SNAM','soundOpen'),
        MelFid('QNAM','soundClose'),
        MelFid('RNAM','soundRandomLooping'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreDial(MelRecord):
    """Dialog record."""
    classType = 'DIAL'
    
    class MelDialData(MelStruct):
        """Handle older trucated DATA for DIAL subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 2:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 1:
                unpacked = ins.unpack('B',size,readId)
            else:
                raise "Unexpected size encountered for DIAL subrecord: %s" % size
            unpacked += self.defaults[len(unpacked):]
            setter = record.__setattr__
            for attr,value,action in zip(self.attrs,unpacked,self.actions):
                if callable(action): value = action(value)
                setter(attr,value)
            if self._debug: print unpacked, record.flags.getTrueAttrs()
    class MelDialDistributor(MelNull):
        def __init__(self):
            self._debug = False
        def getLoaders(self,loaders):
            """Self as loader for structure types."""
            for type in ('INFC','INFX',):
                loaders[type] = self
        def setMelSet(self,melSet):
            """Set parent melset. Need this so that can reassign loaders later."""
            self.melSet = melSet
            self.loaders = {}
            for element in melSet.elements:
                attr = element.__dict__.get('attr',None)
                if attr: self.loaders[attr] = element
        def loadData(self,record,ins,type,size,readId):
            if type in ('INFC', 'INFX'):
                quests = record.__getattribute__('quests')
                if quests:
                    element = self.loaders['quests']
                else:
                    if type == 'INFC':
                        element = self.loaders['bare_infc_p']
                    elif type == 'INFX':
                        element = self.loaders['bare_infx_p']
            element.loadData(record,ins,type,size,readId)
    
    melSet = MelSet(
        MelString('EDID','eid'),
        MelFid('INFC','bare_infc_p'),
        MelFid('INFX','bare_infx_p'),
        MelGroups('quests',
            MelFid('QSTI','quest'),
            MelGroups('unknown',
                MelFid('INFC','infc_p'),
                MelBase('INFX','infx_p'),
            ),
        ),
         MelString('FULL','full'),
        MelStruct('PNAM','f','priority'),
        MelString('TDUM','tdum_p'),
        MelDialData('DATA','BB','dialType','dialFlags'),
        MelDialDistributor(),
     )
    melSet.elements[-1].setMelSet(melSet)
    )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed() + ['infoStamp','infoStamp2','infos']

    def __init__(self,header,ins=None,unpack=False):
        """Initialize."""
        MelRecord.__init__(self,header,ins,unpack)
        self.infoStamp = 0 #--Stamp for info GRUP
        self.infoStamp2 = 0 #--Stamp for info GRUP
        self.infos = []

    def loadInfos(self,ins,endPos,infoClass):
        """Load infos from ins. Called from MobDials."""
        infos = self.infos
        recHead = ins.unpackRecHeader
        infosAppend = infos.append
        while not ins.atEnd(endPos,'INFO Block'):
            #--Get record info and handle it
            header = recHead()
            recType = header[0]
            if recType == 'INFO':
                info = infoClass(header,ins,True)
                infosAppend(info)
            else:
                raise ModError(ins.inName, _('Unexpected %s record in %s group.')
                    % (recType,"INFO"))

    def dump(self,out):
        """Dumps self., then group header and then records."""
        MreRecord.dump(self,out)
        if not self.infos: return
        size = 20 + sum([20 + info.getSize() for info in self.infos])
        out.pack('4sIIIII','GRUP',size,self.fid,7,self.infoStamp,self.infoStamp2)
        for info in self.infos: info.dump(out)

    def updateMasters(self,masters):
        """Updates set of master names according to masters actually used."""
        MelRecord.updateMasters(self,masters)
        for info in self.infos:
            info.updateMasters(masters)

    def convertFids(self,mapper,toLong):
        """Converts fids between formats according to mapper.
        toLong should be True if converting to long format or False if converting to short format."""
        MelRecord.convertFids(self,mapper,toLong)
        for info in self.infos:
            info.convertFids(mapper,toLong)

#------------------------------------------------------------------------------
class MreFact(MelRecord):
    """Faction record."""
    classType = 'FACT'
    _flags = Flags(0L,Flags.getNames('hiddenFromPC','evil','specialCombat'))

    class MelFactData(MelStruct):
        """Handle older trucated DATA for FACT subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 4:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 2:
                #--Else 2 byte record
                unpacked = ins.unpack('2B',size,readId)
            elif size == 1:
                #--Else 1 byte record
                unpacked = ins.unpack('B',size,readId)
            else:
                raise "Unexpected size encountered for FACT:DATA subrecord: %s" % size
            unpacked += self.defaults[len(unpacked):]
            setter = record.__setattr__
            for attr,value,action in zip(self.attrs,unpacked,self.actions):
                if callable(action): value = action(value)
                setter(attr,value)
            if self._debug: print unpacked

    melSet = MelSet(
        MelString('EDID','eid'),
        MelString('FULL','full'),
        MelStructs('XNAM','I2i','relations',(FID,'faction'),'mod','groupCombatReaction'),
        MelFactData('DATA','2BH',(_flags,'flags',0L),'flags2','unknown'),
        MelOptStruct('CNAM','f',('crimeGoldMultiplier',None)),
        MelGroups('ranks',
            MelStruct('RNAM','i','rank'),
            MelString('MNAM','male'),
            MelString('FNAM','female'),
            MelString('INAM','insigniaPath'),),
        MelOptStruct('WMI1','I',(FID,'reputation',None)),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

# Id Functions ----------------------------------------------------------------

ob = getIdFunc('FalloutNV.esm')

# Function Info ---------------------------------------------------------------
conditionFunctionData = ( #--0: no param; 1: int param; 2: formid param
    (153, 'CanHaveFlames', 0, 0, 0, 0),
    (127, 'HasBeenEatan', 0, 0, 0, 0),
    ( 14, 'GetActorValue', 1, 0, 0, 0),
    ( 61, 'GetAlarmed', 0, 0, 0, 0),
    (190, 'GetAmountSoldStolen', 0, 0, 0, 0),
    (  8, 'GetAngle', 1, 0, 0, 0),
    ( 81, 'GetArmorRating', 0, 0, 0, 0),
    (274, 'GetArmorRatingUpperBody', 0, 0, 0, 0),
    ( 63, 'GetAttacked', 0, 0, 0, 0),
    (264, 'GetBarterGold', 0, 0, 0, 0),
    (277, 'GetBaseActorValue', 1, 0, 0, 0),
    (229, 'GetClassDefaultMatch', 0, 0, 0, 0),
    ( 41, 'GetClothingValue', 0, 0, 0, 0),
    (122, 'GetCrime', 2, 1, 0, 0),
    (116, 'GetMinorCrimeCount', 0, 0, 0, 0),
    (110, 'GetCurrentAIPackage', 0, 0, 0, 0),
    (143, 'GetCurrentAIProcedure', 0, 0, 0, 0),
    ( 18, 'GetCurrentTime', 0, 0, 0, 0),
    (148, 'GetCurrentWeatherPercent', 0, 0, 0, 0),
    (170, 'GetDayOfWeek', 0, 0, 0, 0),
    ( 46, 'GetDead', 0, 0, 0, 0),
    ( 84, 'GetDeadCount', 2, 0, 0, 0),
    (203, 'GetDestroyed', 0, 0, 0, 0),
    ( 45, 'GetDetected', 2, 0, 0, 0),
    (180, 'GetDetectionLevel', 2, 0, 0, 0),
    ( 35, 'GetDisabled', 0, 0, 0, 0),
    ( 39, 'GetDisease', 0, 0, 0, 0),
    ( 76, 'GetDisposition', 2, 0, 0, 0),
    (  1, 'GetDistance', 2, 0, 0, 0),
    (215, 'GetDefaultOpen', 0, 0, 0, 0),
    (182, 'GetEquipped', 2, 0, 0, 0),
    ( 73, 'GetFactionRank', 2, 0, 0, 0),
    ( 60, 'GetFactionRankDifference', 2, 2, 0, 0),
    (128, 'GetFatiguePercentage', 0, 0, 0, 0),
    (288, 'GetFriendHit', 2, 0, 0, 0),
    (160, 'GetFurnitureMarkerID', 0, 0, 0, 0),
    ( 74, 'GetGlobalValue', 2, 0, 0, 0),
    ( 48, 'GetGold', 0, 0, 0, 0),
    ( 99, 'GetHeadingAngle', 2, 0, 0, 0),
    (318, 'GetIdleDoneOnce', 0, 0, 0, 0),
    (338, 'GetIgnoreFriendlyHits', 0, 0, 0, 0),
    ( 67, 'GetInCell', 2, 0, 0, 0),
    (230, 'GetInCellParam', 2, 2, 0, 0),
    ( 71, 'GetInFaction', 2, 0, 0, 0),
    ( 32, 'GetInSameCell', 2, 0, 0, 0),
    (310, 'GetInWorldspace', 2, 0, 0, 0),
    ( 91, 'GetIsAlerted', 0, 0, 0, 0),
    ( 68, 'GetIsClass', 2, 0, 0, 0),
    (228, 'GetIsClassDefault', 2, 0, 0, 0),
    ( 64, 'GetIsCreature', 0, 0, 0, 0),
    (161, 'GetIsCurrentPackage', 2, 0, 0, 0),
    (149, 'GetIsCurrentWeather', 2, 0, 0, 0),
    (237, 'GetIsGhost', 0, 0, 0, 0),
    ( 72, 'GetIsID', 2, 0, 0, 0),
    (254, 'GetIsPlayableRace', 0, 0, 0, 0),
    (224, 'GetVATSMode', 0, 0, 0, 0),
    ( 69, 'GetIsRace', 2, 0, 0, 0),
    (136, 'GetIsReference', 2, 0, 0, 0),
    ( 70, 'GetIsSex', 1, 0, 0, 0),
    (246, 'GetIsUsedItem', 2, 0, 0, 0),
    (247, 'GetIsUsedItemType', 1, 0, 0, 0),
    ( 47, 'GetItemCount', 2, 0, 0, 0),
    (107, 'GetKnockedState', 0, 0, 0, 0),
    ( 80, 'GetLevel', 0, 0, 0, 0),
    ( 27, 'GetLineOfSight', 2, 0, 0, 0),
    (  5, 'GetLocked', 0, 0, 0, 0),
    ( 65, 'GetLockLevel', 0, 0, 0, 0),
    (320, 'GetNoRumors', 0, 0, 0, 0),
    (255, 'GetOffersServicesNow', 0, 0, 0, 0),
    (157, 'GetOpenState', 0, 0, 0, 0),
    (193, 'GetPCExpelled', 2, 0, 0, 0),
    (199, 'GetPCFactionAttack', 2, 0, 0, 0),
    (195, 'GetPCFactionMurder', 2, 0, 0, 0),
    (197, 'GetPCEnemyofFaction', 2, 0, 0, 0),
    (132, 'GetPCInFaction', 2, 0, 0, 0),
    (129, 'GetPCIsClass', 2, 0, 0, 0),
    (130, 'GetPCIsRace', 2, 0, 0, 0),
    (131, 'GetPCIsSex', 1, 0, 0, 0),
    (312, 'GetPCMiscStat', 1, 0, 0, 0),
    (225, 'GetPersuasionNumber', 0, 0, 0, 0),
    ( 98, 'GetPlayerControlsDisabled', 0, 0, 0, 0),
    (365, 'IsChild', 0, 0, 0, 0),
    (362, 'GetPlayerHasLastRiddenHorse', 0, 0, 0, 0),
    (  6, 'GetPos', 1, 0, 0, 0),
    ( 56, 'GetQuestRunning', 2, 0, 0, 0),
    ( 79, 'GetQuestVariable', 2, 1, 0, 0),
    ( 77, 'GetRandomPercent', 0, 0, 0, 0),
    (244, 'GetRestrained', 0, 0, 0, 0),
    ( 24, 'GetScale', 0, 0, 0, 0),
    ( 53, 'GetScriptVariable', 2, 1, 0, 0),
    ( 12, 'GetSecondsPassed', 0, 0, 0, 0),
    ( 66, 'GetShouldAttack', 2, 0, 0, 0),
    (159, 'GetSitting', 0, 0, 0, 0),
    ( 49, 'GetSleeping', 0, 0, 0, 0),
    ( 58, 'GetStage', 2, 0, 0, 0),
    ( 59, 'GetStageDone', 2, 1, 0, 0),
    ( 11, 'GetStartingAngle', 1, 0, 0, 0),
    ( 10, 'GetStartingPos', 1, 0, 0, 0),
    ( 50, 'GetTalkedToPC', 0, 0, 0, 0),
    (172, 'GetTalkedToPCParam', 2, 0, 0, 0),
    (361, 'GetTimeDead', 0, 0, 0, 0),
    (315, 'GetTotalPersuasionNumber', 0, 0, 0, 0),
    (144, 'GetTrespassWarningLevel', 0, 0, 0, 0),
    (242, 'GetUnconscious', 0, 0, 0, 0),
    (259, 'GetUsedItemActivate', 0, 0, 0, 0),
    (258, 'GetUsedItemLevel', 0, 0, 0, 0),
    ( 40, 'GetVampire', 0, 0, 0, 0),
    (142, 'GetWalkSpeed', 0, 0, 0, 0),
    (108, 'GetWeaponAnimType', 0, 0, 0, 0),
    (109, 'IsWeaponSkillType', 1, 0, 0, 0),
    (147, 'GetWindSpeed', 0, 0, 0, 0),
    (154, 'HasFlames', 0, 0, 0, 0),
    (214, 'HasMagicEffect', 2, 0, 0, 0),
    (227, 'HasCannibal', 0, 0, 0, 0),
    (353, 'IsActor', 0, 0, 0, 0),
    (314, 'IsActorAVictim', 0, 0, 0, 0),
    (313, 'IsActorEvil', 0, 0, 0, 0),
    (306, 'IsActorUsingATorch', 0, 0, 0, 0),
    (280, 'IsCellOwner', 2, 2, 0, 0),
    (267, 'IsCloudy', 0, 0, 0, 0),
    (150, 'IsContinuingPackagePCNear', 0, 0, 0, 0),
    (163, 'IsCurrentFurnitureObj', 2, 0, 0, 0),
    (162, 'IsCurrentFurnitureRef', 2, 0, 0, 0),
    (354, 'IsEssential', 0, 0, 0, 0),
    (106, 'IsFacingUp', 0, 0, 0, 0),
    (125, 'IsGuard', 0, 0, 0, 0),
    (282, 'IsHorseStolen', 0, 0, 0, 0),
    (112, 'IsIdlePlaying', 0, 0, 0, 0),
    (289, 'IsInCombat', 0, 0, 0, 0),
    (332, 'IsInDangerousWater', 0, 0, 0, 0),
    (300, 'IsInInterior', 0, 0, 0, 0),
    (146, 'IsInMyOwnedCell', 0, 0, 0, 0),
    (285, 'IsLeftUp', 0, 0, 0, 0),
    (278, 'IsOwner', 2, 0, 0, 0),
    (176, 'IsPCAMurderer', 0, 0, 0, 0),
    (175, 'IsPCSleeping', 0, 0, 0, 0),
    (358, 'IsPlayerMovingIntoNewSpace', 0, 0, 0, 0),
    (339, 'IsPlayersLastRiddenHorse', 0, 0, 0, 0),
    (266, 'IsPleasant', 0, 0, 0, 0),
    ( 62, 'IsRaining', 0, 0, 0, 0),
    (327, 'IsRidingHorse', 0, 0, 0, 0),
    (287, 'IsRunning', 0, 0, 0, 0),
    (103, 'IsShieldOut', 0, 0, 0, 0),
    (286, 'IsSneaking', 0, 0, 0, 0),
    ( 75, 'IsSnowing', 0, 0, 0, 0),
    (223, 'IsSpellTarget', 2, 0, 0, 0),
    (185, 'IsSwimming', 0, 0, 0, 0),
    (141, 'IsTalking', 0, 0, 0, 0),
    (265, 'IsTimePassing', 0, 0, 0, 0),
    (102, 'IsTorchOut', 0, 0, 0, 0),
    (145, 'IsTrespassing', 0, 0, 0, 0),
    (111, 'IsWaiting', 0, 0, 0, 0),
    (101, 'IsWeaponOut', 0, 0, 0, 0),
    (309, 'IsXBox', 0, 0, 0, 0),
    ( 36, 'MenuMode', 1, 0, 0, 0),
    ( 42, 'SameFaction', 2, 0, 0, 0),
    (133, 'SameFactionAsPC', 0, 0, 0, 0),
    ( 43, 'SameRace', 2, 0, 0, 0),
    (134, 'SameRaceAsPC', 0, 0, 0, 0),
    ( 44, 'SameSex', 2, 0, 0, 0),
    (135, 'SameSexAsPC', 0, 0, 0, 0),
    (323, 'WhichServiceMenu', 0, 0, 0, 0),
    (449, 'HasPerk', 2, 1, 1, 2),
    (546, 'GetQuestCompleted', 2, 0, 0, 0),
    (427, 'GetIsVoiceType', 2, 0, 0, 0),
    (523, 'IsPS3', 0, 0, 0, 0),
    (524, 'IsWin32', 0, 0, 0, 0),
    (372, 'IsInList', 2, 0, 0, 0),
    (382, 'GetHasNote', 2, 1, 1, 2),
    (492, 'GetMapMakerVisible', 1, 1, 1, 2),
    (446, 'GetInZone', 2, 1, 1, 2),
    ( 25, 'IsMoving', 0, 0, 0, 0),
    ( 26, 'IsTurning', 0, 0, 0, 0),
    (451, 'IsLastIdlePlayed', 2, 0, 0, 0),
    (399, 'IsWeaponInList', 2, 0, 0, 0),
    (408, 'GetVATSValue', 1, 2, 0, 0),
    (435, 'GetDialogueEmotion', 0, 0, 0, 0),
    (235, 'GetVatsTargetHeight', 0, 0, 0, 0),
    (391, 'GetHitLocation', 0, 0, 0, 0),
    (392, 'IsPC1stPerson', 0, 0, 0, 0),
    (226, 'GetSandman', 0, 0, 0, 0),
    (428, 'GetPlantedExplosive', 0, 0, 0, 0),
    (304, 'IsWaterObject', 0, 0, 0, 0),
    (123, 'IsGreetingPlayer', 0, 0, 0, 0),
    (438, 'GetIsCreatureType', 1, 0, 0, 0),
    (503, 'GetRadiationLevel', 0, 0, 0, 0),
    (431, 'GetHealthPercentage', 0, 0, 0, 0),
    (411, 'GetFactionCombatReaction', 2, 2, 0, 0),
    (515, 'IsCombatTarget', 2, 0, 0, 0),
    (495, 'GetPermanentActorValue', 1, 0, 0, 0),
    (474, 'GetIsAlignment', 1, 0, 0, 0),
    (454, 'GetPlayerTeammate', 0, 0, 0, 0),
    (522, 'GetIsLockBroken', 0, 0, 0, 0),
    (433, 'GetIsObjectType', 1, 0, 0, 0),
    (500, 'GetWeaponHealthPerc', 0, 0, 0, 0),
    (368, 'IsPlayerActionActive', 1, 0, 0, 0),
    (416, 'GetGroupMemberCount', 0, 0, 0, 0),
    (417, 'GetGroupTargetCount', 0, 0, 0, 0),
    (510, 'GetLastHitCritical', 0, 0, 0, 0),
    (450, 'GetFactionRelation', 1, 0, 0, 0),
    (455, 'GetPlayerTeammateCount', 0, 0, 0, 0),
    (219, 'GetAnimAction', 0, 0, 0, 0),
    (430, 'IsActorTalkingThroughActivator', 0, 0, 0, 0),
    (480, 'GetIsUsedItemEquipType', 1, 0, 0, 0),
    (398, 'IsLimbGone', 1, 0, 0, 0),
    (550, 'IsGoreDisabled', 0, 0, 0, 0),
    (420, 'GetObjectiveCompleted', 2, 1, 0, 0),
    (421, 'GetObjectiveDisplayed', 2, 1, 0, 0),
    (397, 'GetCauseofDeath', 0, 0, 0, 0),
    (415, 'Exists', 2, 0, 0, 0),
    (117, 'GetMajorCrimeCount', 0, 0, 0, 0),
    (471, 'GetDestructionStage', 0, 0, 0, 0),
    (460, 'GetActorFactionPlayerEnemy', 0, 0, 0, 0),
    (586, 'IsHardcore', 0, 0, 0, 0),
    (575, 'GetReputationThreshold', 2, 1, 0, 0),
    (610, 'GetCasinoWinningStage', 2, 0, 0, 0),
    (573, 'GetReputation', 2, 1, 0, 0),
    (612, 'PlayerInRegion', 2, 0, 0, 0),
    (601, 'GetForceHitReaction', 0, 0, 0, 0),
    (118, 'GetActorAggroRadiusViolated', 0, 0, 0, 0),
    (192, 'GetIgnoreCrime', 0, 0, 0, 0),
    (367, 'GetLastPlayerAction', 0, 0, 0, 0),
    (370, 'IsTalkingActivatorActor', 2, 0, 0, 0),
    (403, 'HasFriendDisposition', 0, 0, 0, 0),
    (409, 'IsKiller', 2, 0, 0, 0),
    (410, 'IsKillerObject', 2, 0, 0, 0),
    (436, 'GetDialogueEmotionValue', 0, 0, 0, 0),
    (459, 'GetActorCrimePlayerEnemy', 0, 0, 0, 0),
    (462, 'IsPlayerTagSkill', 1, 0, 0, 0),
    (464, 'IsPlayerGrabbedRef', 1, 0, 0, 0),
    (478, 'GetThreatRatio', 2, 0, 0, 0),
    (489, 'GetConcussed', 0, 0, 0, 0),
    (496, 'GetKillingBlowLimb', 0, 0, 0, 0),
    (518, 'GetVATSRightAreaFree', 1, 0, 0, 0),
    (519, 'GetVATSLeftAreaFree', 1, 0, 0, 0),
    (520, 'GetVATSBackAreaFree', 1, 0, 0, 0),
    (521, 'GetVATSFrontAreaFree', 1, 0, 0, 0),
    (525, 'GetVATSRightTargetVisible', 1, 0, 0, 0),
    (526, 'GetVATSLeftTargetVisible', 1, 0, 0, 0),
    (527, 'GetVATSBackTargetVisible', 1, 0, 0, 0),
    (528, 'GetVATSFrontTargetVisible', 1, 0, 0, 0),
    (531, 'IsInCriticalStage', 1, 0, 0, 0),
    (533, 'GetXPForNextLevel', 0, 0, 0, 0),
    (555, 'GetSpellUsageNum', 2, 0, 0, 0),
    (557, 'GetActorsInHigh', 0, 0, 0, 0),
    (558, 'HasLoaded3D', 0, 0, 0, 0),
    (574, 'GetReputationPct', 2, 1, 0, 0),
    (607, 'ChallengeLocked', 2, 0, 0, 0),
    (614, 'GetChallengeCompleted', 2, 0, 0, 0),
    (619, 'IsAlwaysHardcore', 0, 0, 0, 0),

    # extended by NVSE
    (1024, 'GetNVSEVersion', 0, 0, 0, 0),
    (1025, 'GetNVSERevision', 0, 0, 0, 0),
    (1213, 'GetNVSEBeta', 0, 0, 0, 0),
    (1082, 'IsKeyPressed', 1, 0, 0, 0),
    (1166, 'IsControlPressed', 1, 0, 0, 0),
    (1028, 'GetWeight', 2, 0, 0, 0),
    (1165, 'GetWeaponHasScope', 0, 0, 0, 0),
    )

#--Plugin format stuff
class esp:
    #--Valid ESM/ESP header versions
    validHeaderVersions = (1.32)