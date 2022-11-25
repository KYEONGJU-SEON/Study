package controller;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import dao.DAO;
import dao.VO;

public class MainPageController implements Controller {

	@Override
	public String requestHandler(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		// 1. 클라이언트의 요청을 받는다
		// 2. Model과 연동을 한다
		DAO dao = new DAO ();
		List<VO> vo = dao.List();
		System.out.println("vo : "+ vo);
		
		// 3. 응답하기(View와 연동)
		// 객체바인딩
		//(key,value) Jsp에서 "vo"로 요청이 왔을때 vo와 묶어줌
		request.setAttribute("vo", vo);
		
		return "MainPage";
		
		
		
		
	}

}
