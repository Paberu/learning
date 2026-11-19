package PowerSet;

import org.junit.jupiter.api.BeforeEach;

public class PowerSet_3 {

    PowerSet set1;
    PowerSet set2;
    PowerSet set3;
    PowerSet set4;

    @BeforeEach
    void setUp() {
        set1 = new PowerSet();
        set2 = new PowerSet();
        set3 = new PowerSet();
        set4 = new PowerSet();

        set2.put("One and only");

        for (int i = 0; i < 10; i++) {
            set3.put("Little" + i);
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                set3.put("Big" + i + j);
            }
        }
    }


}
