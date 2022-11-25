package controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.DAO;
import dao.VO;

public class LoginController implements Controller {

	@Override
	public String requestHandler(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		//Jsp로부터 파라미터 수집(id,pw)
		String id = request.getParameter("id");
		System.out.println("LoginController id : "+ id);
		
		String pw = request.getParameter("pw");
		System.out.println("LoginController pw : "+pw);
		
		VO vo = new VO(id,pw);
		DAO dao = new DAO();
		VO loginVO = dao.Login(vo);
		System.out.println("loginVO : "+ loginVO);
		
		if(loginVO!=null) {
			HttpSession session = request.getSession();
			
			//객체 바인딩
			session.setAttribute("loginVO",loginVO);
		}
		return "redirect:/MainPage.do";
		
		

	}

}
