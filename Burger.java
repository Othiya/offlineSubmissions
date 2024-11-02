public class Burger implements Combo {

    @Override
    public double calculatePrice() {
        return 300;
    }

    @Override
    public String getName() {
        return "Burger";
    }

}