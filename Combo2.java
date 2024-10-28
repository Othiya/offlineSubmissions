public class Combo2 implements Combo {
    CustomCombo combo;

    Combo2() {
        combo = new CustomCombo("Combo2 (Shawarma + Drink)");
        combo.addFood(new Shawarma());
        combo.addFood(new Drink());

    }

    @Override
    public double calculatePrice() {
        return combo.calculatePrice();
    }

    @Override
    public String getName() {
        return combo.getName();
    }

}
