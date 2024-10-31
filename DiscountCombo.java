public class DiscountCombo extends ComboDecorator {
    double discount;

    DiscountCombo(Combo c, double d) {
        super(c);
        discount = d;
    }

    public void setDiscount(double discount) {
        this.discount = discount;
    }

    @Override
    public double calculatePrice() {
        double original_price = combo.calculatePrice();
        System.out.println(original_price);
        return original_price - (original_price * discount);
    }

    @Override
    public String getName() {
        return combo.getName();
    }

}
