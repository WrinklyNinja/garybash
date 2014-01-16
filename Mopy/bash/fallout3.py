# -*- coding: utf-8 -*-

# Wrye Flash
# Module for Fallout 3 definitions.
# When Flash decides what game it should run for, it should then import this module as
# import fallout3 as game
# All code changes made during the merge reference this game module alias instead of a specific game.

#--The main plugin Wrye Bash should look for
masterFiles = [
    u'Fallout3.esm',
    ]

#--INI files that should show up in the INI Edits tab
iniFiles = [
    u'FalloutPrefs.ini',
    ]

#--URL to the Nexus site for this game
nexusUrl = u'http://www.fallout3nexus.com/'
nexusName = u'Fallout 3 Nexus'
nexusKey = 'bash.installers.openFallout3Nexus'
    
#--Script Extender information
class se:
    shortName = u'FOSE'                      # Abbreviated name
    longName = u'Fallout 3 Script Extender'   # Full name
    exe = u'fose_loader.exe'                 # Exe to run
    steamExe = u'fose_loader.dll'           # Exe to run if a steam install
    url = u'http://fose.silverlock.org/'     # URL to download from
    urlTip = u'http://fose.silverlock.org/'  # Tooltip for mouse over the URL
    
#--Game ESM/ESP/BSA files
bethDataFiles = set((
    #--Vanilla
    r'fallout3.esm',
    r'fallout - menuvoices.bsa',
    r'fallout - meshes.bsa',
    r'fallout - misc.bsa',
    r'fallout - sound.bsa',
    r'fallout - textures.bsa',
    r'fallout - voices.bsa',
    #-- DLC
    r'anchorage.esm',
    r'anchorage - main.bsa',
    r'anchorage - sounds.bsa',
    r'thepitt.esm',
    r'thepitt - main.bsa',
    r'thepitt - sounds.bsa',
    r'brokensteel.esm',
    r'brokensteel - main.bsa',
    r'brokensteel - sounds.bsa',
    r'pointlookout.esm',
    r'pointlookout - main.bsa',
    r'pointlookout - sounds.bsa',
    r'zeta.esm',
    r'zeta - main.bsa',
    r'zeta - sounds.bsa',
    ))
