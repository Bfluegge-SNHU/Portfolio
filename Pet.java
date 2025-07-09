// Class and variable declaration:
public class Pet {
	private String petType;
	private String petName;
	private int petAge;
	private int dogSpaces;
	private int catSpaces;
	private int daysStay;
	private double amountDue;
	
	// Default constructor:
	public Pet() {
		petType = "null";
		petName = "null";
		petAge = -1;
		dogSpaces = -1;
		catSpaces = -1;
		daysStay = -1;
		amountDue = 0.00;
	}
	
	//Constructor:
	public Pet(String type, String name, int age, int dSpace, int cSpace, int stayLength, double amount) {
		petType = type;
		petName = name;
		petAge = age;
		dogSpaces = dSpace;
		catSpaces = cSpace;
		daysStay = stayLength;
		amountDue = amount;
	}
	
	// Mutator for petType:
	public void setPetType(String type) {
		petType = type;
	}
	// Mutator for petName:
	public void setPetName(String name) {
		petName = name;
	}
	// Mutator for petAge:
	public void setPetAge(int age) {
		petAge = age;
	}
	// Mutator for dogSpaces:
	public void setDogSpaces(int dSpace) {
		dogSpaces = dSpace;
	}
	// Mutator for catSpaces:
	public void setCatSpaces(int cSpace) {
		catSpaces = cSpace;
	}
	// Mutator for daysStay:
	public void setDaysStay(int stayLength) {
		daysStay = stayLength;
	}
	// Mutator for amountDue:
	public void setAmountDue(int amount) {
		amountDue = amount;
	}
	
	// Accessor for petType:
	public String getPetType() {
		return petType;
	}
	// Accessor for petName:
	public String getPetName() {
		return petName;
	}
	// Accessor for petAge:
	public int getPetAge() {
		return petAge;
	}
	// Accessor for dogSpaces:
	public int getDogSpaces() {
		return dogSpaces;
	}
	// Accessor for catSpaces:
	public int getCatSpaces() {
		return catSpaces;
	}
	// Accessor for daysStay:
	public int getDaysStay() {
		return daysStay;
	}
	// Accessor for amountDue:
	public double getAmountDue() {
		return amountDue;
	}

}
