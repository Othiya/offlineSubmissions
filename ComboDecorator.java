public abstract class ComboDecorator implements Combo {
    Combo combo;

    ComboDecorator(Combo c) {
        combo = c;
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
