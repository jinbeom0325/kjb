console.log("hello!!!");
console.log("hello!!!", "hi", "gdgd");

alert("hello jajvascript!"); //경고문

let str = "hello javascript"; //변수
console.log("문자열:", str);

function sayhello() {
  //함수
  console.log("hello1");
  console.log("hello2");
  console.log("hello2");
}
sayhello();

let obj = {
  //객체
  str: "hello javascript", //객체가 가지고 있는 변수 : 프로퍼티(속성)
  sayhello: function () {
    console.log("obj-hello1");
    console.log("obj-hello2");
    console.log("obj-hello2");
  },
};
obj.sayhello(); //함수
console.log(obj);
console.log(obj.str);