allBethFiles = set((
    #vanilla
    r'Credits.txt',
    r'CreditsWacky.txt',
    r'Fallout3.esm',
    r'Fallout - MenuVoices.bsa',
    r'Fallout - Meshes.bsa',
    r'Fallout - Misc.bsa',
    r'Fallout - Sound.bsa',
    r'Fallout - Textures.bsa',
    r'Fallout - Voices.bsa',
    r'LODSettings\aaaForgotten1.DLODSettings',
    r'LODSettings\aaaForgotten4.DLODSettings',
    r'LODSettings\aaaForgotten5.DLODSettings',
    r'Music\Base\Base_01.mp3',
    r'Music\Base\Base_02.mp3',
    r'Music\Base\Base_03.mp3',
    r'Music\Base\Base_04.mp3',
    r'Music\Battle\Battle_01.mp3',
    r'Music\Battle\Battle_02.mp3',
    r'Music\Battle\Battle_03.mp3',
    r'Music\Battle\Battle_04.mp3',
    r'Music\Battle\Battle_05.mp3',
    r'Music\Battle\Battle_06.mp3',
    r'Music\Battle\Battle_07.mp3',
    r'Music\Battle\Finale\Battle_01.mp3',
    r'Music\Battle\Finale\Battle_02.mp3',
    r'Music\Battle\Finale\Battle_03.mp3',
    r'Music\Battle\Finale\Battle_04.mp3',
    r'Music\Battle\Finale\Battle_05.mp3',
    r'Music\Battle\Finale\Battle_06.mp3',
    r'Music\Battle\Finale\Battle_07.mp3',
    r'Music\Dungeon\Dungeon_01.mp3',
    r'Music\Dungeon\Dungeon_02.mp3',
    r'Music\Dungeon\Dungeon_03.mp3',
    r'Music\Dungeon\Dungeon_04.mp3',
    r'Music\Dungeon\Dungeon_05.mp3',
    r'Music\Endgame\Endgame_01.mp3',
    r'Music\Endgame\Endgame_02.mp3',
    r'Music\Endgame\Endgame_03.mp3',
    r'Music\Endgame\Endgame_04.mp3',
    r'Music\Endgame\Endgame_05.mp3',
    r'Music\Endgame\Endgame_06.mp3',
    r'Music\Endgame\Endgame_07.mp3',
    r'Music\Endgame\Endgame_08.mp3',
    r'Music\Endgame\Endgame_09.mp3',
    r'Music\Endgame\Endgame_11.mp3',
    r'Music\Endgame\Endgame_12.mp3',
    r'Music\Endgame\Endgame_14.mp3',
    r'Music\Endgame\Endgame_15.mp3',
    r'Music\Endgame\Endgame_17.mp3',
    r'Music\Endgame\Endgame_18.mp3',
    r'Music\Endgame\Endgame_19.mp3',
    r'Music\Explore\Explore_01.mp3',
    r'Music\Explore\Explore_02.mp3',
    r'Music\Explore\Explore_03.mp3',
    r'Music\Explore\Explore_04.mp3',
    r'Music\Explore\Explore_05.mp3',
    r'Music\Explore\Explore_06.mp3',
    r'Music\Explore\Explore_07.mp3',
    r'Music\Public\Public_01.mp3',
    r'Music\Public\Public_02.mp3',
    r'Music\Public\Public_03.mp3',
    r'Music\Public\Public_04.mp3',
    r'Music\Public\Public_05.mp3',
    r'Music\Special\Death.mp3',
    r'Music\Special\ExitTheVault.mp3',
    r'Music\Special\MainTitle.mp3',
    r'Music\Special\Success.mp3',
    r'Music\Tension\Tension_01.mp3',
    r'Music\TranquilityLane\MUS_TranquilityLane_01_LP.mp3',
    r'Music\TranquilityLane\MUS_TranquilityLane_02_LP.mp3',
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
    r'Video\1 year later.bik',
    r'Video\2 weeks later.bik',
    r'Video\3 years later.bik',
    r'Video\6 years later.bik',
    r'Video\9 years later.bik',
    r'Video\B01.bik',
    r'Video\B02.bik',
    r'Video\B03.bik',
    r'Video\B04.bik',
    r'Video\B05.bik',
    r'Video\B06.bik',
    r'Video\B07.bik',
    r'Video\B08.bik',
    r'Video\B09.bik',
    r'Video\B10.bik',
    r'Video\B11.bik',
    r'Video\B12.bik',
    r'Video\B13.bik',
    r'Video\B14.bik',
    r'Video\B15.bik',
    r'Video\B16.bik',
    r'Video\B17.bik',
    r'Video\B18.bik',
    r'Video\B19.bik',
    r'Video\B20.bik',
    r'Video\B21.bik',
    r'Video\B22.bik',
    r'Video\B23.bik',
    r'Video\B24.bik',
    r'Video\B25.bik',
    r'Video\B26.bik',
    r'Video\B27.bik',
    r'Video\B28.bik',
    r'Video\B29.bik',
    r'Video\Fallout INTRO Vsk.bik',
    #DLCs
    r'anchorage.esm',
    r'anchorage - main.bsa',
    r'anchorage - sounds.bsa',
    r'thepitt.esm',
    r'thepitt - main.bsa',
    r'thepitt - sounds.bsa',
    r'brokensteel.esm',
    r'brokensteel - main.bsa',
    r'brokensteel - sounds.bsa',
    r'pointlookout.esm',
    r'pointlookout - main.bsa',
    r'pointlookout - sounds.bsa',
    r'zeta.esm',
    r'zeta - main.bsa',
    r'zeta - sounds.bsa',
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
                  'Deflst', 'Destructible'))

   
