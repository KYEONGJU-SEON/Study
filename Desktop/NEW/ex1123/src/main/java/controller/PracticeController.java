package controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.VO;

public class PracticeController implements Controller {

	@Override
	public String requestHandler(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		// 세션 정보 가져오기
		HttpSession session = request.getSession();
		
		// 세션정보 이동할 때 오브젝트 클래스로 업캐스팅되서 불러올 때 하위클래스(VO)
		VO vo = (VO)session.getAttribute("loginVO");
		// 로그인 한 세션정보 
		System.out.println("연습 페이지 세션 정보 : "+ vo);
		request.setAttribute("vo", vo);
		
		ArrayList<VO> list = new ArrayList<>();
		VO vo1 = new VO();
		vo1.setId("하이");
		vo1.setPw("0829");
		list.add(vo1);
		
		VO vo2 = new VO();
		vo2.setId("오마이걸");
		vo2.setPw("0421");
		list.add(vo2);
		
		VO vo3 = new VO("AC/DC","SG");
		list.add(vo3);
		
		request.setAttribute("list", list);
		
		return "Practice";
	}

}
