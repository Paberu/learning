package items;

import java.util.HashMap;
import java.util.Random;


public class Artifact {
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