# Installer -------------------------------------------------------------------
# ensure all path strings are prefixed with 'r' to avoid interpretation of
# accidental escape sequences
ignoreDataFiles = set((
#    r'FOSE\Plugins\Construction Set Extender.dll',
#    r'FOSE\Plugins\Construction Set Extender.ini'
    ))
ignoreDataDirs = set((
#    r'FOSE\Plugins\ComponentDLLs\CSE',
    r'LSData'
    ))
    
# Tes3 Group/Top Types -------------------------------------------------------------

#--Top types in Fallout3 order.
topTypes = ['GMST', 'TXST', 'MICN', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'HAIR', 'EYES',
    'RACE', 'SOUN', 'ASPC', 'MGEF', 'SCPT', 'LTEX', 'ENCH', 'SPEL', 'ACTI', 'TACT',
    'TERM', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'STAT', 'SCOL',
    'MSTT', 'PWAT', 'GRAS', 'TREE', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'CREA', 'LVLC',
    'LVLN', 'KEYM', 'ALCH', 'IDLM', 'NOTE', 'COBJ', 'PROJ', 'LVLI', 'WTHR', 'CLMT',
    'REGN', 'NAVI', 'CELL', 'WRLD', 'DIAL', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR',
    'ANIO', 'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD',
    'ADDN', 'AVIF', 'RADS', 'CAMS', 'CPTH', 'VTYP', 'IPCT', 'IPDS', 'ARMA', 'ECZN',
    'MESG', 'RGDL', 'DOBJ', 'LGTM', 'MUSC',
    # Unused types in fallout3. (dummy)
    'SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA',
    ]
    
