- [ ] Feature: Create a CharacterTest checking if there’s a class
		-test if there’s a class
        - Test checking if the class has a name attribute
        - Test checking if the class name attribute is different then other class name attribute
As a character I want to have a name so that I can be distinguished from other characters
       can get and set Name

	   player1 = character(josh)
       class Character:
            name = name
	



- [ ] Feature: Alignment
		-const of possible alignment attribute
  		-test checking if there’s an attribute for alignment
  		-test checking if alignment equals good, evil, or neutral
As a character I want to have an alignment so that I have something to guide my actions
* can get and set alignment
* alignments are Good, Evil, and Neutral
	


- [ ] Feature: Armor Class & Hit Points
		-test checking if class has an armor attribute
		-test checking if class has a hit points attribute
		-test checking if armor class defaults to 10
		-test checking if hit points defaults to 5
As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies
* has an Armor Class that defaults to 10
* has 5 Hit Points by default





- [ ] Feature: Character Can Attack
		-test checking if class has an attack attribute
		-test checking if class can beat opponents armor class and deal damage
		-test checking if roll of 20 always hits
As a combatant I want to be able to attack other combatants so that I can survive to fight another day
* roll a 20 sided die (don't code the die)
* roll must meet or beat opponents armor class to hit
* a natural roll of 20 always hits



- [ ] Feature: Character Can Be Damaged
		-test checking if class has a damaged attribute
		-test checking if attack is successful health takes 1 point damage
		-test checking if opponent rolls 20 does opponent take 
		-test checking if character is dead if it has less than 0 health
As an attacker I want to be able to damage my enemies so that they will die and I will live
* If attack is successful, other character takes 1 point of damage when hit
* If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
* when hit points are 0 or fewer, the character is dead




- [ ] Feature: Character Has Abilities Scores
As a character I want to have several abilities so that I am not identical to other characters except in name
* Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
* Abilities range from 1 to 20 and default to 10
* Abilities have modifiers according to the following table
- [ ] Feature: Character Ability Modifiers Modify Attributes
As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice
* add Strength modifier to:
    * attack roll and damage dealt
    * double Strength modifier on critical hits
    * minimum damage is always 1 (even on a critical hit)
* add Dexterity modifier to armor class
* add Constitution modifier to hit points (always at least 1 hit point)

- [ ] Feature: A Character can gain experience when attacking
As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern
* When a successful attack occurs, the character gains 10 experience points

- [ ] Feature: A Character Can Level
As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes
* Level defaults to 1
* After 1000 experience points, the character gains a level
    * 0 xp -> 1st Level
    * 1000 xp -> 2nd Level
    * 2000 xp -> 3rd Level
    * etc.
* For each level:
    * hit points increase by 5 plus Con modifier
    * 1 is added to attack roll for every even level achieved