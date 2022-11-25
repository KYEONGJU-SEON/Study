package frontcontroller;

import java.io.IOException;
import java.util.logging.Handler;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import controller.Controller;

@WebServlet("*.do")
public class FrontController extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		
		request.setCharacterEncoding("utf-8");
		
		// 1. 어떤 요청인지 파악하기 (command 구하기)
		String reqPath = request.getRequestURI(); //프로젝트 + 파일 경로
		System.out.println("reqPath : "+ reqPath);
		
		String contextPath = request.getContextPath(); //프로젝트 
		System.out.println("contextPath : "+contextPath);
		
		String command = reqPath.substring(contextPath.length());
		System.out.println("command : "+ command);

		
		// 2. command에 따른 처리(if~ else)
		Controller ctrl = null;
		String nextPath = null;
		
		//HandlerMapping
		HandlerMapping mappings = new HandlerMapping();
		// command는 HandlerMapping의 Key 값
		// nextPath는 Controller의 리턴값
		ctrl = mappings.getController(command);
		nextPath = ctrl.requestHandler(request, response);
		System.out.println("nextPath : " + nextPath);
		
		// 3. 다음 페이지로 이동하기()
		if(nextPath!= null) {
			//값(redirect:)이 없으면 -1을 반환
			if(nextPath.indexOf("redirect:")== -1){
				// 어떤 View로 요청을 [의뢰=포워딩]할 지 jsp 선택
				// RequestDispatcher(요청 의뢰 객체)
				// 서블릿에서 처리한 데이터를 jsp에서 가져다가 사용해야 할 때 쓰는 객쳉
				// RequestDispathcer는 이동할 경로를 설정하고 생성
				// 생성된 객체를 가지고 forward 메소드를 통해 해당 경로 페이지로 이동할 수 있음
				// 이 때, sendRedirect와는 다르게 request와 response객체를 가지고 이동할 수 있음
				// 호출된 페이지는 request.getAttrigute()  메소드를 통해 넘겨받은 데이터를 처리할 수 있음
				
				//페이지 이동
				// 서블릿(컨트롤러)에서 값을 넘겨주고 해당 페이지에서 처리할 수 있도록 하는 방법
				RequestDispatcher rd = request.getRequestDispatcher(ViewResolver.makeView(nextPath));
				
				// 포워딩(해당 주소에 대해 요청하고 응답)
				rd.forward(request, response);
			
			}else {
				//리다이렉트(프로젝트 이름 + |redirect:| + ???.do)
				// !???.do의 Controller로 이동 후 리턴값 nextPath반환
				response.sendRedirect(contextPath+nextPath.split(":")[1]);
			}
		
		}
	}
}

		

