public class FreeCombo extends ComboDecorator {

    FreeCombo(Combo c) {
        super(c);
    }

    @Override
    public double calculatePrice() {
        return 0;
    }

    @Override
    public String getName() {
        return combo.getName() + "(Free!!!)";
    }

}
