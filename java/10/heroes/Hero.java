package heroes;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.logging.Level;

import items.*;
import combatants.*;
import utils.GameLogger;


public class Hero {
	public static final String ATTACK = "attack";
	public static final String DEFENCE = "defence";
	public static final String POWER = "power";
	public static final String KNOWLEDGE = "knowledge";
	public static final String MOVEMENT = "movement";

	protected static Random random = new Random();
	private String name;
	private HashMap<String, Integer> parameters;
	private Artifact[] artifacts;
	private Unit[] units;

	public Hero(String name, int attack, int defence, int power, int knowledge, int movement, Artifact[] artifacts, Unit[] units) {
		
		this.name = name;
		this.parameters = new HashMap<>();
		this.parameters.put(ATTACK, attack);
		this.parameters.put(DEFENCE, defence);
		this.parameters.put(POWER, power);
		this.parameters.put(KNOWLEDGE, knowledge);
		this.parameters.put(MOVEMENT, movement);
		this.artifacts = artifacts;
		this.units = units;

		GameLogger.logCreation(this.getClass().getName(), this.name);
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
		String[] parametersForRandom = {ATTACK, DEFENCE, POWER, KNOWLEDGE};
		int i = random.nextInt(4);
		return parametersForRandom[i];
	}
	
	private HashMap<String, Integer> getArtifactsBonuses() {
		HashMap<String, Integer> bonuses = new HashMap<>();
		for (int i = 0; i < this.artifacts.length; i++){
			Artifact artifact = this.artifacts[i];
			String[] artifactParameters = artifact.getParameters();
			for (int k = 0; k < artifactParameters.length; k++) {
				String artifactParameter = artifactParameters[k];
				int bonus = artifact.getParameterValue(artifactParameter);
				if (!bonuses.containsKey(artifactParameter)) {
					bonuses.put(artifactParameter, bonus);
				} else {
					bonuses.put(artifactParameter, bonus + bonuses.get(artifactParameter));
				}
			}
		}
		return bonuses;
	}
	
	public Map<String, Integer> getHeroParameters() {
		return this.parameters;
	}
	
	public Map<String, Integer> getRealHeroParameters() {
		HashMap<String, Integer> realParameters = new HashMap<>();
		HashMap<String, Integer> heroParameters = (HashMap) this.getHeroParameters();
		HashMap<String, Integer> bonuses = this.getArtifactsBonuses();
		for (Map.Entry<String, Integer> entry : heroParameters.entrySet()) {
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
	
	public static Hero generateHero() {
		Unit peasant = new Unit("Peasant", 1, 1, 1, 1, UnitType.MELEE, new UnitFeature[0], 3, 1);
		int number = Hero.random.nextInt(100);
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

