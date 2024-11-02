public class Combo2 implements Combo {
    CompositeCombo combo;

    Combo2() {
        combo = new CompositeCombo("Combo2 (Shawarma + Drink)");
        combo.addFood(new Shawarma());
        combo.addFood(new Drink());

    }

    @Override
    public double calculatePrice() {
        return 215;
    }

    @Override
    public String getName() {
        return combo.getName();
    }

}
