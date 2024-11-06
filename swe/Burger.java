public class Burger implements Food {

    @Override
    public double calculatePrice() {
        return 300;
    }

    @Override
    public String getName() {
        return "Burger";
    }

}