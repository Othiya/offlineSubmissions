public class Combo1 implements Food {
    CompositeCombo combo;

    Combo1() {
        combo = new CompositeCombo("Combo1 (Burger + Fries + Drink)");
        combo.addFood(new Burger());
        combo.addFood(new Fries());
        combo.addFood(new Drink());

    }

    @Override
    public double calculatePrice() {
        return 400;
    }

    @Override
    public String getName() {
        return combo.getName();
    }

}
