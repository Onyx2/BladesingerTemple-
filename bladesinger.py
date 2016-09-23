from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

###################################################

def GetConditionName():
        return "Bladesinger"

def GetSpellCasterConditionName():
        return "Bladesinger Spellcasting"
    
print "Registering " + GetConditionName()

classEnum = stat_level_bladesinger
classSpecModule = __import__('class033_bladesinger')
###################################################

#### standard callbacks - BAB and Save values
def OnGetToHitBonusBase(attachee, args, evt_obj):
        classLvl = attachee.stat_level_get(classEnum)
        babvalue = game.get_bab_for_class(classEnum, classLvl)
        evt_obj.bonus_list.add(babvalue, 0, 137)
        return 0

def OnGetSaveThrowFort(attachee, args, evt_obj):
        value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Fortitude)
        evt_obj.bonus_list.add(value, 0, 137)
        return 0

def OnGetSaveThrowReflex(attachee, args, evt_obj):
        value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Reflex)
        evt_obj.bonus_list.add(value, 0, 137)
        return 0

def OnGetSaveThrowWill(attachee, args, evt_obj):
        value = char_class_utils.SavingThrowLevel(classEnum, attachee, D20_Save_Will)
        evt_obj.bonus_list.add(value, 0, 137)
        return 0

def IsLightlyArmored( obj ):
        armor = obj.item_worn_at(5)
        if armor != OBJ_HANDLE_NULL:
                armorFlags = armor.obj_get_int(obj_f_armor_flags)
                if armorFlags != ARMOR_TYPE_NONE or ARMOR_TYPE_LIGHT:
                        return 0
        shield = obj.item_worn_at(11)
        if shield != OBJ_HANDLE_NULL:
                return 0
        return 1

def IsRangedWeapon( weap ):
        weapFlags = weap.obj_get_int(obj_f_weapon_flags)
        if (weapFlags & OWF_RANGED_WEAPON) == 0:
                return 0
        return 1

def IsRapierorLongsword( obj, weap):
    weaponType = weap.obj_get_int(obj_f_weapon_type)
    if weaponType != wt_rapier or wt_longsword:
        return 0

def IsUsingBladeSongWeapon( obj ):
        weap = obj.item_worn_at(3)
        offhand = obj.item_worn_at(4)
        if weap == OBJ_HANDLE_NULL and offhand == OBJ_HANDLE_NULL:
                return 0
        if weap == OBJ_HANDLE_NULL:
                weap = offhand
                offhand = OBJ_HANDLE_NULL
        if IsRapierorLongsword(obj, weap):
                return 1
        if offhand != OBJ_HANDLE_NULL:
                if IsRapierorLongsword(obj, offhand):
                        return 1
        return 0
    
def BladesongAcBonus(attachee, args, evt_obj):
        if not IsLightlyArmored(attachee):
                return 0
        if not IsUsingBladeSongWeapon(obj):
                return 0
        if offhand != OBJ_HANDLE_NULL:
                return 0
        weap = attachee.item_worn_at(3)
        if weap == OBJ_HANDLE_NULL or IsRangedWeapon(weap):
                weap = attachee.item_worn_at(4)
        if weap == OBJ_HANDLE_NULL or IsRangedWeapon(weap):
                return 0
        bladesingerLvl = attachee.stat_level_get(classEnum)
        intScore = attachee.stat_level_get(stat_intelligence)
        intBonus = (intScore - 10)/2
        if intBonus <= 0:
                return
        if bladesingerLvl < intBonus:
                intBonus = bladesingerLvl
        evt_obj.bonus_list.modify(intBonus , 3, 104)
        return 0

classSpecObj = PythonModifier(GetConditionName(), 0)
classSpecObj.AddHook(ET_OnToHitBonusBase, EK_NONE, OnGetToHitBonusBase, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_FORTITUDE, OnGetSaveThrowFort, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_REFLEX, OnGetSaveThrowReflex, ())
classSpecObj.AddHook(ET_OnSaveThrowLevel, EK_SAVE_WILL, OnGetSaveThrowWill, ())
classSpecObj.AddHook(ET_OnGetAC, EK_NONE, BladesongAcBonus, ())

##### Spell casting

def OnAddSpellCasting(attachee, args, evt_obj):
        if (args.get_arg(0) == 0):
                args.set_arg(0, char_class_utils.GetHighestArcaneClass(attachee))
        return 0

def OnGetBaseCasterLevel(attachee, args, evt_obj):
        class_extended_1 = args.get_arg(0)
        class_code = evt_obj.arg0
        if (class_code != class_extended_1):
                if (evt_obj.arg1 == 0):
                        return 0
        classLvl = attachee.stat_level_get(classEnum)
        evt_obj.bonus_list.add(classLvl, 0, 137)
        return 0

def OnSpellListExtensionGet(attachee, args, evt_obj):
        class_extended_1 = args.get_arg(0)
        class_code = evt_obj.arg0
        if (class_code != class_extended_1):
                if (evt_obj.arg1 == 0):
                        return 0
        classLvl = attachee.stat_level_get(classEnum)
        evt_obj.bonus_list.add(classLvl, 0, 137)
        return 0

def OnInitLevelupSpellSelection(attachee, args, evt_obj):
        if (evt_obj.arg0 != classEnum):
                return 0
        classLvl = attachee.stat_level_get(classEnum)
        if (classLvl == 0):
                return 0
        class_extended_1 = args.get_arg(0)
        classSpecModule.InitSpellSelection(attachee, class_extended_1)
        return 0

def OnLevelupSpellsCheckComplete(attachee, args, evt_obj):
        if (evt_obj.arg0 != classEnum):
                return 0
        class_extended_1 = args.get_arg(0)
        if (not classSpecModule.LevelupCheckSpells(attachee, class_extended_1) ):
                evt_obj.bonus_list.add(-1, 0, 137)
        return 1
        
def OnLevelupSpellsFinalize(attachee, args, evt_obj):
        if (evt_obj.arg0 != classEnum):
                return 0
        classLvl = attachee.stat_level_get(classEnum)
        if (classLvl == 0):
                return 0
        class_extended_1 = args.get_arg(0)
        classSpecModule.LevelupSpellsFinalize(attachee, class_extended_1)
        return

spellCasterSpecObj = PythonModifier(GetSpellCasterConditionName(), 8)
spellCasterSpecObj.AddHook(ET_OnConditionAdd, EK_NONE, OnAddSpellCasting, ())
spellCasterSpecObj.AddHook(ET_OnGetBaseCasterLevel, EK_NONE, OnGetBaseCasterLevel, ())
spellCasterSpecObj.AddHook(ET_OnSpellListExtensionGet, EK_NONE, OnSpellListExtensionGet, ())
spellCasterSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Activate, OnInitLevelupSpellSelection, ())
spellCasterSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Check_Complete, OnLevelupSpellsCheckComplete, ())
spellCasterSpecObj.AddHook(ET_OnLevelupSystemEvent, EK_LVL_Spells_Finalize, OnLevelupSpellsFinalize, ())
