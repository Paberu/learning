import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

import Artifact.*;
import Unit.*;
import Hero.*;

class Game {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		UnitFeature[] wolfRaiderFeatures = new UnitFeature[]{UnitFeature.ALWAYS_RESPONDING};
		Unit wolfRaider = new Unit("Wolf Raider", 5, 2, 4, 15, UnitType.MELEE, wolfRaiderFeatures, 10, 5);
		
		Unit mage = new Unit("Mage", 4, 4, 5, 10, UnitType.RANGED, new UnitFeature[0], 7, 2);
		
		HashMap<String, Integer> axeParameters = new HashMap<>();
		axeParameters.put("attack", 3);
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
		
		// Barbarian barbarian = new Barbarian("Tarnum", 4, 0, 1, 0, 1000, new Artifact[]{battleAxe}, barbarianArmy);
		// Wizard wizard = new Wizard("Merlin", 0, 0, 2, 3, 800, new Artifact[]{foreverWood, foreverOre, foreverMercury}, new Unit[]{mage});
		
		//Прекрасная иллюстрация переопределения функций или, выражаясь языком курса, полиморфизма подтипов.
		/*
		Hero[] tenHeroes = generateNHeroes(500);
		for (int i = 0; i < 500; i++) {
			Hero tmp_hero = tenHeroes[i];
			System.out.println(tmp_hero.increaseParameter());
		}
		*/
		//Каждый новый запуск программы вывод получается новым, но прослеживается интересная зависимость: частота выпадения
		//knowledge и power почти одинакова, defence выпадает в 2 раза реже, а attack - в 2 раза чаще. Что полностью соответствует 
		//версиям функции у наследников класса Hero.
		
		System.out.println(hero.getRealHeroParameters());
	}
}