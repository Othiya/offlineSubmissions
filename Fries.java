public class Fries extends Food {
    public Fries() {
        super("Fries", 100);
    }

    // @Override
    // public void setFree() {
    // price = 0;
    // }

    @Override
    public double calculatePrice() {
        return price;
    }
}
