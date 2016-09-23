from toee import *
import char_class_utils
import char_editor
###################################################

def GetConditionName(): # used by API
        return "Bladesinger"

def GetSpellCasterConditionName():
        return "Bladesinger Spellcasting"
        
classEnum = stat_level_bladesinger

###################################################


class_feats = {

1: (feat_armor_proficiency_light)
}


class_skills = (skill_balance, skill_concentration, skill_jump, skill_knowledge_arcana, skill_perform, skill_spellcraft, skill_tumble)

def IsEnabled():
        return 1

def GetHitDieType():
        return 8
        
def GetSkillPtsPerLevel():
        return 2
        
def GetBabProgression():
        return base_attack_bonus_type_martial
        
def IsFortSaveFavored():
        return 0
        
def IsRefSaveFavored():
        return 1
        
def IsWillSaveFavored():
        return 1

def GetSpellListType():
        return spell_list_type_arcane

def IsClassSkill(skillEnum):
        return char_class_utils.IsClassSkill(class_skills, skillEnum)

def IsClassFeat(featEnum):
        return char_class_utils.IsClassFeat(class_feats, featEnum)

def GetClassFeats():
        return class_feats

def IsAlignmentCompatible( alignment):
        return 1
        
def ObjMeetsPrereqs( obj ):
        objRace = obj.stat_level_get(stat_race)
        if (not( objRace == race_elf or objRace == race_halfelf)):
                return 0
        if (obj.get_base_attack_bonus() < 5):
                return 0
        if obj.skill_ranks_get(skill_concentration) < 2:
                return 0
        if obj.skill_ranks_get(skill_perform) < 2:
                return 0
        if obj.skill_ranks_get(skill_tumble) < 2:
                return 0
        if (not (obj.has_feat(feat_combat_casting))):
                return 0
        if (not (obj.has_feat(feat_combat_expertise))):
                return 0
        if (not (obj.has_feat (feat_dodge))):
                return 0
        if (not (obj.has_feat(feat_weapon_focus_longsword) or obj.has_feat(feat_weapon_focus_rapier)) ):
                return 0
        if (obj.arcane_spell_level_can_cast() < 1):
                return 0
        return 1

#Spellcasting on Level Up

def IsSelectingSpellsOnLevelup( obj , class_extended_1 = 0):
	if (class_extended_1 == 0):
		class_extended_1 = char_class_utils.GetHighestArcaneClass(obj)
	if (char_editor.is_selecting_spells(obj, class_extended_1)):
		return 1
	return 0

def LevelupCheckSpells( obj , class_extended_1 = 0):
        if (class_extended_1 == 0):
                class_extended_1 = char_class_utils.GetHighestArcaneClass(obj)
        if (not char_editor.spells_check_complete(obj, class_extended_1)):
                return 0
        return 1
        
def InitSpellSelection( obj , class_extended_1 = 0):
	if (class_extended_1 == 0):
		class_extended_1 = char_class_utils.GetHighestArcaneClass(obj)
	char_editor.init_spell_selection(obj, class_extended_1)
	return 0

def LevelupSpellsFinalize( obj , class_extended_1 = 0):
        if (class_extended_1 == 0):
                class_extended_1 = char_class_utils.GetHighestArcaneClass(obj)
        char_editor.spells_finalize(obj, class_extended_1)
        return 0