# Added topTypes are...
# ['BPTD', 'VTYP', 'MUSC', 'FLST', 'PWAT', 'MICN', 'AVIF', 'NOTE', 'TERM', 'ASPC',
#  'PERK', 'HDPT', 'TXST', 'DOBJ', 'NAVI', 'EXPL', 'IPDS', 'IDLM', 'ARMA', 'LVLN',
#  'MSTT', 'IMAD', 'TACT', 'RGDL', 'CPTH', 'IMGS', 'MESG', 'DEBR', 'LGTM', 'SCOL',
#  'ECZN', 'CAMS', 'RADS', 'PROJ', 'IPCT', 'ADDN', 'COBJ']
#
# Removed topTypes are...
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
        MelFid('RNAM','radioStation'),
        MelFid('WNAM','waterType'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreAmmo(MelRecord):
    """Ammo (arrow) record."""
    classType = 'AMMO'
    _flags = Flags(0L,Flags.getNames('notNormalWeapon'))
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FULL','full'),
        MelModel(),
        MelString('ICON','largeIconPath'),
        MelString('MICO','smallIconPath'),
        MelDestructible(),
        MelFid('YNAM','soundPickup'),
        MelFid('ZNAM','soundDrop'),
        MelStruct('DATA','fB3sIB','speed',(_flags,'flags',0L),('unused1',null3),'value','clipRounds'),
        MelString('ONAM','shortName'),
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
        MelStruct('DNAM','=HH','ar','flags'), # AR is multiplied by 100.
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
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreDial(MelRecord):
    """Dialog record."""
    classType = 'DIAL'
    melSet = MelSet(
        MelString('EDID','eid'),
        MelFids('QSTI','quests'), ### QSTRs?
        MelString('FULL','full'),
        MelStruct('DATA','B','dialType'),
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
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreInfo(MelRecord):
    """Info (dialog entry) record."""
    classType = 'INFO'
    _flags = Flags(0,Flags.getNames(
        'goodbye','random','sayOnce','runImmediately','infoRefusal','randomEnd','runForRumors','sayOnceADay','alwaysDarken'))
    class MelInfoData(MelStruct):
        """Support older 2 byte version."""
        def loadData(self,record,ins,type,size,readId):
            if size != 2:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            unpacked = ins.unpack('2B',size,readId)
            unpacked += self.defaults[len(unpacked):]
            setter = record.__setattr__
            for attr,value,action in zip(self.attrs,unpacked,self.actions):
                if callable(action): value = action(value)
                setter(attr,value)
            if self._debug: print (record.dialType,record.flags.getTrueAttrs())

    class MelInfoSchr(MelStruct):
        """Print only if schd record is null."""
        def dumpData(self,record,out):
            if not record.schd_p:
                MelStruct.dumpData(self,record,out)
    #--MelSet
    melSet = MelSet(
        MelInfoData('DATA','HH','dialType',(_flags,'flags')),
        MelFid('QSTI','quests'),
        MelFid('TPIC','topic'),
        MelFid('PNAM','prevInfo'),
        MelFids('NAME','addTopics'),
        MelGroups('responses',
            MelStruct('TRDT','Ii4sB3s','emotionType','emotionValue',('unused1',null4),'responseNum',('unused2',null3)),
            MelString('NAM1','responseText'),
            MelString('NAM2','actorNotes'),
            ),
        MelConditions(),
        MelFids('TCLT','choices'),
        MelFids('TCLF','linksFrom'),
        MelBase('SCHD','schd_p'), #--Old format script header?
        MelInfoSchr('SCHR','4s4I',('unused2',null4),'numRefs','compiledSize','lastIndex','scriptType'),
        MelBase('SCDA','compiled_p'),
        MelString('SCTX','scriptText'),
        MelScrxen('SCRV/SCRO','references')
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreLigh(MelRecord):
    """Light source record."""
    classType = 'LIGH'
    _flags = Flags(0L,Flags.getNames('dynamic','canTake','negative','flickers',
        'unk1','offByDefault','flickerSlow','pulse','pulseSlow','spotLight','spotShadow'))
    #--Mel NPC DATA
    class MelLighData(MelStruct):
        """Handle older trucated DATA for LIGH subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 32:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 24:
                #--Else 24 byte record (skips value and weight...
                unpacked = ins.unpack('iI3BsIff',size,readId)
            else:
                raise ModError(ins.inName,_('Unexpected size encountered for LIGH:DATA subrecord: ')+str(size))
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
        MelModel(),
        MelFid('SCRI','script'),
        MelString('FULL','full'),
        MelString('ICON','iconPath'),
        MelLighData('DATA','iI3BsIffIf','duration','radius','red','green','blue',('unused1',null1),
            (_flags,'flags',0L),'falloff','fov','value','weight'),
        MelOptStruct('FNAM','f',('fade',None)),
        MelFid('SNAM','sound'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreLscr(MelRecord):
    """Load screen."""
    classType = 'LSCR'
    melSet = MelSet(
        MelString('EDID','eid'),
        MelString('ICON','iconPath'),
        MelString('DESC','text'),
        MelStructs('LNAM','2I2h','Locations',(FID,'direct'),(FID,'indirect'),'gridy','gridx'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreMisc(MelRecord):
    """MISC (miscellaneous item) record."""
    classType = 'MISC'
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
        MelFid('YNAM','soundPickUp'),
        MelFid('ZNAM','soundDrop'),
        MelStruct('DATA','if','value','weight'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreRegn(MelRecord):
    """Region record."""
    classType = 'REGN'
    _flags = Flags(0L,Flags.getNames(
        ( 2,'objects'),
        ( 3,'weather'),
        ( 4,'map'),
        ( 6,'grass'),
        ( 7,'sound'),))
    obflags = Flags(0L,Flags.getNames(
        ( 0,'conform'),
        ( 1,'paintVertices'),
        ( 2,'sizeVariance'),
        ( 3,'deltaX'),
        ( 4,'deltaY'),
        ( 5,'deltaZ'),
        ( 6,'Tree'),
        ( 7,'hugeRock'),))
    sdflags = Flags(0L,Flags.getNames(
        ( 0,'pleasant'),
        ( 1,'cloudy'),
        ( 2,'rainy'),
        ( 3,'snowy'),))

    ####Lazy hacks to correctly read/write regn data
    class MelRegnStructA(MelStructA):
        """Handler for regn record. Conditionally dumps next items."""
        def loadData(self,record,ins,type,size,readId):
            if record.entryType == 2 and self.subType == 'RDOT':
                MelStructA.loadData(self,record,ins,type,size,readId)
            elif record.entryType == 3 and self.subType == 'RDWT':
                MelStructA.loadData(self,record,ins,type,size,readId)
            elif record.entryType == 6 and self.subType == 'RDGS':
                MelStructA.loadData(self,record,ins,type,size,readId)
            elif record.entryType == 7 and self.subType == 'RDSD':
                MelStructA.loadData(self,record,ins,type,size,readId)

        def dumpData(self,record,out):
            """Conditionally dumps data."""
            if record.entryType == 2 and self.subType == 'RDOT':
                MelStructA.dumpData(self,record,out)
            elif record.entryType == 3 and self.subType == 'RDWT':
                MelStructA.dumpData(self,record,out)
            elif record.entryType == 6 and self.subType == 'RDGS':
                MelStructA.dumpData(self,record,out)
            elif record.entryType == 7 and self.subType == 'RDSD':
                MelStructA.dumpData(self,record,out)

    class MelRegnString(MelString):
        """Handler for regn record. Conditionally dumps next items."""
        def loadData(self,record,ins,type,size,readId):
            if record.entryType == 4 and self.subType == 'RDMP':
                MelString.loadData(self,record,ins,type,size,readId)
            elif record.entryType == 5 and self.subType == 'ICON':
                MelString.loadData(self,record,ins,type,size,readId)

        def dumpData(self,record,out):
            """Conditionally dumps data."""
            if record.entryType == 4 and self.subType == 'RDMP':
                MelString.dumpData(self,record,out)
            elif record.entryType == 5 and self.subType == 'ICON':
                MelString.dumpData(self,record,out)

    class MelRegnOptStruct(MelOptStruct):
        """Handler for regn record. Conditionally dumps next items."""
        def loadData(self,record,ins,type,size,readId):
            if record.entryType == 7 and self.subType == 'RDMD':
                MelOptStruct.loadData(self,record,ins,type,size,readId)

        def dumpData(self,record,out):
            """Conditionally dumps data."""
            if record.entryType == 7 and self.subType == 'RDMD':
                MelOptStruct.dumpData(self,record,out)

    melSet = MelSet(
        MelString('EDID','eid'),
        MelString('ICON','largeIconPath'),
        MelString('MICO','smallIconPath'),
        MelStruct('RCLR','3Bs','mapRed','mapBlue','mapGreen',('unused1',null1)),
        MelFid('WNAM','worldspace'),
        MelGroups('areas',
            MelStruct('RPLI','I','edgeFalloff'),
            MelStructA('RPLD','2f','points','posX','posY')),
        MelGroups('entries',
            MelStruct('RDAT', 'I2B2s','entryType', (_flags,'flags'), 'priority', ('unused1',null2)), ####flags actually an enum...
            MelRegnStructA('RDOT', 'IH2sf4B2H4s4f3H2s4s', 'objects', (FID,'objectId'), 'parentIndex',
            ('unused1',null2), 'density', 'clustering', 'minSlope', 'maxSlope',
            (obflags, 'flags'), 'radiusWRTParent', 'radius', ('unk1',null4),
            'maxHeight', 'sink', 'sinkVar', 'sizeVar', 'angleVarX',
            'angleVarY',  'angleVarZ', ('unused2',null2), ('unk2',null4)),
            MelRegnString('RDMP', 'mapName'),
            #MelRegnString('ICON', 'iconPath'),  ####Obsolete? Only one record in Fallout3.esm
            MelRegnStructA('RDGS', 'I4s', 'grasses', (FID,'grass'), ('unk1',null4)),
            MelRegnOptStruct('RDMD', 'I', ('musicType',None)),
            MelRegnStructA('RDSD', '3I', 'sounds', (FID, 'sound'), (sdflags, 'flags'), 'chance'),
            MelRegnStructA('RDWT', '3I', 'weather', (FID, 'weather', None), 'chance', (FID, 'global', None))),
    )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreSoun(MelRecord):
    """Sound record."""
    classType = 'SOUN'
    _flags = Flags(0L,Flags.getNames('randomFrequencyShift', 'playAtRandom',
        'environmentIgnored', 'randomLocation', 'loop','menuSound', '2d', '360LFE'))
    class MelSounSndx(MelStruct):
        """SNDX is a reduced version of SNDD. Allow it to read in, but not set defaults or write."""
        def loadData(self,record,ins,type,size,readId):
            MelStruct.loadData(self,record,ins,type,size,readId)
            record.point0 = 0
            record.point1 = 0
            record.point2 = 0
            record.point3 = 0
            record.point4 = 0
            record.reverb = 0
            record.priority = 0
            record.unknown = "\0"*8
        def getSlotsUsed(self):
            return ()
        def setDefault(self,record): return
        def dumpData(self,record,out): return
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelString('FNAM','soundFile'),
        MelOptStruct('SNDD','=2BbsIh2B6HI8s',('minDistance',None), ('maxDistance',None), ('freqAdjustment',None), ('unused1',null1),
            (_flags,'flags',None),('staticAtten',None),('stopTime',None),('startTime',None),
            ('point0',0),('point1',0),('point2',0),('point3',0),('point4',0),('reverb',0),('priority',0),'unknown'),
        MelSounSndx('SNDX','=2BbsIh2B',('minDistance',None), ('maxDistance',None), ('freqAdjustment',None), ('unused1',null1),
            (_flags,'flags',None),('staticAtten',None),('stopTime',None),('startTime',None),),
        MelBase('ANAM','_anam'), #--Should be a struct. Maybe later.
        MelBase('GNAM','_gnam'), #--Should be a struct. Maybe later.
        MelBase('HNAM','_hnam'), #--Should be a struct. Maybe later.
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreStat(MelRecord):
    """Static model record."""
    classType = 'STAT'
    melSet = MelSet(
        MelString('EDID','eid'),
        MelStruct('OBND','=6h',
                  'corner0X','corner0Y','corner0Z',
                  'corner1X','corner1Y','corner1Z'),
        MelModel(),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

#------------------------------------------------------------------------------
class MreWeap(MelRecord):
    """Weapon record."""
    classType = 'WEAP'
    _flags = Flags(0L,Flags.getNames('notNormalWeapon'))
    _dflags1 = Flags(0L,Flags.getNames(
            'ignoresNormalWeaponResistance',
            'isAutomatic',
            'hasScope',
            'cantDrop',
            'hideBackpack',
            'embeddedWeapon',
            'dontUse1stPersonISAnimations',
            'nonPlayable',
        ))
    _dflags2 = Flags(0L,Flags.getNames(
            'playerOnly',
            'npcsUseAmmo',
            'noJamAfterReload',
            'overrideActionPoint',
            'minorCrime',
            'rangeFixed',
            'notUseInNormalCombat',
            'overrideDamageToWeaponMult',
            'dontUse3rdPersonISAnimations',
            'shortBurst',
            'RumbleAlternate',
            'longBurst',
            'unknown12','unknown13','unknown14','unknown15',
            'unknown16','unknown17','unknown18','unknown19',
            'unknown20','unknown21','unknown22','unknown23',
            'unknown24','unknown25','unknown26','unknown27',
            'unknown28','unknown29','unknown30','unknown31',
        ))
    _cflags = Flags(0L,Flags.getNames(
            'onDeath',
            'unknown1','unknown2','unknown3','unknown4',
            'unknown5','unknown6','unknown7',
        ))

    class MelWeapDnam(MelStruct):
        """Handle older trucated DNAM for WEAP subrecord."""
        def loadData(self,record,ins,type,size,readId):
            if size == 136:
                MelStruct.loadData(self,record,ins,type,size,readId)
                return
            elif size == 124:
                #--Else 124 byte record (skips sightUsage, semiAutomaticFireDelayMin and semiAutomaticFireDelayMax...
                unpacked = ins.unpack('Iff4B5fI4BffII11fIIffI',size,readId)
            elif size == 120:
                #--Else 120 byte record (skips resistType, sightUsage, semiAutomaticFireDelayMin and semiAutomaticFireDelayMax...
                unpacked = ins.unpack('Iff4B5fI4BffII11fIIff',size,readId)
            else:
                raise "Unexpected size encountered for WEAP:DNAM subrecord: %s" % size
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
        MelModel('model'),
        MelString('ICON','largeIconPath'),
        MelString('MICO','smallIconPath'),
        MelFid('SCRI','script'),
        MelFid('EITM','effect'),
        MelOptStruct('EAMT','H', 'enchantment'),
        MelFid('NAM0','ammo'),
        MelDestructible(),
        MelFid('REPL','repairList'),
        #0:bigGuns,1:energyWeapons,2:smallGuns,3:meleeWeapons,4:unarmedWeapon,5:thrownWeapons,6:mine,
        MelStruct('ETYP','I','etype'),
        MelFid('BIPL','bipedModelList'),
        MelFid('YNAM','soundPickUp'),
        MelFid('ZNAM','soundDrop'),
        MelModel('shellCasingModel',2),
        MelModel('scopeModel',3),
        MelFid('EFSD','scopeEffect'),
        MelModel('worldModel',4),
        MelString('NNAM','embeddedWeaponNode'),
        MelFid('INAM','impactDataset'),
        MelFid('WNAM','firstPersonModel'),
        MelFid('SNAM','soundGunShot3D'),
        MelFid('XNAM','soundGunShot2D'),
        MelFid('NAM7','soundGunShot3DLooping'),
        MelFid('TNAM','soundMeleeSwingGunNoAmmo'),
        MelFid('NAM6','soundBlock'),
        MelFid('UNAM','idle'),
        MelFid('NAM9','equip'),
        MelFid('NAM8','unequip'),
        MelStruct('DATA','2IfHB','value','health','weight','damage','clipsize'),
        MelWeapDnam('DNAM','Iff4B5fI4BffII11fIIffIfff',
                    'animationType','animationMultiplier','reach',(_dflags1,'dnamFlags1',0L),
                    'gripAnimation','ammoUse','reloadAnimation','minSpread','spread',
                    'unknown','sightFov','unknown2',(FID,'projectile',0L),
                    'baseVatsToHitChance','attackAnimation','projectileCount','embeddedWeaponActorValue','minRange','maxRange',
                    'onHit',(_dflags2,'dnamFlags2',0L),'animationAttackMultiplier','fireRate','overrideActionPoint',
                    'rumbleLeftMotorStrength','rumbleRightMotorStrength','rumbleDuration','overrideDamageToWeaponMult',
                    'attackShotsPerSec','reloadTime','jamTime','aimArc','skill','rumblePattern','rambleWavelangth','limbDmgMult',
                    ('resistType',0xFFFFFFFF),'sightUsage','semiAutomaticFireDelayMin','semiAutomaticFireDelayMax'),
        MelStruct('CRDT','IfHI','criticalDamage','criticalMultiplier',(_cflags,'criticalFlags',0L),(FID,'criticalEffect',0L)),
        MelBase('VNAM','soundLevel'),
        )
    __slots__ = MelRecord.__slots__ + melSet.getSlotsUsed()

# Id Functions ----------------------------------------------------------------

ob = getIdFunc('fallout3.esm')


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

    # extended by FOSE
    (1024, 'GetFOSEVersion', 0, 0, 0, 0),
    (1025, 'GetFOSERevision', 0, 0, 0, 0),
    (1213, 'GetFOSEBeta', 0, 0, 0, 0),
    (1082, 'IsKeyPressed', 1, 0, 0, 0),
    (1166, 'IsControlPressed', 1, 0, 0, 0),
    (1028, 'GetWeight', 2, 0, 0, 0),
    (1165, 'GetWeaponHasScope', 0, 0, 0, 0),
    )

#--Plugin format stuff
class esp:
    #--Valid ESM/ESP header versions
    validHeaderVersions = (0.85)