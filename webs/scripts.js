function SendData(){
    var input = document.getElementById("input_field").value;
    console.log(input);
}

function Background(){
    var scroll_Position = window.scrollY;
    if (scroll_Position > 10){
    document.body.style.backgroundColor = "rgb(0, 255, 0)";
    }
}