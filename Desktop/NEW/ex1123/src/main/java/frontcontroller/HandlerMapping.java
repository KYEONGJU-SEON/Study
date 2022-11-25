package frontcontroller;

import java.util.HashMap;

import controller.Controller;
import controller.LoginController;
import controller.LogoutController;
import controller.MainPageController;
import controller.PracticeController;
import controller.SignupController;
import controller.SignupFormController;

public class HandlerMapping {
	private HashMap<String, Controller> mappings;
	
	
	public HandlerMapping() {
		mappings = new HashMap<String, Controller>();
		mappings.put("/Practice.do",new PracticeController());
		mappings.put("/MainPage.do",new MainPageController());
		mappings.put("/Login.do", new LoginController());
		mappings.put("/Logout.do", new LogoutController());
		mappings.put("/signupform.do", new SignupFormController());
		mappings.put("/signup.do", new SignupController());
		
	}

	public Controller getController(String path) {
		return mappings.get(path);
	}
}
