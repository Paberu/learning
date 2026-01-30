/* Решил позволить себе взять за основу не Dwarf Fortress,
а более привычных в обращении Heroes of Might and Magic 3.

Тем более, что личная заинтересованность даст больший выхлоп.
*/
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

class Hero {
	String name;
	HashMap<String, Integer> parameters;
	Artifact[] artifacts;
	Unit[] units;
	
	public Hero(String name, int attack, int defence, int power, int knowledge, int movement, Artifact artifact, Unit[] units) {
		
		this.name = name;
		this.parameters = new HashMap<>();
		this.parameters.put("attack", attack);
		this.parameters.put("defence", defence);
		this.parameters.put("power", power);
		this.parameters.put("knowledge", knowledge);
		this.parameters.put("movement", movement);
		this.artifacts = new Artifact[1];
		if (artifact != null) {
			this.artifacts[0] = artifact;
		}
		
		this.units = units;
	}	
	
	public HashMap<String, Integer> getArtifactsBonuses() {
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
		
		HashMap<String, Integer> axeParameters = new HashMap<>();
		axeParameters.put("attack", 3);
		Artifact battleAxe = new Artifact("BarbarianAxe", axeParameters);
		
		Unit[] barbarianArmy = new Unit[]{wolfRaider};
		
		Hero barbarian = new Hero("Tarnum", 4, 0, 1, 0, 1000, battleAxe, barbarianArmy);
		System.out.println(barbarian.name + " has " + barbarian.artifacts[0].name);
		System.out.println("Axe is good:" + barbarian.artifacts[0].parameters);
		// допустим, мы решили сделать другой топор, не варварской работы
		// он повышает интеллект и знания достойного рыцаря
		// свойства топора будем делать используя предыдущие наработки и просто накинем свойств в переменную axeParameters
		axeParameters.put("knowledge", 2);
		// но случилось непредвиденное: мы ещё не начали делать топор для рыцаря, а свойства варварского топора уже изменились
		// почему? потому что параметры топора переданы в конструктор варвара не по значению, а по ссылке
		// а значит нечаянное изменение свойств артефакта далее по коду скажется и на свойствах варвара, определённого где-то
		// вначале.
		System.out.println("Barbarian axe've changed: " + barbarian.artifacts[0].parameters);
		System.out.println("Barbarian parameters :" + barbarian.getHeroParameters());
		System.out.println("Barbarian real parameters :" + barbarian.getRealHeroParameters());
		System.out.println("Wolf Raiders parameters: " + wolfRaider.getUnitParameters());
		System.out.println("Wolf Raiders real parameters: " + wolfRaider.getRealUnitParameters(barbarian.getRealHeroParameters()));
	}
}

class Artifact {
	String name;
	HashMap<String, Integer> parameters;
	
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
	String name;
	HashMap<String, Integer> parameters;
	UnitType type;
	UnitFeature[] unitFeatures;
	
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
	
	public HashMap<String, Integer> getUnitParameters() {
		return this.parameters;
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

