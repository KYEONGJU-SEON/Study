package hellospring.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model){
        /*hello! 라는 data를 들고 */
        model.addAttribute("data","hello ! ! ");
        return "hello";
        /*resources - templates - hello.html로 가라 */
    }

    @GetMapping("hello-mvc")
    public String helloMVc(@RequestParam("name") String name, Model model){
        model.addAttribute("name",name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody
    /* http에서 body 부의 data를 내가 직접 넣어주겠다. */
    public String helloString(@RequestParam("name") String name){
        return "hello"+name; //"hello spring"
    }
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
        /* 객체는 json으로 반환 ! */
    }

    static class Hello{
        private String name;

    /*단축키 : alt + Insert */

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
    }