package heroes;

import items.*;
import combatants.*;


public class Barbarian extends Hero {
	
	public Barbarian(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		super(name, attack, defence, power, knowledge, movement, artifacts, units);
	}
	
	public String increaseParameter() {
		String[] parameters = {ATTACK, DEFENCE, ATTACK, ATTACK};
		int i = random.nextInt(4);
		assert parameters[i].equals(ATTACK) || parameters[i].equals(DEFENCE): "Ошибка при повышении параметра (варвары не могут получать магические бонусы)!";
		return parameters[i];
	}
}