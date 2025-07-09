
public class Dog {               //Class and private variable definition
	private int dogSpaceNumber;
	private double dogWeight;
	private boolean grooming;
	
	public Dog() {              //Default Constructor
		dogSpaceNumber = 0;
		dogWeight = 0.0;
		grooming = false;	
	}
	
	public Dog(int space, double weight, boolean groom) { // Constructor
		dogSpaceNumber = space;
		dogWeight = weight;
		grooming = groom;
	}
	
	public void setDogSpaceNumber(int space) { //dogSpaceNumber mutator
		dogSpaceNumber = space;
	}
	
	public void setDogWeight(double weight) {  //dogWeight mutator
		dogWeight = weight;
	}
	
	public void setGrooming(boolean groom) {   //grooming mutator
		grooming = groom;
	}
	
	public int getDogSpaceNumber() {           //dogSpaceNumber accessor
		return dogSpaceNumber;
	}
	
	public double getDogWeight() {             //dogWeight accessor
		return dogWeight;
	}
	
	public boolean getGrooming() {             //grooming accessor
		return grooming;
	}
}
