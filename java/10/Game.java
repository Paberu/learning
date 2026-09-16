import java.util.HashMap;
import java.util.Scanner;

import items.*;
import heroes.*;
import combatants.*;
import utils.GameLogger;

public class Game {
	
	public static void main() {

		Scanner scanner = new Scanner(System.in);
		
		UnitFeature[] wolfRaiderFeatures = new UnitFeature[]{UnitFeature.ALWAYS_RESPONDING};
		Unit wolfRaider = new Unit("Wolf Raider", 5, 2, 4, 15, UnitType.MELEE, wolfRaiderFeatures, 10, 5);
		
		Unit mage = new Unit("Mage", 4, 4, 5, 10, UnitType.RANGED, new UnitFeature[0], 7, 2);
		
		HashMap<String, Integer> axeParameters = new HashMap<>();
		axeParameters.put(Hero.ATTACK, 3);
		Artifact battleAxe = new Artifact("BarbarianAxe", axeParameters);
		
		HashMap<String, Integer> supplyMap = new HashMap<>();
		supplyMap.put("wood", 2);
		Supply foreverWood = new Supply("Forever Wood", supplyMap);
		supplyMap = new HashMap<>();
		supplyMap.put("ore", 2);
		Supply foreverOre = new Supply("Forever Ore", supplyMap);
		supplyMap = new HashMap<>();
		supplyMap.put("mercury", 1);
		Supply foreverMercury = new Supply("Mercury Drop", supplyMap);
		
		Unit[] barbarianArmy = new Unit[]{wolfRaider};
		
		System.out.print("Введи твоё имя: ");
		String name = scanner.nextLine().trim();
		System.out.print("Привет, " + name + ". За кого играешь: за варвара или за мага? ");
		String heroClass = scanner.nextLine().trim();
		System.out.println(heroClass);
		
		Hero hero = null;
		if ("варвар".equalsIgnoreCase(heroClass) || "barbarian".equalsIgnoreCase(heroClass)) {
			hero = new Barbarian("Tarnum", 4, 0, 1, 0, 1000, new Artifact[]{battleAxe}, barbarianArmy);
			System.out.println("Твоего варвара зовут Тарнум");
		} else {
			hero = new Wizard("Merlin", 0, 0, 2, 3, 800, new Artifact[]{foreverWood, foreverOre, foreverMercury}, new Unit[]{mage});
			System.out.println("Поиграешь за Мерлина");
		}

		//Тестируем assert'ы
		for(int i = 0; i < 10; i++) {
			hero.increaseParameter();
		}

		// GameLogger.logCreation(hero, Hero);
		System.out.println(hero.getRealHeroParameters());
	}
}