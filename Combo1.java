public class Combo1 implements Combo {
    CustomCombo combo;

    Combo1() {
        combo = new CustomCombo("Combo1 (Burger + Fries + Drink)");
        combo.addFood(new Burger());
        combo.addFood(new Fries());
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
