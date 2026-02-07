import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.Random;
import java.util.Scanner;

class Hero {
	private String name;
	private HashMap<String, Integer> parameters;
	private Artifact[] artifacts;
	private Unit[] units;
	
	public Hero(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		
		this.name = name;
		this.parameters = new HashMap<>();
		this.parameters.put("attack", attack);
		this.parameters.put("defence", defence);
		this.parameters.put("power", power);
		this.parameters.put("knowledge", knowledge);
		this.parameters.put("movement", movement);
		this.artifacts = artifacts;
		this.units = units;
	}	
	
	public String getName() {
		return this.name;
	}
	
	public Unit[] getUnits(){
		return this.units;
	}
	
	public Artifact[] getArtifacts(){
		return this.artifacts;
	}
	
	public String increaseParameter() {
		Random random = new Random();
		String[] parameters = {"attack", "defence", "power", "knowledge"};
		int i = random.nextInt(4);
		return parameters[i];
	}
	
	private HashMap<String, Integer> getArtifactsBonuses() {
		HashMap<String, Integer> bonuses = new HashMap<>();
		for (int i = 0; i < this.artifacts.length; i++){
			Artifact artifact = this.artifacts[i];
			String[] parameters = artifact.getParameters();
			for (int k = 0; k < parameters.length; k++) {
				String parameter = parameters[k];
				int bonus = artifact.getParameterValue(parameter);
				if (!bonuses.containsKey(parameter)) {
					bonuses.put(parameter, bonus);
				} else {
					bonuses.put(parameter, bonus + bonuses.get(parameter));
				}
			}
		}
		return bonuses;
	}
	
	public HashMap<String, Integer> getHeroParameters() {
		return this.parameters;
	}
	
	public HashMap<String, Integer> getRealHeroParameters() {
		HashMap<String, Integer> realParameters = new HashMap<>();
		HashMap<String, Integer> parameters = this.getHeroParameters();
		HashMap<String, Integer> bonuses = this.getArtifactsBonuses();
		for (Map.Entry<String, Integer> entry : parameters.entrySet()) {
			String key = entry.getKey();
			int value = entry.getValue();
			
			if (bonuses.containsKey(key)) {
				realParameters.put(key, bonuses.get(key) + value);
			} else {
				realParameters.put(key, value);
			}
		}
		return realParameters;		
	}
	
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
	
	public static Hero generateHero() {
		Random random = new Random();
		Unit peasant = new Unit("Peasant", 1, 1, 1, 1, UnitType.MELEE, new UnitFeature[0], 3, 1);
		int number = random.nextInt(100);
		if (number % 2 == 0) {
			return new Wizard("Wizard" + number, 0, 0, 2, 3, 800, new Artifact[0], new Unit[]{new Unit(peasant)});
		}
		return new Barbarian("Barbarian" + number, 4, 1, 0, 0, 1000,  new Artifact[0], new Unit[]{new Unit(peasant)});
	}
	
	public static Hero[] generateNHeroes(int n) {
		Hero[] heroes = new Hero[n];
		for (int i = 0; i < n; i++) {
			heroes[i] = generateHero();
		}
		return heroes;
	}
}

class Barbarian extends Hero {
	
	public Barbarian(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		super(name, attack, defence, power, knowledge, movement, artifacts, units);
	}
	
	public String increaseParameter() {
		Random random = new Random();
		String[] parameters = {"attack", "defence", "attack", "attack"};
		int i = random.nextInt(4);
		return parameters[i];
	}
}

class Wizard extends Hero {
	
	public Wizard(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		super(name, attack, defence, power, knowledge, movement, artifacts, units);
	}
	
	public String increaseParameter() {
		Random random = new Random();
		String[] parameters = {"knowledge", "power", "knowledge", "knowledge"};
		int i = random.nextInt(4);
		return parameters[i];
	}
}