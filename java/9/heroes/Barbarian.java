package heroes;

import java.util.HashMap;
import java.util.Random;

import items.*;
import combatants.*;


public class Barbarian extends Hero {
	
	public Barbarian(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		super(name, attack, defence, power, knowledge, movement, artifacts, units);
	}
	
	public String increaseParameter() {
		Random random = new Random();
		String[] parameters = {"attack", "defence", "attack", "attack"};
		int i = random.nextInt(4);
		assert parameters[i] == "attack" || parameters[i] == "defence": "Ошибка при повышении параметра (варвары не могут получать магические бонусы)!";
		return parameters[i];
	}
}