package contactservice;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ContactTest {
	
	//using junit for testing contact creation
	@Test
	public void testContactCreation() {
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		assertEquals("12345", contact.getContactId());
		assertEquals("Brandon", contact.getFirstName());
		assertEquals("Fluegge", contact.getLastName());
		assertEquals("1231231234", contact.getPhone());
		assertEquals("123 MyHouse Rd.", contact.getAddress());
	}
	
	//junit test for contactId
	//    criteria: null or ID too long
	@Test
	public void testInvalidId() {
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact(null, "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345678900", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		});
	}
	
	//junit test for contact first name
	//    criteria: null or name too long
	@Test
	public void testInvalidFirstName() {
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", null, "Fluegge", "1231231234", "123 MyHouse Rd.");
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "ThisNameIsLongerThan10Characters", "Fluegge", "1231231234", "123 MyHouse Rd.");
		});
	}
	
	//junit test for contact last name
	//    criteria: null or name too long
	@Test
	public void testInvalidLastName() {
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", null, "1231231234", "123 MyHouse Rd.");
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "ThisNameIsLongerThan10Characters", "1231231234", "123 MyHouse Rd.");
		});
	}
	
	//junit test for contact phone number
	//    criteria: null, number too long, or number consisting of characters
	@Test
	public void testInvalidPhone() {
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "Fluegge", null, "123 MyHouse Rd.");
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "Fluegge", "12312312345678", "123 MyHouse Rd.");
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "Fluegge", "abcdefghij", "123 MyHouse Rd.");
		});
	}
	
	//junit test for contact address
	//    criteria: null or address too long
	@Test
	public void testInvalidAddress() {
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "Fluegge", "1231231234", null);
		});
		
		assertThrows(IllegalArgumentException.class, () -> {
			new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee Rd.");
		});
	}
}