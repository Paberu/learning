import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.Random;

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
		
		Barbarian barbarian = new Barbarian("Tarnum", 4, 0, 1, 0, 1000, new Artifact[]{battleAxe}, barbarianArmy);
		Wizard wizard = new Wizard("Merlin", 0, 0, 2, 3, 800, new Artifact[]{foreverWood, foreverOre, foreverMercury}, new Unit[]{mage});
		
		//Прекрасная иллюстрация переопределения функций или, выражаясь языком курса, полиморфизма подтипов.
		Hero[] tenHeroes = generateNHeroes(500);
		for (int i = 0; i < 500; i++) {
			Hero tmp_hero = tenHeroes[i];
			System.out.println(tmp_hero.increaseParameter());
		}
		//Каждый новый запуск программы вывод получается новым, но прослеживается интересная зависимость: частота выпадения
		//knowledge и power почти одинакова, defence выпадает в 2 раза реже, а attack - в 2 раза чаще. Что полностью соответствует 
		//версиям функции у наследников класса Hero.
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

class Artifact {
	private String name;
	private HashMap<String, Integer> parameters;
	
	public Artifact(String name, HashMap<String, Integer> parameters) {
		this.name = name;
		this.parameters = parameters;
	}
	
	//для получения результирующего значения параметра героя надо получить соответствующие значения всех прибавок от всех артефактов,
	//после чего сложить полученные бонусы с исходными значениями
	public int getParameterValue(String parameter) {
		if (!this.parameters.containsKey(parameter)) {
			return 0;
		}
		return this.parameters.get(parameter);
	}
	
	//возможно, потребуется применить другой подход: получить результирующий бонус от всех артефактов, и уже потом учесть все бонусы разом
	public String[] getParameters() {
		Set keys = this.parameters.keySet();
		String[] parameters = new String[keys.size()];
		int i = 0;
		for (Object key : keys) {
			parameters[i] = (String)key;
			i++;
		}
		return parameters;
	}
	
	public String getName() {
		return this.name;
	}
}

class MainHand extends Artifact {
	public MainHand(String name, HashMap<String, Integer> parameters){
		super(name, parameters);
	}
}

class SupportHand extends Artifact {
	public SupportHand(String name, HashMap<String, Integer> parameters){
		super(name, parameters);
	}
}

class Supply extends Artifact {
	public Supply(String name, HashMap<String, Integer> parameters){
		super(name, parameters);
	}
}

public enum UnitType {
	MELEE,
	RANGED,
	FLYING,
	TELEPORTING
}

public enum UnitFeature {
	NOT_RESPONDED_TO,
	ALWAYS_RESPONDING,
	DOUBLE_SHOT,
	BLOW_UP_AT_DEATH	
}

class Unit {
	private String name;
	private HashMap<String, Integer> parameters;
	private UnitType type;
	private UnitFeature[] unitFeatures;
	
	//Здесь представлен ad hoc полиморфизм: можно вызвать конструктор с кучей параметров, который создаст юнита по заданным параметрам,
	//а можно передать в качестве параметра уже имеющийся объекта класса Unit или его потомков и получить точную копию имеющегося объекта.
	public Unit(String name, int attack, int defence, int damage, int health, UnitType type, UnitFeature[] unitFeatures, int speed, int count) {
		this.name = name;
		this.parameters = new HashMap<>();
		this.parameters.put("attack", attack);
		this.parameters.put("defence", defence);
		this.parameters.put("damage", damage);
		this.parameters.put("health", health);
		this.parameters.put("currentHealth", health);
		this.parameters.put("speed", speed);
		this.parameters.put("count", count);
		this.type = type;
		this.unitFeatures = unitFeatures;
	}
	
	public Unit(Unit unit) {
		this.name = unit.getName();
		this.parameters = unit.getUnitParameters();
		this.type = unit.getType();
		this.unitFeatures = unit.getUnitFeatures();
	}
		
	public String getName() {
		return this.name;
	}
	
	public HashMap<String, Integer> getUnitParameters() {
		return this.parameters;
	}
	
	public UnitType getType(){
		return this.type;
	}
	
	public UnitFeature[] getUnitFeatures(){
		return this.unitFeatures;
	}
	
	public HashMap<String, Integer> getRealUnitParameters(HashMap<String, Integer> heroParameters) {
		HashMap<String, Integer> realParameters = new HashMap<>();
		HashMap<String, Integer> parameters = this.getUnitParameters();
		for (Map.Entry<String, Integer> entry : parameters.entrySet()) {
			String unitParameterKey = entry.getKey();
			int unitParameterValue = entry.getValue();
			
			if (heroParameters.containsKey(unitParameterKey)) {
				realParameters.put(unitParameterKey, unitParameterValue + heroParameters.get(unitParameterKey));
			} else {
				realParameters.put(unitParameterKey, unitParameterValue);
			}
		}
		return realParameters;		
	}
}

