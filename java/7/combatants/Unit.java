package combatants;

import java.util.HashMap;


public class Unit {
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

