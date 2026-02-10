package heroes;

import java.util.HashMap;
import java.util.Random;

import items.*;
import combatants.*;


public class Hero {
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

