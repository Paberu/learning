package tests;

import combatants.Unit;
import combatants.UnitFeature;
import combatants.UnitType;
import heroes.Barbarian;
import heroes.Hero;
import items.Artifact;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashMap;

class UnitTest {

    private UnitFeature[] wolfRaiderFeatures;
    private Unit wolfRaider;
    private Unit mage;
    private Unit[] barbarianArmy;
    private Hero hero;

    @BeforeEach
    void setUp() {
        wolfRaiderFeatures = new UnitFeature[]{UnitFeature.ALWAYS_RESPONDING};
        wolfRaider = new Unit("Wolf Raider", 5, 2, 4, 15, UnitType.MELEE, wolfRaiderFeatures, 10, 5);
        mage = new Unit("Mage", 4, 4, 5, 10, UnitType.RANGED, new UnitFeature[0], 7, 2);
        barbarianArmy = new Unit[]{wolfRaider, mage};
        hero = new Barbarian("Tarnum", 4, 0, 1, 0, 1000, new Artifact[]{}, barbarianArmy);
    }

    @AfterEach
    void tearDown() {
        wolfRaiderFeatures = null;
        wolfRaider = null;
        mage = null;
        barbarianArmy = null;
        hero = null;
    }

    @Test
    void getName() {
        assertEquals("Wolf Raider", wolfRaider.getName());
    }

    @Test
    void getUnitParameters() {
        HashMap<String, Integer> parameters = wolfRaider.getUnitParameters();
        assertEquals(5, parameters.get("attack"));
        assertEquals(2, parameters.get("defence"));
    }

    @Test
    void getRealUnitParameters() {
        HashMap<String, Integer> heroParameters = hero.getRealHeroParameters();
        HashMap<String, Integer> unitParameters = wolfRaider.getUnitParameters();
        HashMap<String, Integer> realUnitParameters = wolfRaider.getRealUnitParameters(heroParameters);
        assertEquals(realUnitParameters.get("attack"), heroParameters.get("attack") + unitParameters.get("attack"));
    }

    @Test
    void getType() {
        assertEquals(UnitType.MELEE, wolfRaider.getType());
    }

    @Test
    void getUnitFeatures() {
        assertEquals(UnitFeature.ALWAYS_RESPONDING, wolfRaider.getUnitFeatures()[0]);
    }


}