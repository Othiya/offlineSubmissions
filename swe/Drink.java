public class Drink implements Food {

    @Override
    public double calculatePrice() {
        return 25;
    }

    @Override
    public String getName() {
        return "Drink";
    }

}
